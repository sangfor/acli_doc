---
sidebar_position: 1
---

# status

### Overview

Query the status of the nohz_full kernel boot parameter on the host

### Command Parameters

```bash
-h|--hostname=string    Host node name, e.g. host-0cc47a6bd88e. Defaults to the local node when not provided.
-g|--grub-root=string   Grub directory path, must end with /boot/grub. For aSV containerized deployment the default is /boot/boot/grub; bare-metal scenarios must pass /boot/grub explicitly.
```

### Usage Example

```bash
acli platform node nohz-full status
acli platform node nohz-full status -h host-0cc47a6bd88e
acli platform node nohz-full status -h host-0cc47a6bd88e -g /boot/grub
```

### Output Example

```bash
grub_root: /boot/boot/grub
files:
  - name: grub.cfg
    exists: true
    has_nohz_full: true
    has_rollback: false
  - name: grub.cfg.kdump
    exists: true
    has_nohz_full: true
    has_rollback: false
```
