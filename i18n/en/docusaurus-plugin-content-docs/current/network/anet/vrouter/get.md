---
sidebar_position: 1
---

# get

### Overview

View virtual router information

### Command Parameters
```bash
-i|--id=string      Router ID, Example: 3e1be084-e194-417e-a30d-652c3b415143
-n|--name=string    Router name, Example: vpc_router
```

### Usage Example

```bash
acli network anet vrouter get --id 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
acli network anet vrouter get --name Border_Router_1
```

### Output Example

```bash
evrouters:
    vr_type: evr
    deleted_at: null
    fault_domain_id: null
    direct_route_over_pbr: 0
    schedule_type: 1
    deleted: 0
name: Border Router 1
    ipv4_dns_major:
    run_host_ip: 10.131.201.84
    ha_enable: 1
    ipv4_dns_minor:
    dns_enable: 3
    tenant_id: 707e9d9dac814227b90941362efb6616
    revision_number: 27
    sched_domain_id: null
    heartbeat_ips_info:
        heartbeat_ip: 169.254.192.2
        host_id: host-005056b2a994
        prefix_len: 18
        role: master
        host_ip: 10.131.201.84

        heartbeat_ip: 169.254.192.1
        host_id: host-005056b2ec8d
        prefix_len: 18
        role: slave
        host_ip: 10.131.201.210
    schedule_run_hosts:
    run_host_id: host-005056b2a994
    migrate_host:
    id: 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
    description:
```