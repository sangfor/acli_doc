---
sidebar_position: 1
---

# dpdoctor

### Overview

Run dataplane troubleshooting checks and display environment, interface, service status, and session statistics.

### Command Parameters

Command format:

```bash
acli network dpdoctor <OPTIONS> <VALUE>
```

```text
-h|--help           Show help information; no value is required
-t|--time=string    Specify a date in YYYYMMDD format, for example, 20230101
-c|--case=string    Specify a check; supported values are listed below
-s|--show=string    Specify the information to display; supported values are listed below
```

Supported checks for `-c|--case`:

| Value | Description |
| --- | --- |
| config | Configuration check |
| service | Service check |
| func | Function check |
| vlink | vlink check |
| drop | Packet drop check |
| perf | Performance check |
| log | Log check |
| platform | Platform check |
| upgrade | Upgrade check |
| nic | NIC check |

Supported information types for `-s|--show`:

| Value | Description |
| --- | --- |
| env | Environment information |
| iface | Interface information |
| ifstat | Interface statistics |
| ifirq | Interface interrupt information |
| dpaf | Dataplane CPU affinity |
| session | Session count for each device and the total count |
| alg | ALG count for each device and the total count |
| fdb | FDB count for each device and the total count |
| status | Dataplane service status |

### Usage Example

```bash
acli network dpdoctor -h
```

### Output Example

Running `acli network dpdoctor -h` returns the following help:

```text
Usage: dpdoctor <OPTIONS> <VALUE>
OPTIONS:
    -h|--help:      show help info
    -t|--time:      specify the time, format is 20230101
    -c|--case:      specify the test case
        - config:       config check
        - service:      service check
        - func:         function check
        - vlink:        vlink check
        - drop:         drop pkts check
        - perf:         performance check
        - log:          log check
        - platform:     platform check
        - upgrade:      upgrade check
        - nic:          nic check
    -s|--show:      show the env info
        - env:          show the env info
        - iface:        show the ifaces' info
        - ifstat:       show the ifaces' statistics
        - ifirq:        show the ifaces' irq info
        - dpaf:         show the affinity of dp
        - session:      show the session num for each device and total num
        - alg:          show the alg num for each device and total num
        - fdb:          show the fdb num for each device and total num
        - status:           show the dp service status
```
