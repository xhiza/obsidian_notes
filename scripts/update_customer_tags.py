#!/usr/bin/env python3
"""Sync customer tags in daily notes from prose mentions.

For each daily note in daily_notes/dailies/*.md:
  - Detect mentions of known customer names in the body prose
    (case-insensitive, whole-word; HTML comments are stripped first so
    template placeholder hints don't trigger false positives).
  - Sync the frontmatter `tags:` list: preserve non-customer tags,
    replace any customer tags with the freshly detected set.
  - Sync the `## Customers` section's `<!-- Tag customers: ... -->`
    comment with `#customer/<Name>` for each detected customer; also
    strips legacy lines that contain only `#customer/Name` tokens.

Usage:
    python scripts/update_customer_tags.py            # apply changes
    python scripts/update_customer_tags.py --dry-run  # preview only
    python scripts/update_customer_tags.py --only 2024-06   # filter
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CUSTOMERS: list[str] = [
    "Adena",
    "Adidas",
    "Analytics-Database",
    "AZ-Direct",
    "BlueYonder",
    "DeutschlandCard",
    "Formue",
    "Keboola",
    "Semikron",
    "VENI",
    "Vocare",
    "Wooga",
    "YayPay",
]

VAULT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DAILIES = VAULT_ROOT / "daily_notes" / "dailies"
DAILY_FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
CUSTOMERS_HEADER_RE = re.compile(r"^##[ \t]+Customers[ \t]*$", re.MULTILINE | re.IGNORECASE)
NEXT_H2_RE = re.compile(r"^##[ \t]+", re.MULTILINE)
TAG_COMMENT_RE = re.compile(r"<!--\s*Tag customers.*?-->", re.IGNORECASE | re.DOTALL)
CUSTOMER_ONLY_LINE_RE = re.compile(r"^[ \t]*(#customer/\S+[ \t]*)+\r?\n?$", re.MULTILINE)
TAGS_LINE_RE = re.compile(r"^tags[ \t]*:[ \t]*(.*)$", re.MULTILINE)
BLOCK_TAG_ITEM_RE = re.compile(r"^[ \t]+-[ \t]+(.*)$")


def detect_customers(body: str) -> list[str]:
    """Return customer names mentioned in body, in CUSTOMERS-declaration order."""
    searchable = HTML_COMMENT_RE.sub(" ", body)
    found: list[str] = []
    for name in CUSTOMERS:
        # Whole-word boundary that handles names containing hyphens
        # (e.g. "AZ-Direct"). \b alone would split on the hyphen.
        pattern = re.compile(
            r"(?<![A-Za-z0-9_-])" + re.escape(name) + r"(?![A-Za-z0-9_-])",
            re.IGNORECASE,
        )
        if pattern.search(searchable):
            found.append(name)
    return found


def split_frontmatter(text: str) -> tuple[str | None, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def read_existing_tags(frontmatter: str) -> list[str]:
    """Parse the `tags:` field; supports inline `[a, b]`, single value, or block list."""
    lines = frontmatter.splitlines()
    for idx, line in enumerate(lines):
        m = TAGS_LINE_RE.match(line)
        if not m:
            continue
        inline = m.group(1).strip()
        if inline.startswith("["):
            inner = inline[1:]
            if inner.endswith("]"):
                inner = inner[:-1]
            return [t.strip().strip("\"'") for t in inner.split(",") if t.strip()]
        if inline:
            return [inline.strip("\"'")]
        tags: list[str] = []
        for cont in lines[idx + 1:]:
            cm = BLOCK_TAG_ITEM_RE.match(cont)
            if not cm:
                break
            tags.append(cm.group(1).strip().strip("\"'"))
        return tags
    return []


def render_tags_block(tags: list[str]) -> str:
    if not tags:
        return "tags:"
    return "tags:\n" + "\n".join(f"  - {t}" for t in tags)


def write_tags_field(frontmatter: str, new_tags: list[str]) -> str:
    """Replace the `tags:` block (line + contiguous block-list items) with new_tags."""
    lines = frontmatter.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    replaced = False
    while i < len(lines):
        line = lines[i]
        if not replaced and TAGS_LINE_RE.match(line.rstrip("\n")):
            replaced = True
            i += 1
            while i < len(lines) and BLOCK_TAG_ITEM_RE.match(lines[i].rstrip("\n")):
                i += 1
            block = render_tags_block(new_tags)
            # Preserve the same line-ending style as the file (assume \n).
            out.append(block + "\n")
        else:
            out.append(line)
            i += 1
    if not replaced:
        joined = "".join(out)
        if joined and not joined.endswith("\n"):
            joined += "\n"
        joined += render_tags_block(new_tags) + "\n"
        return joined.rstrip("\n")
    return "".join(out).rstrip("\n")


def render_customer_comment(customers: list[str]) -> str:
    if customers:
        tokens = " ".join(f"#customer/{c}" for c in customers)
        return f"<!-- Tag customers: {tokens} -->"
    return "<!-- Tag customers: -->"


def update_customers_section(body: str, customers: list[str]) -> str:
    header = CUSTOMERS_HEADER_RE.search(body)
    if not header:
        return body
    after = body[header.end():]
    next_h2 = NEXT_H2_RE.search(after)
    section_end = header.end() + next_h2.start() if next_h2 else len(body)
    section = body[header.end():section_end]
    comment = render_customer_comment(customers)

    if TAG_COMMENT_RE.search(section):
        new_section = TAG_COMMENT_RE.sub(lambda _m: comment, section, count=1)
    else:
        cleaned = CUSTOMER_ONLY_LINE_RE.sub("", section)
        rest = cleaned.lstrip("\n")
        separator = "\n\n" if rest else "\n"
        new_section = "\n" + comment + separator + rest
        new_section = re.sub(r"\n{3,}", "\n\n", new_section)

    return body[:header.end()] + new_section + body[section_end:]


def process_file(path: Path, dry_run: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        return {"file": path.name, "skipped": True, "reason": "no frontmatter"}

    detected = detect_customers(body)
    customer_lower = {c.lower() for c in CUSTOMERS}
    existing = read_existing_tags(fm)
    non_customer = [t for t in existing if t.lower() not in customer_lower]

    seen: set[str] = set()
    final_tags: list[str] = []
    for t in (*non_customer, *detected):
        key = t.lower()
        if key not in seen:
            seen.add(key)
            final_tags.append(t)

    new_fm = write_tags_field(fm, final_tags)
    new_body = update_customers_section(body, detected)
    new_text = f"---\n{new_fm}\n---\n{new_body}"

    if new_text == text:
        return {"file": path.name, "detected": detected, "changed": False}
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return {"file": path.name, "detected": detected, "changed": True}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    ap.add_argument("--dailies-dir", default=str(DEFAULT_DAILIES), help="Directory of daily notes")
    ap.add_argument("--only", default="", help="Substring filter on file names")
    ap.add_argument("--quiet", action="store_true", help="Only print files that changed")
    args = ap.parse_args(argv)

    dailies = Path(args.dailies_dir)
    if not dailies.is_dir():
        print(f"error: {dailies} is not a directory", file=sys.stderr)
        return 2

    files = sorted(f for f in dailies.glob("*.md") if DAILY_FILENAME_RE.match(f.name))
    if args.only:
        files = [f for f in files if args.only in f.name]

    changed = 0
    skipped = 0
    for f in files:
        result = process_file(f, args.dry_run)
        if result.get("skipped"):
            skipped += 1
            if not args.quiet:
                print(f"{result['file']}: skipped ({result['reason']})")
            continue
        if result.get("changed"):
            changed += 1
        if args.quiet and not result.get("changed"):
            continue
        names = ", ".join(result["detected"]) or "(none)"
        marker = "" if result.get("changed") else "  [no change]"
        print(f"{result['file']}: {names}{marker}")

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {changed} files; skipped {skipped} (no frontmatter); scanned {len(files)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
