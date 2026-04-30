---
sidebar_position: 1
---

# uninstall

### Overview

Plugin uninstallation

### Command Parameters

```bash
-n|--name=string    Required. Plugin name
```

### Usage Example

```bash
acli plugin uninstall -n plugin_demo
```

### Output Example

```bash
acli plugin uninstall -n plugin_demo
Starting to uninstall plugin: plugin_demo
Start marking plugin status as Uninstalling
Start cleaning the plugin directory of other hosts in the cluster
Start cleaning the main control plugin directory
Start removing plugins from plugin registration file
Start updating the acli command to complete the file
Start synchronizing plugin registration files and command completion to the cluster
Plugin uninstalled successfully! Please execute source ~/.bashrc for a better command completion experience

```