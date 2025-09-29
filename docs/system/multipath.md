---
sidebar_position: 10
---

# multipath
操作概述: 调用系统multipath命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system multipath
```

结果示例:
```bash
24813.628263 | 36000c299e2665d0b78d74dfa49f53b97: addmap [0 268435456 multipath 0 0 1 1 round-robin 0 1 1 8:0 1]
24813.629599 | libdevmapper: ioctl/libdm-iface.c(1705): device-mapper: reload ioctl on 36000c299e2665d0b78d74dfa49f53b97 failed: Device or resource busy
24813.630090 | dm_addmap: libdm task=0 error: Device or resource busy
24813.636661 | 36000c299e2665d0b78d74dfa49f53b97: ignoring map
24813.636878 | 36000c293cadee3074f68ee64716b4163: addmap [0 629145600 multipath 0 0 1 1 round-robin 0 1 1 8:16 1]
24813.637760 | libdevmapper: ioctl/libdm-iface.c(1705): device-mapper: reload ioctl on 36000c293cadee3074f68ee64716b4163 failed: Device or resource busy
24813.639264 | dm_addmap: libdm task=0 error: Device or resource busy
24813.644524 | 36000c293cadee3074f68ee64716b4163: ignoring map
24813.644774 | 36000c29bfbec23f9b0e00b31694b499d: addmap [0 1048576000 multipath 0 0 1 1 round-robin 0 1 1 8:32 1]
24813.645747 | libdevmapper: ioctl/libdm-iface.c(1705): device-mapper: reload ioctl on 36000c29bfbec23f9b0e00b31694b499d failed: Device or resource busy
24813.646309 | dm_addmap: libdm task=0 error: Device or resource busy
24813.651602 | 36000c29bfbec23f9b0e00b31694b499d: ignoring map
24813.651798 | 36000c295af2b7de14743bdcd33025d79: addmap [0 419430400 multipath 0 0 1 1 round-robin 0 1 1 8:48 1]
24813.652513 | libdevmapper: ioctl/libdm-iface.c(1705): device-mapper: reload ioctl on 36000c295af2b7de14743bdcd33025d79 failed: Device or resource busy
24813.652917 | dm_addmap: libdm task=0 error: Device or resource busy
24813.668585 | 36000c295af2b7de14743bdcd33025d79: ignoring map
```