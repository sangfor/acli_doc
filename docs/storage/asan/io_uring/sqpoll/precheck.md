---
sidebar_position: 1
---

# precheck

### 操作概述

检查虚拟存储卷内主机是否支持开启io_uring的sqpoll特性

### 命令参数

```bash
-v|--volume-id=string    必要参数，存储卷id，示例：a4ef106e_vs_vol_rep2
```

### 使用示例

```bash
acli storage asan io_uring sqpoll precheck -v a4ef106e_vs_vol_rep2
```

### 结果示例

全部检查通过：

```bash
sqpoll-precheck vol=a4ef106e_vs_vol_rep2                     STATUS: SUCCESS

  VOLUME CHECKS
    upgrade_in_progress  PASS
    volume_available     PASS
    volume_type          PASS

  host-002246213d6b                                                     PASS
  host-6c92bf51945a                                                     PASS
```

存在未通过的检查项时，失败主机会逐项展开，并在 `BLOCKED BY` 中给出阻塞原因：

```bash
sqpoll-precheck vol=a4ef106e_vs_vol_rep2                      STATUS: FAILED

  VOLUME CHECKS
    upgrade_in_progress  PASS
    volume_available     PASS
    volume_type          FAIL

  host-002246213d6b                                                   FAILED
    sqpoll_storage_eligible  PASS
    tier_v2                  PASS
    kernel_version           FAIL
    legacy_libaio_engine     PASS
    host_maintain            PASS
    cache_disk_maintain      PASS
    nvme_cache_disk_count    PASS
    cpu_count                PASS
  host-6c92bf51945a                                                     PASS

  BLOCKED BY
    volume             volume_type     compound or non-blend volume is not supported
    host-002246213d6b  kernel_version  kernel version below 6.6
```

### 检查项说明

| 检查项 | 级别 | 说明 |
| :---: | :---: | :--- |
| `upgrade_in_progress` | 卷 | 集群/补丁升级进行中则不允许开启 |
| `volume_available` | 卷 | 卷状态必须为 available |
| `volume_type` | 卷 | 不支持复合卷、非混闪卷(全闪卷无缓存层无需开启) |
| `sqpoll_storage_eligible` | 主机 | 缓存盘必须全部为 NVMe 盘 |
| `tier_v2` | 主机 | 不支持分层 v2 版本 |
| `kernel_version` | 主机 | 内核版本需不低于 6.6 |
| `legacy_libaio_engine` | 主机 | 分层IO引擎必须为 cdev_iouring（cdev_aio 不允许） |
| `host_maintain` | 主机 | 主机不能处于维护模式 |
| `cache_disk_maintain` | 主机 | 缓存盘不能处于维护模式 |
| `nvme_cache_disk_count` | 主机 | NVMe 缓存盘数量需为 1~2 块 |
| `cpu_count` | 主机 | 逻辑核数需不少于 16 |