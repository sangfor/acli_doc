---
sidebar_position: 1
---

# info

### Overview

Retrieve specified plugin information

### Command Parameters

```bash
-n|--name=string    Required parameter,Plugin name, please use commas to connect multiple queries, for example: plugin_1,plugin_2
```

### Usage Example

```bash
acli plugin info -n plugin_1
acli plugin info --name=plugin_1,plugin_2
```

### Output Example

```bash
acli plugin info -n asan_ops,vm_start
[0]:
  ACliVersion: >=1.0.0
  Arch: x86
  ChangeLog:
  Dependencies:
  Description: Troubleshooting tool for virtual storage anomaly scenarios
  HCIVersion:
  Name: asan_ops
  Source: Official
  Status: Enabled
  Title: Virtual Storage Anomaly Troubleshooting Tool
  VendorName:
  Version: 1.0.0
[1]:
  ACliVersion: >=1.0.0
  Arch: x86
  ChangeLog:
  Dependencies:
  Description: VM start/stop troubleshooting
  HCIVersion:
  Name: vm_start
  Source: Official
  Status: Enabled
  Title: VM start/stop troubleshooting
  VendorName:
  Version: 1.0.0
```