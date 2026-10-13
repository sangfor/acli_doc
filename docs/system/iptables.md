---
sidebar_position: 1
---

# iptables

### 操作概述

查看系统防火墙规则（iptables，只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。
查询参数 `-L/-S/-n/-v/-t` 等**须与 `-L` 或 `-S` 连用**方才生效（如 `-n -L`、`-t nat -S`）。

```bash
-L|--list=flag             可选参数，列出规则
-S|--list-rules=flag       可选参数，以脚本格式列出规则
-n|--numeric=flag          可选参数，以数字地址列出规则（须配合 -L/-S）
-v|--verbose=flag          可选参数，详细列出规则（须配合 -L/-S）
-t|--table=string          可选参数，指定规则表（filter/nat/mangle/raw），须配合 -L/-S，示例：-t nat -L
--line-numbers=flag        可选参数，列出规则并带行号（无短孪生，须配合 -L）
-h|--help=flag             可选参数，显示帮助信息
-V|--version=flag          可选参数，显示版本信息
```

写参数禁止清单（命中即拒绝，短/长配对）：

```bash
-A|--append        追加规则到链尾（写防火墙规则）
-I|--insert        插入规则到链头（写防火墙规则）
-D|--delete        删除规则（写防火墙规则）
-R|--replace       替换规则（写防火墙规则）
-F|--flush         清空规则（写防火墙规则）
-Z|--zero          清零计数（写防火墙规则）
-P|--policy        设置默认策略（写防火墙规则）
-N|--new-chain     新建链（写防火墙规则）
-X|--delete-chain  删除链（写防火墙规则）
-E|--rename-chain  重命名链（写防火墙规则）
-C|--check         检查规则（写防火墙规则）
```

### 使用示例

```bash
acli system iptables -L -n --line-numbers
```

### 结果示例

```bash
# acli system iptables -L -n --line-numbers
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
num   target     prot opt source               destination
1     ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0
2     DROP       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:22
```
