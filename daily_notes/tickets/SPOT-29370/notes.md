---
id: notes
aliases: []
tags: []
---

The idea is to detach s3 bucket from cloudformation stack.

- [x] remove bucket from cloudformation stack
- [x] [] create a database old fashion way, import data, and create new s3 bucket.
- [~] create a new database and attach the s3 bucket to it.
    Issues: the offline bucket is not created, the offline bucket should be created in advance, the name should be same like platform_reference/cloudformation stack name.

- [] new db is up and running, but attached data from old bucket is missing. I think the problem when created a new database wipes all data in s3 bucket.

```Name: Database01
ID: bC3nzNHhR_iFx54dJtQsnA
State: running
Connection state: up
10 state comments available.
-----
[2026-02-18 14:12:48] (UID 0) User requested setup of system.
[2026-02-18 14:12:48] (UID 0) Set owner of system to UID = 500 (exadefusr), GID = 500.
[2026-02-18 14:12:48] (UID 0) Try to start system with -create-new-db flag.
[2026-02-18 14:12:48] System started successfully in partition 44.
```
