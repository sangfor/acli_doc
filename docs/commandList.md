---
sidebar_position: 2
sidebar_label: 命令列表
title: aCLI命令列表
---


**`跟新时间: 2025-11-14`**
:::info 以下是最新的命令列表
:::

| 序号 | 命令               | 描述                                  | 命名空间                                      | 完整命令                                                |
|------|--------------------|---------------------------------------|-----------------------------------------------|---------------------------------------------------------|
| 1    | info               | 系统CPU信息                           | system.cpu                                    | acli system cpu info                                    |
| 2    | list               | 展示除虚拟存储以外的其他存储信息列表  | storage.other                                 | acli storage other list                                 |
| 3    | list               | 展示所有的acli命令                    | acli.command                                  | acli acli command list                                  |
| 4    | get                | 展示acli工具自身的日志                | acli.log                                      | acli acli log get                                       |
| 5    | mount              | 查看指定存储ID的挂载信息              | storage                                       | acli storage mount                                      |
| 6    | ps                 | ps命令                                | system                                        | acli system ps                                          |
| 7    | ping               | ping命令                              | system                                        | acli system ping                                        |
| 8    | df                 | df命令                                | system                                        | acli system df                                          |
| 9    | free               | free命令                              | system                                        | acli system free                                        |
| 10   | rm                 | rm命令，限制删除特定目录下的文件      | system                                        | acli system rm                                          |
| 11   | ls                 | ls命令，限制查看特定目录下的文件      | system                                        | acli system ls                                          |
| 12   | get                | 获取系统主机信息                      | system.hosts                                  | acli system hosts get                                   |
| 13   | get                | 获取内存的ce_count数据                | system.memory.ce_count                        | acli system memory ce_count get                         |
| 14   | get                | sfd_ps_mem.py命令                     | system.memory.usage                           | acli system memory usage get                            |
| 15   | get                | 获取系统内存ECC数据                   | system.memory.ecc_data                        | acli system memory ecc_data get                         |
| 16   | uname              | uname命令                             | system                                        | acli system uname                                       |
| 17   | kill               | kill命令                              | system                                        | acli system kill                                        |
| 18   | mpstat             | mpstat命令                            | system                                        | acli system mpstat                                      |
| 19   | perf               | perf命令                              | system                                        | acli system perf                                        |
| 20   | lsof               | lsof命令                              | system                                        | acli system lsof                                        |
| 21   | iostat             | iostat命令                            | system                                        | acli system iostat                                      |
| 22   | du                 | du命令                                | system                                        | acli system du                                          |
| 23   | fio                | fio命令                               | system                                        | acli system fio                                         |
| 24   | stat               | stat命令                              | system                                        | acli system stat                                        |
| 25   | lsblk              | lsblk命令                             | system                                        | acli system lsblk                                       |
| 26   | multipath          | multipath命令                         | system                                        | acli system multipath                                   |
| 27   | smartctl           | smartctl命令                          | system                                        | acli system smartctl                                    |
| 28   | chping             | chping命令                            | system                                        | acli system chping                                      |
| 29   | ethtool            | ethtool命令                           | system                                        | acli system ethtool                                     |
| 30   | realethtool        | realethtool命令                       | system                                        | acli system realethtool                                 |
| 31   | tcpdump            | tcpdump命令                           | system                                        | acli system tcpdump                                     |
| 32   | netstat            | netstat命令                           | system                                        | acli system netstat                                     |
| 33   | dmidecode          | dmidecode命令                         | system                                        | acli system dmidecode                                   |
| 34   | lldptool           | lldptool命令                          | system                                        | acli system lldptool                                    |
| 35   | ipmitool           | ipmitool命令                          | system                                        | acli system ipmitool                                    |
| 36   | vmstat             | vmstat命令                            | system                                        | acli system vmstat                                      |
| 37   | uptime             | uptime命令                            | system                                        | acli system uptime                                      |
| 38   | vmware-toolbox-cmd | vmware-toolbox-cmd命令                | system                                        | acli system vmware-toolbox-cmd                          |
| 39   | rpm                | rpm命令                               | system                                        | acli system rpm                                         |
| 40   | dmesg              | dmesg命令                             | system                                        | acli system dmesg                                       |
| 41   | slabtop            | slabtop命令                           | system                                        | acli system slabtop                                     |
| 42   | sysctl             | sysctl命令                            | system                                        | acli system sysctl                                      |
| 43   | watch              | watch命令                             | system                                        | acli system watch                                       |
| 44   |  sar               |  sar命令                              | system                                        | acli system  sar                                        |
| 45   | pmap               | pmap命令                              | system                                        | acli system pmap                                        |
| 46   | taskset            | taskset命令                           | system                                        | acli system taskset                                     |
| 47   | blockdev           | blockdev命令                          | system                                        | acli system blockdev                                    |
| 48   | lsusb              | lsusb命令                             | system                                        | acli system lsusb                                       |
| 49   | lspci              | lspci命令                             | system                                        | acli system lspci                                       |
| 50   | sg_map             | sg_map命令                            | system                                        | acli system sg_map                                      |
| 51   | lsscsi             | lsscsi命令                            | system                                        | acli system lsscsi                                      |
| 52   | rescan-scsi-bus    | rescan-scsi-bus命令                   | system                                        | acli system rescan-scsi-bus                             |
| 53   | systool            | systool命令                           | system                                        | acli system systool                                     |
| 54   | irqtop             | irqtop命令                            | system                                        | acli system irqtop                                      |
| 55   | iscsiadm           | iscsiadm命令                          | system                                        | acli system iscsiadm                                    |
| 56   | megaclisas-status  | megaclisas-status命令                 | system                                        | acli system megaclisas-status                           |
| 57   | storcli            | storcli命令                           | system                                        | acli system storcli                                     |
| 58   | arcconf            | arcconf命令                           | system                                        | acli system arcconf                                     |
| 59   | lsiutil            | lsiutil命令                           | system                                        | acli system lsiutil                                     |
| 60   | lsi_megarc         | lsi_megarc命令                        | system                                        | acli system lsi_megarc                                  |
| 61   | lsi_fw             | lsi_fw命令                            | system                                        | acli system lsi_fw                                      |
| 62   | lsi_mr             | lsi_mr命令                            | system                                        | acli system lsi_mr                                      |
| 63   | sas3ircu           | sas3ircu命令                          | system                                        | acli system sas3ircu                                    |
| 64   | sas2ircu           | sas2ircu命令                          | system                                        | acli system sas2ircu                                    |
| 65   | sas3flash          | sas3flash命令                         | system                                        | acli system sas3flash                                   |
| 66   | lsiutil            | lsiutil命令                           | system                                        | acli system lsiutil                                     |
| 67   | lsi_megarc         | lsi_megarc命令                        | system                                        | acli system lsi_megarc                                  |
| 68   | lsi_fw             | lsi_fw命令                            | system                                        | acli system lsi_fw                                      |
| 69   | lsi_mr             | lsi_mr命令                            | system                                        | acli system lsi_mr                                      |
| 70   | sas3ircu           | sas3ircu命令                          | system                                        | acli system sas3ircu                                    |
| 71   | sas2ircu           | sas2ircu命令                          | system                                        | acli system sas2ircu                                    |
| 72   | sas3flash          | sas3flash命令                         | system                                        | acli system sas3flash                                   |
| 73   | lsiutil            | lsiutil命令                           | system                                        | acli system lsiutil                                     |
| 74   | lsi_megarc         | lsi_megarc命令                        | system                                        | acli system lsi_megarc                                  |
| 75   | lsi_fw             | lsi_fw命令                            | system                                        | acli system lsi_fw                                      |
| 76   | lsi_mr             | lsi_mr命令                            | system                                        | acli system lsi_mr                                      |
| 77   | sas3ircu           | sas3ircu命令                          | system                                        | acli system sas3ircu                                    |
| 78   | sas2ircu           | sas2ircu命令                          | system                                        | acli system sas2ircu                                    |
| 79   | sas3flash          | sas3flash命令                         | system                                        | acli system sas3flash                                   |
| 80   | restart            | 重启pmx-proxy服务                     | service.asv.pmx-proxy                         | acli service asv pmx-proxy restart                      |
| 81   | stop               | 停止pmx-proxy服务                     | service.asv.pmx-proxy                         | acli service asv pmx-proxy stop                         |
| 82   | start              | 启动pmx-proxy服务                     | service.asv.pmx-proxy                         | acli service asv pmx-proxy start                        |
| 83   | status             | 查看pmx-proxy服务状态                 | service.asv.pmx-proxy                         | acli service asv pmx-proxy status                       |
| 84   | restart            | 重启rrdcached服务                     | service.asv.rrdcached                         | acli service asv rrdcached restart                      |
| 85   | status             | 查看zk服务状态                        | service.asv.zk                                | acli service asv zk status                              |
| 86   | start              | 启动authorize_server服务              | service.asv.authorize_server                  | acli service asv authorize_server start                 |
| 87   | status             | 查看vtpalertd服务状态                 | service.asv.vtpalertd                         | acli service asv vtpalertd status                       |
| 88   | status             | 查看mysql服务状态                     | service.asv.mysql                             | acli service asv mysql status                           |
| 89   | restart            | 重启sangfor_waf服务                   | service.asv.sangfor_waf                       | acli service asv sangfor_waf restart                    |
| 90   | status             | 查看corosync服务状态                  | service.asv.corosync                          | acli service asv corosync status                        |
| 91   | restart            | 重启vn-manager-service-api服务        | service.anet.vn-manager-service-api           | acli service anet vn-manager-service-api restart        |
| 92   | start              | 启动vn-manager-service-api服务        | service.anet.vn-manager-service-api           | acli service anet vn-manager-service-api start          |
| 93   | status             | 查看vn-manager-service-api服务状态    | service.anet.vn-manager-service-api           | acli service anet vn-manager-service-api status         |
| 94   | stop               | 停止vn-manager-service-api服务        | service.anet.vn-manager-service-api           | acli service anet vn-manager-service-api stop           |
| 95   | restart            | 重启vn-node-agent-api服务             | service.anet.vn-node-agent-api                | acli service anet vn-node-agent-api restart             |
| 96   | start              | 启动vn-node-agent-api服务             | service.anet.vn-node-agent-api                | acli service anet vn-node-agent-api start               |
| 97   | status             | 查看vn-node-agent-api服务状态         | service.anet.vn-node-agent-api                | acli service anet vn-node-agent-api status              |
| 98   | stop               | 停止vn-node-agent-api服务             | service.anet.vn-node-agent-api                | acli service anet vn-node-agent-api stop                |
| 99   | restart            | 重启exporter服务                      | service.asv.exporter                          | acli service asv exporter restart                       |
| 100  | start              | 启动exporter服务                      | service.asv.exporter                          | acli service asv exporter start                         |
| 101  | status             | 查看exporter服务状态                  | service.asv.exporter                          | acli service asv exporter status                        |
| 102  | stop               | 停止exporter服务                      | service.asv.exporter                          | acli service asv exporter stop                          |
| 103  | restart            | 重启mysql-managerd服务                | service.asv.mysql-managerd                    | acli service asv mysql-managerd restart                 |
| 104  | start              | 启动mysql-managerd服务                | service.asv.mysql-managerd                    | acli service asv mysql-managerd start                   |
| 105  | status             | 查看mysql-managerd服务状态            | service.asv.mysql-managerd                    | acli service asv mysql-managerd status                  |
| 106  | stop               | 停止mysql-managerd服务                | service.asv.mysql-managerd                    | acli service asv mysql-managerd stop                    |
| 107  | start              | 启动vtpalertd服务                     | service.asv.vtpalertd                         | acli service asv vtpalertd start                        |
| 108  | restart            | 重启authorize_client服务              | service.asv.authorize_client                  | acli service asv authorize_client restart               |
| 109  | restart            | 重启vtplogd服务                       | service.asv.vtplogd                           | acli service asv vtplogd restart                        |
| 110  | stop               | 停止zk服务                            | service.asv.zk                                | acli service asv zk stop                                |
| 111  | status             | 查看vtpperlproxy服务状态              | service.asv.vtpperlproxy                      | acli service asv vtpperlproxy status                    |
| 112  | start              | 启动vtplogd服务                       | service.asv.vtplogd                           | acli service asv vtplogd start                          |
| 113  | start              | 启动zk服务                            | service.asv.zk                                | acli service asv zk start                               |
| 114  | restart            | 重启zk服务                            | service.asv.zk                                | acli service asv zk restart                             |
| 115  | restart            | 重启authorize_server服务              | service.asv.authorize_server                  | acli service asv authorize_server restart               |
| 116  | stop               | 停止vtpcron服务                       | service.asv.vtpcron                           | acli service asv vtpcron stop                           |
| 117  | restart            | 重启vtpcron服务                       | service.asv.vtpcron                           | acli service asv vtpcron restart                        |
| 118  | stop               | 停止vtpdaemon服务                     | service.asv.vtpdaemon                         | acli service asv vtpdaemon stop                         |
| 119  | restart            | 重启vtpalertd服务                     | service.asv.vtpalertd                         | acli service asv vtpalertd restart                      |
| 120  | status             | 查看apache2服务状态                   | service.asv.apache2                           | acli service asv apache2 status                         |
| 121  | stop               | 停止corosync服务                      | service.asv.corosync                          | acli service asv corosync stop                          |
| 122  | status             | 查看rrdcached服务状态                 | service.asv.rrdcached                         | acli service asv rrdcached status                       |
| 123  | stop               | 停止authorize_client服务              | service.asv.authorize_client                  | acli service asv authorize_client stop                  |
| 124  | status             | 查看rsyncd服务状态                    | service.asv.rsyncd                            | acli service asv rsyncd status                          |
| 125  | start              | 启动sangfor_waf服务                   | service.asv.sangfor_waf                       | acli service asv sangfor_waf start                      |
| 126  | start              | 启动pmxcfs服务                        | service.asv.pmxcfs                            | acli service asv pmxcfs start                           |
| 127  | status             | 查看redis服务状态                     | service.asv.redis                             | acli service asv redis status                           |
| 128  | restart            | 重启pmxcfs服务                        | service.asv.pmxcfs                            | acli service asv pmxcfs restart                         |
| 129  | restart            | 重启vtpdaemon服务                     | service.asv.vtpdaemon                         | acli service asv vtpdaemon restart                      |
| 130  | stop               | 停止apache2服务                       | service.asv.apache2                           | acli service asv apache2 stop                           |
| 131  | start              | 启动mysql服务                         | service.asv.mysql                             | acli service asv mysql start                            |
| 132  | stop               | 停止rsyncd服务                        | service.asv.rsyncd                            | acli service asv rsyncd stop                            |
| 133  | start              | 启动vtpcron服务                       | service.asv.vtpcron                           | acli service asv vtpcron start                          |
| 134  | status             | 查看pmxcfs服务状态                    | service.asv.pmxcfs                            | acli service asv pmxcfs status                          |
| 135  | stop               | 停止vtplogd服务                       | service.asv.vtplogd                           | acli service asv vtplogd stop                           |
| 136  | stop               | 停止sangfor_waf服务                   | service.asv.sangfor_waf                       | acli service asv sangfor_waf stop                       |
| 137  | stop               | 停止vtpstatd服务                      | service.asv.vtpstatd                          | acli service asv vtpstatd stop                          |
| 138  | restart            | 重启sfd-restart-perl-services.sh服务  | service.asv.perl-services                     | acli service asv perl-services restart                  |
| 139  | status             | 查看authorize_server服务状态          | service.asv.authorize_server                  | acli service asv authorize_server status                |
| 140  | stop               | 停止mysql服务                         | service.asv.mysql                             | acli service asv mysql stop                             |
| 141  | restart            | 重启rrdcached服务                     | service.asv.rrdcached                         | acli service asv rrdcached restart                      |
| 142  | start              | 启动corosync服务                      | service.asv.corosync                          | acli service asv corosync start                         |
| 143  | start              | 启动vtpdaemon服务                     | service.asv.vtpdaemon                         | acli service asv vtpdaemon start                        |
| 144  | restart            | 重启mysql服务                         | service.asv.mysql                             | acli service asv mysql restart                          |
| 145  | stop               | 停止redis服务                         | service.asv.redis                             | acli service asv redis stop                             |
| 146  | stop               | 停止vtpalertd服务                     | service.asv.vtpalertd                         | acli service asv vtpalertd stop                         |
| 147  | restart            | 重启corosync服务                      | service.asv.corosync                          | acli service asv corosync restart                       |
| 148  | restart            | 重启vtpstatd服务                      | service.asv.vtpstatd                          | acli service asv vtpstatd restart                       |
| 149  | status             | 查看vtpdaemon服务状态                 | service.asv.vtpdaemon                         | acli service asv vtpdaemon status                       |
| 150  | get                | 获取平台日志                          | log                                           | acli log get                                            |
| 151  | create             | 创建dump虚拟机内存任务                | vm.memory.dump                                | acli vm memory dump create                              |
| 152  | cancel             | 取消dump虚拟机内存任务                | vm.memory.dump                                | acli vm memory dump cancel                              |
| 153  | progress           | 查询dump虚拟机内存任务的进度          | vm.memory.dump                                | acli vm memory dump progress                            |
| 154  | switch             | 日志轮转命令                          | log                                           | acli log switch                                         |
| 155  | check              | 检查vlink配置状态                     | network.vlink                                 | acli network vlink check                                |
| 156  | get                | 获取虚拟机网卡队列数                  | vm.nic.queuecount                             | acli vm nic queuecount get                              |
| 157  | set                | 更新虚拟机网卡队列数                  | vm.nic.queuecount                             | acli vm nic queuecount set                              |
| 158  | reorder            | 调整网口顺序                          | network.nic                                   | acli network nic reorder                                |
| 159  | set                | 更新集群VXLAN配置                     | network.vxlan                                 | acli network vxlan set                                  |
| 160  | enable             | 启用网口lldp                          | network.nic.lldp                              | acli network nic lldp enable                            |
| 161  | disable            | 禁用网口lldp                          | network.nic.lldp                              | acli network nic lldp disable                           |
| 162  | set                | 设置网口队列数                        | network.nic.queue                             | acli network nic queue set                              |
| 163  | set                | 设置当前网口环形缓冲区参数            | network.nic.ring                              | acli network nic ring set                               |
| 164  | sfd_bytools        | 数据面sfd_byTools.sh脚本              | network                                       | acli network sfd_bytools                                |
| 165  | get                | 查看网口mtu                           | network.nic.mtu                               | acli network nic mtu get                                |
| 166  | set                | 设置网口mtu                           | network.nic.mtu                               | acli network nic mtu set                                |
| 167  | get                | 查看节点信息                          | platform.node                                 | acli platform node get                                  |
| 168  | list               | 查看节点列表                          | platform.node                                 | acli platform node list                                 |
| 169  | list               | 查看主机网口列表                      | network.nic                                   | acli network nic list                                   |
| 170  | get                | 查看主机网口信息                      | network.nic                                   | acli network nic get                                    |
| 171  | get                | 查看网口lldp                          | network.nic.lldp                              | acli network nic lldp get                               |
| 172  | list               | 查看聚合口列表                        | network.bond                                  | acli network bond list                                  |
| 173  | get                | 查看聚合口信息                        | network.bond                                  | acli network bond get                                   |
| 174  | set                | 更新聚合口                            | network.bond                                  | acli network bond set                                   |
| 175  | delete             | 删除聚合口                            | network.bond                                  | acli network bond delete                                |
| 176  | get                | 查看当前网口环形缓冲区参数            | network.nic.ring                              | acli network nic ring get                               |
| 177  | get                | 查看网口队列数                        | network.nic.queue                             | acli network nic queue get                              |
| 178  | set                | 设置主机网口                          | network.nic                                   | acli network nic set                                    |
| 179  | list               | 查询集群vxlan信息列表                 | network.vxlan                                 | acli network vxlan list                                 |
| 180  | list               | 查看虚拟路由器列表                    | network.anet.vrouter                          | acli network anet vrouter list                          |
| 181  | get                | 查看虚拟路由器信息                    | network.anet.vrouter                          | acli network anet vrouter get                           |
| 182  | migrate            | 迁移虚拟路由器                        | network.anet.vrouter                          | acli network anet vrouter migrate                       |
| 183  | list               | 查看流量镜像列表                      | network.anet.mirror                           | acli network anet mirror list                           |
| 184  | get                | 查看流量镜像信息                      | network.anet.mirror                           | acli network anet mirror get                            |
| 185  | delete             | 删除流量镜像                          | network.anet.mirror                           | acli network anet mirror delete                         |
| 186  | fullsync           | 执行全同步任务                        | network.anet.config                           | acli network anet config fullsync                       |
| 187  | get                | 查看转发核                            | network.anet.forwarding                       | acli network anet forwarding get                        |
| 188  | set                | 调整转发核                            | network.anet.forwarding                       | acli network anet forwarding set                        |
| 189  | get                | 查看mac表容量                         | network.anet.config.mac                       | acli network anet config mac get                        |
| 190  | set                | 调整mac表容量                         | network.anet.config.mac                       | acli network anet config mac set                        |
| 191  | get                | 查看nat表项限制                       | network.anet.config.nat                       | acli network anet config nat get                        |
| 192  | set                | 调整nat表项限制                       | network.anet.config.nat                       | acli network anet config nat set                        |
| 193  | get                | 查看数据面session信息                 | network.anet.session                          | acli network anet session get                           |
| 194  | get                | 查看数据面vrrp信息                    | network.anet.vrouter.vrrp                     | acli network anet vrouter vrrp get                      |
| 195  | get                | 查看虚拟机指定磁盘的aio信息           | vm.disk.aio                                   | acli vm disk aio get                                    |
| 196  | get                | 查看虚拟机io_uring的状态              | vm.disk.io_uring                              | acli vm disk io_uring get                               |
| 197  | top                | top命令，用于查看进程实时信息         | system                                        | acli system top                                         |
| 198  | list               | 列出所有cgroup目录下和cpu相关的文件   | system.cgroup.cpu                             | acli system cgroup cpu list                             |
| 199  | list               | 展示GPU配置信息列表                   | hardware.gpu.config                           | acli hardware gpu config list                           |
| 200  | list               | 查看cpu微码文件                       | hardware.cpu.microcode.file                   | acli hardware cpu microcode file list                   |
| 201  | get                | 查看系统mounts信息                    | system.mounts                                 | acli system mounts get                                  |
| 202  | list               | 展示虚拟机锁列表                      | vm.lock                                       | acli vm lock list                                       |
| 203  | get                | 获取进程的栈信息                      | system.proc.stack                             | acli system proc stack get                              |
| 204  | get                | 获得smartpqi的版本信息                | system.smartpqi.version                       | acli system smartpqi version get                        |
| 205  | info               | 查看系统内存详细信息                  | system.memory                                 | acli system memory info                                 |
| 206  | list               | 列出节点证书                          | platform.node.cert                            | acli platform node cert list                            |
| 207  | mysql-manager-cli  | 平台mysql-manager-cli工具             | platform                                      | acli platform mysql-manager-cli                         |
| 208  | lsmod              | lsmod命令，用于查看内核模块           | system                                        | acli system lsmod                                       |
| 209  | date               | date命令，获取当前系统时间            | system                                        | acli system date                                        |
| 210  | get                | 获取虚拟机状态                        | vm.status                                     | acli vm status get                                      |
| 211  | zkcli              | 平台zkcli-c工具                       | platform.zookeeper                            | acli platform zookeeper zkcli                           |
| 212  | get                | 获取虚拟机磁盘路径                    | vm.disk.path                                  | acli vm disk path get                                   |
| 213  | get                | 获取GPU配置信息                       | hardware.gpu.config                           | acli hardware gpu config get                            |
| 214  | list               | 获取所有虚拟机信息                    | vm                                            | acli vm list                                            |
| 215  | get                | 获得系统信息                          | platform.info                                 | acli platform info get                                  |
| 216  | status             | 验证/cfs目录写入能力                  | platform.cfs                                  | acli platform cfs status                                |
| 217  | pidstat            | pidstat命令，用于查看系统进程资源     | system                                        | acli system pidstat                                     |
| 218  | check              | 检查网络端口状态                      | network.port                                  | acli network port check                                 |
| 219  | get                | 获取证书的md5值                       | platform.node.cert                            | acli platform node cert get                             |
| 220  | get                | 获取MySQL配置                         | platform.mysql.config                         | acli platform mysql config get                          |
| 221  | sensors            | sensors命令，用于查看传感器收集的信息 | system                                        | acli system sensors                                     |
| 222  | get                | 获取网络配置通道检测模块配置          | network.anet.config.configchannel             | acli network anet config configchannel get              |
| 223  | set                | 设置网络配置通道检测模块配置          | network.anet.config.configchannel             | acli network anet config configchannel set              |
| 224  | list               | 获取网络配置通道各服务当前健康状态    | network.anet.config.configchannel.serviceinfo | acli network anet config configchannel serviceinfo list |
| 225  | stop               | 停止loadman服务                       | service.asv.loadman                           | acli service asv loadman stop                           |
| 226  | start              | 启动loadman服务                       | service.asv.loadman                           | acli service asv loadman start                          |
| 227  | status             | 查询loadman服务状态                   | service.asv.loadman                           | acli service asv loadman status                         |
| 228  | restart            | 重启loadman服务                       | service.asv.loadman                           | acli service asv loadman restart                        |
| 229  | get                | 获取loadman服务配置                   | service.asv.loadman.config                    | acli service asv loadman config get                     |
| 230  | set                | 更新loadman服务配置                   | service.asv.loadman.config                    | acli service asv loadman config set                     |
| 231  | get                | 获取过载保护功能相关维护信息          | service.asv.loadman.maintenance               | acli service asv loadman maintenance get                |
| 232  | set                | 过载保护功能相关维护操作              | service.asv.loadman.maintenance               | acli service asv loadman maintenance set                |
| 233  | get                | 获取过载保护功能相关维护信息          | service.asv.loadman.maintenance               | acli service asv loadman maintenance get                |
| 234  | set                | 过载保护功能相关维护操作              | service.asv.loadman.maintenance               | acli service asv loadman maintenance set                |
