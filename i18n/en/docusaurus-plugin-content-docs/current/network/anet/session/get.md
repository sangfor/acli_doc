---
sidebar_position: 1
---

# get

### Overview

View the session information on the data plane

### Command Parameters
```bash
-t|--device-type=string    Required parameter, Data plane virtual device types: dfw (distributed firewall), vrouter (virtual router), Enum values: dfw,vrouter
-n|--device-name=string    Required parameter, Name of the data plane distributed firewall(for example: dfw_dcc6c377-24ff-4389-8762-13132c29dbe9) or virtual router ID(for example: 3e1be084-e194-417e-a30d-652c3b415143)
```

### Usage Example

```bash
acli network anet session get --device-type vrouter --device-name 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
```

### Output Example

```bash
host-005056b2ec8d# co t
host-005056b2ec8d(config)#  vrouter 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
host-005056b2ec8d(config-vrouter)#  show session total
session total number : 0
host-005056b2ec8d(config-vrouter)#
```