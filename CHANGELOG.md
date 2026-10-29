# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- 新增 vs_check_vms_poly 命令中英文文档，说明只读选项白名单及位置参数拒绝规则。
- 新增 telnet 命令中英文文档，说明端口探测、主机端口约束及帮助选项例外。
- 新增 scsi_id 命令中英文文档，说明选项白名单、设备路径控制及裸位置参数拒绝规则。
- 新增 pstack 命令中英文文档，说明进程调用栈查询、PID 约束及参数白名单。
- 新增 nvme 命令中英文文档，说明只读子命令白名单及写类子命令拒绝规则。
- 新增 nc 命令中英文文档，说明探测参数白名单、主机端口约束及超时封装行为。
- 新增 modinfo 命令中英文文档，说明只读选项白名单、单模块约束及 basedir 禁止规则。
- 新增 iscsiadm 命令中英文文档，说明只读参数组合白名单及写操作拒绝规则。
- 新增 gluster 命令中英文文档，明确仅放通 v i、v list 及恰好两个子命令参数的限制。
- 新增 dpdebug 命令中英文文档，说明只读采集、位置参数白名单及调用约束。
- 新增 vs_sn 命令中英文文档，说明 VS 序列号查询、校验用法及帮助输出。
- 新增 vgs 命令中英文文档，说明 LVM 卷组查询用法及完整帮助输出。
- 新增 slabtop 命令中英文文档，说明只读参数白名单、取值限制及单次查询输出。
- 新增 rpcinfo 命令中英文文档，明确只读参数白名单及 -d、-Z 拒绝规则。
- 更新 realethtool 命令中英文文档，明确部分参数放通规则及完整参数白名单。
- 新增 pvs 命令中英文文档，说明 LVM 物理卷查询用法及完整帮助输出。
- 新增 lvscan 命令中英文文档，说明逻辑卷扫描用法及完整帮助输出。
- 新增 lvs 命令中英文文档，说明 LVM 逻辑卷查询用法及完整帮助输出。
- 补充 lsusb 命令中英文文档，新增 -D 设备选择参数及完整帮助输出。
- 新增 ibv_devices 命令中英文文档，说明 RDMA 设备名称和节点 GUID 查询用法。
- 新增 dpping 命令中英文文档，说明 SDN 数据面 ping 用法及参数。
- 新增 dpdoctor 命令中英文文档，说明数据面检查项、信息查询参数及帮助输出。
- 新增 clview 命令中英文文档，说明设备心跳块、锁块和锁持有者查询用法。
- 搜索功能支持
- 新增迭代二 KB 排障命令文档（acli system 子命令承载）
  - 完全只读新增命令（15 个）：blkid、dig、dmesg、id、iperf3、lscpu、md5sum、nslookup、sar、ss、turbostat、traceroute、uptime、which、who
  - 部分只读新增命令（8 个）：arp、chkconfig、diff、fdisk、find、iptables、qemu-img、route
  - curl 接口放通命令（1 个）：curl（acli system curl，承载 100 条 GET API）
  - 既有命令路径白名单扩展（4 个）：cat、du、grep、ls（分别挂载 cat 命令族与 ls 命令族的共用路径白名单）

## [0.1.0] - 2025-08-01
### Added
- 新增acli命令说明文档
- 新增一键启动/停止/重启脚本
- 新增自动部署脚本
