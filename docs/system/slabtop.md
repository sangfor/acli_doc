---
sidebar_position: 1
---

# slabtop

### 操作概述

查看内核 slab 缓存的对象数量、使用率及内存占用信息。

### 命令参数

命令格式：

```bash
acli system slabtop [options]
```

支持的参数：

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```text
-o|--once=flag      仅显示一次后退出
-h|--help=flag      显示帮助信息
-V|--version=flag   显示版本信息
-d|--delay=integer  指定刷新间隔（秒），取值范围 1-3600
-s|--sort=string    指定排序字符，仅允许 a、b、c、l、v、n、o、p、s、u 中的单个字符
```

禁止清单：

白名单外选项、超出 1-3600 的刷新间隔及不在 `[abclvnopsu]` 中的排序字符一律拒绝。

### 使用示例

```bash
acli system slabtop -o
```

### 结果示例

```text
slabtop: terminal setting retrieval: Inappropriate ioctl for device
 Active / Total Objects (% used)    : 4210648 / 4268922 (98.6%)
 Active / Total Slabs (% used)      : 113531 / 113531 (100.0%)
 Active / Total Caches (% used)     : 129 / 175 (73.7%)
 Active / Total Size (% used)       : 1220027.33K / 1251331.38K (97.5%)
 Minimum / Average / Maximum Object : 0.01K / 0.29K / 9.06K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME
1032966 1031980  99%    0.21K  27918       37    223344K dentry
602990 598447  99%    0.02K   3547      170     14188K lsm_file_cache
556832 556822  99%    0.12K  17401       32     69604K buffer_head
332552 332552 100%    0.70K  15116       22    241856K inode_cache
205044 205044 100%    0.14K   7323       28     29292K kernfs_node_cache
157696 157457  99%    0.01K    308      512      1232K kmalloc-8
137344 130136  94%    0.06K   2146       64      8584K anon_vma_chain
134160 133223  99%    0.77K   6708       20    107328K proc_inode_cache
103872 103026  99%    1.00K   3246       32    103872K kmalloc-1k
 88026  82841  94%    0.04K    863      102      3452K vma_lock
 87061  82498  94%    0.21K   2353       37     18824K vm_area_struct
 76025  75058  98%    0.31K   3041       25     24328K skbuff_head_cache
 65178  65178 100%    0.04K    639      102      2556K extent_status
 60956  60850  99%    0.57K   2177       28     34832K radix_tree_node
 59520  59265  99%    0.03K    465      128      1860K kmalloc-32
 54976  54976 100%    0.50K   1718       32     27488K pool_workqueue
```

示例首行是终端设置读取提示；本次输出仍包含后续 slab 统计数据。
