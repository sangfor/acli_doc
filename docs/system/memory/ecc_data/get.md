---
sidebar_position: 10
---

# get
操作概述: 查看/var/ECC_data文件内容

命令参数:
```bash
无
```

使用示例:
```bash
# 查看/var/ECC_data文件内容
acli system memory ecc_data get
```

结果示例:
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