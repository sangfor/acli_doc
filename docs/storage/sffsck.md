---
sidebar_position: 10
---

# sffsck
操作概述: 调用系统sffsck命令

命令参数:
```bash
无
```

使用示例:
```bash
acli storage sffsck
```

结果示例:
```bash
# acli system sffsck -C /dev/sdd
this will take a long time
don't break when repair option opened,otherwise may damage the file system
please wait...
dlock lba changed:lock.lba=0,128
inodepno=0,lock 65536 check failed,spb_main
dlock lba changed:lock.lba=0,129
inodepno=0,lock 65536 check failed,spb_main
dlock lba changed:lock.lba=0,130
inodepno=0,lock 65536 check failed,spb_main
dlock lba changed:lock.lba=0,131
inodepno=0,lock 65536 check failed,spb_main
[sffs_mh_check] mh->mh_magic=0x0
[sffs_mh_check] mh->mh_magic=0x0
inode A and B con_xxx corrupt, pos 0x10800!
    a->con_first=0x0, a->con_last=0x0
    b->con_first=0x0, b->con_last=0x0
dlock lba changed:lock.lba=0,1024
inodepno=0,lock 524288 check failed,spb_bak
dlock lba changed:lock.lba=0,1025
inodepno=0,lock 524288 check failed,spb_bak
dlock lba changed:lock.lba=0,1026
inodepno=0,lock 524288 check failed,spb_bak
dlock lba changed:lock.lba=0,1027
inodepno=0,lock 524288 check failed,spb_bak
[sffs_mh_check] mh->mh_magic=0x0
[sffs_mh_check] mh->mh_magic=0x0
inode A and B con_xxx corrupt, pos 0x80800!
    a->con_first=0x0, a->con_last=0x0
    b->con_first=0x0, b->con_last=0x0
can't get valid superblock,try repair and check again
```