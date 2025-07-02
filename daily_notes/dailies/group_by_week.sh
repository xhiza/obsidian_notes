#!/bin/bash

# Make sure this script is run with Bash, not sh
if [ -z "$BASH_VERSION" ]; then
  echo "Please run this script with Bash: bash $0"
  exit 1
fi

TARGET_DIR="${1:-.}"
OUTPUT_DIR="${2:-./weekly_output}"

mkdir -p "$OUTPUT_DIR"

# Clear previous temp list if exists
TMP_DIR=$(mktemp -d)

# Step 1: Collect files and group by week
find "$TARGET_DIR" -maxdepth 1 -type f -print0 | while IFS= read -r -d '' file; do
  # Get modification time
  mod_epoch=$(stat -f "%m" "$file")
  week=$(date -r "$mod_epoch" +%G-W%V)

  # Append file path to the week-based temp file
  echo "$file" >> "$TMP_DIR/$week.list"
done

# Step 2: Create markdown files
for week_file in "$TMP_DIR"/*.list; do
  week=$(basename "$week_file" .list)
  output_file="$OUTPUT_DIR/$week.md"
  echo "# Files for Week $week" > "$output_file"
  echo "" >> "$output_file"

  while IFS= read -r file; do
    echo "## $(basename "$file")" >> "$output_file"
    echo '```' >> "$output_file"
    cat "$file" >> "$output_file"
    echo '```' >> "$output_file"
    echo "" >> "$output_file"
  done < "$week_file"

  echo "Created: $output_file"
done

# Clean up
rm -r "$TMP_DIR"

