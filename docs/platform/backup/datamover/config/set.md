---
sidebar_position: 10
---
 
# set
操作概述: 用于修改datamover的配置文件
 
命令参数: 
```bash
-f|--filename=string                                 必要参数，指定要修改的配置文件名称，枚举值为：'setting', 'default', 'backup-task-config-template', 'writespeed-task-config-template'
-d|--data=object                                     必要参数，待修改的配置项，配置文件中点号分割的字段名需要修改为下划线分割。示例，修改default.json文件的metrics.fail_stop_max为16时，命令参数为 --filename default --data.metrics_fail_stop_max 16
-d|--data.advanced_config_io_queue_depth=integer        每个线程的IO队列深度（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：16
-d|--data.advanced_config_max_block_size=integer        数据传输过程中最大IO块大小, 单位为KB（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：4096
-d|--data.backup_task_template_path=string              本地备份任务的任务配置模板路径（所属配置文件：setting.json）示例：/usr/share/perl5/VTP/Vm/Backup/Datamover/backup_task_config_template.json
-d|--data.cancel_interval_secs=integer                  任务取消的时间间隔（所属配置文件：setting.json）示例：30
-d|--data.cancel_wait_secs=integer                      任务取消的最大等待时间（所属配置文件：setting.json）示例：30
-d|--data.datamover_bin=string                          datamover可执行文件路径（所属配置文件：setting.json）示例：/sf/bin/datamover
-d|--data.datamover_io_retry_times=integer              单个IO失败时的重试次数（所属配置文件：default.json）示例：3
-d|--data.debug_on=integer                              datamover是否开启调试（所属配置文件：setting.json）示例：0
-d|--data.dst_coroutine_num=integer                     当使用baksys.qcow2时, 插件的协程数（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：16
-d|--data.dst_io_queue_size=integer                     当使用baksys.qcow2时, 插件的队列深度（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：128
-d|--data.dst_l2_cache_limit=integer                    当使用baksys.qcow2时, 插件的L2缓存上限（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：8
-d|--data.dst_plugin=string                             目标端插件名称，将与plugin_dir拼接形成完整的插件路径，${plugin_dir}/$dst_plugin.so（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：baksys_qcow2
-d|--data.dst_plugin_dir=string                         当使用baksys.qcow2时, baksys.qcow2插件目录（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：/sf/lib/storage-plugins
-d|--data.dst_plugin_name=string                        当使用baksys.qcow2时, baksys.qcow2插件名称（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：libdatamover_qcow2
-d|--data.http_request_timeout_default=integer          datamover发送HTTP请求的超时默认值, 单位为秒（所属配置文件：default.json）示例：60
-d|--data.http_request_timeout_max=integer              datamover发送HTTP请求的超时最大值, 单位为秒（所属配置文件：default.json）示例：300
-d|--data.http_request_timeout_min=integer              datamover发送HTTP请求的超时最小值, 单位为秒（所属配置文件：default.json）示例：0
-d|--data.http_server_hb_check_interval_seconds=integer datamover监测心跳超时的时间间隔（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：30
-d|--data.http_server_hb_timeout_seconds=integer        管控面查询datamover心跳超时时间，管控面查询请求的间隔超过该时间，datamover自动终止（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：600
-d|--data.http_timeout=integer                          HTTP请求的超时阈值（所属配置文件：setting.json）示例：600
-d|--data.metrics_fail_stop_max=integer                 性能指标采集失败时上报的最大次数, 超过该次数，性能指标将停止（所属配置文件：default.json）示例：32
-d|--data.metrics_report_inflight_sleep_max=integer     生命周期框架监测报告时，等待上报任务结果的最大sleep时间，单位为毫秒（所属配置文件：default.json）示例：128
-d|--data.metrics_report_inflight_sleep_ms=integer      生命周期框架监测报告时，等待上报任务结果的sleep时间，单位为毫秒（所属配置文件：default.json）示例：1
-d|--data.metrics_switch_interval_seconds=integer       性能指标采集接收与上报之间的时间间隔, 单位为秒（所属配置文件：default.json）示例：5
-d|--data.plugin_dir=string                             存储插件so目录（所属配置文件：setting.json, backup_task_config_template.json, writespeed_task_config_template.json）示例：/sf/lib/storage-plugins
-d|--data.plugin_prdsys_sangfor_prefetch_num=integer    生命周期插件中预缓存段的数量（所属配置文件：default.json）示例：5
-d|--data.progress_interval_secs=integer                进度更新间隔时间（所属配置文件：setting.json）示例：10
-d|--data.progress_retry_max_cnt=integer                进度查询的最大重试次数（所属配置文件：setting.json）示例：18
-d|--data.src_advanced_options_compress_lz4=integer     启用LZ4压缩（所属配置文件：backup_task_config_template.json）示例：0
-d|--data.src_advanced_options_skip_zero=integer        是否跳过0数据（所属配置文件：backup_task_config_template.json）示例：1
-d|--data.src_advanced_options_transport_mode=string    数据传输模式（所属配置文件：backup_task_config_template.json）示例：nbd
-d|--data.src_plugin=string                             源端插件名称，将与plugin_dir拼接形成完整的插件路径，${plugin_dir}/$src_plugin.so（所属配置文件：backup_task_config_template.json, writespeed_task_config_template.json）示例：prdsys_sangfor
-d|--data.suspend_timeout=integer                       datamover任务挂起状态的超时时间（所属配置文件：setting.json）示例：600
-d|--data.terminate_wait_secs=integer                   任务强制结束前的最大等待时间（所属配置文件：setting.json）示例：30
-d|--data.writespeed_task_template_path=string          存储备份检测任务的任务配置模板路径（所属配置文件：setting.json）示例：/usr/share/perl5/VTP/Vm/Backup/Datamover/writespeed_task_config_template.json
```
 
使用示例:
```bash
acli platform backup datamover config set --filename setting --data.debug_on 0
acli platform backup datamover config set -f default -d.metrics_fail_stop_max 1
```
 
结果示例:
```bash
错误案例：
Error: Request failed: 字段 'debug_on'(对应的实际配置项 'debug_on')在配置文件 /sf/cfg/datamover/default.json 中不存在
正常案例：
OK
```