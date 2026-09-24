---
sidebar_position: 1
---

# ss

### Overview

View network socket statistics (TCP/UDP connections, etc.; read-only).

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match.

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-F|--filter=<file>  Reads filter conditions from a file (file read operation). Rejected.
                 Because GNU getopt accepts unique-prefix abbreviations, any form starting
                 with --fi (--fi / --fil) is also rejected. Note that --family is unaffected
                 (its shortest unique prefix is --fa).
```

### Usage Example

```bash
acli system ss -tln
```

### Output Example

```bash
# acli system ss -tln
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port
LISTEN   0        128              0.0.0.0:22             0.0.0.0:*
LISTEN   0        128                 [::]:80                [::]:*
```