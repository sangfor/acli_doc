---
sidebar_position: 1
---

# install

### Overview

Plugin installation/update

### Command Parameters

```bash
-p|--path=string    Required. Plugin path, must be a plugin under the /support/tmp directory. Example: /support/tmp/demo.aclix
```

### Usage Example

```bash
acli plugin install -p /support/tmp/plugin_demo-2.0.0.aclix
```

### Output Example

```bash
acli plugin install -p /support/tmp/plugin_demo-2.0.0.aclix
Checking storage space...
Storage space check passed
Verifying plugin package integrity...
Plugin package integrity verified
Checking plugin dependencies...
Plugin dependency check passed
Plugin installed successfully! Please run 'source ~/.bashrc' for better auto-completion experience
```