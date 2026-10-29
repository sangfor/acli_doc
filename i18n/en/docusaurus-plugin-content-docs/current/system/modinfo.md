---
sidebar_position: 1
---

# modinfo

### Overview

Query kernel module file locations, authors, licenses, dependencies, and signatures.

### Command Parameters

Command format:

```bash
acli system modinfo [options] <module>
```

Supported parameters:

This command uses a closed read-only option allowlist. Unlisted options are rejected.

```text
-a|--author=flag        Display the author
-d|--description=flag   Display the module description
-l|--license=flag       Display the license
-p|--parameters=flag    Display module parameter information
-n|--filename=flag      Display the module filename
-0|--null=flag          Separate output with NUL characters
-V|--version=flag       Display the tool version
-h|--help=flag          Display help information
-F|--field=string       Display the specified field
-k|--set-version=string Specify the kernel version to query
<module>               Module name or .ko path; at most one positional argument, for example, ext4
```

Version and help queries do not require a module.

Forbidden arguments:

```text
-b|--basedir=string    Changes the module lookup root and can read .ko files from arbitrary directories; rejected
```

modinfo itself has no write capability; these restrictions control lookup scope and invocation arguments. Unlisted options and calls with more than one module positional argument are rejected.

### Usage Example

```bash
acli system modinfo ext4
```

### Output Example

The following is an excerpt of the actual output; the remaining signature bytes are omitted:

```text
filename:       /lib/modules/6.6.0-99.0.0.102.sfc.7.0.0.0053.sf6.x86_64/kernel/fs/ext4/ext4.ko.xz
softdep:        pre: crc32c
license:        GPL
description:    Fourth Extended Filesystem
author:         Remy Card, Stephen Tweedie, Andrew Morton, Andreas Dilger, Theodore Ts'o and others
alias:          fs-ext4
alias:          ext3
alias:          fs-ext3
alias:          ext2
alias:          fs-ext2
srcversion:     3D72639F7F4812906AEDF83
depends:        jbd2,mbcache
retpoline:      Y
intree:         Y
name:           ext4
vermagic:       6.6.0-99.0.0.102.sfc.7.0.0.0053.sf6.x86_64 SMP mod_unload modversions
sig_id:         PKCS#7
signer:         Cloud kernel signing key
sig_key:        08:1A:F8:80:29:47:CB:D0:E8:72:7D:13:1A:CC:5D:39:C6:B9:12:12
sig_hashalgo:   sha256
signature:      6F:DD:41:45:18:37:2C:72:D7:20:4E:5D:58:81:43:A0:A1:44:DB:5D:
                ...
```
