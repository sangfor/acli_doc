---
sidebar_position: 10
---

# vs_update_nfs
操作概述: vs_update_nfs.sh 命令

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan vs_update_nfs
```

结果示例:
```bash
# acli storage asan vs_update_nfs -h
====打热升级开始标记====
    文件创建成功, nfs_pid_old = 126805, nfs_supervise_pid_old = 126804
    旧进程热升级标记生效
尝试用新命令设置user.nfs.switch:
 /sf/vs/bin/vs_rpc_tool -c set_option --pid 126805 -k user.nfs.switch -v old 2>&1
    设置user.nfs.switch成功
    命令执行成功
     结果： OK
1. 启动新的nfs进程
start new nfs: -h
 start new nfs:  failed
stop new nfs: -h
    清理残留标记
rm /tmp/vs/hotpath_running_flag_nfs
```