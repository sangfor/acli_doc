---
sidebar_position: 1
---

# get

### 操作概述

快照数据库信息查询

### 命令参数

```bash
-v|--vm-id=string      必要参数，指定要查询的快照所属的虚拟机，示例：5050155340046
-s|--snap-id=string    必要参数，指定要查询的快照的id，示例：865dcfe8-c5ab-49a2-a602-c5cffb3d18c0
-f|--filter=string      可选参数，指定是否过滤residual_status、lifespan、tpm_files字段，枚举值为："0"（不过滤）、"1"（过滤），若不传，则默认过滤。取值为"1"时，过滤。取值为"0"时，不过滤。示例：0
```

### 使用示例

```bash
acli platform snapshot mysql get -v 5050155340046 -s 865dcfe8-c5ab-49a2-a602-c5cffb3d18c0
```

### 结果示例

```bash
正确案例：
checkpoint_id: 21474836484
create_time: 1773134983
current: true
desc: 
disk_checkpoint_ids:
  [0]:
    checkpointID: 21474836484
    id: ide0
  [1]:
    checkpointID: 21474836484
    id: ide1
disks:
  [0]:
    boot_disk: 0
    disk_id: 019c3231-b40c-768b-aeee-c2e16f7f968a
    disk_name: virtio1
    disk_type: qcow2
    size: 10741612544
  [1]:
    boot_disk: 0
    disk_id: 019c3231-b40f-74be-bf43-feb65e6ae6ff
    disk_name: virtio0
    disk_type: qcow2
    size: 1440743424
group_id: 
is_protected: true
lifespan: 0
memory: false
memory_size: 0
name: 2026-03-10_17-29-30
parent: 
powerstatus: false
quiesced: false
residual_status: null
size: 12182355968
snap_id: b81c6fb3-bd1c-4148-93d4-c1301412c55c
snap_object: vm
snap_type: external_qcow2
status: normal
tpm_files:
trigger: manual
vmconf: {"use_vhost_user_block": 0, "balloon_memory": 1, "encrypted": 0, "high_performance_disks": "ide0,ide1", "hotplug": 0, "os_installed": 2, "cfgstorage": "355cd2e4153107c65_1c3d2f8337d9", "timing_sync_vm_clock_enable": 0, "mouse_type": "usb", "owner": "admin@vtp", "real_use_vchannel": "yes", "sockets": 1, "digest": "97a603fe4b36f634e3969ff6efca4def2ec3bdc9", "src_vmid": 1907612195165, "ha_enable": 0, "use_vblk": "yes", "application": 1, "use_vnet": "yes", "boot": "cd", "vtool_installed": 1, "source": 0, "no_kvm_clock": 0, "memory": 1024, "virtio0": "355cd2e4153107c65_1c3d2f8337d9:/disks/fe/b6/019c3231-b40f-74be-bf43-feb65e6ae6ff/019c3231-b40f-74be-bf43-feb65e6ae6ff.qcow2,format=qcow2,cache=real_none,preallocate=off,forecast=disable,cache_size=256,unmap=off,id=019c3231-b40f-74be-bf43-feb65e6ae6ff,type=KvmImage,path=/disks/fe/b6/019c3231-b40f-74be-bf43-feb65e6ae6ff/019c3231-b40f-74be-bf43-feb65e6ae6ff.qcow2,storage_id=355cd2e4153107c65_1c3d2f8337d9,name=low-tech-2-disk-0-20260205,state=normal,ownership=2753449823474,application_type=normal,create_time=1770368673,size=10G", "virtio1": "355cd2e4153107c65_1c3d2f8337d9:/disks/c2/e1/019c3231-b40c-768b-aeee-c2e16f7f968a/019c3231-b40c-768b-aeee-c2e16f7f968a.qcow2,format=qcow2,cache=real_none,preallocate=off,forecast=enable,cache_size=256,unmap=off,id=019c3231-b40c-768b-aeee-c2e16f7f968a,type=KvmImage,path=/disks/c2/e1/019c3231-b40c-768b-aeee-c2e16f7f968a/019c3231-b40c-768b-aeee-c2e16f7f968a.qcow2,storage_id=355cd2e4153107c65_1c3d2f8337d9,name=low-tech-2-disk-1-20260205,state=normal,ownership=2753449823474,application_type=normal,create_time=1770368673,size=10G", "is_poly": 1, "invtsc": 0, "enable_network_affinity": 0, "vm_name": "low-tech-2_acmp-6bee", "compatibility_version": "vmx_version=vmx-3.17,src_hci_version=6.12.0", "scsihw": "virtio-scsi-single", "real_use_vblk": "yes", "use_uuid": 0, "abnormal_recovery": 1, "schedopt": 0, "host": "host-1c3d2f8337d9", "hugepage": 0, "numa": 1, "l3_cache_enable": "0", "shutdown_time": "1770368707", "disable_ple": 0, "net0": "virtio=FE:FC:FE:CD:B8:D4,iface_id=072cb47e-2085-48f4-8e28-8b7c56fa42e2,dhcp_reply_flag=0,dhcp6_reply_flag=0,connect=on,qos_enable=0,ingress_kbps=0,egress_kbps=0,host_tso=on", "uefi_bios": 0, "real_use_vnet": "yes", "cpu_exclusive": 0, "name": "2753449823474", "vmtype": "vm", "file_filter": 0, "reset_duid_count": 5, "bootdisk": "virtio0", "ostype": "l564", "cpu_reserve": 0, "sandbox": 0, "create_time": 1770173433, "vm_kernel_version": "3.10", "graphic_type": "std", "convert_scm": {"virtio0": "ide0", "virtio1": "ide1"}, "cores": 1, "cpu": "Cascadelake-Server-noTSX", "os_distribution": "CentOS Linux release 7.1.1503,l2664", "onboot": 0, "dir": "208a2be676cc"}
错误案例：
错误：API返回结果不是字典格式，无法解析！（原因是数据库查询接口没有返回内容）
```
