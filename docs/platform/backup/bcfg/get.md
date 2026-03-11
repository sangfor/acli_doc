---
sidebar_position: 1
---

# get

### 操作概述

备份点的配置文件（bcfg文件）内容查询

### 命令参数

```bash
-s|--storage-name=string    必要参数，指定要查询的备份文件所在的存储的名称，示例：NFS-1
-v|--vm-id=string    必要参数，要查询的备份文件对应的虚拟机id，示例：5050155340046
-b|--backup-id=string    可选参数，要查询的备份文件对应的虚拟机id，示例：auto-260130-122446-cd61f44d-4d55-4218-945a-f858d75702c4
```

### 使用示例

```bash
acli platform backup bcfg get -s NFS-1 -v 5050155340046
acli platform backup bcfg get -s NFS-1 -v 5050155340046 --backup-id auto-260130-122446-cd61f44d-4d55-4218-945a-f858d75702c4
```

### 结果示例

```bash
{
    "data": {
        "add": {
            "backstorage": "355cd2e4151c1590c_1c3d2f8337d9", 
            "backupSize": 3236102144, 
            "backupprotect": "", 
            "backupversion": 1, 
            "current": 0, 
            "description": "", 
            "disks": [
                {
                    "backup_file": "vm-disk-4.qcow2", 
                    "disk_id": "019cbc10-858a-7567-80ab-3a50ec7ddb0d", 
                    "disk_name": "019cbc10-858a-7567-80ab-3a50ec7ddb0d.qcow2", 
                    "drive": "virtio3", 
                    "ds": "ide3"
                }, 
                {
                    "backup_file": "vm-disk-1.qcow2", 
                    "disk_id": "019cbc0f-461d-7410-8c3b-1187e970628c", 
                    "disk_name": "019cbc0f-461d-7410-8c3b-1187e970628c.qcow2", 
                    "drive": "virtio0", 
                    "ds": "ide0"
                }, 
                {
                    "backup_file": "vm-disk-2.qcow2", 
                    "disk_id": "019cbc10-68b2-73d5-82b0-3253489e9cd4", 
                    "disk_name": "019cbc10-68b2-73d5-82b0-3253489e9cd4.qcow2", 
                    "drive": "virtio1", 
                    "ds": "ide1"
                }, 
                {
                    "backup_file": "vm-disk-3.qcow2", 
                    "disk_id": "019cbc10-788e-74ca-a9ef-f001762b971b", 
                    "disk_name": "019cbc10-788e-74ca-a9ef-f001762b971b.qcow2", 
                    "drive": "virtio2", 
                    "ds": "ide2"
                }
            ], 
            "fileSize": 3238002688, 
            "healthcheck_result": "unknown", 
            "healthcheck_time": null, 
            "mapid": "auto-260305-160928-5a7ce3d0-bc2c-47d6-9af0-d5746c7817ac", 
            "parent": "auto-260305-154922-580df023-fae6-4b6d-a395-4dfa94991336", 
            "powerstatus": 1, 
            "quiesced": 0, 
            "seq_id": 100008, 
            "snapname": "backup_2026-03-05_16-17-22", 
            "snaptime": 1772698642, 
            "snaptype": "auto", 
            "tpm_files": [], 
            "trigger": "cdp", 
            "user_defined_conf": null, 
            "version": "6.12.0_B"
        }, 
        "data": {
            "abnormal_recovery": 1, 
            "application": 1, 
            "balloon_memory": 1, 
            "boot": "cd", 
            "bootdisk": "virtio0", 
            "cfgstorage": "355cd2e4153107c65_1c3d2f8337d9", 
            "compatibility_version": "vmx_version=vmx-3.17,src_hci_version=6.12.0", 
            "convert_scm": {
                "virtio0": "ide0", 
                "virtio1": "ide1", 
                "virtio2": "ide2", 
                "virtio3": "ide3"
            }, 
            "cores": 2, 
            "cpu": "core2duo", 
            "cpu_exclusive": 0, 
            "cpu_reserve": 0, 
            "cpuunits": 1000, 
            "create_time": 1772681691, 
            "digest": "e957399920320fcb3ef2958a9a6c66609c83db2d", 
            "dir": "208a2be676cc", 
            "disable_ple": 0, 
            "enable_network_affinity": 0, 
            "encrypted": 0, 
            "file_filter": 0, 
            "graphic_type": "cirrus", 
            "ha_enable": 0, 
            "high_performance_disks": "ide0,ide1,ide2,ide3", 
            "host": "host-1c3d2f8337d9", 
            "hotplug": 0, 
            "hugepage": 0, 
            "invtsc": 0, 
            "is_poly": 1, 
            "l3_cache_enable": "0", 
            "lifespan": "-1", 
            "lock": "running", 
            "logo": 0, 
            "memory": 2048, 
            "mouse_type": "usb", 
            "name": "92815248362", 
            "net0": "virtio=FE:FC:FE:5E:D4:95,iface_id=a5f8062a-3d22-404b-9fe6-9eb8deb7723c,dhcp_reply_flag=0,dhcp6_reply_flag=0,connect=on,qos_enable=0,ingress_kbps=0,egress_kbps=0,host_tso=on", 
            "no_kvm_clock": 0, 
            "numa": 1, 
            "onboot": 0, 
            "os_distribution": "CentOS Linux release 7.1.1503,l2664", 
            "os_installed": 1, 
            "ostype": "l564", 
            "owner": "admin@vtp", 
            "real_use_vblk": "yes", 
            "real_use_vchannel": "yes", 
            "real_use_vnet": "yes", 
            "reset_duid_count": 40961, 
            "sandbox": 0, 
            "schedopt": 0, 
            "scsihw": "virtio-scsi-single", 
            "shutdown_time": "0", 
            "snapshots": {}, 
            "sockets": 1, 
            "source": 0, 
            "splash_time": 0, 
            "template": 4372839925141, 
            "timing_sync_vm_clock_enable": 0, 
            "tpm_enabled": 0, 
            "uefi_bios": 0, 
            "use_uuid": 0, 
            "use_vblk": "yes", 
            "use_vhost_user_block": 0, 
            "use_vnet": "yes", 
            "virtio0": "019c2cf349e87c1a87ee5a8f3d416488:vm-disk-1.qcow2,format=qcow2,cache=real_none,aio=native,preallocate=off,forecast=disable,cache_size=256,unmap=off,protocol_type=scsi-over-ide,id=019cbc0f-461d-7410-8c3b-1187e970628c,type=KvmImage,permanent=yes,path=/disks/11/87/019cbc0f-461d-7410-8c3b-1187e970628c/019cbc0f-461d-7410-8c3b-1187e970628c.qcow2,storage_id=019c2cf349e87c1a87ee5a8f3d416488,name=\u3010\u6f14\u793a\u7528\u3011H2L-_acmp-b9d62-disk-0-20260305,state=normal,ownership=92815248362,application_type=normal,create_time=1772681690,size=10G", 
            "virtio1": "1SANGFOR_ASAN-010-ec13-40f3-b0bb-cc359eb1b842:vm-disk-2.qcow2,format=qcow2,cache=real_none,aio=io_uring,preallocate=off,forecast=enable,cache_size=256,unmap=off,protocol_type=scsi-over-ide,id=019cbc10-68b2-73d5-82b0-3253489e9cd4,type=KvmImage,permanent=yes,path=/disks/32/53/019cbc10-68b2-73d5-82b0-3253489e9cd4/019cbc10-68b2-73d5-82b0-3253489e9cd4.qcow2,storage_id=1SANGFOR_ASAN-010-ec13-40f3-b0bb-cc359eb1b842,name=\u3010\u6f14\u793a\u7528\u3011H2L-_acmp-b9d62-disk-1-20260305,state=normal,ownership=92815248362,iowq_max_workers=1,application_type=normal,create_time=1772681719,size=1G", 
            "virtio2": "355cd2e4153107c65_1c3d2f8337d9:vm-disk-3.qcow2,format=qcow2,cache=real_none,aio=io_uring,preallocate=off,forecast=enable,cache_size=256,unmap=off,protocol_type=scsi-over-ide,id=019cbc10-788e-74ca-a9ef-f001762b971b,type=KvmImage,permanent=yes,path=/disks/f0/01/019cbc10-788e-74ca-a9ef-f001762b971b/019cbc10-788e-74ca-a9ef-f001762b971b.qcow2,storage_id=355cd2e4153107c65_1c3d2f8337d9,name=\u3010\u6f14\u793a\u7528\u3011H2L-_acmp-b9d62-disk-2-20260305,state=normal,ownership=92815248362,iowq_max_workers=1,application_type=normal,create_time=1772681723,size=1G", 
            "virtio3": "355cd2e4151c1590c_1c3d2f8337d9:vm-disk-4.qcow2,format=qcow2,cache=real_none,aio=io_uring,preallocate=off,forecast=enable,cache_size=256,unmap=off,protocol_type=scsi-over-ide,id=019cbc10-858a-7567-80ab-3a50ec7ddb0d,type=KvmImage,permanent=yes,path=/disks/3a/50/019cbc10-858a-7567-80ab-3a50ec7ddb0d/019cbc10-858a-7567-80ab-3a50ec7ddb0d.qcow2,storage_id=355cd2e4151c1590c_1c3d2f8337d9,name=\u3010\u6f14\u793a\u7528\u3011H2L-_acmp-b9d62-disk-3-20260305,state=normal,ownership=92815248362,iowq_max_workers=1,application_type=normal,create_time=1772681727,size=1G", 
            "vm_kernel_version": "3.10", 
            "vm_name": "\u3010\u6f14\u793a\u7528\u3011H2L-_acmp-b9d62", 
            "vmtype": "vm", 
            "vtool_installed": 1
        }
    }, 
    "time": 1773201633
}
```
