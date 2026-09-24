---
sidebar_position: 1
---

# hostname

### 操作概述

查看主机名称及域名信息（仅开放只读形式，不支持改写主机名）。

### 命令参数

```bash
（无参数）             查看完整主机名
-f|--fqdn=flag        查看主机的完全限定域名
-i|--ip-address=flag  查看主机的 IP 地址
-s|--short=flag       查看短主机名
-h|--help=flag        显示帮助信息
```

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-F             禁止参数，从文件读取主机名后改写主机名（等价写操作 + 任意文件读取双重风险），拒绝执行
--file=<file>  禁止参数，从文件读取主机名后改写主机名，拒绝执行；
               因 GNU getopt 支持唯一前缀缩写，--fi 开头的写法（--fi / --fil / --file=x）同样命中拒绝；
               注意 --fqdn 不受影响（其最短唯一前缀为 --fq，--f 会歧义）；-f 是只读的 --fqdn 缩写，也不受影响
<newname>      禁止参数，位置参数形式的新主机名（hostname <newname>），属写操作，拒绝执行；多参数形式一并拒绝
```

### 使用示例

```bash
acli system hostname -f
```

### 结果示例

```bash
host-005056b237a6
```