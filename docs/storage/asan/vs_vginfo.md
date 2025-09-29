---
sidebar_position: 10
---

# vs_vginfo
操作概述: vs_vginfo命令

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan vs_vginfo
```

结果示例:
```bash
PV            VG
/dev/sdd1    XobyDI-5XK3-h2H0-aI2S-w1zE-PNJP-fqJ86s
/dev/sdc1    rwP9Lc-HeVe-aXDe-7CEI-Mcq6-6lHu-88PLtp

  VG                                     VSize   VFree   #VMda VMdaFree  VMdaSize  #LV VG Tags
  XobyDI-5XK3-h2H0-aI2S-w1zE-PNJP-fqJ86s 189.81g 832.00m     1    64.00m   128.00m   3 trusted.asan_client.volume-id:8ba7ccb5-8797-4970-b73f-3a8d12356077
  rwP9Lc-HeVe-aXDe-7CEI-Mcq6-6lHu-88PLtp 474.81g 832.00m     1    64.00m   128.00m   3 trusted.asan_client.volume-id:8ba7ccb5-8797-4970-b73f-3a8d12356077
```