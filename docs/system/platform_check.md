---
sidebar_position: 10
---

# platform_check
操作概述: 执行platform_chk工具进行系统检查

命令参数:
```bash
无
```

使用示例:
```bash
acli system platform_check
```

结果示例:
```bash
(= =###)  执行检测脚本：/sf/debug/platform_check_tools/001.hardware_env.sh
模块负责人：VT-虚机磁盘管理团组
[ ok ] 硬件环境: CPU负载
[ ok ] 硬件环境: /sf/data/local分区使用率
[ ok ] 硬件环境: /sf/log分区使用率
[ ok ] 硬件环境: /boot分区使用率
[ ok ] 硬件环境: /dev/shm分区使用率
[ ok ] 硬件环境: /var分区使用率

(= =###)  执行检测脚本：/sf/debug/platform_check_tools/002.container_status.sh
模块负责人：VT-容器团队
....
```