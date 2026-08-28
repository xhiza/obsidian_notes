---
id: CLUSTER_RESIZING
aliases: []
tags:
  - CLUSTER_RESIZING
---



//NOTE: you need to know the target size id (in this case it was 13)

```sql
/* Query to resize cluster */
INSERT INTO clusters
        ( UUID, NAME, STATUS, MAIN_CLUSTER, CLUSTER_SIZES_ID, DB_UUID, CREATED_AT, CREATED_BY, LAST_MODIFIED_BY, AUTO_STOP_ENABLED, AUTO_STOP_IDLE_TIME, SAASD_IGNORE )
SELECT
        UUID, NAME, 'toscale' STATUS, MAIN_CLUSTER, 13 AS CLUSTER_SIZES_ID, DB_UUID, CREATED_AT, CREATED_BY, LAST_MODIFIED_BY, AUTO_STOP_ENABLED, AUTO_STOP_IDLE_TIME, false AS SAASD_IGNORE
FROM clusters 
WHERE id IN (
        SELECT MAX(id) FROM "CLUSTERS"
        WHERE db_uuid = :{db_uuid} AND uuid = :{cluster_uuid}
        GROUP BY uuid
);
``````

```sql
python3 -c "import base64, uuid; print(base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip(b'=').decode('ascii'))"

INSERT INTO clusters
        (uuid, name, status, cluster_sizes_id, main_cluster, db_uuid, created_by, last_modified_by)
VALUES
        ('qOl6X5p3RhaVAG8iKuqmyg', 'Worker', 'tocreate', 12, False, '4KaNiSODRJKV3v_I3-oR3g', 'mid.L3-3526', 'mid.L3-3526');
``````
