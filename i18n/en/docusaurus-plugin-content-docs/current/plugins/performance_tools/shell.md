---
sidebar_position: 7
---

# shell

### Overview

The program has some built-in script files that can be executed when they don't exist in the environment

### Command Parameters

```bash
[script]                     Specify the script name to execute. Scripts need to be extracted before use, use -e parameter to extract.
-e|--extract                 Extract built-in scripts to configuration directory, directory location: /sf/data/local/performance_tools/scripts/
```

### Usage Example

```bash
# Example 1: Extract built-in scripts to configuration directory
acli performance_tools shell -e

# Example 2: Display help information
acli performance_tools shell vm_isolation.sh
```

### Output Example

```bash
# acli performance_tools shell vm_isolation.sh
usage: /sf/data/local/performance_tools/vm_isolation.sh option
  isolate vmid pcpu_str [inc_service]             Specify PCPU range for VM exclusive, pcpu_str format: 1-3,5
  isolate only_pcpu pcpu_str                      Only specify pcpu isolation
  unisolate vmid|only_pcpu                        Cancel exclusive for a VM or only_pcpu
  isolated_list                                   Get exclusive VM list

# acli performance_tools shell -e
Successfully extracted script: sfd_performance_handling.sh to /sf/data/local/performance_tools/scripts/sfd_performance_handling.sh
Successfully extracted script: vm_isolation.sh to /sf/data/local/performance_tools/scripts/vm_isolation.sh
Successfully extracted script: sfd_mem_tools_new.sh to /sf/data/local/performance_tools/scripts/sfd_mem_tools_new.sh
Successfully extracted script: get_hw_cti.sh to /sf/data/local/performance_tools/scripts/get_hw_cti.sh
Successfully extracted script: pidstat_x86 to /sf/data/local/performance_tools/scripts/pidstat_x86
All scripts successfully extracted to: /sf/data/local/performance_tools/scripts
```
