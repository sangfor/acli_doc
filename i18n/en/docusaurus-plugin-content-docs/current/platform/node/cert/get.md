---
sidebar_position: 1
---

# get

### Overview

Obtain the certificate MD5 value

### Command Parameters
```bash
-p|--path=string    Required parameter, Certificate name, example: vtp-mysql-ssl,key
```

### Usage Example

```bash
acli platform node cert get -p /sf/cfg/mysql/ssl/vtp-mysql-ssl.key
```

### Output Example

```bash
017075738f0ba88fe249d61547d6b5b5
```