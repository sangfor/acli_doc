---
sidebar_position: 10
---

# iostat
操作概述: 获取卷iostat趋势信息

命令参数:
```bash
-v|--volume-id=string        存储卷id，示例：a4ef106e_vs_vol_rep2
-t|--time-frame=string       获取所需的时间长度，枚举值：hour, day, week, custom
-S|--storage=integer         如果需要更新存储趋势则置为1，默认为1。枚举值：0, 1
-h|--hitrate=integer         如果需要更新命中率趋势则置为1，默认为1。枚举值：0, 1
-s|--start=string            (可选)自定义开始时间，配合--time-frame为 custom 使用。格式：'2025-12-12 12:12:12'
-e|--end=string              (可选)自定义结束时间，配合--time-frame为 custom 使用。格式：'2025-12-12 14:12:12'
```

使用示例:
```bash
acli storage asan volume iostat -v a4ef106e_vs_vol_rep2 -t custom -S 1 -h 1 -s '2025-12-12 12:12:12' -e '2025-12-12 14:12:12'
```

结果示例:
```bash
host_hitrate_sheet:
  series:
  start_time: 0
  interval: 0
  end_time: 0
  unit: %
throughput_sheet:
  series:
     data:
     name: IO读数据量

     data:
     name: IO写数据量
  start_time: 1765512735
  interval: 5
  end_time: 1754301690
  unit: Bps
storage_sheet:
  series:
     data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1311921668096, 1311919570944, 1311919570944, 1311919570944, 1311918522368, 1311638552576, 1311638552576, 1311638552576, 1311638552576, 1311638552576
     name: 空闲容量

     data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2097152, 4194304, 4194304, 4194304, 5242880, 285212672, 285212672, 285212672, 285212672, 285212672
     name: 已使用容量

     data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
     name: 失效容量
  start_time: 1749166620
  interval: 86400
  end_time: 1754264220
  unit: B
latency_sheet:
  series:
     data:
     name: IO读延时

     data:
     name: IO写延时
  start_time: 1765512735
  interval: 5
  end_time: 1754301690
  unit: 毫秒
vol_hitrate_sheet:
  series:
     data:
     name: 缓存命中率
  start_time: 0
  interval: 0
  end_time: 0
  unit: %
iops_sheet:
  series:
     data:
     name: IO读次数

     data:
     name: IO写次数
  start_time: 1765512735
  interval: 5
  end_time: 1754301690
  unit: 次/秒
```