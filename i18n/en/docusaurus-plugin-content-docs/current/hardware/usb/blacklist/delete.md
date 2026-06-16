---
sidebar_position: 1
---

# delete

### Overview

Delete USB blacklist

### Command Parameters

```bash
-v|--vendor-id=string    Required parameter, vendor ID, example: 0409
-p|--product-id=string    Required parameter, product ID, example: 55aa
```

### Usage Example

```bash
acli hardware usb blacklist delete -v 0409 -p 55aa
```

### Output Example

```bash
Command executed successfully!
```