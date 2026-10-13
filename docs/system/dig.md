---
sidebar_position: 1
---

# dig

### 操作概述

执行 DNS 查询，获取域名的解析记录（只读）。

### 命令参数

命令格式：

```bash
acli system dig [@<server>] [<domain>] [<type>]
```

位置参数（按声明顺序）：

```bash
@<server>  可选参数，第 1 个位置参数，指定查询的 DNS 服务器（@ 前缀），示例：@8.8.8.8
<domain>   可选参数，第 2 个位置参数，指定要查询的域名，示例：example.com
<type>     可选参数，第 3 个位置参数，指定查询记录类型（A/AAAA/MX/NS/TXT 等），示例：MX
```

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-f|--file=<file>  批量模式，从文件读取查询列表（文件读取操作），拒绝执行；
               因 GNU getopt 支持唯一前缀缩写，--f 开头的写法（--f / --fi / --fil）同样命中拒绝；
               dig 没有其它以 f 开头的长选项，故 --f 即为其最短唯一前缀
```

### 使用示例

```bash
acli system dig @8.8.8.8 example.com
```

### 结果示例

```bash
# acli system dig example.com
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.15 <<>> example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; ANSWER SECTION:
example.com.        3600    IN    A    93.184.216.34
```