---
sidebar_position: 1
---

# check_host

### Overview

Check host environment information: CPU, memory, hyper-threading, etc.

### Command Parameters

```bash
-a|--checkall                Also alert for check items with low alert level, by default no alert for low level items
-d|--date=string             Specify check time, only supported by some check items, format: 2006-01-02 15:04:05
-v|--desc                    Print detailed host environment information
--force-terminal             Force output to the terminal even with a large number of hosts; do not write to file
--html-output=string         HTML format output file path, will be automatically created if it does not exist (default: /sf/data/local/performance_tools/check_result/checkhost_output.html)
--ips=string                 Specify the remote host to detect, format: cluster host management IPs separated by commas or all
-o|--output=string           Output file path, will be created automatically if it doesn't exist (default: /sf/data/local/performance_tools/check_result/output.txt)
--skip-lock                  Whether to lock during detection, internal program use, not recommended for users
--lang=string                Set the command line output language, options are zh_CN and en_US
-h|--help                    Display help information
```

### Usage Example

```bash
# Example 1: Check current host environment information
acli performance_tools check_host

# Example 2: Check current host environment information and print details
acli performance_tools check_host -v

# Example 3: Check all hosts environment information
acli performance_tools check_host --ips all

# Example 4: Check specified hosts environment information
acli performance_tools check_host --ips 10.131.136.156,10.131.136.157

# Example 5: Check all hosts and include low alert level check items
acli performance_tools check_host --ips all -a

# Example 6: Check host environment information and specify output file
acli performance_tools check_host --ips all -o /tmp/host_check.txt

# Example 7: Check host environment information and specify HTML output file
acli performance_tools check_host --ips all --html-output /tmp/host_check.html

# Example 8: Force output to terminal when there are many hosts
acli performance_tools check_host --ips all --force-terminal

# Example 9: Check host environment information and specify check time
acli performance_tools check_host -d "2025-06-25 10:30:00"
```

### Output Example

```bash
Checking host 10.131.136.156
Welcome to virtual machine detection tool! Current time 2026-04-08 14:29:15
Starting host detection...
Host name: host-0050568eb9d8
CPU model: Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
CPU core count: 8
CPU usage: 30.81 %
Total host memory: 33.28 GB
Available host memory: 17.46 GB
Running VM count: 1
Cluster type: HCI
-----------------------------------------------------------------------------------------------------------------------------------

1. Check host CPU information
1.1 CPU sys usage √
Details: Physical host CPU sys usage is 10.00%, detection threshold is 15.00%

1.2 Non-forwarding core single-core CPU usage √
Details: Maximum non-forwarding core single-core CPU usage is 33.33%, detection threshold is 95.00%

1.3 SPDK forwarding core usage √ 
Details: SPDK forwarding core usage is 0.00%, detection threshold is 90.00%

1.4 CPU overcommit ratio check √
Details: Host CPU overcommit ratio is 200.00%, detection threshold is 200.00%
List of VMs running on host at that time:
VMID                 CPU        MEM        %CPU_UTIL  MEM_USED        VmName                                            
6025407369236        8          4.00GB     1.27       436.14MB        123                                               


1.5 Check host SMI interrupts √ 
Details: Host CPU has no SMI interrupts

1.6 Host CPU iowait check √
Details: Host CPU iowait usage is 0.00%, detection threshold is 10.00%

1.7 Check host non-exclusive CPU usage √ 
Details: No exclusive VMs in environment, no need to check

1.8 CPU hyper-threading √
Details: Physical host CPU hyper-threading is not enabled

1.9 CPU frequency reduction check √ 
Details: Unable to get current environment turbo frequency information

1.10 CPU usage √
Details: Physical host CPU usage is 30.81%, detection threshold is 65.00%
Top 10 processes by CPU usage:
PID        %CPU  MEM      STAT  START    TIME     COMMAND                                           
40576      52.9  1.16GB   S<Ll  07:07    233:34   /sf/sdn/bin/dataplane --proc-type secondary -l 1,2...
50179      14.0  35.84MB  S<l   07:08    62:02    -w                                                
193558     10.2  436.14MB Sl    07:14    44:39    /usr/bin/kvm -id 6025407369236 -chardev socket,id=...
1052034    7.1   505.92MB S     14:28    0:02     vtpdaemon                                         
996744     7.0   509.74MB S     14:24    0:22     vtpdaemon                                         
998480     6.7   508.87MB S     14:24    0:20     vtpdaemon                                         
1045828    6.7   508.92MB S     14:28    0:04     vtpdaemon                                         
997194     6.5   508.28MB S     14:24    0:20     vtpdaemon                                         
998461     6.4   507.48MB S     14:24    0:19     vtpdaemon                                         
1038296    6.0   506.55MB S     14:27    0:06     vtpdaemon                                         


1.11 CPU frequency check √ 
Details: CPU frequency is 2.2GHz, detection threshold is 2.4GHz

1.12 CPU clock source check √
Details: CPU clock source is tsc, X86 and C86 architecture clock source needs to be tsc
```
