---
sidebar_position: 2
sidebar_label: 命令列表
title: aCLI命令列表
---

**`更新时间: 2026-09-21`**
:::info 以下是最新的命令列表
:::

| acli命令 | 命令操作概述 |
| :---: | :---: |
| acli acli command list | 展示所有的acli命令 |
| acli acli log get | 展示acli工具自身的日志 |
| acli acli sync | 同步acli命令到其他节点 |
| acli alert get | 查询告警信息 |
| acli alert list | 展示当天去重的告警 |
| acli hardware configstorecli | 查看、变更主机配置命令 |
| acli hardware cpu microcode file list | 查看cpu微码文件 |
| acli hardware gpu config get | 获取GPU配置信息 |
| acli hardware gpu config list | 展示GPU配置信息列表 |
| acli hardware hostcli hostcli | 管理和监控主机硬件相关命令 |
| acli hardware pcie list | 查询集群 PCI 设备列表 |
| acli hardware usb blacklist add | 新增USB黑名单 |
| acli hardware usb blacklist delete | 删除USB黑名单 |
| acli log cgroup parse | 解析cgroup黑盒日志 |
| acli log get | 获取平台日志 |
| acli log switch | 日志轮转命令 |
| acli network anet config configchannel get | 获取网络配置通道检测模块配置 |
| acli network anet config configchannel serviceinfo list | 获取网络配置通道各服务当前健康状态 |
| acli network anet config configchannel set | 设置网络配置通道检测模块配置 |
| acli network anet config fullsync | 执行全同步任务 |
| acli network anet config mac get | 查看mac表容量 |
| acli network anet config mac set | 调整mac表容量 |
| acli network anet config nat get | 查看nat表项限制 |
| acli network anet config nat set | 调整nat表项限制 |
| acli network anet forwarding get | 查看转发核 |
| acli network anet forwarding set | 调整转发核 |
| acli network anet forwarding status | 查询当前主机转发核利用率 |
| acli network anet mirror delete | 删除流量镜像 |
| acli network anet mirror get | 查看流量镜像信息 |
| acli network anet mirror list | 查看流量镜像列表 |
| acli network anet session get | 查看数据面session信息 |
| acli network anet vrouter get | 查看虚拟路由器信息 |
| acli network anet vrouter list | 查看虚拟路由器列表 |
| acli network anet vrouter migrate | 迁移虚拟路由器 |
| acli network anet vrouter vrrp get | 查看数据面vrrp信息 |
| acli network bond arp_interval get | 获得聚合口arp活性探测频率 |
| acli network bond delete | 删除聚合口 |
| acli network bond get | 查看聚合口信息 |
| acli network bond list | 查看聚合口列表 |
| acli network bond mode get | 查看聚合口组网模式 |
| acli network bond set | 更新聚合口 |
| acli network cli get | 在 vn-agent 容器内执行 SDN cli 的只读 show 查询命令 |
| acli network faultdomain list | 查询故障域列表 |
| acli network ip route get | 获取到指定目的地址的路由信息 |
| acli network mgmt switch | 切换管理口角色到指定网口 |
| acli network nettools iptables list | 查询 iptables 防火墙规则列表，支持按链名、表名过滤，默认以数字形式显示 |
| acli network nettools iptables rule check | 检查 iptables 指定链上是否存在符合条件的规则，支持按协议、端口、目标动作过滤 |
| acli network nettools netstat connection check | 检查指定端口的网络连接数，支持按连接状态过滤 |
| acli network nettools netstat list | 列出网络连接和端口监听状态，支持按 TCP/UDP、监听、数字形式、进程等过滤 |
| acli network nettools netstat port check | 检查指定端口是否处于监听状态，支持 TCP/UDP 协议 |
| acli network nic down | 禁用主机网口 |
| acli network nic get | 查看主机网口信息 |
| acli network nic irqcpu list | 展示网口中断核信息列表 |
| acli network nic list | 查看主机网口列表 |
| acli network nic lldp disable | 禁用网口lldp |
| acli network nic lldp enable | 启用网口lldp |
| acli network nic lldp get | 查看网口lldp |
| acli network nic mtu get | 查看网口mtu |
| acli network nic mtu set | 设置网口mtu |
| acli network nic queue get | 查看网口队列数 |
| acli network nic queue set | 设置网口队列数 |
| acli network nic rdma disable | 关闭指定厂商的指定ib网卡设备的rdma功能 |
| acli network nic rdma enable | 开启指定厂商的指定ib网卡设备的rdma功能 |
| acli network nic rdma get | 获取指定厂商的指定ib网卡设备的信息 |
| acli network nic rdma list | 获取指定厂商的所有ib网卡设备 |
| acli network nic rdma whitelist check | 检查rdma白名单配置 |
| acli network nic rdma whitelist set | 更新rdma白名单配置 |
| acli network nic reorder | 调整网口顺序 |
| acli network nic ring get | 查看当前网口环形缓冲区参数 |
| acli network nic ring set | 设置当前网口环形缓冲区参数 |
| acli network nic set | 设置主机网口 |
| acli network nic up | 启用主机网口 |
| acli network pfc create | 创建优先级流控(PFC)配置（异步任务，返回 taskId） |
| acli network pfc delete | 删除优先级流控(PFC)配置（异步任务，返回 taskId） |
| acli network pfc get | 查询单条优先级流控(PFC)配置（按 domainId 过滤后取首条；后端无 get-by-id 端点） |
| acli network pfc list | 查询优先级流控(PFC)配置列表 |
| acli network pfc set | 更新优先级流控(PFC)配置（异步任务，返回 taskId） |
| acli network port check | 检查网络端口状态 |
| acli network sfd_bytools | 数据面sfd_byTools.sh脚本 |
| acli network vlink check | 检查vlink配置状态 |
| acli network vxlan list | 查询集群vxlan信息列表 |
| acli network vxlan set | 更新集群VXLAN配置 |
| acli platform arbiter get | 查询当前节点是否为仲裁节点 |
| acli platform backup bcfg get | 查看备份点配置文件\{$vmid\}.conf.bcfg内容 |
| acli platform backup cbt file cbtinfo get | 显示虚拟机目录下所有磁盘的CBT信息 |
| acli platform backup cbt file dump | 以十六进制格式展示CBT文件内容 |
| acli platform backup cbt file verify | 验证CBT文件的完整性和一致性 |
| acli platform backup config get | 查询备份相关配置 |
| acli platform backup config set | 设置备份任务配置文件backup.json的内容 |
| acli platform backup datamover config get | 获取datamover配置文件内容 |
| acli platform backup datamover config set | 设置datamover配置文件内容 |
| acli platform backup datamover performancedetect set | 开启或关闭datamover性能瓶颈探测 |
| acli platform backup datamover performanceindicator get | 查询datamover运行过程中的性能指标项和运行状态 |
| acli platform backup datamover performancereport get | 获取datamover运行过程中的性能瓶颈探测报告 |
| acli platform backup mergedata config get | 查询数据合并任务配置文件merge_data.json内容 |
| acli platform backup mergedata config set | 设置数据合并任务配置文件merge_data.json内容 |
| acli platform backup region config set | 设置区域快照的运行时参数配置 |
| acli platform cfs admin status set |  |
| acli platform cfs status | 验证/cfs目录写入能力 |
| acli platform datareport set | 设置报表数据配置 |
| acli platform info get | 获得系统信息 |
| acli platform info system_language get | 查询系统语言 |
| acli platform mysql config get | 获取MySQL配置 |
| acli platform mysql-manager-cli | 平台mysql-manager-cli工具 |
| acli platform node cert get | 获取证书的md5值 |
| acli platform node cert list | 列出节点证书 |
| acli platform node get | 查看节点信息 |
| acli platform node list | 查看节点列表 |
| acli platform patches alert get | 查询补丁服务的告警信息 |
| acli platform patches list | 查询本机已打补丁列表 |
| acli platform port list | 查询平台端口列表 |
| acli platform redis redis-cli | 平台redis-cli工具 |
| acli platform scheduler quota get | 查询调度器配额 |
| acli platform scheduler quota set | 修改调度器配额 |
| acli platform sn get | 查询集群序列号和各组件授权信息 |
| acli platform snapshot mysql get | 快照数据库信息查询 |
| acli platform syncvmtime get | 查询集群虚拟机时间同步配置 |
| acli platform syslog config get | 查询 syslog 转发配置 |
| acli platform system_config get | 查询集群系统配置 |
| acli platform vcpu_type list | 查询集群支持的和全部 vCPU 型号 |
| acli platform version get | 获取平台版本 |
| acli platform version info | 查询 API 版本详情 |
| acli platform version security verify | 查询平台是否为涉密版本 |
| acli platform vssn verify | 校验本机所有 VS 序列号的完整性和授权限制 |
| acli platform vtsn keyid get | 获取 USB Key ID |
| acli platform vtsn owner get | 获取 USB Key 持有者信息 |
| acli platform zookeeper zkcli | 平台zkcli-c工具 |
| acli plugin cleanup | 对指定插件进行清理目录和kill相关进程 |
| acli plugin info | 获取指定插件信息 |
| acli plugin install | 插件安装/更新 |
| acli plugin list | 获取已安装的插件列表 |
| acli plugin sync | 将已安装的所有插件及配置同步到指定集群节点 |
| acli plugin uninstall | 插件卸载 |
| acli plugins asan_ops asan_ops | 执行虚拟存储检测工具 |
| acli plugins asys asys | 执行系统检查工具对主机进行检测 |
| acli plugins log_collect cancel | 取消日志收集任务 |
| acli plugins log_collect create | 创建日志收集任务 |
| acli plugins log_collect progress | 查看日志采集任务的进度 |
| acli plugins netdoctor netdoctor | 进行网络相关问题的排障，支持诊断箱（多场景排障）和工具箱（快速工具）两种模式。 |
| acli plugins performance_tools analyze | 分析日志数据，找出系统、虚拟机大致瓶颈 |
| acli plugins performance_tools check_host | 检查宿主机环境信息：CPU、内存、超线程等 |
| acli plugins performance_tools check_vm | 检查虚拟机的状态（虚拟机配置文件、IO、MEM、CPU），同时自动检测虚拟机运行主机，必须输入虚拟机ID |
| acli plugins performance_tools check_vm_model | 检测虚拟机业务模型 |
| acli plugins performance_tools collect_log | 收集主机性能相关日志、配置、命令运行结果 |
| acli plugins performance_tools combined collect_log | 以虚拟机为单位，自动监控虚拟机，自动检测虚拟机和所在主机，并将相关日志进行打包 |
| acli plugins performance_tools isolate list | 查看 CPU 的隔离状态 |
| acli plugins performance_tools isolate only_pcpu | 指定 CPU 核心隔离 |
| acli plugins performance_tools isolate vs_network_irq | 自动找到存储通信口网卡中断隔离 |
| acli plugins performance_tools monitor clean | 删除上次产生的监控数据 |
| acli plugins performance_tools monitor start | 监控（磁盘 IO、VS IO、虚拟机 IO、pidstat、网络）信息存储文件中 |
| acli plugins performance_tools monitor status | 获取监控数据状态 |
| acli plugins performance_tools monitor stop | 退出监控程序 |
| acli plugins performance_tools shell | 程序内置了一些脚本文件，当环境中不存在时可执行 |
| acli plugins performance_tools unisolate | 取消 CPU 隔离，还原设置；取消虚拟机隔离 |
| acli plugins performance_tools update | 更新程序 |
| acli plugins performance_tools version | 版本信息 |
| acli plugins vm_start vm_start | 虚拟机开机失败检测 |
| acli plugins vm_suspend vm_suspend | 虚拟机挂起检测 |
| acli service anet kafka-consumer-groups get | 查询 Kafka 消费者组的详细信息，包括 topic、partition、offset、lag 等 |
| acli service anet sdn status | 查询 SDN（软件定义网络）服务的运行状态 |
| acli service anet vn-cluster-service-api rps disable | 禁用主机负载均衡RPS |
| acli service anet vn-cluster-service-api rps enable | 启用主机负载均衡RPS |
| acli service anet vn-cluster-service-api rps status | 获取主机负载均衡RPS启用状态 |
| acli service anet vn-manager-service-api restart | 重启vn-manager-service-api服务 |
| acli service anet vn-manager-service-api start | 启动vn-manager-service-api服务 |
| acli service anet vn-manager-service-api status | 查看vn-manager-service-api服务状态 |
| acli service anet vn-manager-service-api stop | 停止vn-manager-service-api服务 |
| acli service anet vn-node-agent-api restart | 重启vn-node-agent-api服务 |
| acli service anet vn-node-agent-api start | 启动vn-node-agent-api服务 |
| acli service anet vn-node-agent-api status | 查看vn-node-agent-api服务状态 |
| acli service anet vn-node-agent-api stop | 停止vn-node-agent-api服务 |
| acli service asv apache2 restart | 重启apache2服务 |
| acli service asv apache2 start | 启动apache2服务 |
| acli service asv apache2 status | 查看apache2服务状态 |
| acli service asv apache2 stop | 停止apache2服务 |
| acli service asv authorize_client restart | 重启authorize_client服务 |
| acli service asv authorize_client start | 启动authorize_client服务 |
| acli service asv authorize_client status | 查看authorize_client服务状态 |
| acli service asv authorize_client stop | 停止authorize_client服务 |
| acli service asv authorize_server restart | 重启authorize_server服务 |
| acli service asv authorize_server start | 启动authorize_server服务 |
| acli service asv authorize_server status | 查看authorize_server服务状态 |
| acli service asv authorize_server stop | 停止authorize_server服务 |
| acli service asv corosync restart | 重启corosync服务 |
| acli service asv corosync start | 启动corosync服务 |
| acli service asv corosync status | 查看corosync服务状态 |
| acli service asv corosync stop | 停止corosync服务 |
| acli service asv exporter restart | 重启exporter服务 |
| acli service asv exporter start | 启动exporter服务 |
| acli service asv exporter status | 查看exporter服务状态 |
| acli service asv exporter stop | 停止exporter服务 |
| acli service asv loadman config get | 获取loadman服务配置 |
| acli service asv loadman config set | 更新loadman服务配置 |
| acli service asv loadman maintenance get | 获取过载保护功能相关维护信息 |
| acli service asv loadman maintenance set | 过载保护功能相关维护操作 |
| acli service asv loadman restart | 重启loadman服务 |
| acli service asv loadman start | 启动loadman服务 |
| acli service asv loadman status | 查询loadman服务状态 |
| acli service asv loadman stop | 停止loadman服务 |
| acli service asv mgmt-node-agent-api get | 请求mgmt-node-agent-api获取接口数据 |
| acli service asv mgmt-node-agent-api restart | 重启mgmt-node-agent-api服务 |
| acli service asv mgmt-node-agent-api start | 启动mgmt-node-agent-api服务 |
| acli service asv mgmt-node-agent-api status | 查看mgmt-node-agent-api服务运行状态 |
| acli service asv mgmt-node-agent-api stop | 停止mgmt-node-agent-api服务 |
| acli service asv mgmt-node-agent-periodic restart | 重启mgmt-node-agent-periodic服务 |
| acli service asv mgmt-node-agent-periodic start | 启动mgmt-node-agent-periodic服务 |
| acli service asv mgmt-node-agent-periodic status | 查看mgmt-node-agent-periodic服务运行状态 |
| acli service asv mgmt-node-agent-periodic stop | 停止mgmt-node-agent-periodic服务 |
| acli service asv mysql restart | 重启mysql服务 |
| acli service asv mysql start | 启动mysql服务 |
| acli service asv mysql status | 查看mysql服务状态 |
| acli service asv mysql stop | 停止mysql服务 |
| acli service asv mysql-managerd restart | 重启mysql-managerd服务 |
| acli service asv mysql-managerd start | 启动mysql-managerd服务 |
| acli service asv mysql-managerd status | 查看mysql-managerd服务状态 |
| acli service asv mysql-managerd stop | 停止mysql-managerd服务 |
| acli service asv perl-services restart | 重启基础的perl相关的服务 |
| acli service asv pmxcfs restart | 重启pmxcfs服务 |
| acli service asv pmxcfs start | 启动pmxcfs服务 |
| acli service asv pmxcfs status | 查看pmxcfs服务状态 |
| acli service asv pmxcfs stop | 停止pmxcfs服务 |
| acli service asv redis restart | 重启redis服务 |
| acli service asv redis start | 启动redis服务 |
| acli service asv redis status | 查看redis服务状态 |
| acli service asv redis stop | 停止redis服务 |
| acli service asv rrdcached restart | 重启rrdcached服务 |
| acli service asv rrdcached start | 启动rrdcached服务 |
| acli service asv rrdcached status | 查看rrdcached服务状态 |
| acli service asv rrdcached stop | 停止rrdcached服务 |
| acli service asv rsyncd restart | 重启rsyncd服务 |
| acli service asv rsyncd start | 启动rsyncd服务 |
| acli service asv rsyncd status | 查看rsyncd服务状态 |
| acli service asv rsyncd stop | 停止rsyncd服务 |
| acli service asv sangfor_waf restart | 重启sangfor_waf服务 |
| acli service asv sangfor_waf start | 启动sangfor_waf服务 |
| acli service asv sangfor_waf status | 查看sangfor_waf服务状态 |
| acli service asv sangfor_waf stop | 停止sangfor_waf服务 |
| acli service asv vtpalertd restart | 重启vtpalertd服务 |
| acli service asv vtpalertd start | 启动vtpalertd服务 |
| acli service asv vtpalertd status | 查看vtpalertd服务状态 |
| acli service asv vtpalertd stop | 停止vtpalertd服务 |
| acli service asv vtpcron restart | 重启vtpcron服务 |
| acli service asv vtpcron start | 启动vtpcron服务 |
| acli service asv vtpcron status | 查看vtpcron服务状态 |
| acli service asv vtpcron stop | 停止vtpcron服务 |
| acli service asv vtpdaemon opqueue config get | 获取进程操作队列配置 |
| acli service asv vtpdaemon opqueue config set | 设置进程操作队列配置 |
| acli service asv vtpdaemon restart | 重启vtpdaemon服务 |
| acli service asv vtpdaemon start | 启动vtpdaemon服务 |
| acli service asv vtpdaemon status | 查看vtpdaemon服务状态 |
| acli service asv vtpdaemon stop | 停止vtpdaemon服务 |
| acli service asv vtplogd restart | 重启vtplogd服务 |
| acli service asv vtplogd start | 启动vtplogd服务 |
| acli service asv vtplogd status | 查看vtplogd服务状态 |
| acli service asv vtplogd stop | 停止vtplogd服务 |
| acli service asv vtpperlproxy restart | 重启vtpperlproxy服务 |
| acli service asv vtpperlproxy start | 启动vtpperlproxy服务 |
| acli service asv vtpperlproxy status | 查看vtpperlproxy服务状态 |
| acli service asv vtpperlproxy stop | 停止vtpperlproxy服务 |
| acli service asv vtpstatd restart | 重启vtpstatd服务 |
| acli service asv vtpstatd start | 启动vtpstatd服务 |
| acli service asv vtpstatd status | 查看vtpstatd服务状态 |
| acli service asv vtpstatd stop | 停止vtpstatd服务 |
| acli service asv zk restart | 重启zk服务 |
| acli service asv zk start | 启动zk服务 |
| acli service asv zk status | 查看zk服务状态 |
| acli service asv zk stop | 停止zk服务 |
| acli service host hostd restart | 重启hostd服务 |
| acli service host hostd start | 启动hostd服务 |
| acli service host hostd status | 查看hostd服务状态 |
| acli service host hostd stop | 停止hostd服务 |
| acli service host lsud restart | 重启lsud服务 |
| acli service host lsud start | 启动lsud服务 |
| acli service host lsud status | 查看lsud服务状态 |
| acli service host lsud stop | 停止lsud服务 |
| acli storage asan brick iostat | 查看brick的iostat |
| acli storage asan disk list | 展示虚拟存储卷的磁盘信息列表 |
| acli storage asan disk residual clean | 清理磁盘残留信息 |
| acli storage asan io_uring sqpoll disable | 关闭虚拟存储卷缓存服务中io_uring的sqpoll模式 |
| acli storage asan io_uring sqpoll enable | 开启虚拟存储卷缓存服务中io_uring的sqpoll模式 |
| acli storage asan io_uring sqpoll precheck | 检查虚拟存储卷内主机是否支持开启io_uring的sqpoll特性 |
| acli storage asan io_uring sqpoll status | 查看虚拟存储卷缓存服务中io_uring的sqpoll模式状态 |
| acli storage asan version get | 获取VS版本号 |
| acli storage asan volume iostat | 获取虚拟存储卷iostat信息 |
| acli storage asan volume list | 获取虚拟存储卷信息列表 |
| acli storage asan vs_disk_scan | disk_scan.sh命令 |
| acli storage asan vs_hotplug | vs_hotplug.sh命令 |
| acli storage asan vs_json_rw | vs_json_rw.py命令 |
| acli storage asan vs_rpc_tool | vs_rpc_tool命令 |
| acli storage asan vs_tier | vs_tier_cli.py命令 |
| acli storage asan vs_update_nfs | vs_update_nfs.sh命令 |
| acli storage asan vs_vginfo | vs_vginfo.sh命令 |
| acli storage backuppool list | 查询备份池存储列表 |
| acli storage display config get | 获取是否展示可用空间大于等于100G的Local系统盘 |
| acli storage display config set | 设置是否展示可用空间大于等于100G的Local系统盘 |
| acli storage fc host list | FC存储HBA设备列表信息 |
| acli storage fc host statistics get | FC存储HBA设备相关统计信息 |
| acli storage mount | 查看指定存储ID的挂载信息 |
| acli storage other list | 展示除虚拟存储以外的其他存储信息列表 |
| acli storage sffsck | sffsck命令 |
| acli storage umount | 卸载指定存储的挂载点 |
| acli storage vs_status volume list | 查询 VS 虚拟存储卷列表 |
| acli storage vsmgr fault-domains list | 查询指定卷的故障域列表 |
| acli storage vsmgr host-in-volume get | 查询主机是否在 VS 卷中 |
| acli storage vsmgr ippool ip get | 查询主机在指定类型 IP 池中已分配的 IP |
| acli storage vsmgr ippool used-net get | 查询 IP 池配置的网络段 |
| acli storage vsmgr volume get | 查询 VS 虚拟存储卷详情 |
| acli storage vsmgr volume has-stretch-volume | 查询是否存在延伸卷 |
| acli system arp | 查看 ARP 表（地址解析协议缓存表，只读）。 |
| acli system arping | 向指定主机发送 ARP 请求以探测其在线状态 |
| acli system blkid | 查询块设备的 UUID、文件系统类型及其他属性信息（只读）。 |
| acli system cat | 读取并查看系统白名单内指定文件的内容 |
| acli system cgroup cpu list | 列出所有cgroup目录下和cpu相关的文件 |
| acli system cgroup cpu tree | 显示cpu cgroup子系统的子组结构 |
| acli system cgroup get | 显示指定cgroup的所有参数信息 |
| acli system cgroup memory tree | 显示内存cgroup子系统的子组结构 |
| acli system chkconfig | 查看系统服务的运行级别配置（只读）。 |
| acli system chping | chping命令 |
| acli system cpu info | 系统CPU信息 |
| acli system curl | 通过 `acli system curl` 子命令受控调用 HCI 平台服务的 GET 接口（只读），承载 KB 排障知识库中的 100 条 GET API 放通。 |
| acli system date | date 命令，获取当前系统时间（只读）。 |
| acli system df | df命令 |
| acli system diff | 比较两个文件的内容差异（只读）。 |
| acli system dig | 执行 DNS 查询，获取域名的解析记录（只读）。 |
| acli system dmesg | 查看内核环形缓冲区日志（只读）。 |
| acli system dmidecode | dmidecode 命令，读取并展示 DMI/SMBIOS 硬件信息（只读，禁止把 DMI 数据转储为文件）。 |
| acli system du | 统计指定目录或文件的磁盘占用空间（只读）。 |
| acli system ethtool | ethtool命令 |
| acli system fdisk | 查看磁盘分区信息（只读）。 |
| acli system file sqlite3 backup | 备份 SQLite 数据库到指定输出文件 |
| acli system file sqlite3 integrity-check | 检查 SQLite 数据库的完整性（PRAGMA integrity_check 和 quick_check） |
| acli system file sqlite3 query | 执行 SQLite 数据库 SQL 查询，支持 csv、column、list 三种输出格式 |
| acli system file test exist | 检查指定路径是否存在，可指定类型为文件、目录或任意 |
| acli system file test read | 检查指定文件是否可读 |
| acli system file test socket exist | 检查指定 Unix socket 是否存在 |
| acli system file test write | 检查指定文件是否可写 |
| acli system file touch create | 创建空文件或更新已有文件的时间戳 |
| acli system file wget download | 从指定 URL 下载文件，支持超时设置、SSL 跳过、输出到文件或 stdout |
| acli system find | 在指定目录中按条件查找文件（只读）。 |
| acli system fio | fio命令 |
| acli system free | free命令 |
| acli system grep | 在白名单内的配置或系统文件中按关键字搜索匹配行 |
| acli system hostname | 查看主机名称及域名信息（仅开放只读形式，不支持改写主机名）。 |
| acli system hosts get | 获取系统主机信息 |
| acli system hwclock | 查询硬件时钟时间 |
| acli system id | 查询当前用户或指定用户的身份信息（uid/gid/groups，只读）。 |
| acli system ifconfig | 查看主机网卡的配置信息 |
| acli system iostat | iostat命令 |
| acli system ip | 查看主机网络信息，支持只读查询地址、路由、链路及邻居信息 |
| acli system iperf3 | 网络带宽测量诊断工具，测量 TCP/UDP 吞吐量（只读，不改系统状态）。命令在 vs-cp-manager 容器内执行（与 vs 容器共享网络命名空间）。 |
| acli system ipmitool | ipmitool命令 |
| acli system iptables | 查看系统防火墙规则（iptables，只读）。 |
| acli system kill | kill命令 |
| acli system lldptool | lldptool命令 |
| acli system ls | 列出白名单内指定目录下的文件 |
| acli system lsblk | lsblk命令 |
| acli system lscpu | 查看 CPU 架构信息（架构、型号、核数、线程数等，只读）。 |
| acli system lsmod | lsmod命令，用于查看内核模块 |
| acli system lsof | lsof命令 |
| acli system lspci | 查看主机 PCI 设备信息 |
| acli system lsusb | 查询 USB 设备信息 |
| acli system mcelog | 查询 CPU MCE 硬件错误日志 |
| acli system md5sum | 计算指定文件的 MD5 校验值（只读）。 |
| acli system memory ce_count get | 获取内存的ce_count数据 |
| acli system memory dump | 系统内存占用情况 |
| acli system memory ecc_data get | 获取系统内存ECC数据 |
| acli system memory info | 查看系统内存详细信息 |
| acli system memory usage get | sfd_ps_mem.py命令 |
| acli system mounts get | 查看系统mounts信息 |
| acli system mpstat | mpstat命令 |
| acli system multipath | multipath命令 |
| acli system multipathconfig clear | 清除multipath多路径策略 |
| acli system multipathconfig devicepolicy clear | 清除指定节点上指定 vendor/product 的 device 级 multipath 自定义配置。 |
| acli system multipathconfig devicepolicy list | 列出指定节点上所有已设置 device 级 multipath 自定义配置的厂商型号、自定义参数及同型号存储列表。 |
| acli system multipathconfig devicepolicy set | 设置指定节点上指定 vendor/product 的 device 级 multipath 自定义配置 |
| acli system multipathconfig get | 查询指定节点上指定存储实际生效的多路径策略。 |
| acli system multipathconfig reload | 重新扫描磁盘使multipath配置生效，默认FC |
| acli system multipathconfig set | 修改multipath多路径策略 |
| acli system netstat | netstat命令 |
| acli system nslookup | 执行 DNS 查询，获取域名或 IP 的解析记录（只读）。 |
| acli system numactl | 查询 NUMA 拓扑和策略 |
| acli system perf | perf命令 |
| acli system pidstat | pidstat命令，用于查看系统进程资源 |
| acli system ping | ping命令 |
| acli system proc cgroup get | 获取指定进程的cgroup信息 |
| acli system proc fuser check | 查询占用指定文件或目录的进程 |
| acli system proc stack get | 获取进程的栈信息 |
| acli system proc starttime get | 查询指定进程的启动时间 |
| acli system ps | ps命令 |
| acli system qemu-img | 查询磁盘映像信息与一致性检查（只读，不修复）。 |
| acli system realethtool | realethtool命令 |
| acli system rm | rm 命令，限制删除特定目录下的文件（仅允许删除白名单目录内的文件，禁止递归删除）。 |
| acli system route | 查看系统路由表（只读）。 |
| acli system sar | 收集并查看系统活动报告（CPU、内存、IO 等，只读）。 |
| acli system sensors | sensors命令，用于查看传感器收集的信息 |
| acli system smartctl | smartctl命令 |
| acli system smartpqi version get | 获得smartpqi的版本信息 |
| acli system ss | 查看网络套接字统计信息（TCP/UDP 连接等，只读）。 |
| acli system stat | stat命令 |
| acli system strace | strace 命令，仅支持追踪 acli 命令的系统调用（只读，不修改系统状态）。 |
| acli system tail | 查看白名单内指定文件的末尾内容，支持实时跟踪 |
| acli system tcpdump | tcpdump命令 |
| acli system top | top命令，用于查看进程实时信息 |
| acli system traceroute | 追踪数据包到达目标主机的网络路径（只读）。 |
| acli system turbostat | 查看 CPU 拓扑、频率与功耗统计信息（只读）。命令在 asv-con 容器内执行，最长执行 15 秒。 |
| acli system uname | uname命令 |
| acli system uniq | 过滤并输出文件或输入中相邻的重复行，支持管道输入（只读）。 |
| acli system uptime | 查看系统运行时间、当前时间、登录用户数与系统负载（只读）。 |
| acli system vtpclustat local-id get | 获取本机在 VTP 集群中的节点 ID |
| acli system vtpclustat online list | 获取 VTP 集群中所有在线节点的列表 |
| acli system vtpclustat status | 查询 VTP 集群的整体状态 |
| acli system which | 查询指定命令的可执行文件路径（只读）。 |
| acli system who | 查看当前登录系统的用户信息（只读）。 |
| acli system who boot-time get | 查询系统最近一次启动时间 |
| acli task get | 查询操作任务信息 |
| acli task list | 展示当天的操作任务 |
| acli vm advcfg disktype get | 查询虚拟机指定磁盘的驱动类型 |
| acli vm advcfg disktype list | 列出虚拟机全部磁盘及驱动类型（含总开关状态） |
| acli vm advcfg disktype set | 修改虚拟机磁盘的驱动类型（冷编辑，仅支持关机状态下修改；不指定 --disk-id 则修改全部 ide 族磁盘） |
| acli vm advcfg nictype get | 查询虚拟机指定网卡的型号 |
| acli vm advcfg nictype list | 列出虚拟机全部网卡及型号 |
| acli vm advcfg nictype set | 修改虚拟机指定网卡的型号（仅支持关机状态下修改） |
| acli vm advcfg wwn get | 查询虚拟机指定磁盘的 WWN（磁盘唯一标识） |
| acli vm advcfg wwn list | 列出虚拟机全部磁盘及 WWN |
| acli vm advcfg wwn set | 修改虚拟机磁盘的 WWN（冷编辑，仅支持关机状态下修改；仅支持 virtio-scsi 总线磁盘设置非空 WWN） |
| acli vm config get | 获取虚拟机配置信息 |
| acli vm config pending delete | 删除虚拟机未生效配置 |
| acli vm config pending get | 查询虚拟机未生效配置 |
| acli vm cpu consistency get | 获取CPU一致性状态，对比数据库、CFS 和 Qemu 的 CPU 插槽数、每插槽核心数和总vCPU数 |
| acli vm cpu consistency set | 设置CPU一致性，根据指定的插槽数和每插槽核心数修改 DB 和 CFS 配置（危险操作：会覆盖现有配置） |
| acli vm delete | 删除虚拟机 |
| acli vm disk aio get | 查看虚拟机指定磁盘的aio信息 |
| acli vm disk check | 使用qcow2-dump工具检查磁盘镜像是否损坏 |
| acli vm disk consistency check | 检测磁盘一致性，对比数据库和 CFS 配置的 path 和 size_gib 字段 |
| acli vm disk consistency sync | 同步磁盘配置，根据传入的路径和大小同时修改 CFS 和 DB（危险操作：会覆盖现有配置） |
| acli vm disk io_uring get | 查看虚拟机io_uring的状态 |
| acli vm disk list | 展示目标虚拟机的磁盘镜像列表 |
| acli vm disk path get | 获取虚拟机磁盘路径 |
| acli vm dr config import | 从复制存储导入虚拟机配置，读取源 VM 的 conf，按用户下发的存储映射生成磁盘映射，调用 vmman import-config 接口下发导入指令。 |
| acli vm dr placeholder convert | 将普通云主机转换为占位云主机，把复制存储中的普通云主机 VM 转成占位 VM，占位存储由用户指定，调用 vmman convert-to-placeholder 接口下发转换指令。 |
| acli vm hotplug whitelist add | 放通指定OS或所有未知OS的CPU/内存热添加 |
| acli vm hotplug whitelist delete | 删除指定OS的放通配置或关闭全局兜底 |
| acli vm hotplug whitelist list | 查询已放通CPU/内存热添加的OS白名单及全局兜底状态 |
| acli vm hotplug whitelist reset | 还原所有自定义的OS白名单(出厂保留) |
| acli vm hotplug whitelist set | 修改指定OS的CPU/内存热添加放通能力 |
| acli vm int3 | int3的方式dump虚拟机内存 |
| acli vm list | 获取所有虚拟机信息 |
| acli vm lock clean | 删除特定虚拟机锁文件 |
| acli vm lock list | 展示虚拟机锁列表 |
| acli vm memory consistency get | 获取内存一致性状态，对比数据库、CFS 和 Qemu 的内存配置（MB） |
| acli vm memory consistency set | 设置内存一致性，根据指定的内存大小修改 DB 和 CFS 配置（危险操作：会覆盖现有配置） |
| acli vm memory dump cancel | 取消dump虚拟机内存任务 |
| acli vm memory dump create | 创建dump虚拟机内存任务 |
| acli vm memory dump progress | 查询dump虚拟机内存任务的进度 |
| acli vm nic consistency get | 获取网卡一致性状态，对比 Qemu、VN、CFS、DB 的 MAC 地址和接口 ID |
| acli vm nic consistency set | 设置网卡一致性，根据指定的 MAC 地址修改 VN 和 CFS 配置（危险操作：会覆盖现有配置） |
| acli vm nic queuecount get | 获取虚拟机网卡队列数 |
| acli vm nic queuecount set | 更新虚拟机网卡队列数 |
| acli vm sagaflow branch rollback skip | 跳过sagaflow分支回滚 |
| acli vm sagaflow get | 查询sagaflow信息 |
| acli vm sagaflow workflow rollback list | 获取sagaflow工作流回滚列表 |
| acli vm sagaflow workflow rollback set | 设置sagaflow工作流回滚 |
| acli vm shareddisk repair | 修复共享盘扩容异常 |
| acli vm shutdown | 关闭虚拟机 |
| acli vm start | 开启虚拟机 |
| acli vm status get | 获取虚拟机状态 |
| acli vm status set | 设置虚拟机状态 |
| acli vm vnc all disable | 禁用所有虚拟机控制台的访问权限 |
| acli vm vnc all enable | 启用所有虚拟机控制台的访问权限 |
| acli vm vnc clean close | 关闭虚拟机控制台访问权限回收的功能 |
| acli vm vnc clean open | 开启虚拟机控制台访问权限每日回收的功能 |
| acli vm vnc disable | 禁用虚拟机控制台的访问权限 |
| acli vm vnc enable | 启用虚拟机控制台的访问权限 |
| acli vm vnc get | 获取虚拟机控制台的配置 |
