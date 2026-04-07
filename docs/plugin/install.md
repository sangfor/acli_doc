---
sidebar_position: 1
---

# install

### 操作概述

插件安装/更新

### 命令参数

```bash
-p|--path=string    必要参数，插件路径，必须是 /support/tmp 目录下的插件，示例：/support/tmp/demo.aclix
```

### 使用示例

```bash
acli plugin install -p /support/tmp/plugin_demo-2.0.0.aclix
```

### 结果示例

```bash
acli plugin install -p /support/tmp/plugin_demo-2.0.0.aclix
正在检查存储空间...
存储空间检查通过
正在校验插件包完整性...
插件包完整性校验通过
正在检查插件依赖关系...
插件依赖检查通过
插件安装成功！请执行 source ~/.bashrc 以获得更好的命令补全体验

```
