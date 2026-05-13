---
sidebar_position: 1
---

# set

### Overview

Set the content of backup task configuration file backup.json

### Command Parameters
```bash
--limited-task=integer                           Limit on the number of block stream tasks running concurrently, range: 1 to 10, example: 5
--limited-speed=integer                          Maximum speed limit for block stream, range: 1 to 314572800 (300MB/s), example: 104857600
--backup-speed=integer                           Total speed limit for creating backup, range: min-backup-speed to max-backup-speed, example: 52428800
--backup-job-speed=integer                       Speed limit for single disk image job when creating backup, range: 1 to 209715200 (200MB/s), example: 104857600
--max-count=integer                              Maximum number of tasks for non-VS storage, range: min-storage-task-count to max-storage-task-count, example: 10
--auto-speed=integer                             Automatic speed reduction switch, enumeration value: 0 or 1, example: 1, Enum values: 0,1
--max-delete-task=integer                        Maximum number of tasks for deleting backup files, range: min-storage-delete-task-count to max-storage-delete-task-count, example: 5
--delete-speed=integer                           Maximum speed for deleting backup, range: min-delete-speed to max-delete-speed, example: 104857600
--max-archive-task=integer                       Maximum number of tasks for archive task, range: 1 to 16, example: 8
--max-backup-copy-task=integer                   Maximum number of tasks for backup copy task, range: 1 to 16, example: 8
--max-healthcheck-task=integer                   Maximum number of tasks for backup health check task, range: 1 to 16, example: 8
--healthcheck-speed=integer                      Maximum speed for health check backup, range: 1 to 314572800 (300MB/s), example: 104857600
--backup-speed-limit-connection=integer          Speed limit for single disk connection in agentless backup, range: backup-speed-limit-connection-min to backup-speed-limit-connection-max, example: 52428800
--backup-speed-limit-host=integer                Speed limit for single host in agentless backup, range: backup-speed-limit-host-min to backup-speed-limit-host-max, example: 262144000
--storage-task-limit=integer                     Storage task concurrency limit for agentless backup, range: storage-task-limit-min to storage-task-limit-max, example: 8
--snapshot-merge-speed=integer                   Maximum merge rate when deleting snapshot, range: snapshot-merge-speed-min to snapshot-merge-speed-max, example: 104857600
--backup-io-queue-max-concurrency=integer        Maximum concurrency of single host backup IO queue, range: min-backup-io-queue-max-concurrency to max-backup-io-queue-max-concurrency, example: 16
--min-backup-speed=integer                       Minimum speed for creating backup, example: 10485760
--max-backup-speed=integer                       Maximum speed for creating backup, example: 314572800
--min-delete-speed=integer                       Minimum speed for deleting backup, example: 10485760
--max-delete-speed=integer                       Maximum speed for deleting backup, example: 314572800
--write-merge-num=integer                        Number of write merge threads, example: 4
--num-coroutines=integer                         Number of coroutines, example: 16
--is-separate=integer                            IO read/write separation flag, non-zero means separation improves backup speed, 0 means no separation is slower, example: 1
--read-merge-cluster=integer                     Number of read merge clusters, example: 4
--read-co-num=integer                            Number of read coroutines, example: 16
--min-backup-io-queue-max-concurrency=integer    Minimum value limit of single host backup IO queue concurrency, example: 4
--max-backup-io-queue-max-concurrency=integer    Maximum value limit of single host backup IO queue concurrency, example: 32
--cdp-io-queue-max-concurrency=integer           Maximum concurrency of single host CDP backup IO queue, example: 16
--healthcheck-host-limited-task=integer          Limit on concurrent tasks for single host health check, example: 4
--storage-task-limit-min=integer                 Minimum value limit of agentless backup storage task concurrency, example: 2
--storage-task-limit-max=integer                 Maximum value limit of agentless backup storage task concurrency, example: 16
--backup-speed-limit-host-min=integer            Minimum value limit of agentless backup host speed, example: 10485760
--backup-speed-limit-host-max=integer            Maximum value limit of agentless backup host speed, example: 524288000
--backup-speed-limit-connection-min=integer      Minimum value limit of agentless backup connection speed, example: 10485760
--backup-speed-limit-connection-max=integer      Maximum value limit of agentless backup connection speed, example: 262144000
--agentless-backup-task=integer                  Default number of concurrent tasks for single host in agentless backup, range: agentless-backup-task-min to agentless-backup-task-max, example: 4
--agentless-backup-task-min=integer              Minimum value limit of concurrent tasks for single host in agentless backup, example: 1
--agentless-backup-task-max=integer              Maximum value limit of concurrent tasks for single host in agentless backup, example: 8
--agentless-disk-resource-task=integer           Number of concurrent tasks for disk resources of single host in agentless backup, range: agentless-disk-resource-task-min to agentless-disk-resource-task-max, example: 4
--agentless-disk-resource-task-min=integer       Minimum value limit of concurrent tasks for disk resources of single host in agentless backup, example: 1
--agentless-disk-resource-task-max=integer       Maximum value limit of concurrent tasks for disk resources of single host in agentless backup, example: 8
--backup-cmk-recycle-seconds=integer             Recycle time (seconds) of backup master key CMK, example: 604800
--min-s3-capacity=integer                        Minimum capacity limit of single S3 storage 256GB, example: 274877906944
--max-s3-capacity=integer                        Maximum capacity limit of single S3 storage 100TB, example: 109951162777600
--max-s3-num-limit=integer                       Maximum number of S3 storages that can be mounted in the cluster, example: 16
--min-storage-task-count=integer                 Minimum value limit of storage backup concurrency, example: 4
--max-storage-task-count=integer                 Maximum value limit of storage backup concurrency, example: 32
--min-storage-delete-task-count=integer          Minimum value limit of storage cleanup concurrency, example: 2
--max-storage-delete-task-count=integer          Maximum value limit of storage cleanup concurrency, example: 16
--snapshot-merge-speed-min=integer               Minimum value limit of merge rate when deleting external snapshot, example: 10485760
--snapshot-merge-speed-max=integer               Maximum value limit of merge rate when deleting external snapshot, example: 209715200
```

### Usage Example

```bash
acli platform backup config set --limited-task 5 --auto-speed 1
```

### Output Example

```bash
ok
```