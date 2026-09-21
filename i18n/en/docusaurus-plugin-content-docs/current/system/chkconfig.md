---
sidebar_position: 1
---

# chkconfig

### Overview

View the runlevel configuration of system services (read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

Command format:

```bash
acli system chkconfig --list [<service>]
acli system chkconfig -l [<service>]
```

Supported parameters (whitelist):

```bash
-l|--list [<service>]  Optional parameter. List the runlevel configuration of services; when
                       <service> is omitted all services are listed, otherwise only the given
                       service is listed. Example: acli system chkconfig --list sshd
```

Write parameters (rejected on match):

```bash
--level <levels> <service> on/off/reset  Modifies the startup configuration of a service at specified runlevels (write)
-a|--add                                 Adds a service to chkconfig management (write)
-d|--del                                 Removes a service from chkconfig management (write)
```

### Usage Example

```bash
acli system chkconfig --list sshd
```

### Output Example

```bash
# acli system chkconfig --list sshd
sshd           	0:off	1:off	2:on	3:on	4:on	5:on	6:off
```
