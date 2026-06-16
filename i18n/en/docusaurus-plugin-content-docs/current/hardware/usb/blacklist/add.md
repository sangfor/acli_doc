---
sidebar_position: 1
---

# add

### Overview

Add USB blacklist

### Command Parameters

```bash
-v|--vendor-id=string    Required parameter, vendor ID, example: 0409
-p|--product-id=string    Required parameter, product ID, example: 55aa
-n|--name=string          Required parameter, device name, example: NEC Corp. Hub SANGFOR USB Hub
```

### Usage Example

```bash
acli hardware usb blacklist add -v 0409 -p 55aa -n "NEC Corp. Hub SANGFOR USB Hub"
```

### Output Example

```bash
Command executed successfully!
```