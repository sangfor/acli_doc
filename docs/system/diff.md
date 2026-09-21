---
sidebar_position: 1
---

# diff

### 操作概述

比较两个文件的内容差异（只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
-u|--unified=flag             可选参数，以统一格式输出差异，示例：acli system diff -u fileA fileB
-q|--brief=flag               可选参数，仅比较两文件是否不同，不输出具体差异，示例：acli system diff -q fileA fileB
-i|--ignore-case=flag         可选参数，忽略大小写差异，示例：acli system diff -i fileA fileB
-w|--ignore-all-space=flag    可选参数，忽略空白差异，示例：acli system diff -w fileA fileB
<fileA> <fileB>  必要参数，指定待比较的两个文件（两个路径均须在 cat 命令族共用路径白名单内）
```

可比较的路径白名单（cat 命令族共用：cat/grep/tail/diff 文本查看/比较族，去包含后 81 条，节选）：

```bash
/etc/hosts
/etc/fstab
/sf/version
/sf/log/
/var/log/
```

写参数禁止清单（命中即拒绝）：

```bash
--version  查询 diff 版本信息（未放通，拒绝）
-r         递归比较目录（未放通，拒绝）
-N         将缺失文件视为空文件（未放通，拒绝）
-y         并排输出（未放通，拒绝）
--help     帮助信息（未放通，拒绝）
```

### 使用示例

```bash
acli system diff -u /etc/hosts /etc/fstab
```

### 结果示例

```bash
# acli system diff -u /etc/hosts /etc/fstab
--- /etc/hosts	2026-09-01 10:00:00.000000000 +0800
+++ /etc/fstab	2026-09-02 11:00:00.000000000 +0800
@@ -1,3 +1,4 @@
-127.0.0.1   localhost localhost.localdomain
+UUID=1a2b  /  ext4  defaults  1 1
```
