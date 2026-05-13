---
sidebar_position: 1
---

# get

### Overview

Obtain ECC data from system memory

### Command Parameters

No parameters
### Usage Example

```bash
# View the contents of /var/ECC_data file
acli system memory ecc_data get
```

### Output Example

```bash
{
    "ECC_UE": {
       "UE_error_sign": 0,
       "index": []
    },
    "ECC_UE": {
       "CPU0-MV1-CHAN0-DIMM0-UE_count": 160,
        "CPU0-MV1-CHAN0-DIMM1",
       "UE_error_sign": 1,
       "index": [
        "CPU0-MV1-CHAN0-DIMM1",
        ]
    },
    "ECC_UE": {
       "UE_error_sign": 0,
       "index": []
    },
}
```