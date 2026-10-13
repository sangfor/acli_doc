---
sidebar_position: 1
---

# blkid

### Overview

Query the UUID, file system type and other attributes of block devices (read-only).

### Command Parameters

Command format:

```bash
acli system blkid [<dev>]
```

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match.

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-c|--cache-file=string  Writes a cache file (write operation). Rejected;
                        because GNU getopt accepts unique-prefix abbreviations, any form
                        starting with --c (e.g. --c / --ca) is also rejected
-w|--write=string       Writes the device cache to the specified file (write operation). Rejected;
                        because GNU getopt accepts unique-prefix abbreviations, any form
                        starting with --w (e.g. --w) is also rejected
```

Path whitelist (dev command family path whitelist; only 1 entry, the /dev/ directory):

```bash
/dev/  (block device directory, prefix match, e.g. /dev/sda)
```

### Usage Example

```bash
acli system blkid /dev/sda
```

### Output Example

```bash
# acli system blkid /dev/sda
/dev/sda: UUID="1a2b3c4d-5e6f-7890-abcd-ef1234567890" TYPE="ext4" PARTUUID="12345678-01"
```
