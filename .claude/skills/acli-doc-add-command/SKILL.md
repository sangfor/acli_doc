---
name: acli-doc-add-command
description: Use when adding a single new aCLI command entry to the docs, creating the markdown documentation file and any needed category directories. Triggers on requests like "add a command to the docs", "document this acli command", "create a doc entry for acli ...".
---

# aCLI Doc 单命令添加工具

为一条 aCLI 命令在 `docs/`（中文）和 `i18n/en/docusaurus-plugin-content-docs/current/`（英文）目录下同步创建完整的文档条目。

## 双语言路径

每条命令需要同时在两个位置创建文件，路径结构完全镜像：

```
docs/<ns1>/<ns2>/.../<command>.md                   # 中文
i18n/en/docusaurus-plugin-content-docs/current/<ns1>/<ns2>/.../<command>.md  # 英文
```

- `acli system df` → `docs/system/df.md` + `i18n/en/.../system/df.md`
- `acli hardware gpu config get` → `docs/hardware/gpu/config/get.md` + `i18n/en/.../hardware/gpu/config/get.md`

## 工作流程

### 第一步：解析命令结构

从完整 aCLI 命令字符串中提取命名空间（目录路径）和命令名（文件名）：

```bash
acli hardware usb blacklist add
# 命名空间: hardware/usb/blacklist
# 命令名: add
# 文件路径: docs/hardware/usb/blacklist/add.md
```

### 第二步：确保目录结构存在

对 `docs/` 和 `i18n/en/docusaurus-plugin-content-docs/current/` **两个基础目录**，逐级检查命名空间中每个目录。每级目录按以下流程处理——**中英文需要同时创建对应文件**。

#### 2.1 检查目录是否已存在

目录已存在 → 跳到 2.4（检查现有 `_category_.json` 是否正确）。  
目录不存在 → 继续 2.2。

#### 2.2 全局搜索 label 冲突

**在创建 `_category_.json` 之前，必须先在 `docs/` 下全局搜索是否有同名目录使用了 `generated-index`：**

```bash
# 搜索同名目录，检查它们是否使用 generated-index
find docs/ -type d -name "<目录名>" -exec test -f {}/_category_.json \; -print
```

然后读取搜到的其他路径下的 `_category_.json`，检查 `link.type` 是否为 `"generated-index"`。

- **有冲突**（其他路径下存在同名目录且使用 `generated-index`）→ 走 2.3 情况 B（doc 链接模式）
- **无冲突** → 走 2.3 情况 A（generated-index 模式）

> 此检查只需在 `docs/` 下做，`i18n/en/.../` 镜像处理即可。

#### 2.3 创建目录和 `_category_.json`

**情况 A：无 label 冲突** → 使用 `generated-index`。

中文版 (`docs/<path>/_category_.json`)：
```json
{
  "label": "<目录名>",
  "position": 1,
  "link": {
    "type": "generated-index",
    "description": "<中文描述>"
  }
}
```

英文版 (`i18n/en/docusaurus-plugin-content-docs/current/<path>/_category_.json`)：
```json
{
  "label": "<目录名>",
  "position": 1,
  "link": {
    "type": "generated-index",
    "description": "<English description>"
  }
}
```

> `label` 保持为目录名（不翻译），`description` 需翻译为英文。英文描述格式：首字母大写的名词短语，如 "Operating System Operations"、"Alert Related Operations"。

**情况 B：有 label 冲突** → 使用 doc 链接模式，同时创建 `category.md`。

`_category_.json`，中文版 (`docs/<path>/_category_.json`)：
```json
{
  "label": "<目录名>",
  "position": 1,
  "link": {
    "type": "doc",
    "id": "<完整路径>/category"
  }
}
```

`_category_.json`，英文版 (`i18n/en/.../<path>/_category_.json`)，额外带 `description` 字段：
```json
{
  "label": "<目录名>",
  "position": 1,
  "link": {
    "type": "doc",
    "id": "<完整路径>/category",
    "description": ""
  }
}
```

`category.md`，中文版：
```markdown
---
sidebar_position: 1
---

# <目录名>
<中文描述>

import DocCardList from '@theme/DocCardList';

<DocCardList />
```

`category.md`，英文版：
```markdown
---
sidebar_position: 1
---

# <目录名>
<English description>

import DocCardList from '@theme/DocCardList';

<DocCardList />
```

#### 2.4 目录已存在时检查现有配置

**情况 C：目录已存在且有正确的 `_category_.json`** → 跳过。

如果已有 `_category_.json` 但类型不正确（如 label 冲突用了 `generated-index`），按情况 B 修正为 doc 链接模式。

### 第三步：创建命令 .md 文件

**创建前先检查：** 如果 `<命令名>.md` 已存在（中文或英文路径），询问用户是否覆盖或更新。

**中文版** (`docs/<path>/<command>.md`)：

```markdown
---
sidebar_position: <N>
---

# <命令名>

### 操作概述

<一句话描述这条命令做什么>

### 命令参数

```bash
<-短参数>|--<长参数>=<类型>    <必要/可选>参数，<说明>，示例：<示例值>
```

### 使用示例

```bash
acli <完整命令路径> <示例参数>
```

### 结果示例

```bash
<命令执行后的预期输出>
```
```

**英文版** (`i18n/en/docusaurus-plugin-content-docs/current/<path>/<command>.md`)：

```markdown
---
sidebar_position: <N>
---

# <命令名>

### Overview

<One-line description of what this command does>

### Command Parameters

```bash
<-短参数>|--<长参数>=<类型>    <Required/Optional> parameter, <description>, example: <value>
```

### Usage Example

```bash
acli <完整命令路径> <示例参数>
```

### Output Example

```bash
<Expected output>
```
```

**section 标题对照表**：

| 中文 | 英文 |
|------|------|
| `### 操作概述` | `### Overview` |
| `### 命令参数` | `### Command Parameters` |
| `### 使用示例` | `### Usage Example` |
| `### 结果示例` | `### Output Example` |

**sidebar_position**：默认设为 `1`。Docusaurus 根据文件系统自动生成侧边栏，`sidebar_position` 仅控制同一目录下的排序。大多数现有命令都用 `1`——除非需要特定排序，否则保持 `1` 即可。**中英文保持相同值。**

### 第四步：确认完成

列出所有创建的文件，中英文各列一份：

```
已创建文件列表：（共 N 个文件）

中文（docs/）：
1. docs/xxx/_category_.json
2. docs/xxx/yyy.md
...

英文（i18n/en/.../）：
1. i18n/en/docusaurus-plugin-content-docs/current/xxx/_category_.json
2. i18n/en/docusaurus-plugin-content-docs/current/xxx/yyy.md
...
```

### 第五步：构建验证

文档创建完成后，启动 Docusaurus 本地服务验证页面是否正常渲染：

**准备工作**：
1. 检查 `package.json` 和 `package-lock.json` 是否有变更——有变更则回退（本次仅添加文档，不应改动依赖）
2. 检查是否存在 `node_modules/` 目录——有则删除

**构建与启动**：
```bash
npm install
npm run build
npm run serve
```

构建成功后确认：
- 无报错信息
- 中文和英文页面均可正常访问
- 新增的命令文档出现在侧边栏中

## 内容填充指南

每个 `.md` 文件的四个 section 必须填写完整，不能留空：

| Section（中）| Section（英）| 要求 |
|---|---|---|
| 操作概述 | Overview | 一句话描述命令功能（中/英）|
| 命令参数 | Command Parameters | 每个参数一行，格式：`-x\|--xxxx=type   描述，示例：value` |
| 使用示例 | Usage Example | 完整的可执行命令，带 `acli` 前缀 |
| 结果示例 | Output Example | 真实的命令输出格式（允许模拟数据）|

### 命令参数格式参考

中文版：
```bash
-s|--storage-id=string    必要参数，指定存储id，示例：36000c29a...
-v|--vendor-id=string      必要参数，厂商ID，示例：0409
-l|--limit=integer         指定展示记录的数目（默认值为50），示例：1，2等
```

英文版：
```bash
-s|--storage-id=string    Required parameter, specify storage id, example: 36000c29a...
-v|--vendor-id=string      Required parameter, vendor ID, example: 0409
-l|--limit=integer         Number of records to display (default 50), example: 1, 2, etc.
```

规则：
- 用空格对齐描述列（通常 4 个空格分隔）
- 参数中 `=` 号左侧是短参数和长参数名，右侧是类型
- 中文版：必填参数前加"必要参数"；英文版：加"Required parameter"
- 可选参数：中文版直接写说明，英文版省略 "Required"

## 现有分类及 position 参考

| 目录 | position | 中文说明 | 英文说明 |
|------|----------|---------|---------|
| acli | 10 | acli 工具相关 | aCLI Tool Related Commands |
| alert | 30 | 告警相关 | Alert Related Operations |
| task | 40 | 任务相关 | Task Related Operations |
| log | 50 | 日志相关 | Log Related Operations |
| service | 60 | 服务相关 | Service Related Operations |
| vm | 70 | 虚拟机相关 | Virtual Machine Related Operations |
| system | 80 | 操作系统相关 | Operating System Operations |
| network | 90 | 网络相关 | Network Related Operations |
| storage | 100 | 存储相关 | Storage Related Operations |
| platform | 110 | 平台相关 | Platform Related Operations |
| plugin | 120 | 插件相关 | Plugin Related Operations |
| hardware | 130 | 硬件相关 | Hardware Related Operations |
| plugins | 140 | 插件（复数）| Plugins Related Operations |

> 新一级分类的 position 按上表顺延（如新增分类用 150）。

## 与 acli-doc-gen-skill 的关系

- `acli-doc-gen-skill`：批量从 xlsx 生成**空模板**（仅目录结构 + 占位符），用于初始批量导入
- `acli-doc-add-command`（本 skill）：逐条创建**完整文档**（含实际内容），**中英文同步生成**，用于日常增量添加
