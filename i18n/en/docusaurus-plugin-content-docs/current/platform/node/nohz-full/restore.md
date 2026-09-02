---
sidebar_position: 3
---

# restore

### Overview

Restore the nohz_full kernel boot parameter on the host

### Command Parameters

```bash
-h|--hostname=string    Host node name, e.g. host-0cc47a6bd88e. Defaults to the local node when not provided.
-g|--grub-root=string   Grub directory path, must end with /boot/grub. For aSV containerized deployment the default is /boot/boot/grub; bare-metal scenarios must pass /boot/grub explicitly.
```

### Usage Example

```bash
acli platform node nohz-full restore
acli platform node nohz-full restore -h host-0cc47a6bd88e
acli platform node nohz-full restore -h host-0cc47a6bd88e -g /boot/grub
```

### Output Example

```bash
success: 1
action: restore
grub_root: /boot/boot/grub
```
