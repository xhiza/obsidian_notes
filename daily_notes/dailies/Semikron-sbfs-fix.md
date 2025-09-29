---
id: Semikron-sbfs-fix
aliases: []
tags:
  - Semikron
---

- AccountUUID: jntuvw96QqeVGdhjx1dmzg
- DBUUID: MPiCdBNMTG6F6YgvaSo7Qw

Done:
    1. Bucket Replication - Done
    2. Bucket Versioning - Done
    3. EBS Snapshot - Done


Steps to follow:

1. sbfs list 2  # we checked what snapshots are there
2. dwad_client snapshot <> 2 300  # we took one more snapshot
3. sbfs list 2  # checked the new snapshot is there
4. confd_client db_stop db_name: <> 
5. sbfs format 2 -metadata-volume 0 -data-volume 1
6. sbfs list 2  # checked all snapshots are gone
7. confd_client db_start db_name: <> 
8. sbfs remote-format 4 -metadata-volume 0 -data-volume 3  # format 4 as well after formating 2
9. dwad_client snapshot <> 2 300  # created a new snapshot
10. sbfs list 2  # checked the new snapshot is in the list
11. /exa/etc/dwad/<>_snapshot_sync  # we synced 2 to 4
12. sbfs list 4  # checked the new snapshot is now also on volume 4
