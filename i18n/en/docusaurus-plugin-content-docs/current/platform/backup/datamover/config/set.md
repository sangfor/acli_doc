---
sidebar_position: 1
---

# set

### Overview

set datamover config file

### Command Parameters
```bash
-f|--filename=string                                    Required parameter, Specify the config file name to set, The enumerated values are: 'setting', 'default', 'backup-task-config-template', 'writespeed-task-config-template', Enum values: setting,backup-task-config-template,writespeed-task-config-template,default
-d|--data=object                                        Required parameter, Configuration items to be modified, The fields separated by dots in the configuration file need to be changed to be separated by underscores. For example, when modifying the metrics.fail_stop_max field in default.json file to 16, the command parameters are: --filename default --data.metrics_fail_stop_max 16
--data.backup_task_template_path=string                 Local backup task configuration template path (config file: setting,json) example: /usr/share/perl5/VTP/Vm/Backup/Datamover/backup_task_config_template.json
--data.writespeed_task_template_path=string             Storage backup detection task configuration template path (config file: setting,json) example: /usr/share/perl5/VTP/Vm/Backup/Datamover/writespeed_task_config_template.json
--data.datamover_bin=string                             datamover executable file path (config file: setting.json) example: /sf/bin/datamover
--data.progress_retry_max_cnt=integer                   Maximum retry count for progress query (config file: setting,json) example: 18
--data.progress_interval_secs=integer                   Progress update interval time (config file: setting,json) example: 10
--data.cancel_interval_secs=integer                     Task cancellation interval time (config file: setting,json) example: 30
--data.terminate_wait_secs=integer                      Maximum wait time before forced task termination (config file: setting,json) example: 30
--data.cancel_wait_secs=integer                         Maximum wait time for task cancellation (config file: setting,json) example: 30
--data.http_timeout=integer                             HTTP request timeout threshold (config file: setting,json) example: 600
--data.suspend_timeout=integer                          Timeout time for datamover task suspension state (config file: setting,json) example: 600
--data.debug_on=integer                                 Whether to enable debug for datamover (config file: setting,json) example: 0
--data.plugin_dir=string                                Storage plugin so directory (config file: setting,json, backup_task_config_template.json, writespeed_task_config_template.json) example: /sf/lib/storage-plugins
--data.http_server_hb_timeout_seconds=integer           Timeout for management plane to query datamover heartbeat, If the interval of management plane query requests exceeds this time, datamover will automatically terminate (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: 600
--data.http_server_hb_check_interval_seconds=integer    Time interval for datamover to monitor heartbeat timeout (config file: backup_task_config_template,json, writespeed_task_config_template.json) example: 30
--data.src_plugin=string                                Source plugin name, will be concatenated with plugin_dir to form the complete plugin path, ${plugin_dir}/$src_plugin,so (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: prdsys_sangfor
--data.src_advanced_options_skip_zero=integer           Whether to skip zero data (config file: backup_task_config_template,json) example: 1
--data.src_advanced_options_compress_lz4=integer        Enable LZ4 compression (config file: backup_task_config_template,json) example: 0
--data.src_advanced_options_transport_mode=string       Data transmission mode (config file: backup_task_config_template,json) example: nbd
--data.dst_plugin=string                                Destination plugin name, will be concatenated with plugin_dir to form the complete plugin path, ${plugin_dir}/$dst_plugin,so (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: baksys_qcow2
--data.dst_plugin_dir=string                            When using baksys,qcow2, baksys.qcow2 plugin directory (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: /sf/lib/storage-plugins
--data.dst_plugin_name=string                           When using baksys,qcow2, baksys.qcow2 plugin name (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: libdatamover_qcow2
--data.dst_io_queue_size=integer                        When using baksys,qcow2, plugin queue depth (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: 128
--data.dst_coroutine_num=integer                        When using baksys,qcow2, plugin coroutine count (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: 16
--data.dst_l2_cache_limit=integer                       When using baksys,qcow2, plugin L2 cache limit (config file: backup_task_config_template.json, writespeed_task_config_template.json) example: 8
--data.advanced_config_max_block_size=integer           Maximum IO block size during data transmission, unit: KB (config file: backup_task_config_template,json, writespeed_task_config_template.json) example: 4096
--data.advanced_config_io_queue_depth=integer           IO queue depth per thread (config file: backup_task_config_template,json, writespeed_task_config_template.json) example: 16
--data.http_request_timeout_min=integer                 Minimum timeout value for datamover HTTP requests, unit: seconds (config file: default,json) example: 0
--data.http_request_timeout_max=integer                 Maximum timeout value for datamover HTTP requests, unit: seconds (config file: default,json) example: 300
--data.http_request_timeout_default=integer             Default timeout value for datamover HTTP requests, unit: seconds (config file: default,json) example: 60
--data.plugin_prdsys_sangfor_prefetch_num=integer       Number of pre-cache segments in lifecycle plugin (config file: default,json) example: 5
--data.metrics_report_inflight_sleep_ms=integer         Sleep time for waiting task result reporting during lifecycle framework monitoring, unit: milliseconds (config file: default,json) example: 1
--data.metrics_report_inflight_sleep_max=integer        Maximum sleep time for waiting task result reporting during lifecycle framework monitoring, unit: milliseconds (config file: default,json) example: 128
--data.metrics_switch_interval_seconds=integer          Time interval between performance metrics collection reception and reporting, unit: seconds (config file: default,json) example: 5
--data.metrics_fail_stop_max=integer                    Maximum retry count for performance metrics collection failure reporting, Performance metrics will stop after exceeding this count (config file: default.json) example: 32
--data.datamover_io_retry_times=integer                 Retry count when single IO fails (config file: default,json) example: 3
```

### Usage Example

```bash
acli platform backup datamover config set --filename setting --data.debug_on 0
acli platform backup datamover config set -f default -d.metrics_fail_stop_max 1
```

### Output Example

```bash
Error Examples:
Error: Request failed: Field 'debug_on' (corresponding actual configuration item 'debug_on') does not exist in configuration file /sf/cfg/datamover/default.json
Normal case:
OK
```