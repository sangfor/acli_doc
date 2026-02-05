---
sidebar_position: 1
---

# get

### 操作概述

获取datamover运行过程中的性能瓶颈探测报告

### 命令参数

```bash
-v|--vm-id=string      必要参数，指定datamover对应的虚拟机，示例：7441066936147
-i|--host-id=string    必要参数，用于指出datamover服务运行的主机节点，示例：host-9cc2c4105d08
```

### 使用示例

```bash
acli platform backup datamover performancereport get -v=4529668817336 --host-id="host-0050569b7e33"
```

### 结果示例

```bash
正确案例:
{"full_report":{"seconds":24,"report":{"merged":[{"metrics":{"count":501,"min":3,"avg":164,"max":3359,"metrics_per_second":20},"type":{"unit":"ms","desc":"duration time","name":"metrics_type_span"},"children":[{"metrics":{"count":508,"min":3,"avg":105,"max":2775,"metrics_per_second":21},"type":{"unit":"ms","desc":"duration time","name":"metrics_type_span"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io read","name":"metrics_dm_io_read","type":"metrics_type_span"}},{"metrics":{"count":504,"min":63,"avg":71,"max":799,"metrics_per_second":21},"type":{"unit":"ms","desc":"duration time","name":"metrics_type_span"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io write","name":"metrics_dm_io_write","type":"metrics_type_span"}}],"meta":{"level":"FAST","parent":"","unit":"","desc":"async io read and write","name":"metrics_dm_io","type":"metrics_type_span"}},{"metrics":{"count":520,"min":0,"avg":13,"max":16,"metrics_per_second":21},"type":{"unit":"","desc":"","name":"metrics_type_int"},"children":[{"metrics":{"count":508,"min":0,"avg":4,"max":14,"metrics_per_second":21},"type":{"unit":"","desc":"","name":"metrics_type_int"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in write","name":"metrics_dm_io_queue_write","type":"metrics_type_int"}},{"metrics":{"count":520,"min":0,"avg":8,"max":15,"metrics_per_second":21},"type":{"unit":"","desc":"","name":"metrics_type_int"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in read","name":"metrics_dm_io_queue_read","type":"metrics_type_int"}}],"meta":{"level":"FAST","parent":"","unit":"count","desc":"queue length in read/write","name":"metrics_dm_io_queue","type":"metrics_type_int"}}],"threads":[{"report":[{"metrics":{"count":501,"min":3,"avg":164,"max":3359,"metrics_per_second":20},"type":{"unit":"ms","desc":"duration time","name":"metrics_type_span"},"children":[{"metrics":{"count":508,"min":3,"avg":105,"max":2775,"metrics_per_second":21},"type":{"unit":"ms","desc":"duration time","name":"metrics_type_span"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io read","name":"metrics_dm_io_read","type":"metrics_type_span"}},{"metrics":{"count":504,"min":63,"avg":71,"max":799,"metrics_per_second":21},"type":{"unit":"ms","desc":"duration time","name":"metrics_type_span"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io write","name":"metrics_dm_io_write","type":"metrics_type_span"}}],"meta":{"level":"FAST","parent":"","unit":"","desc":"async io read and write","name":"metrics_dm_io","type":"metrics_type_span"}},{"metrics":{"count":520,"min":0,"avg":13,"max":16,"metrics_per_second":21},"type":{"unit":"","desc":"","name":"metrics_type_int"},"children":[{"metrics":{"count":508,"min":0,"avg":4,"max":14,"metrics_per_second":21},"type":{"unit":"","desc":"","name":"metrics_type_int"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in write","name":"metrics_dm_io_queue_write","type":"metrics_type_int"}},{"metrics":{"count":520,"min":0,"avg":8,"max":15,"metrics_per_second":21},"type":{"unit":"","desc":"","name":"metrics_type_int"},"children":[],"meta":{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in read","name":"metrics_dm_io_queue_read","type":"metrics_type_int"}}],"meta":{"level":"FAST","parent":"","unit":"count","desc":"queue length in read/write","name":"metrics_dm_io_queue","type":"metrics_type_int"}}],"tid":"140379649087232"}]},"begin":"2025-12-25T22:26:10+08:00","end":"2025-12-25T22:26:34+08:00"},"level":"FULL","full_bottleneck":{"IO":"read bottleneck "}}
错误案例：
错误：请求失败： 无法找到datamover进程的配置文件路径
```
