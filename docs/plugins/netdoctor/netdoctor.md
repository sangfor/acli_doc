---
sidebar_position: 1
---

# netdoctor

### 操作概述

进行网络相关问题的排障，支持诊断箱（多场景排障）和工具箱（快速工具）两种模式。

### 命令参数

```bash
acli netdoctor [OPTIONS]

# 诊断箱参数

| 参数 | 说明 |
|------|------|
| `-c` / `--case=string` | （必要参数）排障场景选择，支持英文逗号拼接多场景，示例：`vm` 或 `vm,mgmt` |
| `-d` / `--date=string` | 指定日期的日志，示例：`2023-06-25` 或 `2023-06-25,07:37`（日期和时间使用英文逗号分隔） |

可供选择的场景：
- `vm`（虚拟机丢包诊断）
- `mgmt`（管理网丢包诊断）
- `vxlan`（VxLAN网丢包诊断）
- `vs`（存储网丢包诊断）
- `offline`（主机离线诊断）
- `perf`（虚拟机时延卡顿诊断）
- `drop`（物理口丢包/错包诊断）
- `nic`（主机网卡诊断）
- `upg`（升级诊断）
- `srv`（虚拟网络服务异常诊断）
- `all`（全场景诊断）

# 工具箱参数

| 参数 | 说明 |
|------|------|
| `-t` / `--tool=string` | 工具箱模式，快速执行指定工具 |

可供选择的工具：
- `vlink`（检查VM vlink状态，可指定VMID）
- `ifaces`（查看所有网口信息）
- `ifcheck`（检查指定网口统计信息）
- `ifstat`（检测网口RX/TX详细收发包信息）
- `ifirq`（查看所有网口中断核分布信息）
- `vmmac`（检查VM MAC地址冲突）
- `ipmac`（检查集群IP和MAC冲突情况）
- `fullsync`（执行全同步）
- `reorder`（执行网卡序调整）
- `topo`（VM到VM网络拓扑路径分析）
- `dfw`（分布式防火墙工具箱）
- `ifcfg`（后端网口配置工具箱）
- `mirror`（流镜像配置工具箱）
- `netdump`（高效抓包工具）
```

### 使用示例

```bash
# 示例1：默认不带参数，展示各排障场景供选择
acli netdoctor

# 示例2：指定单个场景进行诊断
acli netdoctor -c vm

# 示例3：指定多个场景进行诊断（英文逗号分隔）
acli netdoctor -c vm,mgmt

# 示例4：指定场景并搜索指定日期的日志
acli netdoctor -c all -d 2023-06-26,07:37

# 示例5：使用工具箱检查所有虚拟机vlink
acli netdoctor -t vlink

# 示例6：使用工具箱检查指定虚拟机的vlink
acli netdoctor -t vlink <vm_id>

# 示例7：使用工具箱查看所有网口信息
acli netdoctor -t ifaces

# 示例8：使用工具箱查看所有网口中断核分布
acli netdoctor -t ifirq

# 示例9：使用工具箱检查VM MAC地址冲突
acli netdoctor -t vmmac

# 示例10：使用工具箱检查集群IP和MAC冲突情况
acli netdoctor -t ipmac

# 示例11：使用工具箱执行全同步
acli netdoctor -t fullsync

# 示例12：使用工具箱执行网卡序调整
acli netdoctor -t reorder

# 示例13：使用工具箱进行VM到VM网络拓扑路径分析
acli netdoctor -t topo

# 示例14：使用工具箱进入分布式防火墙工具箱
acli netdoctor -t dfw

# 示例15：使用工具箱进入后端网口配置工具箱
acli netdoctor -t ifcfg

# 示例16：使用工具箱进入流镜像配置工具箱
acli netdoctor -t mirror

# 示例17：使用工具箱进入高效抓包工具
acli netdoctor -t netdump
```

### 结果示例

```bash
============================诊断虚拟机网络============================
如果要检查某个虚拟机的网络，请输入VMID，否则请输入（y/Y）键继续：
y
========================================================================

[1] 诊断集群所有虚拟机vlink情况(如果虚拟机较多可能耗时过长)，请稍等...

=> 正在诊断集群所有虚拟机是否存在 vlink，请稍等...
VM(vmid: 6025407369236, name: 123) 的第 1 张网卡没连线
所有虚拟机都检测完成，所检虚拟机都有vlink
有虚拟机没有连线，请判断如跟问题不相关，可忽略

[2] 诊断是否网络数据面异常导致的丢包，请稍等...

=>检查dp服务是否存在异常，请稍等...

=>检查集群所有主机dataplane服务是否在运行，请稍等...

=>检查集群所有主机除dp外的其他SDN服务是否在运行，请稍等...

=>检查当前主机dataplane服务启动时间，请稍等...
当前主机 dataplane 在 today 这天启动过，启动时间为：2026-04-08 07:08:00.772008186，请确认如果是重启过主机或人为重启过SDN服务，可以忽略

=>检查集群所有主机SDN服务状态当前是否正常，请稍等...

=>检查集群所有主机today这天blackbox日志SDN服务状态是否正常，请稍等...

=>检查集群所有主机SDN服务是否出过core，请稍等...

=>诊断网卡是否存在乱序问题，请稍等...
```

