---
sidebar_position: 1
---

# mount

### Overview

View the mounting information of the specified storage ID

### Command Parameters
```bash
-s|--storage-id=string    Required parameter, Specify a storage ID, Example: 36000c29a3c9419c600cdb98b5f823744_005056893c9d
```

### Usage Example

```bash
acli storage mount -s 36000c29a3c9419c600cdb98b5f823744_005056893c9d
```

### Output Example

```bash
/dev/sdb on /sf/data/36000c29a3c9419c600cdb98b5f823744_005056893c9d type sffs (rw,relatime,id=host-005056893c9d,flush=no)
```