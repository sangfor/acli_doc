---
sidebar_position: 1
---

# check_host

### 操作概述

检查宿主机环境信息：CPU、内存、超线程等

### 命令参数

```bash
-a|--checkall                 对告警等级为低的检测项也进行告警，默认对告警等级为低的检测项不进行告警
-d|--date=string              指定检查时间，仅部分检测项支持，格式：2006-01-02 15:04:05
-v|--desc                     打印主机环境详细信息
--force-terminal              主机数量较多时，也强制将结果输出到终端上，不写入文件
--html-output=string          HTML 格式输出文件路径，不存在会自动创建（默认：/sf/data/local/performance_tools/check_result/checkhost_output.html）
--ips=string                  指定要检测的远程主机，格式：使用逗号分割的集群主机管理IP 或 all，示例：1.1.1.1,1.1.1.2
-o|--output=string            输出文件路径，不存在会自动创建（默认：/sf/data/local/performance_tools/check_result/output.txt）
--skip-lock                   检测时是否加锁，程序内部使用，不建议用户使用
--lang=string                 设置命令行输出语言，可选项：zh_CN、en_US（全局参数）
-h|--help                     显示帮助信息
```

### 使用示例

```bash
# 示例1：检查当前主机环境信息
acli performance_tools check_host

# 示例2：检查当前主机环境信息并打印详细信息
acli performance_tools check_host -v

# 示例3：检查所有主机环境信息
acli performance_tools check_host --ips all

# 示例4：检查指定主机环境信息
acli performance_tools check_host --ips 10.131.136.156,10.131.136.157

# 示例5：检查所有主机并包含低告警等级的检测项
acli performance_tools check_host --ips all -a

# 示例6：检查主机环境信息并指定输出文件
acli performance_tools check_host --ips all -o /tmp/host_check.txt

# 示例7：检查主机环境信息并指定 HTML 输出文件
acli performance_tools check_host --ips all --html-output /tmp/host_check.html

# 示例8：主机数量较多时强制输出到终端
acli performance_tools check_host --ips all --force-terminal

# 示例9：检查主机环境信息并指定检查时间
acli performance_tools check_host -d "2025-06-25 10:30:00"
```

### 结果示例

```bash
正在检查主机10.131.136.156
欢迎使用虚拟机检测工具！当前时间 2026-04-08 14:29:15
正在进行主机检测...
主机名: host-0050568eb9d8
CPU型号: Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
CPU核心数: 8
CPU使用率: 30.81 %
主机总内存大小: 33.28 GB
主机剩余内存大小 17.46 GB
运行虚拟机数量: 1
集群类型: HCI
-----------------------------------------------------------------------------------------------------------------------------------

一、检查主机CPU信息
1.1 CPU sys使用率 √
详细信息: 物理主机的CPU sys使用率为10.00%，检测阈值为15.00%

1.2 非转发核单核CPU使用率 √
详细信息: 非转发核单核CPU使用率最高为33.33%，检测阈值为95.00%

1.3 SPDK 转发核占用情况 √ 
详细信息: SPDK 转发核核使用率为0.00%，检测阈值为90.00%

1.4 CPU超配比检测 √
详细信息: 主机CPU超配比为200.00%，检测阈值为200.00%
主机当时运行虚拟机列表如下：
VMID                 CPU        MEM        %CPU_UTIL  MEM_USED        VmName                                            
6025407369236        8          4.00GB     1.27       436.14MB        123                                               


1.5 检查主机SMI中断 √ 
详细信息: 主机CPU不存在SMI中断

1.6 主机CPU iowait检测 √
详细信息: 主机CPU iowait占用率为0.00%，检测阈值为10.00%

1.7 检查主机非独占CPU使用率 √ 
详细信息: 环境上无独占虚拟机，无需检测

1.8 CPU超线程 √
详细信息: 物理主机未开启CPU超线程

1.9 CPU降频检查 √ 
详细信息: 无法获取当前环境睿频信息

1.10 CPU使用率 √
详细信息: 物理主机的CPU使用率为30.81%，检测阈值为65.00%
当时CPU占用最高的10个进程为：
PID        %CPU  MEM      STAT  START    TIME     COMMAND                                           
40576      52.9  1.16GB   S<Ll  07:07    233:34   /sf/sdn/bin/dataplane --proc-type secondary -l 1,2...
50179      14.0  35.84MB  S<l   07:08    62:02    -w                                                
193558     10.2  436.14MB Sl    07:14    44:39    /usr/bin/kvm -id 6025407369236 -chardev socket,id=...
1052034    7.1   505.92MB S     14:28    0:02     vtpdaemon                                         
996744     7.0   509.74MB S     14:24    0:22     vtpdaemon                                         
998480     6.7   508.87MB S     14:24    0:20     vtpdaemon                                         
1045828    6.7   508.92MB S     14:28    0:04     vtpdaemon                                         
997194     6.5   508.28MB S     14:24    0:20     vtpdaemon                                         
998461     6.4   507.48MB S     14:24    0:19     vtpdaemon                                         
1038296    6.0   506.55MB S     14:27    0:06     vtpdaemon                                         


1.11 CPU主频检测 √ 
详细信息: CPU主频为2.2GHz，检测阈值为2.4GHz

1.12 CPU时钟源检测 √
详细信息: CPU时钟源为tsc，X86和C86架构检测时钟源需要是tsc
```
