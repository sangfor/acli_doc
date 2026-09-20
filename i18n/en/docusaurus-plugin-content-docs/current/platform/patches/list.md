---
sidebar_position: 1
---

# list

### Overview

List patched patches on this host

### Command Parameters

```bash
-r|--raw=string   Whether to output the real patch name (strip the NN- prefix). 0=keep prefix (e.g. 01-fix-a), 1=strip prefix (e.g. fix-a). default='0' enum=['0', '1']
```

### Usage Example

```bash
acli platform patches list --raw <string>
```

### Output Example

Default (keep NN- prefix):

```bash
["01-sp-HCI-6.11.1_R1-c86-col-20260729"]
```

With `--raw 1` (strip NN- prefix):

```bash
["sp-HCI-6.11.1_R1-c86-col-20260729"]
```
