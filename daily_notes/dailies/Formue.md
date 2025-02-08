---
id: Formue
aliases: []
tags: []
---

Formue client:

AccountUUID: acc_8xdvgfppTBKCiQvUgCoLyA

```bash
Standby
Region: eu-west-1 (Dublin)
Account ID: org_6Jh1EU8XbW7I8Ifg (FORMUE)
Database ID: 7XyVbsJKQy27-ntpn0OiYw (ClientFacingStandby)
Main Cluster ID: -_0ophwzQiOnFSU8DiMvvw (OnDemand)
Version: 8.26.0


Production
Region: eu-central-1 (Frankfurt)
Account ID: org_6Jh1EU8XbW7I8Ifg (FORMUE)
Database ID: _uWTJ9MXRDmMxsxDz53YKg (ClientFacing)
Main Cluster ID: HSCWHgtTQIuYIhqzhG8jqw (AlwaysOn)
Worker 1 Cluster ID: ioXPnOx4RoWMIjuinPlhRg (OnDemand)
Worker 2 Cluster ID: iuTO7OhhRW6xompZRmDpFw (PeakHours)
Version: 826.0

```

The Plan on patching with the Fix (db_configure timeout)

```
You patch StandBy
You let us know when we can switch over to use Standby
We switch the API over to StandBy
We will let you know when you can patch Production
You let us know when we can switch back to Production
We will let you know when we have switched back to Production
```
