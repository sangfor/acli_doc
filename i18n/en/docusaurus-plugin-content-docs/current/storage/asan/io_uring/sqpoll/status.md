---
sidebar_position: 1
---

# status

### Overview

View the io_uring sqpoll mode status in the cache service of a virtual datastore

### Command Parameters

```bash
-v|--volume-id=string      Required parameter, volume id, example: a4ef106e_vs_vol_rep2
```

### Usage Example

```bash
acli storage asan io_uring sqpoll status -v a4ef106e_vs_vol_rep2
```

### Output Example

sqpoll mode is enabled and all hosts in the volume are converged:

```bash
sqpoll-status   vol=a4ef106e_vs_vol_rep2                   STATUS: CONVERGED

  volume: desired=sqpoll  enabled=yes  hosts=3

  HOST               MODE    CONVERGED  KERNEL  SQD CPUS  NOTE
  host-002246213d6b  sqpoll  yes        6.6     70,72
  host-6c92bf51945a  sqpoll  yes        6.6     70,72

  DISKS
    4 disk(s) in sqpoll as expected
```

When the volume has never been configured or hosts are not converged, host status and disk details are expanded item by item:

```bash
sqpoll-status   vol=a4ef106e_vs_vol_rep2               STATUS: NOT CONVERGED

  volume: desired=<unset>  enabled=no  hosts=2   (never configured)

  HOST               MODE       CONVERGED  KERNEL  SQD CPUS  NOTE
  host-002246213d6b  sqpoll     NO         6.6     70        maintenance
  host-6c92bf51945a  interrupt  yes        5.10    -

  DISKS
    1 disk(s) in interrupt as expected
    host-002246213d6b  nvme0n1  nvme  cdev_iouring  sqpoll  cpu70
```


### Field Reference

| Field | Description |
| :---: | :--- |
| `desired` | Desired mode of the volume, `sqpoll` / `interrupt`; shows `<unset>` when never configured |
| `enabled` | Whether sqpoll is enabled for the volume (yes/no) |
| `hosts` | Number of target hosts in the volume |
| `MODE` | Actual mode in effect on the host: sqpoll / interrupt / unknown |
| `CONVERGED` | Whether the actual mode matches the desired mode |
| `KERNEL` | Host kernel version (major.minor only) |
| `SQD CPUS` | CPU cores exclusively occupied by sqpoll on the host |
| `NOTE` | Shows `maintenance` when the host is in maintenance mode |