---
sidebar_position: 1
---

# uninstall

### 操作概述

插件卸载

### 命令参数

```bash
-n|--name=string    必要参数，插件名称
```

### 使用示例

```bash
acli plugin uninstall -n plugin_demo
```

### 结果示例

```bash
acli plugin uninstall -n plugin_demo
开始卸载插件：plugin_demo
开始标记插件状态为：卸载中
开始清理集群其他主机的插件目录
开始清理主控插件目录
开始从插件注册文件中移除插件
开始更新acli命令补全文件
开始同步插件注册文件和命令补全到集群
插件卸载成功！请执行 source ~/.bashrc 以获得更好的命令补全体验
```
