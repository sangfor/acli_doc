---
sidebar_position: 10
---

# vs_json_rw
操作概述: vs_json_rw.py 文件

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan vs_json_rw
```

结果示例:
```bash
# acli storage asan vs_json_rw -h
usage: vs_json_rw.py [-h] [-w | -r | -c] -f FILE [-k KEY [KEY ...]]
                     [-v VAL [VAL ...]] [-a CONTENT] [-m {disk}]
                     [-t {int,float,string,json} [{int,float,string,json} ...]]
                     [-UL]

modify or read the json file

optional arguments:
  -h, --help            show this help message and exit
  -w                    modify the key val
  -r                    read the key
  -c                    create file
  -f FILE, --file FILE  the target file
  -k KEY [KEY ...], --key KEY [KEY ...]
                        the key want to modify or read
  -v VAL [VAL ...], --val VAL [VAL ...]
                        the val want to modify
  -a CONTENT, --content CONTENT
                        file content
  -m {disk}, --template {disk}
                        template type
  -t {int,float,string,json} [{int,float,string,json} ...], --type {int,float,string,json} [{int,float,string,json} ...]
                        contorl value type
  -UL                   unlock file when read or write
```