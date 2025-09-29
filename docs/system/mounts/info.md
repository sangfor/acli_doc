---
sidebar_position: 10
---

# info
操作概述: 查看系统mounts信息

命令参数:
```bash
无
```

使用示例:
```bash
acli system mounts info
```

结果示例:
```bash
/dev/loop89 /sf/data/local/drs/algorithm ext3 rw,noatime 0 0
/dev/loop90 /sf/data/datareport_database ext3 rw,noatime 0 0
/dev/sdb /sf/data/36000c293cadee3074f68ee64716b4163_005056893b01 sffs rw,relatime,id=host-005056893b01,flush=no 0 0
overlay /run/containerd/io.containerd.runtime.v2.task/k8s.io/e77d88519c2365a0c02f8bed0efd5157e07af997377a4243268dd6752d199366/rootfs overlay rw,relatime,lowerdir=/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/27/fs:/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/26/fs:/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/20/fs:/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/19/fs:/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/18/fs,upperdir=/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/564/fs,workdir=/container-data/containerd/io.containerd.snapshotter.v1.squashfs/snapshots/564/work 0 0
```