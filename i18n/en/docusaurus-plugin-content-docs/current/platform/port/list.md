---
sidebar_position: 1
---

# list

### Overview

List platform ports

### Command Parameters

```bash
-s|--service-ids=string   Comma-separated service ID list to query. If omitted, returns all service ports, example: ssh,agentless_backup
```

### Usage Example

```bash
acli platform port list --service-ids ssh
```

### Output Example

```bash
[
  {
    "description": "Used for agentless backup data transfer. If enabled, third-party backup management platforms can back up and recover VMs.",
    "disable_desc": "If disabled, the third-party backup management platform cannot perform backup and recovery operations on VMs.",
    "port": "40809-40824",
    "protocol": "tcp",
    "service_id": "agentless_backup",
    "service_name": "Agentless backup data transfer service",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Used to automatically detect new servers when adding nodes to a cluster",
    "disable_desc": "After disabled, the system will not automatically detect new servers when you add nodes to a cluster.",
    "port": "4099",
    "protocol": "udp",
    "service_id": "host_found",
    "service_name": "Host discovery",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "Port for VM migration within a cluster or across clusters. It will be automatically enabled after being centrally managed by SCP.",
    "disable_desc": "After disabled, virtual machines can only be migrated within cluster, and migration across clusters will not be supported.",
    "port": "7001-7019",
    "protocol": "tcp",
    "service_id": "migrate_live",
    "service_name": "VM migration",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "Used to synchronize time with other devices",
    "disable_desc": "After this option is disabled, the system will stop synchronizing time with other devices.",
    "port": "123",
    "protocol": "udp",
    "service_id": "ntp_svr",
    "service_name": "NTP service",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Port for processing migration requests and transmitting data during executing P2V tasks",
    "disable_desc": "After disabled, P2V will not be supported.",
    "port": "4000-4010,10809-10900",
    "protocol": "tcp/udp",
    "service_id": "p2v_svr",
    "service_name": "P2V migration",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Port for management of Samba shared directories",
    "disable_desc": "After disabled, datastore sharing will not be supported.",
    "port": "139,445",
    "protocol": "tcp",
    "service_id": "samba",
    "service_name": "Samba",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Used for accessing HCI from Desktop Cloud, aSecurity, and third-party correlated security service platforms.",
    "disable_desc": "After disabled, this port cannot be used by Desktop Cloud, aSecurity, and third-party correlated security service platforms to access HCI, making related services unavailable.",
    "port": "4433",
    "protocol": "tcp",
    "service_id": "sf_sdk",
    "service_name": "Correlated security service",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "The SNMP service enables users to access HCI resources using an independent account, helping administrators see usage of physical resources in use.",
    "disable_desc": "Once disabled, you cannot manage physical nodes via SNMP service.",
    "port": "161",
    "protocol": "udp",
    "service_id": "snmp",
    "service_name": "SNMP",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Port for remote technical support regarding remote diagnostics, troubleshooting and recovery to improve system performance. It will be automatically enabled after being centrally managed by SCP.",
    "disable_desc": "After this option is disabled, Sangfor technical support cannot remotely log in to your Sangfor HCI physical host to help you resolve technical issues. Meanwhile, VM migration and the image distribution over the cloud management platform in other clusters are affected.",
    "port": "22",
    "protocol": "tcp",
    "service_id": "ssh",
    "service_name": "Remote technical support",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "Used for desktop cloud access service",
    "disable_desc": "After this option is disabled, you cannot use the desktop cloud access service that depends on correlated security services. If correlated security services are not required, disable this option manually.",
    "port": "5500,8888,13500-13999",
    "protocol": "tcp/udp",
    "service_id": "vdi_access",
    "service_name": "Desktop cloud access service",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Port for access to admin console of VMware vCenter virtual machine",
    "disable_desc": "After disabled, access to VMware VMs via Web console will not be supported.",
    "port": "4481",
    "protocol": "tcp",
    "service_id": "vmware_console_proxy",
    "service_name": "VMware VM console proxy",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Port for problem diagnosis and fault recovery. It will be automatically enabled after starting aCLI troubleshooting service on SCP.",
    "disable_desc": "",
    "port": "11022",
    "protocol": "tcp",
    "service_id": "acli_ssh",
    "service_name": "troubleshooting service",
    "status": "enable",
    "status_modifiable": "0"
  },
  {
    "description": "Port for external access to storage based on iSCSI virtual disks and shared disks, iSCSI protocol parsing and data transmission",
    "disable_desc": "",
    "port": "3260",
    "protocol": "tcp",
    "service_id": "iscsi_svr",
    "service_name": "iSCSI",
    "status": "enable",
    "status_modifiable": "0"
  },
  {
    "description": "Port for web access to admin console of virtual network device. The service is protected by Sangfor-WAF",
    "disable_desc": "",
    "port": "4480",
    "protocol": "tcp",
    "service_id": "sso_proxy",
    "service_name": "Access to web admin console of the virtual network device",
    "status": "enable",
    "status_modifiable": "0"
  },
  {
    "description": "Port for web access to HCI admin console",
    "disable_desc": "",
    "port": "80,443",
    "protocol": "tcp",
    "service_id": "web_svr",
    "service_name": "Web access to HCI admin console",
    "status": "enable",
    "status_modifiable": "0"
  }
]
```
