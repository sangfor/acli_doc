---
sidebar_position: 1
---

# list

### Overview

Display the VM lock list

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM ID, Example: 2848367193475
```

### Usage Example

```bash
acli vm lock list -v 1072335336316
```

### Output Example

```bash
# Get the files and directories starting with "vm-id" in the following directory
# "/var/lock/flag_dir/"
# "/cfs/vm_tmp_status/flag_dir/"
# "/cfs/priv/lock/"
1072335336316_vm
1072335336316_p
1072335336316_lock_file
```