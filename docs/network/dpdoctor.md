---
sidebar_position: 1
---

# dpdoctor

### 操作概述

执行数据面排障检查，查看环境、网卡、服务状态及会话等统计信息。

### 命令参数

命令格式：

```bash
acli network dpdoctor <OPTIONS> <VALUE>
```

```text
-h|--help           显示帮助信息，无需指定值
-t|--time=string    指定日期，格式为 YYYYMMDD，例如 20230101
-c|--case=string    指定检查项，取值见下表
-s|--show=string    指定要展示的信息，取值见下表
```

`-c|--case` 支持的检查项：

| 取值 | 说明 |
| --- | --- |
| config | 配置检查 |
| service | 服务检查 |
| func | 功能检查 |
| vlink | vlink 检查 |
| drop | 丢包检查 |
| perf | 性能检查 |
| log | 日志检查 |
| platform | 平台检查 |
| upgrade | 升级检查 |
| nic | 网卡检查 |

`-s|--show` 支持的信息类型：

| 取值 | 说明 |
| --- | --- |
| env | 环境信息 |
| iface | 网卡信息 |
| ifstat | 网卡统计信息 |
| ifirq | 网卡中断信息 |
| dpaf | 数据面 CPU 亲和性 |
| session | 各设备的会话数及总数 |
| alg | 各设备的 ALG 数及总数 |
| fdb | 各设备的 FDB 数及总数 |
| status | 数据面服务状态 |

### 使用示例

```bash
acli network dpdoctor -h
```

### 结果示例

执行 `acli network dpdoctor -h` 返回以下帮助信息：

```text
Usage: dpdoctor <OPTIONS> <VALUE>
OPTIONS:
    -h|--help:      show help info
    -t|--time:      specify the time, format is 20230101
    -c|--case:      specify the test case
        - config:       config check
        - service:      service check
        - func:         function check
        - vlink:        vlink check
        - drop:         drop pkts check
        - perf:         performance check
        - log:          log check
        - platform:     platform check
        - upgrade:      upgrade check
        - nic:          nic check
    -s|--show:      show the env info
        - env:          show the env info
        - iface:        show the ifaces' info
        - ifstat:       show the ifaces' statistics
        - ifirq:        show the ifaces' irq info
        - dpaf:         show the affinity of dp
        - session:      show the session num for each device and total num
        - alg:          show the alg num for each device and total num
        - fdb:          show the fdb num for each device and total num
        - status:           show the dp service status
```
