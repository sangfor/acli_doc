---
sidebar_position: 1
---

# iptables

### Overview

View system firewall rules (iptables, read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).
Query parameters such as `-L/-S/-n/-v/-t` take effect only when combined with `-L` or `-S` (e.g. `-n -L`, `-t nat -S`).

```bash
-L|--list=flag              Optional parameter. List rules.
-S|--list-rules=flag        Optional parameter. List rules in script format.
-n|--numeric=flag           Optional parameter. List rules with numeric addresses (use with -L/-S).
-v|--verbose=flag           Optional parameter. List rules verbosely (use with -L/-S).
-t|--table=string           Optional parameter. Specify the rule table (filter/nat/mangle/raw); use with -L/-S. Example: -t nat -L
--line-numbers=flag         Optional parameter. List rules with line numbers (no short twin; use with -L).
-h|--help=flag              Optional parameter. Show help.
-V|--version=flag           Optional parameter. Show version.
```

Write parameters (rejected on match; short/long pairs):

```bash
-A|--append        Append rule to chain (write firewall rule)
-I|--insert        Insert rule into chain (write firewall rule)
-D|--delete        Delete rule (write firewall rule)
-R|--replace       Replace rule (write firewall rule)
-F|--flush         Flush rules (write firewall rule)
-Z|--zero          Zero counters (write firewall rule)
-P|--policy        Set default policy (write firewall rule)
-N|--new-chain     Create new chain (write firewall rule)
-X|--delete-chain  Delete chain (write firewall rule)
-E|--rename-chain  Rename chain (write firewall rule)
-C|--check         Check rule (write firewall rule)
```

### Usage Example

```bash
acli system iptables -L -n --line-numbers
```

### Output Example

```bash
# acli system iptables -L -n --line-numbers
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
num   target     prot opt source               destination
1     ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0
2     DROP       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:22
```