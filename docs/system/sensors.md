---
sidebar_position: 10
---

# sensors
操作概述: sensors命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system sensors
```

结果示例:
```bash
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +45.0°C  (high = +80.0°C, crit = +100.0°C)
Core 0:        +43.0°C  (high = +80.0°C, crit = +100.0°C)
Core 1:        +44.0°C  (high = +80.0°C, crit = +100.0°C)
Core 2:        +42.0°C  (high = +80.0°C, crit = +100.0°C)
Core 3:        +45.0°C  (high = +80.0°C, crit = +100.0°C)

nct6779-isa-0290
Adapter: ISA adapter
Vcore:        +0.87 V  (min =  +0.00 V, max =  +1.74 V)
+12V:        +12.19 V  (min =  +0.00 V, max = +15.36 V)
+5V:          +5.05 V  (min =  +0.00 V, max =  +7.68 V)
CPU Fan:     1256 RPM  (min =    0 RPM)
System Fan:   856 RPM  (min =    0 RPM)
```