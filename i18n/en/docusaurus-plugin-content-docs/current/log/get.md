---
sidebar_position: 1
---

# get

### Overview

Obtain platform logs

### Command Parameters
```bash
-k|--keyword=string       Search keyword, Example: license key
-i|--request-id=string    Call chain request_id, Example: 82ab4228259a3f227b763dd0cc6b53df
-t|--time=string          Specify time, Format: YYYY-MM-DD HH:MM:SS, YYYY-MM-DD HH
-f|--file=string          Specify a file, ensuring the filename does not include a path, Example: sfvt_vtpdaemon.log
-c|--context=integer      Specify the number of context lines, such as 2 or 3
-E|--extend=flag          Use extended regular expressions for the --keyword parameter
-p|--path=string          Specify the absolute path for the search, Only files or directories under /sf/log or /sf/data/local may be specified. If no path is provided, the default search location will be /sf/log. 
                          Only the file or directory names at the specified path may use the wildcard *. The path must be enclosed in quotes. Example: '/sf/log/today/' '/sf/log/today/sfvt*'
-g|--gzip=flag            When the --path parameter is used, the contents of ,gz files can be searched.
                          However, if the --path parameter specifies a directory, only files within the directory can be searched, while files in deeper subdirectories cannot be searched. 

                          Notes:
                          Cross-node search is not supported. To search on another node, please use SSH to connect to that node.
                          If the time is not specified, the default directory for search is /sf/log. Specifying a date is recommended to improve search efficiency.

                          Example 1: Specify a time to automatically decompress white-box logs and quickly view logs on the node for the 6th with the error code of 0x010019FA.
                          acli log get -t '2025-06-06' -k 0x010019FA

                          Example 2: Specify an error to quickly view sfvt_vtpdaemon.log logs on the node containing the following field: Failed to back up the report data.
                          acli log get -k 'Failed to back up the report data.' -f sfvt_vtpdaemon.log

                          Example 3: Specify a call chain to quickly search within the /sf/data/local directory on the node for logs with the request_id (82ab4228259a3f227b763dd0cc6b53df)
                          acli log get -i 82ab4228259a3f227b763dd0cc6b53df -p /sf/data/local
```

### Usage Example

```bash
acli log get -k "info" -f sfvt_vtpsh.log
```

### Output Example

```bash
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.366806 info [sfvt_vtpsh] 21:39:11.366 I 61678 Register.pm(VTP::xx):41 | [7v2#Gq10F3k.0.0] [register_replace] register replace(DataReport process_when_controller_change).
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.499877 info [sfvt_vtpsh] 21:39:11.499 I 61678 Register.pm(VTP::xx):32 | [7v2#Gq10F3k.0.0] [register_precheck] register precheck(DBManager check_replace).
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.499931 info [sfvt_vtpsh] 21:39:11.499 I 61678 Register.pm(VTP::xx):41 | [7v2#Gq10F3k.0.0] [register_replace] register replace(DBManager deal_replaced_db_nodes).
```