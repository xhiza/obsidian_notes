---
id: Unattended-upgrades
aliases:
  - Backlog
tags:
  - SPOT-19935
  - SPOT-19221
---

Test done to non exasol db:

Steps I took to test whether the update stoppes when reboot is initiated.

- Created a terraform file to deploy ec2 instance with old image
- Update the repository package:
  - sudo apt-get update
- Added crontab jobs as below:
  - (crontab -l 2>/dev/null; echo "\* \* \* \* \* sudo /usr/bin/unattended-upgrade") | crontab -
  - (crontab -l 2>/dev/null; echo "5,10,15,20,25,30,35,40,45,50,55 \* \* \* \* /sbin/shutdown -r now") | crontab -
- Restart:
  - Restart was successful if was initiatted with sudo
  - Restart failed if was initiated with reboot command

The output during the testing:

Tried to shutdown the system manually as well during the update:

```bash
- ubuntu@ip-10-0-1-80:/var/log/unattended-upgrades$ shutdown -r now
- Operation inhibited by "APT" (PID 8432 "unattended-upgr", user root), reason is "APT is installing or removing packages".
- Please retry operation after closing inhibitors and logging out other users.
- Alternatively, ignore inhibitors and users with 'systemctl reboot -i'

- 2024-05-22 19:46:01,759 ERROR Lock file is already taken, exiting.

- ubuntu@ip-10-0-1-80:/var/log/unattended-upgrades$ ps -ef | grep unattended
- root         628       1  0 19:35 ?        00:00:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
- ubuntu      1871    1868  0 19:43 ?        00:00:00 /bin/sh -c sudo /usr/bin/unattended-upgrade
- root        1873    1871  0 19:43 ?        00:00:00 sudo /usr/bin/unattended-upgrade
- root        1875    1873 98 19:43 ?        00:02:06 /usr/bin/python3 /usr/bin/unattended-upgrade
- ubuntu      1922    1309  0 19:43 pts/1    00:00:00 tail -f unattended-upgrades.log
- ubuntu      1983    1193  0 19:45 pts/0    00:00:00 grep --color=auto unattended
```

New soulution:

```


#!/bin/bash

cat <<EOL > /etc/systemd/system/unattended-upgrades.service
[Unit]
Description=Unattended Upgrades

[Service]
Type=oneshot
ExecStart=/usr/bin/unattended-upgrade -v
EOL


cat <<EOL > /etc/systemd/system/unattended-upgrades.timer
[Unit]
Description=Run Unattended Upgrades 15minutes after boot and every day.

[Timer]
OnCalendar=
OnBootSec=15min
OnUnitActiveSec=1d
AccuracySec=1h
RandomizedDelaySec=30min
Persistent=true

[Install]
WantedBy=timers.target
EOL

sudo systemctl daemon-reload
sudo systemctl enable unattended-upgrades.timer
sudo systemctl start unattended-upgrades.timer

# Uncomment the specified line in 50unattended-upgrades
sudo sed -i '/^.*"${distro_id}:${distro_codename}-updates";/s/^\/\///' /etc/apt/apt.conf.d/50unattended-upgrades

echo "Directories and files created successfully, systemd reloaded, and 50unattended-upgrades updated."
```
