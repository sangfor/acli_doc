---
sidebar_position: 2
---

# remove

### Overview

Remove the nohz_full kernel boot parameter from the host

### Command Parameters

```bash
-h|--hostname=string    Host node name, e.g. host-0cc47a6bd88e. Defaults to the local node when not provided.
-g|--grub-root=string   Grub directory path, must end with /boot/grub. For aSV containerized deployment the default is /boot/boot/grub; bare-metal scenarios must pass /boot/grub explicitly.
```

### Usage Example

```bash
acli platform node nohz-full remove
acli platform node nohz-full remove -h host-0cc47a6bd88e
acli platform node nohz-full remove -h host-0cc47a6bd88e -g /boot/grub
```

### Output Example

```bash
success: 1
action: remove
grub_root: /boot/boot/grub
```
