---
sidebar_position: 1
---

# rm

### Overview

rm command, only deletes files inside the specified directories (only files under whitelisted
directories may be deleted; recursive deletion is forbidden).

### Command Parameters

```bash
-f      Optional parameter. Force deletion without confirmation. Example: acli system rm -f /tmp/test.log
<path>  Positional argument. Absolute path of the file to delete; it must be inside a whitelisted
        directory. Example: acli system rm /tmp/test.log
```

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-r           Forbidden. Recursive deletion (removes a directory and all of its contents), a high-risk
             write operation. Rejected.
-R           Forbidden. Recursive deletion, equivalent to -r. Rejected.
-rf / -fr    Forbidden. Combined short options: any short-option string containing r or R is rejected.
--recursive  Forbidden. Long form of recursive deletion. Rejected. Because GNU getopt accepts
             unique-prefix abbreviations, any form starting with --r (--r / --re / --rec) is also
             rejected. rm has no other long option starting with r, so --r is its shortest unique prefix.
--           Forbidden. The option separator makes the following arguments skip option checking and can
             bypass the forbidden-parameter check. Rejected.
```

Besides the forbidden parameters above, positional arguments may only be absolute paths of files inside
the whitelisted directories; deleting the `/sf/data/local/acli/tmp` directory is forbidden.

### Usage Example

```bash
acli system rm /var/spool/test.log
```

### Output Example

The example below passes a path that is not inside a whitelisted directory; after confirmation the command is
rejected and the list of deletable directories is printed:

```bash
# acli system rm /var/spool/test.log
Are you sure you want to execute the operation? (y[es]/n[o]):Please use absolute paths; you can only delete files under the following directories:
/sf/log/
/run/
/var/log/
/tmp/
/sf/data/
/sf/cfg/
/sf/vs/vscfg/
```