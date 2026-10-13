---
sidebar_position: 1
---

# hostname

### Overview

View node name and domain name (only read-only forms are available; rewriting the node name is not supported).

### Command Parameters

```bash
(None)                View full node name
-f|--fqdn=flag        View fully qualified domain name (FQDN) of node
-i|--ip-address=flag  View IP address of node
-s|--short=flag       View short node name
-h|--help=flag        Print this page
```

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-F             Forbidden. Reads the node name from a file and rewrites the node name (both a write
               operation and an arbitrary file read). Rejected.
--file=<file>  Forbidden. Reads the node name from a file and rewrites the node name. Rejected.
               Because GNU getopt accepts unique-prefix abbreviations, any form starting with --fi
               (--fi / --fil / --file=x) is also rejected. Note that --fqdn is unaffected (its shortest
               unique prefix is --fq, since --f alone is ambiguous), and -f is the read-only
               abbreviation of --fqdn and is also unaffected.
<newname>      Forbidden. A positional new node name (hostname <newname>) is a write operation.
               Rejected; multiple positional arguments are rejected as well.
```

### Usage Example

```bash
acli system hostname -f
```

### Output Example

```bash
host-005056b237a6
```