---
sidebar_position: 1
---

# nvme

### 操作概述

查询 NVMe 设备、标识、状态、日志及特性信息，仅放通指定的只读子命令。

### 命令参数

命令格式：

```bash
acli system nvme <subcommand> [arguments]
```

支持的参数：

本命令采用封闭式子命令白名单（未列举即拒绝），仅支持一级子命令。

只读子命令白名单：

```text
list
id-ns
id-ctrl
list-ns
list-subsys
show-regs
error-log
smart-log
effects-log
fw-log
get-feature
get-log
version
help
```

禁止清单：

```text
format
create-ns
delete-ns
attach-ns
detach-ns
reset
sanitize
fw-download
fw-commit
```

拒绝时返回人类可读的原因及非零退出码，不泄露敏感路径或内部实现细节。

### 使用示例

```bash
acli system nvme list
```

### 结果示例

未指定子命令时：

```text
请指定 nvme 只读子命令（如 list/id-ns/smart-log）
```

执行 `acli system nvme list`：

```text
Node                  Generic               SN                   Model                                    Namespace  Usage                      Format           FW Rev
--------------------- --------------------- -------------------- ---------------------------------------- ---------- -------------------------- ---------------- --------
```

本示例仅显示表头，表示本次查询未列出设备。
