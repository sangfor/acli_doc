---
sidebar_position: 1
---

# asan_ops

### 操作概述

执行虚拟存储检测工具

### 命令参数

```bash
-s=string                     （必要参数），子命令选择，枚举值：
                                - check（检查存储网络、服务、磁盘、内存、告警等）
                                - repair（修复 VG、NFS 进程/配置、元数据目录等）
                                - guide（向导）
                                - case（检查特定场景问题）
                                - search（搜索日志）
                              check 子类型：
                                - all（检查所有项）
                                - network（检查存储网络）
                                - service（检查存储服务/配置）
                                - disk（检查磁盘）
                                - mem（检查内存）
                                - BUG（检查已知预警）
                              repair 子类型：
                                - vg（修复活跃 VG）
                                - nfspid（修正 NFS 进程/配置不一致）
                                - meta_dir_left（修复目录遗留）
                              case 子类型：
                                - slowdisk（慢盘）                    - storage（存储）
                                - latency（时延）                     - data_sync（数据同步）
                                - splitbrain（脑裂）                  - vm（虚拟机）
                                - iscsi（iSCSI）                     - vmfault（虚拟机故障）
                                - databalance（数据均衡）              - upgrade（升级）
                                - two_expand_three（两地三中心）       - system_hang（系统hang）
                                - vs_dog（vs dog）                   - bad_sector（坏扇区）
                                - remove_tfile（删除tfile）           - check_tgtd_conn（检查tgtd连接）
                                - create_volume（创建卷）             - volume_expand（卷扩容）
                                - volume_replace（卷替换）
                              blackbox 子类型：
                                - iostat（解析 iostat 黑盒日志）
                              sample 子类型：
                                - cache（采样缓存命中率）
                                - polyhost（采样多主机/多副本）
-t=string                     （必要参数）子命令下的检查类型，与 -s 配合使用，示例：-s check -t all
-n=string                     指定执行的主机节点，示例：-n host-b4055d27cb0e,host-b4055d278a6a
-d=string                     搜索日志的时间范围，格式：YYYY-MM-DD,HH:MM:SS，示例：-d "2023-06-26,07:37:"
-i=string                     检查虚拟机 ID 或 iSCSI ID，示例：-i 1649206016202
-l=integer                    搜索日志的行数，示例：-l 1000
-z=bool                       搜索压缩日志
-g=integer                    设置每个检测命令的超时时间（秒），示例：-g 20
-o=bool                       将结果输出到文件
-h=bool                       显示帮助信息
```

### 使用示例

```bash
# 示例1：检查所有项
asan_ops -s check -t all

# 示例2：检查存储网络
asan_ops -s check -t network

# 示例3：检查存储服务
asan_ops -s check -t service

# 示例4：检查已知预警
asan_ops -s check -t BUG

# 示例5：修复活跃 VG
asan_ops -s repair -t vg

# 示例6：修正 NFS 进程/配置不一致
asan_ops -s repair -t nfspid

# 示例7：检查慢盘问题
asan_ops -s case -t slowdisk

# 示例8：检查虚拟机问题
asan_ops -s case -t vm -i 1649206016202

# 示例9：检查慢盘问题（指定主机）
asan_ops -s case -t slowdisk -n host-b4055d27cb0e

# 示例10：检查慢盘问题（指定日志行数和压缩日志）
asan_ops -s case -t slowdisk -l 1000 -z true
```

### 结果示例

```bash
查看lvm配置是否存在磁盘VG:
{
    "vg_list": [  ], 
    "vg_list1": [  ]
}

尝试激活一次VG...

  Reading all physical volumes.  This may take a while...
  Found volume group "GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV" using metadata type lvm2
  Found volume group "RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP" using metadata type lvm2
  3 logical volume(s) in volume group "GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV" now active
  3 logical volume(s) in volume group "RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP" now active


再次查看VG信息
PV            VG
/dev/sdd1    GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV
/dev/sdb1    RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP

  VG                                     VSize   VFree   #VMda VMdaFree  VMdaSize  #LV VG Tags                                                         
  GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV 189.81g 832.00m     1    64.00m   128.00m   3 trusted.glusterfs.volume-id:aac5141a-e43f-4478-9dd3-cdd9a4e02276
  RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP 474.81g 832.00m     1    64.00m   128.00m   3 trusted.glusterfs.volume-id:aac5141a-e43f-4478-9dd3-cdd9a4e02276
```
