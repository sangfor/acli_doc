---
sidebar_position: 1
---

# set

### 操作概述

设置指定节点上指定 vendor/product 的 device 级 multipath 自定义配置

### 命令参数

```bash
-n|--hostname=string              可选参数，目标主机名，缺省为当前节点，示例：host-xxxx
-v|--vendor=string                必要参数，multipath.conf vendor 字段，示例：DellEMC
-p|--product=string               必要参数，multipath.conf product 字段，示例：PowerStore
--path_grouping_policy=string     可选参数，路径分组策略，可选值：failover（主备模式）/multibus（默认，负载均衡模式）/group_by_prio（按路径优先级分组）/group_by_serial（按储存控制器序号分组）/group_by_node_name（按目标节点名称分组），示例：--path_grouping_policy=failover
--path_selector=string            可选参数，路径选择算法，可选值：round-robin 0（默认）/service-time 0/queue-length 0，示例：--path_selector="service-time 0"
--path_checker=string             可选参数（高危），路径状态检测方式，可选值：tur（默认）/directio/readsector0/emc_clariion/hp_sw/rdac/cciss_tur/none，示例：--path_checker=tur
--detect_checker=string           可选参数（高危），自动选择路径检测方式，可选值：yes（默认）/no，示例：--detect_checker=yes
--prio=string                     可选参数，路径优先级计算方式，可选值：alua/const（默认）/rdac/ontap/emc/hp_sw/hds/datacore/random/sysfs/ana/weightedpath/path_latency/iet，示例：--prio=const
--prio_args=string                可选参数，优先级附加参数，exclusive_pref_bit（仅 prio alua/sysfs 生效）/preferredip=ip（仅 prio iet 生效），示例：--prio_args="exclusive_pref_bit"
--detect_prio=string              可选参数，自动检测优先级方式，可选值：yes（默认）/no，示例：--detect_prio=yes
--failback=string                 可选参数，高优先级路径组故障恢复切换策略，可选值：immediate（默认）/manual/followover/<正整数>（延迟 N 秒后切换），示例：--failback=immediate
--rr_weight=string                可选参数，轮询路径权重分配方式，可选值：uniform（默认）/priorities，示例：--rr_weight=priorities
--dev_loss_tmo=string             可选参数，物理路径丢失后等待移除设备的最长时间，可选值：infinity（默认，永不超时）/<整数>（N 秒后删除），示例：--dev_loss_tmo=infinity
--fast_io_fail_tmo=string         可选参数，物理路径故障时阻塞 I/O 的最长等待时间（必须小于 dev_loss_tmo），可选值：off（禁用）/<整数>（N 秒后失败，默认 5），示例：--fast_io_fail_tmo=5
--no_path_retry=string            可选参数，所有路径离线时的 I/O 重试行为，可选值：fail（默认，立即失败）/queue（一直排队重试）/<正整数>（重试 N 次后失败），示例：--no_path_retry=fail
--uid_attribute=string            可选参数（高危），指定 udev 属性作为路径 WWID，可选值：ID_SERIAL（默认）/ID_WWN/ID_UID，示例：--uid_attribute=ID_SERIAL
--features=string                 可选参数，启用的内核多路径模块特殊功能，默认值 0，格式：features "N feature1 [args] ..."，支持 feature 类型：queue_if_no_path/pg_init_retries [N]/pg_init_delay_msecs [N]，示例：--features="1 queue_if_no_path"
--max_sectors_kb=string           可选参数，LUN 设备单次下发的最大扇区数，可选值：0（默认，使用系统默认）/<正整数>（单位 kb），示例：--max_sectors_kb=0
--flush_on_last_del=string        可选参数（高危），最后一个路径被删除时的删除策略，可选值：never（有 I/O 在排队则拒绝删除）/unused（默认，LUN 设备正在被打开使用则拒绝删除）/always（触发刷 I/O 后再删除，可能卡主），示例：--flush_on_last_del=unused
```


### 使用示例

```bash
acli system multipathconfig devicepolicy set -n host-xxxx -v DellEMC -p PowerStore --path_checker tur --features "1 queue_if_no_path"
```

### 结果示例

```bash
{"affected_storages": ["3648bd4a100fa95b6550a2d9c000002ac"]}
```
