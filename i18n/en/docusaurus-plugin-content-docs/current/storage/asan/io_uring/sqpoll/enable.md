---
sidebar_position: 1
---

# enable

### Overview

Enable io_uring sqpoll mode in the cache service of a virtual datastore

### Command Parameters

```bash
-v|--volume-id=string      Required parameter, volume id, example: a4ef106e_vs_vol_rep2
```

### Usage Example

```bash
acli storage asan io_uring sqpoll enable -v a4ef106e_vs_vol_rep2
```

### Output Example

```bash
sqpoll-enable   vol=a4ef106e_vs_vol_rep2  target=sqpoll      STATUS: SUCCESS

  HOST               RESULT  DETAIL
  host-002246213d6b  OK      converged, bind ok
  host-6c92bf51945a  OK      converged, bind ok
  host-a0369f9be720  OK      converged, bind ok

  volume mode: sqpoll (persisted)
  hosts: 3/3 converged
```

If a host in the volume fails the prechecks, the switch fails and is rolled back, showing only the failed host and the reverting state:

```bash
sqpoll-enable   vol=a4ef106e_vs_vol_rep2  target=sqpoll       STATUS: FAILED

  HOST               RESULT     DETAIL
  host-002246213d6b  FAILED     precheck: kernel version below 6.6
  host-6c92bf51945a  REVERTING  applied here, cron will revert

  volume mode: interrupt (unchanged, not persisted)
  hosts: 1/2 converged
```