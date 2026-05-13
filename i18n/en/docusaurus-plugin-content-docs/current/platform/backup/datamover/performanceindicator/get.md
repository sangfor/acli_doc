---
sidebar_position: 1
---

# get

### Overview

Query performance indicators and running status during datamover operation

### Command Parameters
```bash
-v|--vm-id=string      Required parameter, Specifies the VM corresponding to the datamover, example: 7441066936147
-i|--host-id=string    Required parameter, Used to indicate the host node where the datamover service runs, example: host-9cc2c4105d08
```

### Usage Example

```bash
acli platform backup datamover performanceindicator get -v=4529668817336 --host-id="host-0050569b7e33"
```

### Output Example

```bash
Correct Example:
{"level":"FULL","types":[{"unit":"ms","desc":"duration time","name":"metrics_type_span"},{"unit":"","desc":"","name":"metrics_type_total"},{"unit":"count","desc":"statistic bool count","name":"metrics_type_bool"},{"unit":"","desc":"","name":"metrics_type_int"}],"metrics":[{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io write","name":"metrics_dm_io_write","type":"metrics_type_span"},{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in read","name":"metrics_dm_io_queue_read","type":"metrics_type_int"},{"level":"FAST","parent":"","unit":"count","desc":"queue length in read/write","name":"metrics_dm_io_queue","type":"metrics_type_int"},{"level":"FAST","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in write","name":"metrics_dm_io_queue_write","type":"metrics_type_int"},{"level":"FULL","parent":"metrics_dm_io","unit":"","desc":"async io read dst","name":"metrics_dm_io_read_dst","type":"metrics_type_span"},{"level":"FAST","parent":"metrics_dm_io","unit":"","desc":"async io read","name":"metrics_dm_io_read","type":"metrics_type_span"},{"level":"FULL","parent":"","unit":"count","desc":"queue length in calc hash","name":"metrics_dm_calc_queue","type":"metrics_type_int"},{"level":"FAST","parent":"","unit":"","desc":"async io read and write","name":"metrics_dm_io","type":"metrics_type_span"},{"level":"FULL","parent":"metrics_dm_io_queue","unit":"count","desc":"queue length in read dst","name":"metrics_dm_io_queue_read_dst","type":"metrics_type_int"},{"level":"FULL","parent":"metrics_dm_io","unit":"","desc":"calc hash","name":"metrics_dm_io_calc_hash","type":"metrics_type_span"}]}
Error Case:
Error: Request failed - Unable to locate the configuration file path for the datamover process
```