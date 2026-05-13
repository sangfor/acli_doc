---
sidebar_position: 1
---

# iostat

### Overview

View brick iostat

### Command Parameters
```bash
-c|--count=integer    Required parameter, The number of times iostat information is viewed, Example: 2
```

### Usage Example

```bash
acli storage asan brick iostat -c 2
```

### Output Example

```bash
s_show_default: 1 s_show_mds_lba: 0 s_show_logstore: 0
Process: 2025-08-04 17:54:23            r/s         w/s       rKB/s       wKB/s    rrq_sz    wrq_sz    rqu-sz    wqu-sz   r_await   w_await     r_max     w_max
asan_client.70933.io-stats               0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
asan_clientd.42435.io-stats              0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
asan_clientd.41841.io-stats              0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
asan_clientd.41505.io-stats              0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000

Process: 2025-08-04 17:54:24            r/s         w/s       rKB/s       wKB/s    rrq_sz    wrq_sz    rqu-sz    wqu-sz   r_await   w_await     r_max     w_max
asan_client.70933.io-stats               0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
asan_clientd.42435.io-stats              0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
asan_clientd.41841.io-stats              0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
asan_clientd.41505.io-stats              0.00        0.00        0.00        0.00      0.00      0.00      0.00      0.00     0.000     0.000     0.000     0.000
```