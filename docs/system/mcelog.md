---
sidebar_position: 1
---

# mcelog

### 操作概述

查询 CPU MCE 硬件错误日志

### 命令参数

```bash
无参数
```

### 使用示例

```bash
acli system mcelog
```

### 结果示例

```bash
HARDWARE ERROR. This is *NOT* a software problem!
Please contact your hardware vendor
CPU 0 BANK 5
MISC 4000000086
STATUS b200000000070f0f
ADDR 7f123400
MCG STATUS 0
MCG CAP 100c16
APICID 0 SOCKETID 0
CPUID Vendor GenuineIntel Family 6 Model 85
  cache or interface corrected error
  correctable error ( processor core corrected )
  FRU: memory controller, channel 0x0, DIMM 0x0
```
