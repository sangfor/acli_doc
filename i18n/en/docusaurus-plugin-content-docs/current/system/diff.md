---
sidebar_position: 1
---

# diff

### Overview

Compare the content differences of two files (read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

```bash
-u|--unified=flag              Optional parameter. Output differences in unified format. Example: acli system diff -u fileA fileB
-q|--brief=flag                Optional parameter. Only report whether the two files differ, without printing detailed differences. Example: acli system diff -q fileA fileB
-i|--ignore-case=flag          Optional parameter. Ignore case differences. Example: acli system diff -i fileA fileB
-w|--ignore-all-space=flag     Optional parameter. Ignore whitespace differences. Example: acli system diff -w fileA fileB
<fileA> <fileB>  Required parameter. Specify the two files to compare (both paths must be in the shared path whitelist of the cat command family).
```

Path whitelist (shared by the cat command family: cat/grep/tail/diff text-view/compare family; 81 entries after redundancy removal; excerpt):

```bash
/etc/hosts
/etc/fstab
/sf/version
/sf/log/
/var/log/
```

Write parameters (rejected on match):

```bash
--version  Query diff version (not allowed, rejected)
-r         Recursively compare directories (not allowed, rejected)
-N         Treat missing files as empty (not allowed, rejected)
-y         Side-by-side output (not allowed, rejected)
--help     Help information (not allowed, rejected)
```

### Usage Example

```bash
acli system diff -u /etc/hosts /etc/fstab
```

### Output Example

```bash
# acli system diff -u /etc/hosts /etc/fstab
--- /etc/hosts	2026-09-01 10:00:00.000000000 +0800
+++ /etc/fstab	2026-09-02 11:00:00.000000000 +0800
@@ -1,3 +1,4 @@
-127.0.0.1   localhost localhost.localdomain
+UUID=1a2b  /  ext4  defaults  1 1
```
