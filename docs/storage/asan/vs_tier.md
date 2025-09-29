---
sidebar_position: 10
---

# vs_tier
操作概述: 调用 vs_tier_cli 命令

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan vs_tier
```

结果示例:
```bash
# acli storage asan vs_tier -h
usage: vs_tier_cli.py [-h]
                      [-c {dump,mempool,iostat,setparam,getparam,kickout,block_utime,dumpsense,dump_dirty,update_fuse_conf,mkfs,load,delete,delbrick,file,setprio,lookup,algo,bitmap_file,setsense,getprio,log,ssdlife,standalone,all_return,hit,error,readfile,getsize,suspend_wb,inject,bak_sb,flush_hot,flush_meta,update_conf,badblock,rw,environment,replay,dumpcomm}]
                      [-a ARGUMENT]

Vs tier cli mgt module.

optional arguments:
  -h, --help            show this help message and exit
  -c {dump,mempool,iostat,setparam,getparam,kickout,block_utime,dumpsense,dump_dirty,update_fuse_conf,mkfs,load,delete,delbrick,file,setprio,lookup,algo,bitmap_file,setsense,getprio,log,ssdlife,standalone,all_return,hit,error,readfile,getsize,suspend_wb,inject,bak_sb,flush_hot,flush_meta,update_conf,badblock,rw,environment,replay,dumpcomm}
                        The specified command to execute.
  -a ARGUMENT           The argument for specified command.
```