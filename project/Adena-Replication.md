- [x] TODO: Create new SAAS Account for Adena Replication
- [x] TODO: Create a Database for Adena Replication
- [x] TODO: give Avantika access to Adena Replication Database and Account.
- [x] TODO: create inventory configuration on source offline bucket Database.


```json
{
    "InventoryConfiguration": {
        "Destination": {
            "S3BucketDestination": {
                "AccountId": "013892436430",
                "Bucket": "arn:aws:s3:::psjwxelnnvgt",
                "Format": "CSV"
            }
        },
        "IsEnabled": true,
        "Filter": {
            "Prefix": "volumes/"
        },
        "Id": "inventory_adenadb",
        "IncludedObjectVersions": "Current",
        "OptionalFields": [
            "Size",
            "LastModifiedDate",
            "StorageClass",
            "ETag",
            "ChecksumAlgorithm"
        ],
        "Schedule": {
            "Frequency": "Daily"
        }
    }
}

```
