---
sidebar_position: 10
---

# list
操作概述: 查看特定目录下所有的证书
有目录限制，目前仅支持：
```shell
/sf/cfg/certs/cluster-intra/
/sf/cfg/mysql/ssl/
```

命令参数:
```bash
无
```

使用示例:
```bash
acli platform node cert list
```

结果示例:
```bash
/sf/cfg/certs/cluster-intra/root-ca.key
/sf/cfg/certs/cluster-intra/root-ca.pem
/sf/cfg/mysql/ssl/vtp-root-ca.pem
/sf/cfg/mysql/ssl/vtp-mysql-ssl.key
/sf/cfg/mysql/ssl/vtp-mysql-ssl.pem
```