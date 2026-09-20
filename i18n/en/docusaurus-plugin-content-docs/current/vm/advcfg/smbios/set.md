---
sidebar_position: 2
---

# set

### Overview

Modify the custom SMBIOS manufacturer information (manufacturer) of the virtual machine and the enable switch (cold edit, only supported when the VM is powered off; a running virtual machine will be rejected)

### Command Parameters

```bash
-v|--vm-id=string          Required parameter, virtual machine ID, example: 614182240912
-m|--manufacturer=string   Required parameter, target manufacturer information, length 1-64 characters (printable ASCII characters only; Chinese characters, line breaks, tabs and other non-printable characters are not supported); commas should be entered as-is (e.g. VMware, Inc.) and will be escaped by the code layer; it is recommended to avoid using the equals sign '=', which may cause QEMU parsing issues; this value must be provided when enabling the custom manufacturer, example: HPE
-e|--enabled=boolean       Required parameter, whether to enable the custom SMBIOS manufacturer information, enum values: true (the custom value takes effect), false (use the default sangfor logic but keep the old manufacturer value without clearing it), example: true
```

### Usage Example

```bash
acli vm advcfg smbios set -v 614182240912 -m HPE -e true
acli vm advcfg smbios set -v 614182240912 -m "VMware, Inc." -e true
```

### Output Example

```bash
Are you sure you want to perform this operation? (y[es]/n[o]): y
enabledAfter: true
enabledBefore: false
manufacturerAfter: HPE
manufacturerBefore: null
taskID: host-005056b2894b:280998:1760441353:6913569233831
vmID: 614182240912
```