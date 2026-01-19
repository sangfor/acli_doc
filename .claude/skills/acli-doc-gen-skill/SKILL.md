---
name: acli-doc-gen-skill
description: 解析开发者传入的定义了aCLI命令的xlsx文件，根据其中的aCLI命令生成aCLI_Doc所需要的目录层级。
---

# aCLI_Doc文件生成工具

将新加的aCLI命令转换为aCLI_Doc项目的正确层次结构

## 核心能力

### 1. 解析和补充命令

- 解析输入的xlsx文件，提取其中每一行aCLI命令的定义。
- 将提取出来的命令利用模型自身的能力补全（相同关键字合并）
  - 作为一个智能模型，你需要考虑填充提取出来的 `nan` 字段，比如：在excel中，合并相同字段的值通过`pandas`库解析之后会显示`nan`。因此，你需要发挥你作为一个excel专家的能力，推测一下`nan`字段是否需要填充！

### 2. 为新命令生成目录结构

- 根据当前命令结构是否存在来确定是否需要创建新目录
- 为每个新目录添加`_category_.json` 以适配 `Docusaurus` 的自动目录生成机制
- 如果存在同名的目录，则表示存在标签冲突，在这种情况下，根据冲突规则生成相应的文件

## 输入要求

### 定义了新增命令的xlsx文件

- 用户的输入应该包括一个xlsx文件，里面定义了所有待新增的aCLI命令。
- 如果用户没有明确输入的xlsx文件，请让用户提供。

## 输出内容

### 本地创建文件

- `acli_doc_generate.py`脚本将在项目根目录的 `docs/` 目录中生成相应的文件
- 注意，当前版本仅生成目录结构；文件内容需要手动调整!!

## 包含脚本

- `acli_doc_generate.py`: 在根目录的`/docs`下根据acli_doc的标准为输入的命令生成目标文件结构

## 工作流程

### 第一步：解析Excel文件

1、接收用户上传的Excel文件
2、使用以下命令从*.xlsx文件中提取数据：

```bash
python -c "import pandas as pd; df = pd.read_excel('*.xlsx'); print(df.to_string())"
```

3、从固定格式中提取命令定义（行/列包含命令字符串）
4、注意事项：某些行因内容相同已被合并，可能导致输出为nan。需要根据语义上下文填充这些内容，确保形成完整的命令。不要尝试创建新的python文件，你只需要自行判断，我相信你的能力。
5、提取后必须显示提取结果，并让用户确认，返回的格式如下：

```bash
        1. acli log get
        2. acli hardware cpu info get
        ... ...
```

### 第二步：生成文档模板

1、调用`acli_doc_generate.py`脚本生成文档模板
2、输入格式：JSON格式的字符串数组，每个字符串是完整的acli命令（例如：`["acli system ipconfig","acli platform nic ipconfig set"]`）

```bash
python .claude/skills/acli-doc-gen-skill/doc_generate.py(相对于根目录的相对路径) --commands "[\"acli network nic config config get\", \"acli system config config change\"]"
```

3、脚本会自己创建文件，你不需要再次创建。

### 第三步：确认完成

1、总结所有创建的文件
2、显示创建的文件路径和数量，采用以下格式：

```shell
已创建文件列表：（共x个文件）
1. xxx/xxx/xxx.md
2. xxx/xxx/xxx/xxx.json
......

目录结构：
platform/backup/test/
  ├── _category_.json
  ├── namespace1/
  │   ├── _category_.json
  │   └── set.md
  └── namespace2/
      ├── _category_.json
      └── start.md
```

3、建议开发者运行`npm run start`来验证整个项目结构的正确
4、提醒开发者自行填充生成文件的文本内容!
