---
sidebar_position: 10
---
 
# dump
操作概述: 以十六进制格式展示CBT文件内容
 
命令参数: 
```bash
-f|--filename=string 必要参数，磁盘文件绝对路径，示例：/sf/xxx/vm-disk-1.qcow2
-s|--start=integer   起始偏移量（可选，默认为0），示例：0
-l|--length=integer  转储长度（可选，不传表示从start开始到文件结束全部转储），示例1024
```
 
使用示例:
```bash
acli platform backup cbt file dump -f="/sf/data/36000c299bd876efc9d30909bec1d556b_0050569b7e33/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1.qcow2" -s 0 --length 1024
```
 
结果示例:
```bash
cbt file path: /sf/data/36000c299bd876efc9d30909bec1d556b_0050569b7e33/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1.qcow2.cbt.version
version_id: 1
inc_id: 16
checkpoint_id: 4294967312
granularity: 65536 bytes
cluster_count: 3276800 
disk_size: 214748364800 bytes
data_crc: 4294967295, it is not reset
header_crc: 3686558728
0000000000000000         3 
```