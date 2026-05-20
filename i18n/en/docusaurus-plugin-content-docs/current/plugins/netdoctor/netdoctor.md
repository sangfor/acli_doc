---
sidebar_position: 1
---

# netdoctor

### Overview

Network troubleshooting tool that supports two modes: Diagnosis Box (multi-scenario troubleshooting) and Tools Box (quick tools).

### Command Parameters

```bash
acli netdoctor [OPTIONS]

# Diagnosis Box Parameters

| Parameter | Description |
|-----------|-------------|
| `-c` / `--case=string` | (Required) Troubleshooting scenario selection, supports English comma concatenation for multiple scenarios, example: `vm` or `vm,mgmt` |
| `-d` / `--date=string` | Specify date for log search, example: `2023-06-25` or `2023-06-25,07:37` (date and time separated by English comma) |

Available scenarios:
- `vm` (VM Packet Loss Diagnosis)
- `mgmt` (Management Network Packet Loss Diagnosis)
- `vxlan` (VxLAN Network Packet Loss Diagnosis)
- `vs` (Storage Network Packet Loss Diagnosis)
- `offline` (Host Offline Diagnosis)
- `perf` (VM Latency/Stutter Diagnosis)
- `drop` (Physical Port Packet Loss/Error Diagnosis)
- `nic` (Host NIC Diagnosis)
- `upg` (Upgrade Diagnosis)
- `srv` (Virtual Network Service Anomaly Diagnosis)
- `all` (Full-Scenario Diagnosis)

# Tools Box Parameters

| Parameter | Description |
|-----------|-------------|
| `-t` / `--tool=string` | Tools Box mode, quickly execute specified tool |

Available tools:
- `vlink` (Check VM vlink status, can specify VMID)
- `ifaces` (View information of all network interfaces)
- `ifcheck` (Check statistics of a specific network interface)
- `ifstat` (Detect detailed packet sending/receiving information of a specific network interface)
- `ifirq` (View interrupt core distribution information of all network interfaces)
- `vmmac` (Check VM MAC address conflicts)
- `ipmac` (Check cluster IP and MAC conflicts)
- `fullsync` (Execute full synchronization)
- `reorder` (Execute network card reordering)
- `topo` (VM to VM network topology path analysis)
- `dfw` (Distributed firewall toolbox)
- `ifcfg` (Background network interface configuration toolbox)
- `mirror` (Flow mirror configuration toolbox)
- `netdump` (Efficient packet capture tool)
```

### Usage Examples

```bash
# Example 1: Default without parameters, display various troubleshooting scenarios for selection
acli netdoctor

# Example 2: Specify single scenario for diagnosis
acli netdoctor -c vm

# Example 3: Specify multiple scenarios for diagnosis (separated by English comma)
acli netdoctor -c vm,mgmt

# Example 4: Specify scenario and search logs for specified date
acli netdoctor -c all -d 2023-06-26,07:37

# Example 5: Use Tools Box to check all VM vlink
acli netdoctor -t vlink

# Example 6: Use Tools Box to check vlink for specific VM
acli netdoctor -t vlink <vm_id>

# Example 7: Use Tools Box to view all network interfaces information
acli netdoctor -t ifaces

# Example 8: Use Tools Box to view all network interfaces interrupt core distribution
acli netdoctor -t ifirq

# Example 9: Use Tools Box to check VM MAC address conflicts
acli netdoctor -t vmmac

# Example 10: Use Tools Box to check cluster IP and MAC conflicts
acli netdoctor -t ipmac

# Example 11: Use Tools Box to execute full synchronization
acli netdoctor -t fullsync

# Example 12: Use Tools Box to execute network card reordering
acli netdoctor -t reorder

# Example 13: Use Tools Box for VM to VM network topology path analysis
acli netdoctor -t topo

# Example 14: Use Tools Box to enter distributed firewall toolbox
acli netdoctor -t dfw

# Example 15: Use Tools Box to enter background network interface configuration toolbox
acli netdoctor -t ifcfg

# Example 16: Use Tools Box to enter flow mirror configuration toolbox
acli netdoctor -t mirror

# Example 17: Use Tools Box to enter efficient packet capture tool
acli netdoctor -t netdump
```

### Result Example

```bash
============================Diagnosing VM Network============================
If you want to check a specific VM's network, please enter VMID, otherwise press (y/Y) to continue:
y
========================================================================

[1] Diagnosing vlink status of all virtual machines in the cluster (may take too long if there are many virtual machines), please wait...

=> Diagnosing whether all virtual machines in the cluster have vlink, please wait...
VM(vmid: 6025407369236, name: 123) NIC 1 is not connected
All virtual machines have been detected, all checked virtual machines have vlink
Some virtual machines are not connected, please judge if unrelated to the issue, can ignore

[2] Diagnosing whether packet loss is caused by network data plane abnormalities, please wait...

=> Checking whether dp service has abnormalities, please wait...

=> Checking whether dataplane service is running on all hosts in the cluster, please wait...

=> Checking whether other SDN services except dp are running on all hosts in the cluster, please wait...

=> Checking the startup time of dataplane service on the current host, please wait...
Current host dataplane was started on today, startup time: 2026-04-08 07:08:00.772008186. Please confirm if the host was restarted or SDN service was manually restarted, it can be ignored

=> Checking whether SDN service status on all hosts in the cluster is currently normal, please wait...

=> Checking whether SDN service status in blackbox logs on today is normal for all hosts in the cluster, please wait...

=> Checking whether SDN services on all hosts in the cluster have ever cored, please wait...

=> Diagnosing whether network card has disorder problem, please wait...
```
