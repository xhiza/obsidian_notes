---
title: Database update from 2025.1.11 to 2025.1.16
date: 2026-10-02
status: resolved
ticket: L3-4474
tags:
  - post-mortem
  - database-update
  - saas
---

# Database update from 2025.1.11 to 2025.1.16

## Incident summary

On Friday evening, 2026-10-02, we attempted to update the database from `2025.1.11` to `2025.1.16` under [L3-4474](https://exasol.atlassian.net/browse/L3-4474).

The update Step Function detected insufficient disk space and followed its expected recovery path: it ran C4 cleanup, checked the available space again, and then performed a coredump cleanup. Although the coredump cleanup completed, the workflow continued to report that there was not enough space to update the database.

## Impact

- The automated update could not complete without manual intervention.
- The update process generated repeated disk-space failures despite the filesystem not being full.
- A separate file-ownership problem prevented C4 from creating files during one retry.
- The database update eventually completed successfully on all nodes.

## Investigation

Manual filesystem checks showed the following available space:

| Node | `/home` available | `/home` utilization |
| --- | ---: | ---: |
| `172.16.2.34` | 55 GB | 42% |
| `172.16.2.5` | 31 GB | 67% |
| `172.16.2.49` | 32 GB | 67% |

The root filesystem had approximately 39 GB available on each node.

The standard cleanup command used was:

```bash
c4 x cleanup \
  --repository local \
  --all-except=<existing_version> \
  --all-except=@license:v8-saas
```

Because the Step Function continued to report insufficient space, the update was also triggered manually from a database node:

```bash
c4 update -P -t <target-version>
```

C4 fetched the packages successfully, but the update failed immediately afterward with another insufficient-space error. Disk utilization at that point was approximately 81%.

## Secondary permission issue

After removing logs and old packages to create additional space, a retry failed because C4 could not create a file under a directory owned by `root` rather than `ubuntu`.

The ownership was corrected with:

```bash
sudo chown -R ubuntu:ubuntu ~/.ccc/x/u/branch/
```

The update was retried, but C4 still reported insufficient space when disk utilization was approximately 79%.

## Root cause discovery

Further investigation found a 10 GB swap file in the home directory:

```text
-rw------- 1 root root 10737418240 Jul 21 10:33 .swap
```

Its active usage was verified with:

```bash
swapon --show
```

The result showed:

```text
NAME               TYPE SIZE USED PRIO
/home/ubuntu/.swap file  10G 512K   -2
```

Although the swap file was barely used, it consumed approximately 10 GB of disk space and contributed to the C4 disk-space validation failure.

## Resolution

The swap file was safely disabled and removed, and its persistent configuration was deleted:

```bash
sudo swapoff /home/ubuntu/.swap
sudo rm /home/ubuntu/.swap
sudo sed -i '\|/home/ubuntu/.swap|d' /etc/fstab
```

The same remediation steps were applied to the two remaining database nodes. The updates completed successfully on all nodes.

The Step Function then required manual continuation. The resume command documented in the `#saas-update` Slack channel was used to allow the workflow to complete its remaining steps.

## Timeline

| Stage | Event |
| --- | --- |
| 1 | Started the update from `2025.1.11` to `2025.1.16`. |
| 2 | Step Function detected insufficient space and ran C4 cleanup and coredump cleanup. |
| 3 | Step Function continued to report insufficient space. |
| 4 | Manual node checks showed available filesystem capacity. |
| 5 | Manual `c4 update` was started; package download succeeded, but the update failed its space check. |
| 6 | Logs and old packages were removed. A retry exposed incorrect `root:root` ownership in the C4 working directory. |
| 7 | C4 working-directory ownership was changed to `ubuntu:ubuntu`. |
| 8 | A 10 GB active swap file was discovered and safely removed. |
| 9 | The same remediation was applied to the other two nodes. |
| 10 | Updates succeeded on all nodes, and the Step Function was resumed using the documented Slack command. |

## Contributing factors

- The Step Function’s disk-space check did not provide enough diagnostic detail about the filesystem, threshold, or temporary-space requirement.
- The standard cleanup did not remove or identify the large swap file.
- The C4 working directory had unexpected ownership, which caused a separate failure during the retry.
- The workflow required manual continuation after the node-level updates completed.

## Corrective and preventive actions

| Action | Status |
| --- | --- |
| Improve disk-space failure messages to include the checked filesystem, required free space, and observed free space. | Open |
| Add validation for large swap files and other non-obvious disk consumers to the update preflight. | Open |
| Ensure cleanup operations preserve expected `ubuntu:ubuntu` ownership under `~/.ccc`. | Open |
| Document the manual recovery path, including the node-level update and Step Function resume procedure. | Partially complete |
| Add an end-to-end test covering low-space detection, cleanup, package extraction, and final Step Function completion. | Open |

## Lessons learned

- Overall filesystem utilization is not sufficient to diagnose an update-space failure; the update’s actual working filesystem and temporary-space requirements must be checked.
- Swap files can consume significant disk capacity even when their active usage is minimal.
- File ownership must be verified after cleanup and before retrying an automated update.
- The Step Function should expose a clear, supported recovery path when node-level remediation succeeds but orchestration remains paused.

## References

- [L3-4474](https://exasol.atlassian.net/browse/L3-4474)
- `#saas-update` Slack channel — Step Function resume command
