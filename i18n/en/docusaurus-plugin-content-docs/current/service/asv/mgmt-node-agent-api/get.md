---
sidebar_position: 1
---

# get

### Overview

Request API data from mgmt-node-agent-api

### Command Parameters
```bash
-p|--param=string         GET request parameters, example: groupPath=/management/unstrict/asv
-g|--group-id=string      Specify parameters for the mem_group subcommand, example: compute_root_group
-s|--service-id=string    Specify parameters for the service subcommand separately, which can be obtained through the services subcommand, example: 28b4a4e4-dde6-4777-9394-fc940f643cab
-i|--interface=string     Required parameter, Specify the service interface aliases to request, The available aliases are as follows:
                           available_cpus: Get the list of available CPU cores
                           cpu_procs: Get the list of processes within the specified CPU group
                           cpu_tasks: Get the list of tasks within the specified CPU group
                           cpu_groups: Get the list of CPU groups
                           monopoly_cpus: Get the list of exclusive CPU cores
                           children_groups: Get the list of child groups
                           cpu_group_exists: Check if the specified CPU group exists
                           cpu_groups_repair: Query the self-repair status of CPU resource groups
                           mem_memory: Get memory usage information
                           mem_hugepage: Get HugePage memory usage information
                           mem_layout: Get memory layout information
                           mem_kernel_usage: Get kernel memory usage information
                           mem_group_repair: Query the self-repair status of memory resource groups
                           mem_allocable_group: Get the resource groups with allocable memory
                           mem_group: Get the list of memory resource groups (need --group-id)
                           list_mem_groups: Get the list of memory resource groups
                           service: Get service information (need --service-id)
                           services: Get the list of services
                           ping: Check if the service is available
                           compute_config: Get computing resource configuration
                           compute_cpu: Get computing resource CPU information
                           compute_memory: Get computing resource memory information, Enum values: available_cpus,cpu_procs,cpu_tasks,cpu_groups,monopoly_cpus,children_groups,cpu_group_exists,cpu_groups_repair,mem_memory,mem_hugepage,mem_layout,mem_kernel_usage,mem_group_repair,mem_allocable_group,mem_group,list_mem_groups,service,services,ping,compute_config,compute_cpu,compute_memory
```

### Usage Example

```bash
acli service asv mgmt-node-agent-api get -i service --service-id ea69d188-1966-4f26-ada7-2b2511c34ef3
```

### Output Example

```bash
Requesting: http://127.0.0.1:15001/v1/services/ea69d188-1966-4f26-ada7-2b2511c34ef3
{
    "data": {
        "uuid": "ea69d188-1966-4f26-ada7-2b2511c34ef3",
        "max_instance_count": 1024,
        "cmdline": "",
        "config_type": "static",
        "memory": {
            "min_byte": 5368709120,
            "max_byte": 5368709120,
            "avg_byte": 5368709120
        },
        "service_type": "normal_service",
        "desc": "normal services memory, exclude system service and vs, default is 5G, may be modified just like system_service",
        "name_regex": [
            "(?P.*$"
        ],
        "name": "all_normal_service"
    },
    "success": 1
}
```