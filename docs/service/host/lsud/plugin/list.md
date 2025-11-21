---
sidebar_position: 10
---

# list
操作概述: 获取lsud支持的插件列表

命令参数:
```bash
无
```

使用示例:
```bash
acli service host lsud plugin list
```

结果示例:
```bash
PLUGIN NAME               VERSION         TOOL                 DESCRIPTION
-----------               -------         ----                 -----------
libarcconf.so.1.0.0       1.0.0           arcconf              arcconf Controller Plugin
libdell.so.1.0.0          1.0.0           perccli              dell Controller Plugin
libdell2.so.1.0.0         1.0.0           perccli2             dell2 Controller Plugin
libhp.so.1.0.0            1.0.0           ssacli               hp Controller Plugin
libhq.so.1.0.0            1.0.0           unknown              hq Controller Plugin
liblinkdata.so.1.0.0      1.0.0           ps3cli               linkdata Controller Plugin
libsas3ircu.so.1.0.0      1.0.0           sas3ircu             sas3ircu Controller Plugin
libstorcli.so.1.0.0       1.0.0           storcli              storcli Controller Plugin
libstorcli2.so.1.0.0      1.0.0           storcli2             storcli2 Controller Plugin

Total: 9 plugins
```