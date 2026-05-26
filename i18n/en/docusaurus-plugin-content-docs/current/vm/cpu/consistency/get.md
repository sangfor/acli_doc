---
sidebar_position: 1
---

# get

### Overview

Get CPU consistency status, compare CPU sockets, cores per socket, and total vCPUs across DB, CFS, and Qemu

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID. Example: 614182240912
```

### Usage Example

```bash
acli vm cpu consistency get -v 614182240912
```

### Output Example

```bash
{"VMID":"614182240912","Sockets":{"DBValue":"1","CfsValue":"1","QemuValue":"","Consistent":true},"CoresPerSocket":{"DBValue":"1","CfsValue":"1","QemuValue":"","Consistent":true},"TotalVCPUs":{"DBValue":"1","CfsValue":"1","QemuValue":"1","Consistent":true},"CheckTime":"2026-05-26T11:18:46+08:00","Status":"consistent"}
```