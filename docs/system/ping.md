---
sidebar_position: 10
---

# ping
操作概述: 调用系统ping命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system ping
```

结果示例:
```bash
# acli system ping 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.026 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.037 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.043 ms
```