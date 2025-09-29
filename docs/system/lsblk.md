---
sidebar_position: 10
---

# lsblk
操作概述: lsblk命令用于列出系统中的块设备信息，包括磁盘和分区。

命令参数:
```bash
无
```

使用示例:
```bash
acli system lsblk
```

结果示例:
```bash
NAME  MAJ:MIN RM    SIZE RO TYPE  MOUNTPOINT
loop1   7:1    0    100M  0 loop  /mnt/shared/sf/cfg
loop29  7:29   0     60K  0 loop  /run/containerd/io.containerd.runtime.v2.task/k8s.io/e8d41e03c1107afa55b2db11cc61e07825ffe8b0305c6881a703314bc838ad9e/rootfs/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/35/fs
loop57  7:57   0     12K  0 loop  /run/containerd/io.containerd.runtime.v2.task/k8s.io/e8d41e03c1107afa55b2db11cc61e07825ffe8b0305c6881a703314bc838ad9e/rootfs/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/60/fs
loop85  7:85   0    664K  0 loop  /run/containerd/io.containerd.runtime.v2.task/k8s.io/e8d41e03c1107afa55b2db11cc61e07825ffe8b0305c6881a703314bc838ad9e/rootfs/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/86/fs
loop19  7:19   0  120.9M  0 loop  /run/containerd/io.containerd.runtime.v2.task/k8s.io/e8d41e03c1107afa55b2db11cc61e07825ffe8b0305c6881a703314bc838ad9e/rootfs/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/26/fs
```