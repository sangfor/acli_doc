---
sidebar_position: 1
---

# get

### 操作概述

根据sagaflow gid 或者 treace id 获得sagaflow的状态

### 命令参数

```bash
-g|--gid=string         -g和-t二选一，sagaflow的id，示例：7832ac58-41ea-4f2f-8423-0255a927998e
-t|--trace=string       -g和-t二选一，trace的id，示例：9afef2c16aaeb46047b51d09843e8cce
-c|--children           是否输出所有的子sagaflow

```

### 使用示例

```bash
acli vm sagaflow get -g 7832ac58-41ea-4f2f-8423-0255a927998e -c
acli vm sagaflow get -g 7832ac58-41ea-4f2f-8423-0255a927998e
acli vm sagaflow get -t 9afef2c16aaeb46047b51d09843e8cce -c
acli vm sagaflow get -t 9afef2c16aaeb46047b51d09843e8cce
```

### 结果示例

```bash

acli vm sagaflow get --gid 7832ac58-41ea-4f2f-8423-0255a927998e
sagaflow info:
{"ID":1,"create_time":"2026-03-10T18:15:09+08:00","update_time":"2026-03-10T18:15:12+08:00","gid":"7832ac58-41ea-4f2f-8423-0255a927998e","trans_type":"workflow","status":"succeed","query_prepared":"https://svc-master:20210/hci/volume/server/v1/workflow/resume","protocol":"http","finish_time":"2026-03-10T18:15:12+08:00","result":"Ct8EChkKCGVuY29kaW5nEg1qc29uL3Byb3RvYnVmCi8KC21lc3NhZ2VUeXBlEiB3b3JrZmxvdy5PZmZsaW5lUmVwbGljYVRyYW5zRm9ybRKQBHsic3RhcnRTYWdhZmxvd09wdGlvbiI6eyJydW5JZCI6Ijc4MzJhYzU4LTQxZWEtNGYyZi04NDIzLTAyNTVhOTI3OTk4ZSIsInRhc2tVc2luZ1Jlc291cmNlIjp0cnVlLCJicmFuY2hJbmRleCI6MjJ9LCJmb3JtIjp7InJlcXVlc3QiOnsic3RvcmFnZUlEIjoiMzYwMDBjMjk0NWEzMTdlOGU0MjU4ZmFkMWM5ODFlNGM2XzAwNTA1NjhlNmFmNSJ9LCJ0YXJnZXRGaWxlUGF0aCI6InZvbHVtZS9kdW1wLzM2MDAwYzI5NDVhMzE3ZThlNDI1OGZhZDFjOTgxZTRjNl8wMDUwNTY4ZTZhZjUvMzYwMDBjMjk0NWEzMTdlOGU0MjU4ZmFkMWM5ODFlNGM2XzAwNTA1NjhlNmFmNV9yZXBsaWNhLmpzb24iLCJ0bXBSZXBsaWNhRGF0YUZpbGVQYXRoIjoidm9sdW1lL3RlbXAvcmVwbGljYS8zNjAwMGMyOTQ1YTMxN2U4ZTQyNThmYWQxYzk4MWU0YzZfMDA1MDU2OGU2YWY1Lmpzb24iLCJ0YXNrSW5mbyI6eyJ0YXNrSWQiOiI3ODMyYWM1OC00MWVhLTRmMmYtODQyMy0wMjU1YTkyNzk5OGUiLCJydW5uaW5nSG9zdCI6Imhvc3QtMDA1MDU2OGU2YWY1In19fQ==","options":"{\"timeout_to_fail\":86400,\"retry_interval\":10,\"backoff_coefficient\":2,\"concurrent\":false,\"continue_finished_as_new\":false,\"continue_failed_as_new\":false,\"max_retry_interval\":600}","custom_data":"{\"data\":\"CukBChkKCGVuY29kaW5nEg1qc29uL3Byb3RvYnVmCi8KC21lc3NhZ2VUeXBlEiB3b3JrZmxvdy5PZmZsaW5lUmVwbGljYVRyYW5zRm9ybRKaAXsic3RhcnRTYWdhZmxvd09wdGlvbiI6eyJydW5JZCI6Ijc4MzJhYzU4LTQxZWEtNGYyZi04NDIzLTAyNTVhOTI3OTk4ZSJ9LCJmb3JtIjp7InJlcXVlc3QiOnsic3RvcmFnZUlEIjoiMzYwMDBjMjk0NWEzMTdlOGU0MjU4ZmFkMWM5ODFlNGM2XzAwNTA1NjhlNmFmNSJ9fX0=\",\"name\":\"workflow.OfflineReplica\"}","next_cron_interval":10,"next_cron_time":"2026-03-10T18:15:19+08:00","ext_data":"{\"trace_id\":\"\",\"user_data\":\"{\\\"progress\\\":100}\"}","concurrent":false}


decoded result :
 Protobuf decode succeeded, contains 1 Payload(s)

=== Payload 1 ===
Metadata:
  messageType: workflow.OfflineReplicaTransForm
  encoding: json/protobuf
Data (raw, 528 bytes):
  {"startSagaflowOption":{"runId":"7832ac58-41ea-4f2f-8423-0255a927998e","taskUsingResource":true,"branchIndex":22},"form":{"request":{"storageID":"36000c2945a317e8e4258fad1c981e4c6_0050568e6af5"},"targetFilePath":"volume/dump/36000c2945a317e8e4258fad1c981e4c6_0050568e6af5/36000c2945a317e8e4258fad1c981e4c6_0050568e6af5_replica.json","tmpReplicaDataFilePath":"volume/temp/replica/36000c2945a317e8e4258fad1c981e4c6_0050568e6af5.json","taskInfo":{"taskId":"7832ac58-41ea-4f2f-8423-0255a927998e","runningHost":"host-0050568e6af5"}}}

branches not found

```
