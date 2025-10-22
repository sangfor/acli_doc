---
sidebar_position: 10
---

# list
操作概述: 查看虚拟路由器列表

命令参数:  
```bash
无
```

使用示例:
```bash
acli network anet vrouter list
```

结果示例:
```bash
evrouters:
    vr_type: evr
    deleted_at: null
    fault_domain_id: null
    direct_route_over_pbr: 0
    schedule_type: 1
    deleted: 0
    name: 边界路由器1
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