---
id: subscription-cancellation
aliases: []
tags: []
---

payload for cancellation:
``````
{
    "id": "ev_16BTZYUQx0KBVb8QM",
    "occurred_at": 1728698402,
    "source": "scheduled_job",
    "object": "event",
    "api_version": "v2",
    "content": {
        "subscription": {
            "id": "16CMpPUToS7pJTXU",
            "billing_period": 1,
            "billing_period_unit": "month",
            "trial_end": 1728698402,
            "customer_id": "acc_OnljQnIvR46ObDLAS_Ls1w",
            "status": "cancelled",
            "trial_start": 1728406414,
            "created_at": 1728406414,
            "started_at": 1728406414,
            "cancelled_at": 1728698402,
            "updated_at": 1728698402,
            "has_scheduled_changes": false,
            "channel": "web",
            "resource_version": 1728698402564,
            "deleted": false,
            "object": "subscription",
            "currency_code": "USD",
            "subscription_items": [
                {
                    "item_price_id": "e20cbb74eebe494d83f9f7753e5b8fbd",
                    "item_type": "plan",
                    "unit_price": 0,
                    "unit_price_in_decimal": "0.0000",
                    "free_quantity": 0,
                    "free_quantity_in_decimal": "0.00000000",
                    "trial_end": 1728698402,
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c62d13fb358846f38c1075518dcaa25b",
                    "item_type": "addon",
                    "unit_price": 0,
                    "unit_price_in_decimal": "0.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "9707e2ae3a1d437ba79cff36bdfc0716",
                    "item_type": "addon",
                    "unit_price": 2,
                    "unit_price_in_decimal": "0.0250",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "bc30fbfcbb1b4148beee1e34f41cb378",
                    "item_type": "addon",
                    "unit_price": 9,
                    "unit_price_in_decimal": "0.0900",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fbc9f99548b744e9ba071b4921bc4e97",
                    "item_type": "addon",
                    "unit_price": 2,
                    "unit_price_in_decimal": "0.0250",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "12707554d3d14d6a94105a2154973021",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "bed92963d47b45bfb986442545f9a4fd",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "793f3fd4b9c64d599cbbe82de3cb8e90",
                    "item_type": "addon",
                    "unit_price": 345,
                    "unit_price_in_decimal": "3.4500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4ef25192f93f4f1eb9c701548e5285de",
                    "item_type": "addon",
                    "unit_price": 345,
                    "unit_price_in_decimal": "3.4500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b029ed933667485b82d34f4d8617a23a",
                    "item_type": "addon",
                    "unit_price": 360,
                    "unit_price_in_decimal": "3.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "00953f5b60754f84aa717478b72d7c3f",
                    "item_type": "addon",
                    "unit_price": 360,
                    "unit_price_in_decimal": "3.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "213e09107b034580bb7f51665b9d7203",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e1239d35b5404fc9baaebafba70cbeb8",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b1b39228b6d64b9a8c9d073a5a2d8543",
                    "item_type": "addon",
                    "unit_price": 690,
                    "unit_price_in_decimal": "6.9000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "091505b5fa6a4f25a13db4e9fc14b19c",
                    "item_type": "addon",
                    "unit_price": 690,
                    "unit_price_in_decimal": "6.9000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "330b109a0bca42c09a59585a6bc95bbe",
                    "item_type": "addon",
                    "unit_price": 720,
                    "unit_price_in_decimal": "7.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7b9d918c20a54322ae5f39b61e267c7e",
                    "item_type": "addon",
                    "unit_price": 720,
                    "unit_price_in_decimal": "7.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "54b12476a1f346d88e4efbcd52012b04",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "68f768ec8c484f3bb42f5341fbb97c4c",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e4c2ee43c92a4014a0ef46e533580be8",
                    "item_type": "addon",
                    "unit_price": 1380,
                    "unit_price_in_decimal": "13.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e3d69dc83bf44920b11eb71c23651334",
                    "item_type": "addon",
                    "unit_price": 1380,
                    "unit_price_in_decimal": "13.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7bb9652091164f09860da61684e3482d",
                    "item_type": "addon",
                    "unit_price": 1440,
                    "unit_price_in_decimal": "14.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "82f06c29bbce450abfc4eb4eedc2a0c4",
                    "item_type": "addon",
                    "unit_price": 1440,
                    "unit_price_in_decimal": "14.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "55df63f4c0bc40eea4d782d6a5ce7080",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f4a8376b1e2d4bd9a2ee0a38e7ceba36",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4225eec24a7b497582ef2025f74328be",
                    "item_type": "addon",
                    "unit_price": 2760,
                    "unit_price_in_decimal": "27.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6615901cb3884a75891e04de2ae79c51",
                    "item_type": "addon",
                    "unit_price": 2760,
                    "unit_price_in_decimal": "27.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a7b33ac377ec47eab34cbd185c84ca26",
                    "item_type": "addon",
                    "unit_price": 2880,
                    "unit_price_in_decimal": "28.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "46ee65e6a539457e8b212fd3ebcf6f7a",
                    "item_type": "addon",
                    "unit_price": 2880,
                    "unit_price_in_decimal": "28.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f3efd07bd1c846979b7ad587afc62990",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f0426ea992c247bf8eda3054400f84a2",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "eefb021ee9a54c43964e52e85d8995a6",
                    "item_type": "addon",
                    "unit_price": 5520,
                    "unit_price_in_decimal": "55.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "506ddc85717c491cb73db9c3517f071e",
                    "item_type": "addon",
                    "unit_price": 5520,
                    "unit_price_in_decimal": "55.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e97e1204c9344c76991b05f103d6eb3e",
                    "item_type": "addon",
                    "unit_price": 5760,
                    "unit_price_in_decimal": "57.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a6c0c4d874244988816e1f820a2808e0",
                    "item_type": "addon",
                    "unit_price": 5760,
                    "unit_price_in_decimal": "57.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "9986bc036484442e8f6eb3c57d81fd7b",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "3a86ae9139644950b9f58160e9c16600",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b73528d898014c92b42b228999e96cf3",
                    "item_type": "addon",
                    "unit_price": 11040,
                    "unit_price_in_decimal": "110.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b260e9ce0a304773bceb9ef65337141f",
                    "item_type": "addon",
                    "unit_price": 11040,
                    "unit_price_in_decimal": "110.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "09a3139dc2ca4cb281351178d6674e7c",
                    "item_type": "addon",
                    "unit_price": 11520,
                    "unit_price_in_decimal": "115.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "55381a9ae0d141858263ba0514221b1d",
                    "item_type": "addon",
                    "unit_price": 11520,
                    "unit_price_in_decimal": "115.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "45e837a402db456ab6f85283f82597b9",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "9fe4659ec3f746908b2d3a75623fba0a",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "0e09d41bcf7c42dd9bd5bc0cbd0569b1",
                    "item_type": "addon",
                    "unit_price": 16560,
                    "unit_price_in_decimal": "165.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fc133f31626a4adc8e493b061115533e",
                    "item_type": "addon",
                    "unit_price": 16560,
                    "unit_price_in_decimal": "165.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "467dd7c42f6e43329ca60c6bedec4b14",
                    "item_type": "addon",
                    "unit_price": 17280,
                    "unit_price_in_decimal": "172.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "02c82bd9b78142758d0c97a6c3446465",
                    "item_type": "addon",
                    "unit_price": 17280,
                    "unit_price_in_decimal": "172.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4aeb40cb770341559ab8c7faa9bcf04e",
                    "item_type": "addon",
                    "unit_price": 100,
                    "unit_price_in_decimal": "1.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b277e55bb9174bee8c5aa4a08ba0bb17",
                    "item_type": "addon",
                    "unit_price": 100,
                    "unit_price_in_decimal": "1.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f8d71fd4ebee4cb2a5540a9f8fcf7349",
                    "item_type": "addon",
                    "unit_price": 100,
                    "unit_price_in_decimal": "1.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ed053ff4a289401e910eadcc37f4d717",
                    "item_type": "addon",
                    "unit_price": 2,
                    "unit_price_in_decimal": "0.0250",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7a62be94330649aabe27946f1fab985e",
                    "item_type": "addon",
                    "unit_price": 250,
                    "unit_price_in_decimal": "2.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "771b41a6a1c345e28cae9fe5b7ea2da1",
                    "item_type": "addon",
                    "unit_price": 250,
                    "unit_price_in_decimal": "2.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c02158f4c95743d79ce5d626d8a321da",
                    "item_type": "addon",
                    "unit_price": 288,
                    "unit_price_in_decimal": "2.8750",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "730c7b29e7164a00bfc03eca12a907b4",
                    "item_type": "addon",
                    "unit_price": 288,
                    "unit_price_in_decimal": "2.8750",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "d75e274ec4aa46db901f5291f7b54220",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "71a6df4e2dbb495ebc01c345d80b129a",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "2b84ccdb6e574c5482d405f88bedd79b",
                    "item_type": "addon",
                    "unit_price": 500,
                    "unit_price_in_decimal": "5.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "463dcb5983a443bcb127ecabf16258c3",
                    "item_type": "addon",
                    "unit_price": 500,
                    "unit_price_in_decimal": "5.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "85fbcc04c1ae40988c549f76767f0e5d",
                    "item_type": "addon",
                    "unit_price": 575,
                    "unit_price_in_decimal": "5.7500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e7b12b81d8844cd3b845cebddf7fde00",
                    "item_type": "addon",
                    "unit_price": 575,
                    "unit_price_in_decimal": "5.7500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fcb2a1fd4d1640ee874b41fca889af75",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ebe656e2297445bb8450133befb47c69",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f6e5a15dc3634d1cb83dc9f9efc1be9c",
                    "item_type": "addon",
                    "unit_price": 1000,
                    "unit_price_in_decimal": "10.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a86095385df44bf687fb231259347035",
                    "item_type": "addon",
                    "unit_price": 1000,
                    "unit_price_in_decimal": "10.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6c84aee723604db98cc2b1fe8cafc26b",
                    "item_type": "addon",
                    "unit_price": 1150,
                    "unit_price_in_decimal": "11.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "09ce2b4e5c0f4fe48e531809a7844ac1",
                    "item_type": "addon",
                    "unit_price": 1150,
                    "unit_price_in_decimal": "11.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6c148f5f13e545da8d1f332fbb111746",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "777f1a15eef64d57b85c7215251572b3",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ea10b95ebe3e4689a657295080fc6a68",
                    "item_type": "addon",
                    "unit_price": 2000,
                    "unit_price_in_decimal": "20.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "30c9b85f690f466b926ced70cd897d18",
                    "item_type": "addon",
                    "unit_price": 2000,
                    "unit_price_in_decimal": "20.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "1dd6807abf2f42bebf8b13acd38c8cf5",
                    "item_type": "addon",
                    "unit_price": 2300,
                    "unit_price_in_decimal": "23.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "3ce961ec16014fc2928374d0d4ea8c67",
                    "item_type": "addon",
                    "unit_price": 2300,
                    "unit_price_in_decimal": "23.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4ef0c16e9526437d9d01b9a99e454b6d",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "3887e77b18794bbe9a6d75b10ab8f2c7",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4ddd8a517bdb4c13a6ad2ced7d3232a4",
                    "item_type": "addon",
                    "unit_price": 4000,
                    "unit_price_in_decimal": "40.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "391c45cb52764607a64f3ff231c3ee1b",
                    "item_type": "addon",
                    "unit_price": 4000,
                    "unit_price_in_decimal": "40.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "225539d0e3274f2eb9d6419c29cd9003",
                    "item_type": "addon",
                    "unit_price": 4600,
                    "unit_price_in_decimal": "46.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "1b69886cbb6f47248ca82f8509ab6a2f",
                    "item_type": "addon",
                    "unit_price": 4600,
                    "unit_price_in_decimal": "46.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "2466830f458144cd995e293e5a91f528",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ea65a1a75f4b4ed58886125d82fa5509",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fa66e3515dca4edeadfc7bbe6bf435c4",
                    "item_type": "addon",
                    "unit_price": 8000,
                    "unit_price_in_decimal": "80.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6edd544a35084c65bd74a7d36ff4b284",
                    "item_type": "addon",
                    "unit_price": 8000,
                    "unit_price_in_decimal": "80.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fe25e8e6dede40baa0f5314ef198ed0b",
                    "item_type": "addon",
                    "unit_price": 9200,
                    "unit_price_in_decimal": "92.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4b9f3d8f6f374a44b5fe9998a934dcde",
                    "item_type": "addon",
                    "unit_price": 9200,
                    "unit_price_in_decimal": "92.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "70aa48577bdc4399989b52d9c530d746",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c09bbd7f8361477890b8fb7e1f4f8fff",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c2ca68e9a75743a88824c3ccf2c79209",
                    "item_type": "addon",
                    "unit_price": 12000,
                    "unit_price_in_decimal": "120.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "2a502a7f291f40f9a2a6acd9481b4666",
                    "item_type": "addon",
                    "unit_price": 12000,
                    "unit_price_in_decimal": "120.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "72d4ba11b9c54df892189f0732f20587",
                    "item_type": "addon",
                    "unit_price": 13800,
                    "unit_price_in_decimal": "138.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7cb098629855411a88dba14939c4f590",
                    "item_type": "addon",
                    "unit_price": 13800,
                    "unit_price_in_decimal": "138.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "00379518cec648aca9bcffc28e3ea80c",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "70bd47195ce445f480555ff2769bdc08",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f982af3a5de94d628f1d1cc3d32a0b93",
                    "item_type": "addon",
                    "unit_price": 360,
                    "unit_price_in_decimal": "3.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b528a741433e4e959ca2537c4fe23c84",
                    "item_type": "addon",
                    "unit_price": 720,
                    "unit_price_in_decimal": "7.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c42be8999c1d460799ce4d5710a27ca1",
                    "item_type": "addon",
                    "unit_price": 1440,
                    "unit_price_in_decimal": "14.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "42835dbff13c47bfbd65a7b6369f1740",
                    "item_type": "addon",
                    "unit_price": 2880,
                    "unit_price_in_decimal": "28.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "664f7e52159646b6ae0573c5c5b6d66c",
                    "item_type": "addon",
                    "unit_price": 5760,
                    "unit_price_in_decimal": "57.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a4177d59bc764a95b0c61f59de847c78",
                    "item_type": "addon",
                    "unit_price": 11520,
                    "unit_price_in_decimal": "115.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f8c23a4ae86a49e6b8ebe1f73b50de9d",
                    "item_type": "addon",
                    "unit_price": 17280,
                    "unit_price_in_decimal": "172.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "edcb7062e5764ff99934b9de15ebe929",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b92b394e73844e16b8dcd4c1bff4622a",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7ec69bbee1284957b9f3a4d6f8e1abc5",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "60ed739ed9814016ab8c7ccfcda9e52f",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "20e3d293d4d0466aa33d1fb8a01b3446",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "0003a9761e574bb091e4ca665bc3bdc1",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "31fef063358d4d47a38e9287077f342c",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                }
            ],
            "due_invoices_count": 0,
            "mrr": 0,
            "cf_edition": "advanced",
            "has_scheduled_advance_invoices": false,
            "create_pending_invoices": true,
            "auto_close_invoices": false,
            "trial_end_action": "site_default"
        },
        "customer": {
            "id": "acc_OnljQnIvR46ObDLAS_Ls1w",
            "company": "ExasolSignup",
            "auto_collection": "off",
            "net_term_days": 0,
            "allow_direct_debit": false,
            "created_at": 1728406412,
            "taxability": "taxable",
            "updated_at": 1728467586,
            "pii_cleared": "active",
            "channel": "web",
            "resource_version": 1728467586495,
            "deleted": false,
            "object": "customer",
            "card_status": "no_card",
            "balances": [{
                "promotional_credits": 50000,
                "excess_payments": 0,
                "refundable_credits": 0,
                "unbilled_charges": 0,
                "object": "customer_balance",
                "currency_code": "USD",
                "balance_currency_code": "USD"
            }],
            "promotional_credits": 50000,
            "refundable_credits": 0,
            "excess_payments": 0,
            "unbilled_charges": 0,
            "preferred_currency_code": "USD",
            "mrr": 0,
            "auto_close_invoices": false,
            "cf_billing_info_optional": "True",
            "cf_country": "BE",
            "meta_data": {"trigger": "customer_changed event"}
        }
    },
    "event_type": "subscription_cancelled",
    "webhook_status": "succeeded",
    "webhooks": [{
        "id": "whv2_169loNT1kUcDb2oZy",
        "webhook_status": "succeeded",
        "object": "webhook"
    }]
}

```json```



```json```

{
    "id": "ev_16CRfBUT9XSA74jk",
    "occurred_at": 1730715880,
    "source": "admin_console",
    "user": "edis.shabi@exasol.com",
    "object": "event",
    "api_version": "v2",
    "content": {
        "subscription": {
            "id": "16CMpPUToS7pJTXU",
            "billing_period": 1,
            "billing_period_unit": "month",
            "trial_end": 1732154400,
            "customer_id": "acc_OnljQnIvR46ObDLAS_Ls1w",
            "status": "in_trial",
            "trial_start": 1730715870,
            "next_billing_at": 1732154400,
            "created_at": 1730715558,
            "started_at": 1730715558,
            "updated_at": 1730715879,
            "has_scheduled_changes": false,
            "channel": "web",
            "resource_version": 1730715879360,
            "deleted": false,
            "object": "subscription",
            "currency_code": "USD",
            "subscription_items": [
                {
                    "item_price_id": "e20cbb74eebe494d83f9f7753e5b8fbd",
                    "item_type": "plan",
                    "unit_price": 0,
                    "unit_price_in_decimal": "0.0000",
                    "free_quantity": 0,
                    "free_quantity_in_decimal": "0.00000000",
                    "trial_end": 1732154400,
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c62d13fb358846f38c1075518dcaa25b",
                    "item_type": "addon",
                    "unit_price": 0,
                    "unit_price_in_decimal": "0.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "9707e2ae3a1d437ba79cff36bdfc0716",
                    "item_type": "addon",
                    "unit_price": 2,
                    "unit_price_in_decimal": "0.0250",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "bc30fbfcbb1b4148beee1e34f41cb378",
                    "item_type": "addon",
                    "unit_price": 9,
                    "unit_price_in_decimal": "0.0900",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fbc9f99548b744e9ba071b4921bc4e97",
                    "item_type": "addon",
                    "unit_price": 2,
                    "unit_price_in_decimal": "0.0250",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "12707554d3d14d6a94105a2154973021",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "bed92963d47b45bfb986442545f9a4fd",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "793f3fd4b9c64d599cbbe82de3cb8e90",
                    "item_type": "addon",
                    "unit_price": 345,
                    "unit_price_in_decimal": "3.4500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4ef25192f93f4f1eb9c701548e5285de",
                    "item_type": "addon",
                    "unit_price": 345,
                    "unit_price_in_decimal": "3.4500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b029ed933667485b82d34f4d8617a23a",
                    "item_type": "addon",
                    "unit_price": 360,
                    "unit_price_in_decimal": "3.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "00953f5b60754f84aa717478b72d7c3f",
                    "item_type": "addon",
                    "unit_price": 360,
                    "unit_price_in_decimal": "3.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "213e09107b034580bb7f51665b9d7203",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e1239d35b5404fc9baaebafba70cbeb8",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b1b39228b6d64b9a8c9d073a5a2d8543",
                    "item_type": "addon",
                    "unit_price": 690,
                    "unit_price_in_decimal": "6.9000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "091505b5fa6a4f25a13db4e9fc14b19c",
                    "item_type": "addon",
                    "unit_price": 690,
                    "unit_price_in_decimal": "6.9000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "330b109a0bca42c09a59585a6bc95bbe",
                    "item_type": "addon",
                    "unit_price": 720,
                    "unit_price_in_decimal": "7.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7b9d918c20a54322ae5f39b61e267c7e",
                    "item_type": "addon",
                    "unit_price": 720,
                    "unit_price_in_decimal": "7.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "54b12476a1f346d88e4efbcd52012b04",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "68f768ec8c484f3bb42f5341fbb97c4c",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e4c2ee43c92a4014a0ef46e533580be8",
                    "item_type": "addon",
                    "unit_price": 1380,
                    "unit_price_in_decimal": "13.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e3d69dc83bf44920b11eb71c23651334",
                    "item_type": "addon",
                    "unit_price": 1380,
                    "unit_price_in_decimal": "13.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7bb9652091164f09860da61684e3482d",
                    "item_type": "addon",
                    "unit_price": 1440,
                    "unit_price_in_decimal": "14.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "82f06c29bbce450abfc4eb4eedc2a0c4",
                    "item_type": "addon",
                    "unit_price": 1440,
                    "unit_price_in_decimal": "14.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "55df63f4c0bc40eea4d782d6a5ce7080",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f4a8376b1e2d4bd9a2ee0a38e7ceba36",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4225eec24a7b497582ef2025f74328be",
                    "item_type": "addon",
                    "unit_price": 2760,
                    "unit_price_in_decimal": "27.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6615901cb3884a75891e04de2ae79c51",
                    "item_type": "addon",
                    "unit_price": 2760,
                    "unit_price_in_decimal": "27.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a7b33ac377ec47eab34cbd185c84ca26",
                    "item_type": "addon",
                    "unit_price": 2880,
                    "unit_price_in_decimal": "28.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "46ee65e6a539457e8b212fd3ebcf6f7a",
                    "item_type": "addon",
                    "unit_price": 2880,
                    "unit_price_in_decimal": "28.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f3efd07bd1c846979b7ad587afc62990",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f0426ea992c247bf8eda3054400f84a2",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "eefb021ee9a54c43964e52e85d8995a6",
                    "item_type": "addon",
                    "unit_price": 5520,
                    "unit_price_in_decimal": "55.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "506ddc85717c491cb73db9c3517f071e",
                    "item_type": "addon",
                    "unit_price": 5520,
                    "unit_price_in_decimal": "55.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e97e1204c9344c76991b05f103d6eb3e",
                    "item_type": "addon",
                    "unit_price": 5760,
                    "unit_price_in_decimal": "57.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a6c0c4d874244988816e1f820a2808e0",
                    "item_type": "addon",
                    "unit_price": 5760,
                    "unit_price_in_decimal": "57.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "9986bc036484442e8f6eb3c57d81fd7b",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "3a86ae9139644950b9f58160e9c16600",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b73528d898014c92b42b228999e96cf3",
                    "item_type": "addon",
                    "unit_price": 11040,
                    "unit_price_in_decimal": "110.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b260e9ce0a304773bceb9ef65337141f",
                    "item_type": "addon",
                    "unit_price": 11040,
                    "unit_price_in_decimal": "110.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "09a3139dc2ca4cb281351178d6674e7c",
                    "item_type": "addon",
                    "unit_price": 11520,
                    "unit_price_in_decimal": "115.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "55381a9ae0d141858263ba0514221b1d",
                    "item_type": "addon",
                    "unit_price": 11520,
                    "unit_price_in_decimal": "115.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "45e837a402db456ab6f85283f82597b9",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "9fe4659ec3f746908b2d3a75623fba0a",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "0e09d41bcf7c42dd9bd5bc0cbd0569b1",
                    "item_type": "addon",
                    "unit_price": 16560,
                    "unit_price_in_decimal": "165.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fc133f31626a4adc8e493b061115533e",
                    "item_type": "addon",
                    "unit_price": 16560,
                    "unit_price_in_decimal": "165.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "467dd7c42f6e43329ca60c6bedec4b14",
                    "item_type": "addon",
                    "unit_price": 17280,
                    "unit_price_in_decimal": "172.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "02c82bd9b78142758d0c97a6c3446465",
                    "item_type": "addon",
                    "unit_price": 17280,
                    "unit_price_in_decimal": "172.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4aeb40cb770341559ab8c7faa9bcf04e",
                    "item_type": "addon",
                    "unit_price": 100,
                    "unit_price_in_decimal": "1.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b277e55bb9174bee8c5aa4a08ba0bb17",
                    "item_type": "addon",
                    "unit_price": 100,
                    "unit_price_in_decimal": "1.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f8d71fd4ebee4cb2a5540a9f8fcf7349",
                    "item_type": "addon",
                    "unit_price": 100,
                    "unit_price_in_decimal": "1.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ed053ff4a289401e910eadcc37f4d717",
                    "item_type": "addon",
                    "unit_price": 2,
                    "unit_price_in_decimal": "0.0250",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7a62be94330649aabe27946f1fab985e",
                    "item_type": "addon",
                    "unit_price": 250,
                    "unit_price_in_decimal": "2.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "771b41a6a1c345e28cae9fe5b7ea2da1",
                    "item_type": "addon",
                    "unit_price": 250,
                    "unit_price_in_decimal": "2.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c02158f4c95743d79ce5d626d8a321da",
                    "item_type": "addon",
                    "unit_price": 288,
                    "unit_price_in_decimal": "2.8750",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "730c7b29e7164a00bfc03eca12a907b4",
                    "item_type": "addon",
                    "unit_price": 288,
                    "unit_price_in_decimal": "2.8750",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "d75e274ec4aa46db901f5291f7b54220",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "71a6df4e2dbb495ebc01c345d80b129a",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "2b84ccdb6e574c5482d405f88bedd79b",
                    "item_type": "addon",
                    "unit_price": 500,
                    "unit_price_in_decimal": "5.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "463dcb5983a443bcb127ecabf16258c3",
                    "item_type": "addon",
                    "unit_price": 500,
                    "unit_price_in_decimal": "5.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "85fbcc04c1ae40988c549f76767f0e5d",
                    "item_type": "addon",
                    "unit_price": 575,
                    "unit_price_in_decimal": "5.7500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "e7b12b81d8844cd3b845cebddf7fde00",
                    "item_type": "addon",
                    "unit_price": 575,
                    "unit_price_in_decimal": "5.7500",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fcb2a1fd4d1640ee874b41fca889af75",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ebe656e2297445bb8450133befb47c69",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f6e5a15dc3634d1cb83dc9f9efc1be9c",
                    "item_type": "addon",
                    "unit_price": 1000,
                    "unit_price_in_decimal": "10.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a86095385df44bf687fb231259347035",
                    "item_type": "addon",
                    "unit_price": 1000,
                    "unit_price_in_decimal": "10.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6c84aee723604db98cc2b1fe8cafc26b",
                    "item_type": "addon",
                    "unit_price": 1150,
                    "unit_price_in_decimal": "11.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "09ce2b4e5c0f4fe48e531809a7844ac1",
                    "item_type": "addon",
                    "unit_price": 1150,
                    "unit_price_in_decimal": "11.5000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6c148f5f13e545da8d1f332fbb111746",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "777f1a15eef64d57b85c7215251572b3",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ea10b95ebe3e4689a657295080fc6a68",
                    "item_type": "addon",
                    "unit_price": 2000,
                    "unit_price_in_decimal": "20.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "30c9b85f690f466b926ced70cd897d18",
                    "item_type": "addon",
                    "unit_price": 2000,
                    "unit_price_in_decimal": "20.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "1dd6807abf2f42bebf8b13acd38c8cf5",
                    "item_type": "addon",
                    "unit_price": 2300,
                    "unit_price_in_decimal": "23.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "3ce961ec16014fc2928374d0d4ea8c67",
                    "item_type": "addon",
                    "unit_price": 2300,
                    "unit_price_in_decimal": "23.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4ef0c16e9526437d9d01b9a99e454b6d",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "3887e77b18794bbe9a6d75b10ab8f2c7",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4ddd8a517bdb4c13a6ad2ced7d3232a4",
                    "item_type": "addon",
                    "unit_price": 4000,
                    "unit_price_in_decimal": "40.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "391c45cb52764607a64f3ff231c3ee1b",
                    "item_type": "addon",
                    "unit_price": 4000,
                    "unit_price_in_decimal": "40.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "225539d0e3274f2eb9d6419c29cd9003",
                    "item_type": "addon",
                    "unit_price": 4600,
                    "unit_price_in_decimal": "46.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "1b69886cbb6f47248ca82f8509ab6a2f",
                    "item_type": "addon",
                    "unit_price": 4600,
                    "unit_price_in_decimal": "46.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "2466830f458144cd995e293e5a91f528",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "ea65a1a75f4b4ed58886125d82fa5509",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fa66e3515dca4edeadfc7bbe6bf435c4",
                    "item_type": "addon",
                    "unit_price": 8000,
                    "unit_price_in_decimal": "80.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "6edd544a35084c65bd74a7d36ff4b284",
                    "item_type": "addon",
                    "unit_price": 8000,
                    "unit_price_in_decimal": "80.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "fe25e8e6dede40baa0f5314ef198ed0b",
                    "item_type": "addon",
                    "unit_price": 9200,
                    "unit_price_in_decimal": "92.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "4b9f3d8f6f374a44b5fe9998a934dcde",
                    "item_type": "addon",
                    "unit_price": 9200,
                    "unit_price_in_decimal": "92.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "70aa48577bdc4399989b52d9c530d746",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c09bbd7f8361477890b8fb7e1f4f8fff",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c2ca68e9a75743a88824c3ccf2c79209",
                    "item_type": "addon",
                    "unit_price": 12000,
                    "unit_price_in_decimal": "120.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "2a502a7f291f40f9a2a6acd9481b4666",
                    "item_type": "addon",
                    "unit_price": 12000,
                    "unit_price_in_decimal": "120.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "72d4ba11b9c54df892189f0732f20587",
                    "item_type": "addon",
                    "unit_price": 13800,
                    "unit_price_in_decimal": "138.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7cb098629855411a88dba14939c4f590",
                    "item_type": "addon",
                    "unit_price": 13800,
                    "unit_price_in_decimal": "138.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "00379518cec648aca9bcffc28e3ea80c",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "70bd47195ce445f480555ff2769bdc08",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f982af3a5de94d628f1d1cc3d32a0b93",
                    "item_type": "addon",
                    "unit_price": 360,
                    "unit_price_in_decimal": "3.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b528a741433e4e959ca2537c4fe23c84",
                    "item_type": "addon",
                    "unit_price": 720,
                    "unit_price_in_decimal": "7.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "c42be8999c1d460799ce4d5710a27ca1",
                    "item_type": "addon",
                    "unit_price": 1440,
                    "unit_price_in_decimal": "14.4000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "42835dbff13c47bfbd65a7b6369f1740",
                    "item_type": "addon",
                    "unit_price": 2880,
                    "unit_price_in_decimal": "28.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "664f7e52159646b6ae0573c5c5b6d66c",
                    "item_type": "addon",
                    "unit_price": 5760,
                    "unit_price_in_decimal": "57.6000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "a4177d59bc764a95b0c61f59de847c78",
                    "item_type": "addon",
                    "unit_price": 11520,
                    "unit_price_in_decimal": "115.2000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "f8c23a4ae86a49e6b8ebe1f73b50de9d",
                    "item_type": "addon",
                    "unit_price": 17280,
                    "unit_price_in_decimal": "172.8000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "edcb7062e5764ff99934b9de15ebe929",
                    "item_type": "addon",
                    "unit_price": 300,
                    "unit_price_in_decimal": "3.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "b92b394e73844e16b8dcd4c1bff4622a",
                    "item_type": "addon",
                    "unit_price": 600,
                    "unit_price_in_decimal": "6.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "7ec69bbee1284957b9f3a4d6f8e1abc5",
                    "item_type": "addon",
                    "unit_price": 1200,
                    "unit_price_in_decimal": "12.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "60ed739ed9814016ab8c7ccfcda9e52f",
                    "item_type": "addon",
                    "unit_price": 2400,
                    "unit_price_in_decimal": "24.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "20e3d293d4d0466aa33d1fb8a01b3446",
                    "item_type": "addon",
                    "unit_price": 4800,
                    "unit_price_in_decimal": "48.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "0003a9761e574bb091e4ca665bc3bdc1",
                    "item_type": "addon",
                    "unit_price": 9600,
                    "unit_price_in_decimal": "96.0000",
                    "object": "subscription_item"
                },
                {
                    "item_price_id": "31fef063358d4d47a38e9287077f342c",
                    "item_type": "addon",
                    "unit_price": 14400,
                    "unit_price_in_decimal": "144.0000",
                    "object": "subscription_item"
                }
            ],
            "due_invoices_count": 0,
            "cf_edition": "advanced",
            "has_scheduled_advance_invoices": false,
            "create_pending_invoices": true,
            "auto_close_invoices": false,
            "trial_end_action": "site_default"
        },
        "customer": {
            "id": "acc_OnljQnIvR46ObDLAS_Ls1w",
            "company": "exasol",
            "auto_collection": "off",
            "net_term_days": 0,
            "allow_direct_debit": false,
            "created_at": 1730715556,
            "taxability": "taxable",
            "updated_at": 1730715556,
            "pii_cleared": "active",
            "channel": "web",
            "resource_version": 1730715556935,
            "deleted": false,
            "object": "customer",
            "card_status": "no_card",
            "balances": [{
                "promotional_credits": 50000,
                "excess_payments": 0,
                "refundable_credits": 0,
                "unbilled_charges": 0,
                "object": "customer_balance",
                "currency_code": "USD",
                "balance_currency_code": "USD"
            }],
            "promotional_credits": 50000,
            "refundable_credits": 0,
            "excess_payments": 0,
            "unbilled_charges": 0,
            "preferred_currency_code": "USD",
            "mrr": 0,
            "auto_close_invoices": false,
            "cf_billing_info_optional": "True",
            "cf_country": "AR"
        }
    },
    "event_type": "subscription_reactivated",
    "webhook_status": "succeeded",
    "webhooks": [
        {
            "id": "whv2_AzqaLxURqS6eb20p4",
            "webhook_status": "not_applicable",
            "object": "webhook"
        },
        {
            "id": "whv2_169loNT1kUcDb2oZy",
            "webhook_status": "succeeded",
            "object": "webhook"
        }
    ]
}

