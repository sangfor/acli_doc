---
sidebar_position: 2
---

# check_vm

### Overview

Check virtual machine status (VM configuration file, IO, MEM, CPU), automatically detect the host where the VM is running, must input VM ID

### Command Parameters

```bash
[vmid]                        Required parameter, virtual machine id, example: 6025407369236
-a|--checkall                 Also alert for check items with low alert level, by default no alert for low level items
--checkdbvm                   Check best practices for database virtual machine configuration POC testing
-d|--date=string              Specify check time, only supported by some check items, format: 2006-01-02 15:04:05
-v|--desc                     Print detailed virtual machine detection information
--html-output=string          HTML format output file path, will be automatically created if it does not exist (default: /sf/data/local/performance_tools/check_result/checkvm_output.html)
-o|--output=string            Output file path, will be created automatically if it doesn't exist (default: /sf/data/local/performance_tools/check_result/output.txt)
--lang=string                 Set the command line output language, options are zh_CN and en_US
-h|--help                     Display help information
```

### Usage Example

```bash
# Example 1: Check specified virtual machine
acli performance_tools check_vm 1649206016202

# Example 2: Check specified virtual machine and print detailed information
acli performance_tools check_vm 1649206016202 -v

# Example 3: Check specified virtual machine and specify check time
acli performance_tools check_vm 1649206016202 -d "2025-06-25 10:30:00"
```

### Output Example

```bash
Welcome to virtual machine detection tool! Current time 2026-04-08 14:35:58
Starting virtual machine detection...
VM name: 123
VM VMID: 6025407369236
VM running location: 10.131.136.156
VM operating system: 
VM power state: Powered on
VM uptime: 7 hours 21 minutes 17 seconds
VM configuration: 8 cores | 4G | 2D virtual machine
VM type: HCI
VM storage location: lv_1772191199
-----------------------------------------------------------------------------------------------------------------------------------

1. Check if VM configuration follows best practices:
1.1 Check VM vcpu option √
Details: VM currently using CPU type Cascadelake-Server-noTSX

1.2 Check VM NUMA scheduling option √
Details: VM has NUMA scheduling option enabled

1.3 Check Windows VM high-performance timer option √
Details: VM has high-performance timer option enabled

1.4 Check VM huge page memory option ×
Details: VM does not have huge page memory option enabled
Alert level: Medium
Recommendation: If this VM has high performance requirements, it is recommended to enable huge page memory option. If no changes were made before the slowness, this may not be the main cause, you can check other alert items first. To achieve optimal results, you can adjust and test according to recommendations.

1.5 Check VM memory reclaim option √
Details: VM does not have memory reclaim option enabled

1.6 Check VM using Virtio disk option √
Details: VM has Virtio disk usage enabled

1.7 Check VM disk space reclaim option √
Details: VM has no disks with space reclaim enabled

1.8 Check VM disk allocation method √
Details: VM has no disks using thin provisioning

1.9 Check VM operating system √
Details: VM operating system is l564

1.10 Check VM CPU frequency limit option √
Details: VM has CPU frequency limit not enabled

1.11 Check VM nested virtualization option √
Details: VM has nested virtualization option not enabled
```
