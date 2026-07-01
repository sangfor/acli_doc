---
sidebar_position: 1
---

# asan_ops

### Overview

Execute virtual storage detection tool

### Command Parameters

```bash
-s=string                     (Required) Subcommand selection, enumerate values:
                                - check (Check storage network, service, disk, memory, alerts, etc.)
                                - repair (Repair VG, NFS process/config, metadata directory, etc.)
                                - guide (Guide)
                                - case (Check specific scenario issues)
                                - search (Search logs)
                              check subtypes:
                                - all (Check all items)
                                - network (Check storage network)
                                - service (Check storage service/config)
                                - disk (Check disk)
                                - mem (Check memory)
                                - BUG (Check known early warning)
                              repair subtypes:
                                - vg (Repair active VG)
                                - nfspid (Correction NFS pid/conf not same)
                                - meta_dir_left (Repair directory leftover)
								- replace_self_disk（repace self disk）
								- disk_scan （scan disk）
                              case subtypes:
                                - slowdisk (Slow disk)                  - storage (Storage)
                                - latency (Latency)                     - data_sync (Data sync)
                                - splitbrain (Split brain)              - vm (Virtual machine)
                                - iscsi (iSCSI)                       - vmfault (VM fault)
                                - databalance (Data balance)            - upgrade (Upgrade)
                                - two_expand_three (Two-site three-center) - system_hang (System hang)
                                - vs_dog (vs dog)                     - bad_sector (Bad sector)
                                - remove_tfile (Remove tfile)           - check_tgtd_conn (Check tgtd connection)
                                - create_volume (Create volume)         - volume_expand (Volume expand)
                                - volume_replace (Volume replace)
                              blackbox subtypes:
                                - iostat (Parse iostat blackbox log)
                              sample subtypes:
                                - cache (Sample cache hit rate)
                                - polyhost (Sample polyhost/polyrep)
-t=string                     (Required) Check type under subcommand, used with -s, example: -s check -t all
-n=string                     Specify execution host node, example: -n host-b4055d27cb0e,host-b4055d278a6a
-d=string                     Search log time range, format: YYYY-MM-DD,HH:MM:SS, example: -d "2023-06-26,07:37:"
-i=string                     Check VM ID or iSCSI ID, example: -i 1649206016202
-l=integer                    Search log lines, example: -l 1000
-z=bool                       Search zipped log
-g=integer                    Set timeout for each detection command (seconds), example: -g 20
-o=bool                       Output the results to a file
-h=bool                       Show help information
```

### Usage Examples

```bash
# Example 1: Check all items
acli asan_ops -s check -t all

# Example 2: Check storage network
acli asan_ops -s check -t network

# Example 3: Check storage service
acli asan_ops -s check -t service

# Example 4: Check known early warning
acli asan_ops -s check -t BUG

# Example 5: Repair active VG
acli asan_ops -s repair -t vg

# Example 6: Correction NFS pid/conf not same
acli asan_ops -s repair -t nfspid

# Example 7: Check slow disk issue
acli asan_ops -s case -t slowdisk

# Example 8: Check VM issue
acli asan_ops -s case -t vm -i 1649206016202

# Example 9: Check slow disk issue (specify host)
acli asan_ops -s case -t slowdisk -n host-b4055d27cb0e

# Example 10: Check slow disk issue (specify log lines and zipped log)
acli asan_ops -s case -t slowdisk -l 1000 -z true

# Example 11: replace self disk issue (requires -u parameter for disk information: https://support.sangfor.com.cn/cases/list?product_id=33&type=1&category_id=40353)
acli asan_ops -s repair -t replace_self_disk -u 00505695c3b0_36000c29eaabc424a17cdfede2690f0f6

# Example 12: scan disk issue (Scanning disks on specified hosts. Specify a list of hosts separated by commas. If no parameter is passed, all hosts in the cluster will be scanned. Example: acli asan_ops -s repair -t disk_scan )
acli asan_ops -s repair -t disk_scan -n host-abc,host-def
```

### Result Example

```bash
Check if disk VG exists in lvm configuration:
{
    "vg_list": [  ], 
    "vg_list1": [  ]
}

Attempting to activate VG once...

  Reading all physical volumes.  This may take a while...
  Found volume group "GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV" using metadata type lvm2
  Found volume group "RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP" using metadata type lvm2
  3 logical volume(s) in volume group "GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV" now active
  3 logical volume(s) in volume group "RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP" now active


Check VG information again
PV            VG
/dev/sdd1    GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV
/dev/sdb1    RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP

  VG                                     VSize   VFree   #VMda VMdaFree  VMdaSize  #LV VG Tags                                                         
  GNzt4x-lvtv-7Klm-qgF1-62N2-1XuL-wPBZjV 189.81g 832.00m     1    64.00m   128.00m   3 trusted.glusterfs.volume-id:aac5141a-e43f-4478-9dd3-cdd9a4e02276
  RD40dF-J2mT-26Si-4aUK-g0bb-zfQ2-jQfnOP 474.81g 832.00m     1    64.00m   128.00m   3 trusted.glusterfs.volume-id:aac5141a-e43f-4478-9dd3-cdd9a4e02276
```
