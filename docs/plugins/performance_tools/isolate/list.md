---
sidebar_position: 1
---

# list

### 操作概述

查看 CPU 的隔离状态

### 命令参数

无

### 使用示例

```bash
# 示例1：查看 CPU 的隔离状态
acli performance_tools isolate list
```

### 结果示例

```bash
cgroup                                                                 cpulist             
---                                                                    ---                 
/sys/fs/cgroup/cpuset/./isolate_vm/only_pcpu/cpuset.cpus               0                   
/sys/fs/cgroup/cpuset/./isolate_vm/cpuset.cpus                         0                   
/sys/fs/cgroup/cpuset/./compute/6025407369236/cpuset.cpus              2-7                 
/sys/fs/cgroup/cpuset/./compute/cpuset.cpus                            2-7                 
/sys/fs/cgroup/cpuset/./sys-fs-fuse-connections.mount/cpuset.cpus                          
/sys/fs/cgroup/cpuset/./sys-kernel-debug.mount/cpuset.cpus                                 
/sys/fs/cgroup/cpuset/./user.slice/cpuset.cpus                                             
/sys/fs/cgroup/cpuset/./sys-kernel-tracing.mount/cpuset.cpus                               
/sys/fs/cgroup/cpuset/./init.scope/cpuset.cpus                                             
/sys/fs/cgroup/cpuset/./system.slice/containerd.service/cpuset.cpus                        
/sys/fs/cgroup/cpuset/./system.slice/cron.service/cpuset.cpus                              
/sys/fs/cgroup/cpuset/./system.slice/run-shm.mount/cpuset.cpus                             
/sys/fs/cgroup/cpuset/./system.slice/host-sdog.service/cpuset.cpus                         
/sys/fs/cgroup/cpuset/./system.slice/system-sshd\x2dkeygen.slice/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/idsd.service/cpuset.cpus                              
/sys/fs/cgroup/cpuset/./system.slice/kubelet.service/cpuset.cpus                           
/sys/fs/cgroup/cpuset/./system.slice/system-modprobe.slice/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/host-agentd.service/cpuset.cpus                       
/sys/fs/cgroup/cpuset/./system.slice/systemd-journald.service/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/dev-disk-by\x2dlabel-vtpswap.swap/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/sshd.service/cpuset.cpus                              
/sys/fs/cgroup/cpuset/./system.slice/run-lock.mount/cpuset.cpus                            
/sys/fs/cgroup/cpuset/./system.slice/iMSApp.service/cpuset.cpus                            
/sys/fs/cgroup/cpuset/./system.slice/sf-data.mount/cpuset.cpus                             
/sys/fs/cgroup/cpuset/./system.slice/rsyslog.service/cpuset.cpus                           
/sys/fs/cgroup/cpuset/./system.slice/hostd.service/cpuset.cpus                             
/sys/fs/cgroup/cpuset/./system.slice/lsud.service/cpuset.cpus                              
/sys/fs/cgroup/cpuset/./system.slice/service-monitor.service/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/diagfix-server.service/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/mcelog.service/cpuset.cpus                            
/sys/fs/cgroup/cpuset/./system.slice/containerd-squashfs-grpc.service/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./system.slice/cpuset.cpus                                           
/sys/fs/cgroup/cpuset/./system.slice/dbus.service/cpuset.cpus                              
/sys/fs/cgroup/cpuset/./system.slice/ce_monitor.service/cpuset.cpus                        
/sys/fs/cgroup/cpuset/./system.slice/system-getty.slice/cpuset.cpus                        
/sys/fs/cgroup/cpuset/./system.slice/systemd-logind.service/cpuset.cpus                     
/sys/fs/cgroup/cpuset/./management/unstrict/asan/cpuset.cpus           0,2-7               
/sys/fs/cgroup/cpuset/./management/unstrict/compute/cpuset.cpus        0,2-7               
/sys/fs/cgroup/cpuset/./management/unstrict/bdr/cpuset.cpus            0,2-7               
/sys/fs/cgroup/cpuset/./management/unstrict/adesk/cpuset.cpus          0,2-7               
/sys/fs/cgroup/cpuset/./management/unstrict/asv/cpuset.cpus            0,2-7               
/sys/fs/cgroup/cpuset/./management/unstrict/system/cpuset.cpu
```
