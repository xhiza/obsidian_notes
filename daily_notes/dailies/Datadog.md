---
id: Datadog
aliases: []
tags: []
---

Datadog Domain:

The page where is populated with the issues and findings and reviews during the week.

The main problem right now is that the dashboards are not created and the graphs are not populated.

The findings are:

```
2024-05-31 08:48:27.130020 +00:00] [n0011] Trace for top 1 largest memory block: - memory blocks = 244869, size_KiB = 21205.556640625- /opt/exasol/runtime-8.5.0/lib/python3.10/json/decoder.py:353: obj, end = self.scan_once(s, idx)
[2024-05-31 08:48:32.286321 +00:00] [n0011] ERROR:datadog.api:Could not request POST https://api.datadoghq.eu/api/v1/series: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')). Please check the network connection or try again later. If the problem persists, please contact support@datadoghq.com

[2024-05-31 09:37:09.512296] INFO: Catch the exception with traceback: Error: Dashboard prod.cloud.exasol.com - acc_ug9l-xk-qyqui7dmbord1q was not created!!!
Traceback (most recent call last):
File "/exa/data/bucketfs/bfsdefault/default/plugins:dashboards.py", line 58, in create_dashboard
raise Exception(f"Dashboard {title} was not created!!!")
Exception: Dashboard prod.cloud.exasol.com - acc_ug9l-xk-qyqui7dmbord1q was not created!!!

[root@n11 default]# PYTHONPATH=$COS_DIRECTORY/lib python3 /exa/data/bucketfs/bfsdefault/default/plugins:sync.py
Traceback (most recent call last):
File "/exa/data/bucketfs/bfsdefault/default/plugins:sync.py", line 799, in <module>
s.main()
File "/exa/data/bucketfs/bfsdefault/default/plugins:sync.py", line 37, in main
self.sync_accounts_dashboards()
File "/exa/data/bucketfs/bfsdefault/default/plugins:sync.py", line 159, in sync_accounts_dashboards
self.create_customer_dashboard(
File "/exa/data/bucketfs/bfsdefault/default/plugins:sync.py", line 563, in create_customer_dashboard
self.add_db_cluster_widgets(
File "/exa/data/bucketfs/bfsdefault/default/plugins:sync.py", line 751, in add_db_cluster_widgets
dbw = dashboards.deployment_widgets(db_name, "", sync)
File "/exa/data/bucketfs/bfsdefault/default/plugins:customer_dashboard.py", line 148, in deployment_widgets
xy = self.calculate_events_widget_layouts(self.dboard_info)
File "/exa/data/bucketfs/bfsdefault/default/plugins:customer_dashboard.py", line 431, in calculate_events_widget_layouts
for w in dboard_info["widgets"]:
TypeError: 'NoneType' object is not subscriptable

```

Solution: The API Key and APP Key used in production is bound to a user that Role is updated to readme role, which has insufficient privileges for an api to create dashboards.
