---
sidebar_position: 1
---

# dmesg

### Overview

View kernel ring buffer logs (read-only).

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match. No positional argument is accepted (no positional key is declared, so all positional arguments are rejected).

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-F <file>      Reads logs from a file (file read operation, bypassing the read-only kernel
               ring buffer semantics). Rejected.
--file=<file>  Reads logs from a file (file read operation, bypassing the read-only kernel
               ring buffer semantics). Rejected. Because GNU getopt accepts unique-prefix
               abbreviations, any form starting with --fi (--fi / --fil) is also rejected.
               Note that --facility / --follow / --force-prefix are unaffected
               (their shortest unique prefixes are --fa / --fo).
```

### Usage Example

```bash
acli system dmesg -T --level=err
```

### Output Example

```bash
# acli system dmesg -T --level=err
[Tue Sep  8 10:30:01 2026] EDAC sbridge: ECC errors on CPU0
[Tue Sep  8 10:31:12 2026] megaraid_sas 0000:03:00.0: resetting adapter
```