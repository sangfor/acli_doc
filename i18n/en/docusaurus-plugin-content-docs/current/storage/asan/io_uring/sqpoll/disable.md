---
sidebar_position: 1
---

# disable

### Overview

Disable io_uring sqpoll mode in the cache service of a virtual datastore

### Command Parameters

```bash
-v|--volume-id=string      Required parameter, volume id, example: a4ef106e_vs_vol_rep2
```

### Usage Example

```bash
acli storage asan io_uring sqpoll disable -v a4ef106e_vs_vol_rep2
```

### Output Example

```bash
sqpoll-disable  vol=a4ef106e_vs_vol_rep2  target=interrupt   STATUS: SUCCESS

  HOST               RESULT  DETAIL
  host-002246213d6b  OK      converged
  host-6c92bf51945a  OK      converged

  volume mode: interrupt (persisted)
  hosts: 2/2 converged
```

If a host in the volume fails the prechecks, the switch fails and is rolled back:

```bash
sqpoll-disable  vol=a4ef106e_vs_vol_rep2  target=interrupt   STATUS: FAILED

  HOST               RESULT     DETAIL
  host-002246213d6b  FAILED     precheck: host is in maintenance
  host-6c92bf51945a  REVERTING  applied here, cron will revert

  volume mode: sqpoll (unchanged, not persisted)
  hosts: 1/2 converged
```