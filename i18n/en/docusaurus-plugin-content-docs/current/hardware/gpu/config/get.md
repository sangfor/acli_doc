---
sidebar_position: 1
---

# get

### Overview

Get GPU configuration information

### Command Parameters
```bash
-n|--name=string    Required parameter, Graphics Card Configuration File Name, example: gpu_info,ini
```

### Usage Example

```bash
acli hardware gpu config get -n host-005056893c9d_vgpu_load_file.json
```

### Output Example

```bash
# Simulated data; actual values shall prevail.
{
"gpuname": "Tesla A2000"
}
```