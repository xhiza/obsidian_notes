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

1. sbfs list 2  
2. dwad_client snapshot <> 2 300  
3. sbfs list 2  
4. confd_client db_stop db_name: <> 
5. sbfs format 2 -metadata-volume 0 -data-volume 1
6. sbfs list 2  
7. confd_client db_start db_name: <> 
8. sbfs remote-format 4 -metadata-volume 0 -data-volume 3 
9. dwad_client snapshot <> 2 300  
10. sbfs list 2  
11. /exa/etc/dwad/<>_snapshot_sync  
12. sbfs list 4  


We stopped and started the DB, and the sbfs was fixed, no need for reformatting, waiting for cos to run snapshot automatically at 10CEST.

Disable Versioning and Empty copy bucket.
