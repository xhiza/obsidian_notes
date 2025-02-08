```sql
WITH 
    stage1 AS 
    (   SELECT 
            "CLS_ID", 
            "ACCOUNT_UUID", 
            "SUBSCRIPTION_ID", 
            "CLS_UUID", 
            "DB_UUID", 
            "PLATFORM_UUID", 
            "DBS_REGION", 
            "CLUSTER_SIZES_ID", 
            "EDITION_NAME", 
            "FROM_STATUS", 
            "TO_STATUS",
            CASE 
                WHEN "FROM_TS" < :{start} 
                THEN :{start} 
                ELSE "FROM_TS" 
            END FROM_TS, 
            CASE 
                WHEN "TO_TS" > :{end} 
                THEN :{end} 
                ELSE "TO_TS" 
            END TO_TS
        FROM 
            "CLUSTERS_STATUS_TRANSITIONS"
        WHERE 
            to_status = 'error'
            AND to_ts >= :{start}
        ORDER BY 
            cls_uuid, 
            from_ts 
    )
SELECT 
    stage1.*, 
    HOURS_BETWEEN(TO_TS, FROM_TS) HOURS
FROM 
    stage1
WHERE TO_TS > :{start} AND FROM_TS < :{end};
```

Insert status to databases table

```sql
INSERT INTO
    "CLUSTERS"
    (
        "UUID",
        "NAME",
        "STATUS",
        "COMMENT",
        "MAIN_CLUSTER",
        "CLUSTER_SIZES_ID",
        "DB_UUID",
        "CREATED_AT",
        "CREATED_BY",
        "LAST_MODIFIED_BY",
        "AUTO_STOP_ENABLED",
        "AUTO_STOP_IDLE_TIME"
    )
    VALUES
    (
        'BKiceMu5TduXuUdaqbhn6g',
        'Cluster02',
        'deleted',
        NULL,
        false,
        1,
        'vT1nVibWTluXJaV9DyegVw',
        '2024-09-02 08:16:18',
        'auth0|66bf0d597c0e0e9df1d26c14',
        'edsh',
        true,
        120
    );

INSERT INTO 
    "CLUSTERS" 
    ( 
        "UUID", 
        "NAME", 
        "STATUS", 
        "COMMENT", 
        "MAIN_CLUSTER", 
        "CLUSTER_SIZES_ID", 
        "DB_UUID", 
        "CREATED_AT", 
        "CREATED_BY", 
        "LAST_MODIFIED_BY", 
        "AUTO_STOP_ENABLED", 
        "AUTO_STOP_IDLE_TIME" 
    ) 
    VALUES 
    ( 
        '81bqnTZTRr6zjCg5Chku2w', 
        'Cluster02', 
        'stopped', 
        NULL, 
        true, 
        4, 
        '81bqnTZTRr6zjCg5Chku2w', 
        '2024-07-29 10:17:36', 
        'auth0|66a76bd626c0e144e1de17fe', 
        'edsh', 
        true, 
        30 
    );

```

-- Get databases and the owner of them

```sql
WITH db AS (
SELECT
    *
FROM
    VALUES
    (
('Wtat5hcVSn26Fiu1Yklcuw','exasol-8.23.4'),
('_6hNbFTDTFCD8GeIhPW9W','exasol-8.18.2'),
('tFccwOAbQ1q9P5Ot4vbwgA','exasol-8.24.0')
    )
    AS d(uuid, version)
),
users AS (
SELECT * FROM users WHERE id in (SELECT max(id) FROM users GROUP BY uuid)),
subscriptions AS (
        SELECT
            occured_at,
            object_id subscription_id,
            JSON_VALUE(event_payload, '$.customer_id' NULL ON EMPTY DEFAULT 'N/A' ON ERROR) as customer_id,
            JSON_VALUE(event_payload, '$.status' NULL ON EMPTY DEFAULT 'N/A' ON ERROR) as subscription_status
        FROM chargebee_events
        WHERE rowid in (
                SELECT max(rowid)
                FROM chargebee_events
                WHERE object_type = 'subscription' GROUP BY object_id
        )
),
latest_databases AS (
SELECT d1.* FROM databases AS d1
INNER JOIN ( SELECT uuid, MAX(last_modified_at) AS MaxUpdate
FROM databases
GROUP BY uuid
) AS d2
ON d1.uuid = d2.uuid
AND d1.last_modified_at = d2.MaxUpdate
WHERE d1.status = 'running'
)
SELECT latest_databases.uuid,latest_databases.status, latest_databases.name, d.version, users.email
FROM latest_databases
JOIN users ON latest_databases.created_by = users.uuid
JOIN db d ON latest_databases.uuid = d.uuid
ORDER BY latest_databases.uuid DESC
```
