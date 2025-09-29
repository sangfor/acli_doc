---
sidebar_position: 10
---

# vs_rpc_tool
操作概述: vs_rpc_tool命令

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan vs_rpc_tool
```

结果示例:
```bash
# acli storage asan vs_rpc_tool -h
--cmd list --brickno num [ --filter str]
--cmd list_bricks --brickno_list <bno1,bno2,...>
--cmd check --brickno num [ --exclude yes|default|weak|finish_weak]
--cmd check_parallel --brickno_list num [ --exclude yes|default|weak|finish_weak] (warn:input must be the same type brick)
--cmd get_rebuild_file
--cmd check_by_gfid --gfids <gfid1,gfid2,...> --exclude_no num
--cmd stat --gfids <gfid1,gfid2,...>
--cmd afr_inject --op <write,read,fallocate,discard,zerofill,create,mkdir,rename,unlink,setxattr,pre_op,post_op> --type [fixed|random] --point [before|after|offline] --fault <0,1,2,3,4> --afr [meta|data] --gfid [gfid] [--client <nfs|tgtd|spdk>]
--cmd afr_inject_heal --enable [0|1] --type [fixed|random] --point [before|middle|after]
--cmd clnt --hostname host --state UNNORMAL
--cmd file_pathinfo --file <gfid1,gfid2,...> or <path1,path2,...>
--cmd lookup [--client <nfs|tgtd|spdk>] --gfids <gfid1,gfid2,...> or --filepath /1.qcow2 /2.qcow2
--cmd heal_meta --gfids <gfid1,gfid2,...>
--cmd memc_enable --enable [0|1]
--cmd memc_change_size --size [0-?]
--cmd memc_get_hit
--cmd memc_clear_hit
--cmd memc_get_status [--status host ]
--cmd memc_dump_filemeta --brickid brickid --gfid gfid
--cmd memc_dump_fileinfo --brickid brickid [ --gfid gfid ]
--cmd memc_del_file --brickid brickid --gfid gfid
--cmd memc_inject --point [write_hdd|write_mem|read_hdd|read_mem|discard_hdd|discard_mem|zero_hdd|zero_mem] --brickid brickid --gfid [gfid]
--cmd prealloc_dump_fiemap --brickid brickid --gfid gfid
--cmd prealloc_info --brickid brickid
--cmd prealloc_rm_lv --brickid brickid --size size
--cmd iolog_nfs --iolog on/off
--cmd get_iolog_nfs
--cmd snapshot_enable --switch on/off
--cmd check_mem_leak
--cmd get_policy_hex --sp_dir /storage_policy[/policy_id]
--cmd dr_file_dump --brickid brickid --gfid gfid
--cmd dr_file_set --brickid brickid --gfid gfid --offset offset --len len --fail fail
--cmd afr_dr_file_dump --gfid gfid
--cmd drc_dump --brickid brickid --verbose <0,1>
--cmd drc_set_range --brickid brickid --gfid gfid --offset offset --size size --value value
--cmd drc_get_range --brickid brickid --gfid gfid
--cmd drc_invalidate --brickid brickid --gfid gfid
--cmd drc_logfile_blocks --brickid brickid
--cmd drc_demote
--cmd drc_hibernate --resume <0,1>
--cmd drc_inject --point [read_log_fail | write_log_fail | request_f_write | request_b_write | get_range | clean_range | get_range_dr | wr_fail_return_ack | wr_fail_return_cbk] --brickid brickid --gfid gfid –-errno errno
--cmd set_ban_read_flag --gfid gfid --value <0,1>
--cmd get_heal_state --gfid gfid [--client <nfs|tgtd|spdk>]
--cmd get_heal_state_all [--client <nfs|tgtd|spdk>]
--cmd brick_exit [--pid pid]
--cmd dump_heal_queue --type [wait_list|run_list|all_list] [--client <nfs|tgtd|spdk>]
--cmd brick_dump_client_info --brickid brickid
--cmd dump_vtnfs_info
--cmd set_option --pid pid --option_key key --option_value value
--cmd snapshot_merge_tasks_cancel --pid pid --client nfs/tgtd/vhost
--cmd vss_get_files --brickno num
--cmd vss_unlink --brickno num --gfids <gfid1,gfid2,...>
```