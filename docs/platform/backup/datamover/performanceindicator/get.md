---
sidebar_position: 10
---
 
# get
操作概述: 查询datamover运行过程中的性能指标项和运行状态
 
命令参数: 
```bash
-v|--vm-id=string                   必要参数，指定datamover对应的虚拟机，示例：7441066936147
-i|--host-id=string                 必要参数，用于指出datamover服务运行的主机节点，示例：host-9cc2c4105d08
```
 
使用示例:
```bash
acli platform backup datamover performanceindicator get -v=4529668817336 --host-id="host-0050569b7e33"
```
 
结果示例:
```bash
正确案例：
{"level":"FULL","types":[{"unit":"ms","desc":"duration time","name":"metrics_type_span"},{"unit":"","desc":"","name":"metrics_type_total"},{"unit":"count","desc":"statistic bool count","name":"metrics_type_bool"},{"unit":"","desc":"","name":"metrics_type_int"}],"metrics":[{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io write","name":"metrics_dm_io_write","type":"metrics_type_span"},{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in read","name":"metrics_dm_io_queue_read","type":"metrics_type_int"},{"level":"FAST","parent":"","unit":"count","desc":"queue length in read/write","name":"metrics_dm_io_queue","type":"metrics_type_int"},{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in write","name":"metrics_dm_io_queue_write","type":"metrics_type_int"},{"level":"FULL","parent":"metrics_dm_io","unit":"","desc":"async io read dst","name":"metrics_dm_io_read_dst","type":"metrics_type_span"},{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io read","name":"metrics_dm_io_read","type":"metrics_type_span"},{"level":"FULL","parent":"","unit":"count","desc":"queue length in calc hash","name":"metrics_dm_calc_queue","type":"metrics_type_int"},{"level":"FAST","parent":"","unit":"","desc":"async io read and write","name":"metrics_dm_io","type":"metrics_type_span"},{"level":"FULL","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in read dst","name":"metrics_dm_io_queue_read_dst","type":"metrics_type_int"},{"level":"FULL","parent":"metrics_dm_io","unit":"","desc":"calc hash","name":"metrics_dm_io_calc_hash","type":"metrics_type_span"}]}
错误案例：
错误：请求失败： 无法找到datamover进程的配置文件路径
```