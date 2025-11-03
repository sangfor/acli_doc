---
sidebar_position: 10
---

# set
操作概述: 设置网络配置通道检测模块配置

命令参数:
```bash
-p|--periodic-detect-enable=boolean 是否开启网络配置通道定时检测，示例：true开启，false关闭
-r|--recovery-enable=boolean        是否开启网络配置通道自动恢复，示例：true开启，false关闭
-a|--alert-enable=boolean           是否开启网络配置通道告警，示例：true开启，false关闭
```

使用示例:
```bash
acli network anet config configchannel set --periodic-detect-enable false --recovery-enable true --alert-enable true
```

结果示例:
```bash
periodicDetectEnable: false
recoveryEnable: true
alertEnable: true
```
