---
sidebar_position: 1
---

# set

### Overview

Set device-level multipath custom configuration for the specified vendor/product on the specified node. 

### Command Parameters

```bash
-n|--hostname=string              Optional parameter, target host name. Defaults to the current node. Example: host-xxxx
-v|--vendor=string                Required parameter, multipath.conf vendor field. Example: DellEMC
-p|--product=string               Required parameter, multipath.conf product field. Example: PowerStore
--path_grouping_policy=string     Optional parameter, path grouping policy. Values: failover (active/standby)/multibus (default, load balancing)/group_by_prio (group by path priority)/group_by_serial (group by storage controller serial)/group_by_node_name (group by target node name). Example: --path_grouping_policy=failover
--path_selector=string            Optional parameter, path selection algorithm. Values: round-robin 0 (default)/service-time 0/queue-length 0. Example: --path_selector="service-time 0"
--path_checker=string             Optional parameter (high-risk), path status check method. Values: tur (default)/directio/readsector0/emc_clariion/hp_sw/rdac/cciss_tur/none. Example: --path_checker=tur
--detect_checker=string           Optional parameter (high-risk), auto-select path check method. Values: yes (default)/no. Example: --detect_checker=yes
--prio=string                     Optional parameter, path priority calculation method. Values: alua/const (default)/rdac/ontap/emc/hp_sw/hds/datacore/random/sysfs/ana/weightedpath/path_latency/iet. Example: --prio=const
--prio_args=string                Optional parameter, priority additional arguments. exclusive_pref_bit (only for prio alua/sysfs)/preferredip=ip (only for prio iet). Example: --prio_args="exclusive_pref_bit"
--detect_prio=string              Optional parameter, auto-detect priority method. Values: yes (default)/no. Example: --detect_prio=yes
--failback=string                 Optional parameter, high-priority path group failback strategy. Values: immediate (default)/manual/followover/<positive integer> (delay N seconds before switching). Example: --failback=immediate
--rr_weight=string                Optional parameter, round-robin path weight distribution. Values: uniform (default)/priorities. Example: --rr_weight=priorities
--dev_loss_tmo=string             Optional parameter, max wait time before removing device after physical path loss. Values: infinity (default, never timeout)/<integer> (remove after N seconds). Example: --dev_loss_tmo=infinity
--fast_io_fail_tmo=string         Optional parameter, max blocking I/O wait time when physical path fails (must be less than dev_loss_tmo). Values: off (disabled)/<integer> (fail after N seconds, default 5). Example: --fast_io_fail_tmo=5
--no_path_retry=string            Optional parameter, I/O retry behavior when all paths of a LUN are offline. Values: fail (default, fail immediately)/queue (retry in queue indefinitely)/<positive integer> (fail after N retries). Example: --no_path_retry=fail
--uid_attribute=string            Optional parameter (high-risk), udev attribute used as path WWID. Values: ID_SERIAL (default)/ID_WWN/ID_UID. Example: --uid_attribute=ID_SERIAL
--features=string                 Optional parameter, kernel multipath module special features to enable, default 0. Format: features "N feature1 [args] ...". Supported feature types: queue_if_no_path/pg_init_retries [N]/pg_init_delay_msecs [N]. Example: --features="1 queue_if_no_path"
--max_sectors_kb=string           Optional parameter, max sectors sent per I/O for a LUN device. Values: 0 (default, system default)/<positive integer> (unit: kb). Example: --max_sectors_kb=0
--flush_on_last_del=string        Optional parameter (high-risk), deletion strategy when the last path of a LUN is deleted. Values: never (reject if I/O is queued)/unused (default, reject if LUN is in use)/always (flush I/O then delete, may hang). Example: --flush_on_last_del=unused
```

### Usage Example

```bash
acli system multipathconfig devicepolicy set -n host-xxxx -v DellEMC -p PowerStore --path_checker tur --features "1 queue_if_no_path"
```

### Output Example

```bash
{"affected_storages": ["3648bd4a100fa95b6550a2d9c000002ac"]}
```
