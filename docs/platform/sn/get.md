---
sidebar_position: 1
---

# get

### 操作概述

查询集群序列号和各组件授权信息

### 命令参数

```bash
-i|--is-all=integer         是否返回全部序列号信息。1=返回全部，0=仅返回基础信息
-g|--get-used=integer       是否返回已使用信息。1=返回已使用统计，0=不返回
-o|--only-nfv=integer       只获取 nfv 授权信息。1=是，0=否
-n|--no-filter-sn=integer   不过滤序列号。1=是，0=否
-s|--sn-modules=string      获取指定授权模块的授权数据，需传 JSON 数组格式，示例：['asv','anet']
```

### 使用示例

```bash
acli platform sn get
acli platform sn get --sn-modules '["asv","anet"]'
```

### 结果示例

```bash
{
  "aapi": {
    "activated": 0,
    "authorize_status": 0,
    "component_version": "7.0.0",
    "end_time": 0,
    "never_expired": 1,
    "remain_days": -2,
    "sec_device": 0,
    "sec_device_used": 0,
    "start_time": 0
  },
  "acmp": {
    "acmp_cpu": 0,
    "activated": 0,
    "authorize_status": 0,
    "component_version": "7.0.0",
    "enable_cm": 0,
    "end_time": 0,
    "never_expired": 0,
    "remain_days": -2,
    "start_time": 0,
    "version": 1
  },
  "adesk": {
    "component_version": "7.0.0",
    "coremax": 0,
    "date": "1970-01-01 08:00:00",
    "last_days": -1,
    "sn_flag": 0,
    "sn_test": 0,
    "upgrade_expire_date": "1970-01-01 08:00:00",
    "upgrade_remain_days": -1,
    "version": 0,
    "vm2d_cpu_limit": 0,
    "vm2d_mem_limit": 0,
    "vm3d_cpu_limit": 0,
    "vm3d_mem_limit": 0
  },
  "agpu": {
    "activated": 1,
    "agpu_used": 0,
    "authorize_status": 1,
    "component_version": "7.0.0",
    "end_time": 1791333871,
    "never_expired": 0,
    "physical_graphics_limit": 9999,
    "remain_days": 28
  },
  "ahm": {
    "activated": 1,
    "authorize_status": 1,
    "component_version": "7.0.0",
    "cpu_type": 0,
    "enable_vmware_management": 1,
    "end_time": 1791333871,
    "never_expired": 0,
    "remain_days": 28,
    "start_time": 1776237704,
    "version": 0,
    "vmware_backup_vm": 1000,
    "vmware_backup_vm_unlimited": 0
  },
  "anet": {
    "activated": 1,
    "anet_cpu": 9999,
    "anet_cpu_used": 3,
    "authorize_status": 1,
    "bvs_max": 0,
    "bvs_unlimited": 1,
    "component_version": "7.0.0",
    "cpu_type": 0,
    "dvs_max": 0,
    "dvs_unlimited": 1,
    "enable_apm": 1,
    "enable_dfw": 1,
    "end_time": 1791333871,
    "never_expired": 0,
    "remain_days": 28,
    "start_time": 1776237704,
    "version": 1,
    "vr_max": 0,
    "vr_unlimited": 1
  },
  "asan": {
    "component_version": "7.0.0_B",
    "use_vs": 1,
    "vs_cpu_limit": 9999,
    "vs_cpu_used": 3,
    "vs_last_days": 0,
    "vs_sn": "J3CmNwAAAgAACAAQDycAAAAAAAAAAAAAAAAAAAAAAACAAAAAOdMLlX6D8qNiPKq14I2CUy5xavgEUYxyfQes30zU4P5EAO2fAqiRvoOR6a9dQz3Xah2lQtyjIyw0dwQX3e1lmMNZxfKLIkYTrAZIUY+0twaF0N043mIE5/wtRIc/ewwC57zD8C/sXPHf2zDlyAh72QsKWVnAtK2cGk14PFvlrM8="
  },
  "asan-adesk": {
    "component_version": "7.0.0_B",
    "use_vs": 0,
    "vs_cpu_limit": 0,
    "vs_cpu_used": 0,
    "vs_last_days": 0,
    "vs_sn": ""
  },
  "asc": {
    "activated": 1,
    "component_version": "7.0.0_B",
    "never_expired": 0,
    "use_vs": 1,
    "vs_cpu": 9999,
    "vs_cpu_limit": 9999,
    "vs_cpu_used": 0,
    "vs_last_days": null,
    "vs_sn": ""
  },
  "asv": {
    "component_version": "7.0.0",
    "coremax": 9999,
    "date": "2026-10-07 08:44:31",
    "dev_count": 0,
    "enable_cm": 0,
    "enable_sdn": 0,
    "key_state": 0,
    "key_type": 0,
    "keyid": "FFFFFFFFFFFFFFFF",
    "last_days": 28,
    "local_vls_sn": 0,
    "new_keyid": "",
    "sn": "RYNSK3K3-4V2S7W48-7J5QCQJA-CFWLESA9-M7DCRVXX",
    "sn_flag": 2,
    "sn_test": 0,
    "tp_last_days": 88,
    "upgrade_expire_date": "2026-10-07 08:44:31",
    "upgrade_remain_days": 28,
    "user_name": "",
    "version": 6,
    "vmmax1": 0,
    "vmmax2": 0,
    "vmmem1": 0,
    "vmmem2": 0
  },
  "auth_mode": "key",
  "cdp": {
    "activated": 1,
    "authorize_status": 1,
    "component_version": "7.0.0",
    "cpu_type": 0,
    "end_time": 1791333871,
    "never_expired": 0,
    "protect_vm": 1000,
    "protect_vm_unlimited": 0,
    "remain_days": 28,
    "start_time": 1776237704,
    "version": 0
  },
  "cloud_manager_auth": 0,
  "cross_data": {
    "is_platform_expired": 0,
    "platform_last_days": 28,
    "sn_flag": 2,
    "upgrade_expire_date": "2026-10-07 08:44:31",
    "upgrade_remain_days": 28
  },
  "key_state": 0,
  "key_type": 0,
  "keyid": "FFFFFFFFFFFFFFFF",
  "meta_authinfo": {
    "authorize_mode": "0"
  },
  "new_keyid": "",
  "sn": "RYNSK3K3-4V2S7W48-7J5QCQJA-CFWLESA9-M7DCRVXX",
  "sn_type": 2,
  "tp_last_days": -1,
  "upload_host": "host-0050568ec35e",
  "use_apm_num": 0,
  "use_dfw": 1,
  "use_key": 1,
  "use_keyid": "FFFFFFFFFFFFFFFF",
  "use_route": 1,
  "use_route_num": -1,
  "use_sdn": 1,
  "use_switch": 1,
  "use_switch_num": -1,
  "use_vac": "nodevsn",
  "use_vad": "nodevsn",
  "use_vaf": "nodevsn",
  "use_vapm": "ok",
  "use_vdas": "nodevsn",
  "use_viam": "nodevsn",
  "use_vnetdev": "ok",
  "use_vssl": "nodevsn",
  "use_vwoc": "nodevsn",
  "vkey_global": {
    "clusterid": "",
    "verify_code": ""
  },
  "vnet_info": {}
}
```
