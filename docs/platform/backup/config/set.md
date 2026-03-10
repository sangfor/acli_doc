---
sidebar_position: 1
---

# set

### 操作概述

修改备份任务配置文件backup.json的内容

### 命令参数

```bash
  --limited-task=integer                        并发运行的块流任务数限制，范围：1 到 10，示例：5
  --limited-speed=integer                       块流的最大速率限制，范围：1 到 314572800（300MB/s），示例：104857600
  --backup-speed=integer                        创建备份的总限速，范围：min-backup-speed 到 max-backup-speed，示例：52428800
  --backup-job-speed=integer                    创建备份时单个磁盘镜像的作业限速，范围：1 到 209715200（200MB/s），示例：104857600
  --max-count=integer                           非VS存储的最大任务数，范围：min-storage-task-count 到 max-storage-task-count，示例：10
  --auto-speed=integer                          自动降速开关，枚举值：0 或 1，示例：1
  --max-delete-task=integer                     删除备份文件的最大任务数，范围：min-storage-delete-task-count 到 max-storage-delete-task-count，示例：5
  --delete-speed=integer                        删除备份的最大速率，范围：min-delete-speed 到 max-delete-speed，示例：104857600
  --max-archive-task=integer                    归档任务的最大任务数，范围：1 到 16，示例：8
  --max-backup-copy-task=integer                备份复制任务的最大任务数，范围：1 到 16，示例：8
  --max-healthcheck-task=integer                备份健康检查任务的最大任务数，范围：1 到 16，示例：8
  --healthcheck-speed=integer                   健康检查备份的最大速率，范围：1 到 314572800（300MB/s），示例：104857600
  --backup-speed-limit-connection=integer       无代理备份单磁盘连接的速率限制，范围：backup-speed-limit-connection-min 到 backup-speed-limit-connection-max，示例：52428800
  --backup-speed-limit-host=integer             无代理备份单主机的速率限制，范围：backup-speed-limit-host-min 到 backup-speed-limit-host-max，示例：262144000
  --storage-task-limit=integer                  无代理备份的存储任务并发数限制，范围：storage-task-limit-min 到 storage-task-limit-max，示例：8
  --snapshot-merge-speed=integer                删除快照时的最大合并速率，范围：snapshot-merge-speed-min 到 snapshot-merge-speed-max，示例：104857600
  --backup-io-queue-max-concurrency=integer     单主机备份IO队列的最大并发数，范围：min-backup-io-queue-max-concurrency 到 max-backup-io-queue-max-concurrency，示例：16
  --min-backup-speed=integer                    创建备份的最小速率，示例：10485760
  --max-backup-speed=integer                    创建备份的最大速率，示例：314572800
  --min-delete-speed=integer                    删除备份的最小速率，示例：10485760
  --max-delete-speed=integer                    删除备份的最大速率，示例：314572800
  --write-merge-num=integer                     写合并线程数，示例：4
  --num-coroutines=integer                      协程数，示例：16
  --is-separate=integer                         IO读写分离标志，非0代表分离会提高备份速度，0代表不分离速度较慢，示例：1
  --read-merge-cluster=integer                  读合并集群数，示例：4
  --read-co-num=integer                         读协程数，示例：16
  --min-backup-io-queue-max-concurrency=integer 单主机备份IO队列并发数的最小值限制，示例：4
  --max-backup-io-queue-max-concurrency=integer 单主机备份IO队列并发数的最大值限制，示例：32
  --cdp-io-queue-max-concurrency=integer        单主机CDP备份IO队列的最大并发数，示例：16
  --healthcheck-host-limited-task=integer       单主机健康检查的并发任务数限制，示例：4
  --storage-task-limit-min=integer              无代理���份存储任务并发数的最小值限制，示例：2
  --storage-task-limit-max=integer              无代理备份存储任务并发数的最大值限制，示例：16
  --backup-speed-limit-host-min=integer         无代理备份主机速率的最小值限制，示例：10485760
  --backup-speed-limit-host-max=integer         无代理备份主机速率的最大值限制，示例：524288000
  --backup-speed-limit-connection-min=integer   无代理备份连接速率的最小值限制，示例：10485760
  --backup-speed-limit-connection-max=integer   无代理备份连接速率的最大值限制，示例：262144000
  --agentless-backup-task=integer               无代理备份单主机的默认并发任务数，范围：agentless-backup-task-min 到 agentless-backup-task-max，示例：4
  --agentless-backup-task-min=integer           无代理备份单主机并发任务数的最小值限制，示例：1
  --agentless-backup-task-max=integer           无代理备份单主机并发任务数的最大值限制，示例：8
  --agentless-disk-resource-task=integer        无代理备份单主机磁盘资源的并发任务数，范围：agentless-disk-resource-task-min 到 agentless-disk-resource-task-max，示例：4
  --agentless-disk-resource-task-min=integer    无代理备份单主机磁盘资源并发任务数的最小值限制，示例：1
  --agentless-disk-resource-task-max=integer    无代理备份单主机磁盘资源并发任务数的最大值限制，示例：8
  --backup-cmk-recycle-seconds=integer          备份主密钥CMK的回收时间（秒），示例：604800
  --min-s3-capacity=integer                     单个S3存储的最小容量限制256GB，示例：274877906944
  --max-s3-capacity=integer                     单个S3存储的最大容量限制100TB，示例：109951162777600
  --max-s3-num-limit=integer                    集群中最多能挂载的S3存储数量，示例：16
  --min-storage-task-count=integer              存储备份并发的最小值限制，示例：4
  --max-storage-task-count=integer              存储备份并发的最大值限制，示例：32
  --min-storage-delete-task-count=integer       存储清理并发的最小值限制，示例：2
  --max-storage-delete-task-count=integer       存储清理并发的最大值限制，示例：16
  --snapshot-merge-speed-min=integer            外部快照删除时合并速率的最小值限制，示例：10485760
  --snapshot-merge-speed-max=integer            外部快照删除时合并速率的最大值限制，示例：209715200
```

### 使用示例

```bash
acli platform backup datamover config set --read-co-num 4 --is-separate 0
```

### 结果示例

```bash
ok
```
