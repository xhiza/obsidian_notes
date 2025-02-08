---
id: note
aliases: []
tags:
  - saas-plugin
---

Ticket:
https://exasol.atlassian.net/browse/SPOT-21783

```

The metrics we should take a look:
post_actions_dispatcher = {
"saas_account_register": self.saas_account_register,
"saas_account_create": self.saas_account_register, --> this exajobs doesn't exist
"saas_db_create": self.saas_db_create,
"deployment_creating": self.deployment_creating,
"deployment_creating_pooling": self.deployment_creating_pooling,
"deployment_deleted": self.deployment_deleted,
"main_cluster_running": self.main_cluster_running,
"main_cluster_stopping": self.main_cluster_stopping, --> sometimes events are coming late and teh cluster avaialability is triggered before the cluster event is processed, that raise an alert.
"main_cluster_starting": self.main_cluster_starting,
"main_cluster_stopped": self.main_cluster_stopped,
"main_cluster_scaling": self.main_cluster_scaling, --> missing stateMetric
"worker_cluster_creating": self.worker_cluster_creating,
"worker_cluster_stopped": self.worker_cluster_stopped,
"worker_cluster_starting": self.worker_cluster_starting,
"worker_cluster_deleted": self.worker_cluster_deleted,
"worker_cluster_running": self.worker_cluster_running,
"worker_cluster_scaling": self.worker_cluster_scaling, --> missing stateMetric
"current_db_state": self.current_db_state,
"current_cluster_state": self.current_cluster_state,
"plugin_health_check": self.plugin_health_check,
"db_backup_progress": self.db_backup_progress, -> Body json showing result_code always 0 and the progress is not progressing from 0 -> 100, if it succesfull shows only 100.
}
```
