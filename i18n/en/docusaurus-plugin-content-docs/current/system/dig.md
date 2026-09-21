---
sidebar_position: 1
---

# dig

### Overview

Perform DNS queries and get domain resolution records (read-only).

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match.

Command format:

```bash
acli system dig [@<server>] [<domain>] [<type>]
```

Positional arguments (in declaration order):

```bash
@<server>  Optional parameter. 1st positional argument, specify the DNS server to query (@ prefix). Example: @8.8.8.8
<domain>   Optional parameter. 2nd positional argument, specify the domain to query. Example: example.com
<type>     Optional parameter. 3rd positional argument, specify the record type (A/AAAA/MX/NS/TXT, etc.). Example: MX
```

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-f|--file=<file>  Batch mode, reads the query list from a file (file read operation). Rejected.
               Because GNU getopt accepts unique-prefix abbreviations, any form starting with
               --f (--f / --fi / --fil) is also rejected. dig has no other long option starting
               with f, so --f is its shortest unique prefix.
```

### Usage Example

```bash
acli system dig @8.8.8.8 example.com
```

### Output Example

```bash
# acli system dig example.com
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.15 <<>> example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; ANSWER SECTION:
example.com.        3600    IN    A    93.184.216.34
```