---
sidebar_position: 1
---

# turbostat

### Overview

View CPU topology, frequency and power consumption statistics (read-only). The command runs inside the asv-con container, with a maximum execution time of 15 seconds.

> Only supported on x86/c86 architectures. On arm architecture, `acli system turbostat` is rejected with an "unsupported on this architecture" message.

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match. Subcommands and positional arguments are not accepted (no positional key is declared, so all positional arguments are rejected).

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-o|--out=<file>  Writes statistics to a file (write operation). Rejected;
              because GNU getopt accepts unique-prefix abbreviations, any form
              starting with --o (--o / --ou) is also rejected
<subcommand>  No positional argument or subcommand is accepted; rejected on match
```

### Usage Example

```bash
acli system turbostat -i 1 --quiet
```

### Output Example

```bash
# acli system turbostat -i 1 --quiet
CPU     GHz    %Busy   Bzy_MHz   TSC_MHz     CPU%c1    CPU%c6    CPU%c7
-       1.60    25.30     2200      2200       3.20      0.00     71.50
0       1.90    30.00     2200      2200       5.00      0.00     65.00
1       1.30    20.60     2200      2200       1.40      0.00     78.00
```
