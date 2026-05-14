---
sidebar_position: 1
---

# create

### Overview

Create log collection task

### Command Parameters

```bash
-s|--save-filename=string          Required parameter, collection file name (no file suffix required), use icare ticket number, example: Q2025052718316
-m|--modules=string                Log collection module, use English comma to concatenate specified modules, example: vm_suspend,network
                                   Available modules, default is other, enumerate:
                                      vm_suspend（VM Suspend Issue）             vm_start（VM Start Failure Issue）
                                      host_offline（Host Offline Issue）         network（Network Issue）
                                      storage（Virtual Storage Issue）           slowdisk（Slow Disk Issue, approx. 4min collection time per day）
                                      performance（Performance Issue）           system（Platform Issue）
                                      other（Default Collection Issue, does not collect logs for the above n scenarios）
-d|--date-range=string             Specify date range (use English comma to concatenate start date, example: 2025-06-25,2025-06-27)
                                   Specify a specific date (example: 2025-06-25), default is today if not set
-i|--ips=string                    Specify host ip, use English comma to concatenate specified ips, example: 1.1.1.1,1.2.3.4
                                   Default is collect current host log, set all to collect all hosts
-p|--paths=string                  Specify additional directories or files to collect, will be compressed into extra_tar.tar.gz
                                   Use English comma to concatenate multiple paths, for example: /sf/data/local/you,/sf/ls.txt
-c|--config=string                 JSON configuration file path, used for advanced control of log collection
                                   Example: --config /sf/data/local/config.json
-u|--remote-url=string             Remote target address (check network connectivity before use), example: http://acli.sangfor.com.cn:5888/
-H|--header=string                 HTTP request header, globally valid, format: Header-Name: value
-L|--url-header=string             URL-specific request header, priority higher than --header, format: index:Header-Name:value
                                   Note: index starts from 0
-U|--auth-username=string          Authentication username, note: if multiple target addresses, configure the one with auth-username first
-P|--auth-password=string          Authentication password, note: must appear with auth-username together
                                   If multiple target addresses, configure the one with auth-password first
-v|--vm-ids=string                 Specify virtual machine id, use English comma to concatenate specified vm ids
```

### Usage Example

```bash
# Example 1: Collect network module logs, host 1.1.1.1, date range 2025-06-25 to 2025-06-28
acli log_collect create -s Q2025052777777 -m network -i 1.1.1.1 -d 2025-06-25,2025-06-28

# Example 2: Through ping found HCI can ping acli.sangfor.com.cn; collect vm_suspend module logs, all hosts today's logs
# and automatically upload to log server after collection completes
acli log_collect create -s Q2025062888888 -m vm_suspend -i all -u http://acli.sangfor.com.cn:5888/

# Example 3: No module specified, collect all hosts current date other logs (other is default collection module, does not collect logs for all provided scenarios above)
acli log_collect create -s Q2025072999999 -i all
```

### Output Example

```bash
Log collection task created successfully!
```
