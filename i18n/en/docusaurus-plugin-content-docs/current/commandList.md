---
sidebar_position: 2
sidebar_label: Command List
title: aCLI Command List
---

**`Updated: 2026-09-21`**
:::info Below is the latest command list
:::

| acli Command | Command Overview |
| :---: | :---: |
| acli acli command list | Display all aCLI commands |
| acli acli log get | Display logs of the aCLI tool |
| acli acli sync | Synchronize the acli command to other nodes. |
| acli alert get | Query alert information |
| acli alert list | Display deduplicated alerts of the current day |
| acli hardware configstorecli | View and modify host configuration commands |
| acli hardware cpu microcode file list | View CPU microcode file |
| acli hardware gpu config get | Get GPU configuration information |
| acli hardware gpu config list | Display GPU configuration information list |
| acli hardware hostcli hostcli | Manage and monitor host hardware related commands |
| acli hardware pcie list | List cluster PCI devices |
| acli hardware usb blacklist add | Add USB blacklist |
| acli hardware usb blacklist delete | Delete USB blacklist |
| acli log cgroup parse | Parse cgroup black-box logs |
| acli log get | Obtain platform logs |
| acli log switch | Log rotation commands |
| acli network anet config configchannel get | Get network configuration channel detection module settings |
| acli network anet config configchannel serviceinfo list | Get current health status of services in network configuration channel |
| acli network anet config configchannel set | Set network configuration channel detection module settings |
| acli network anet config fullsync | Execute full synchronization task |
| acli network anet config mac get | Check the capacity of the mac table |
| acli network anet config mac set | Adjust the capacity of the mac table |
| acli network anet config nat get | Check NAT entry restrictions |
| acli network anet config nat set | Adjust NAT entry restrictions |
| acli network anet forwarding get | View forwarding core |
| acli network anet forwarding set | Adjust forwarding core |
| acli network anet forwarding status | Query the forwarding core utilization of the current host |
| acli network anet mirror delete | Delete traffic mirroring policy |
| acli network anet mirror get | View traffic mirroring information |
| acli network anet mirror list | View the traffic mirroring policy list |
| acli network anet session get | View the session information on the data plane |
| acli network anet vrouter get | View virtual router information |
| acli network anet vrouter list | View virtual router list |
| acli network anet vrouter migrate | Migrate a virtual router |
| acli network anet vrouter vrrp get | View the VRRP information on the data plane |
| acli network bond arp_interval get | Obtain the ARP liveness probing frequency of aggregate interface |
| acli network bond delete | Delete aggregate interface |
| acli network bond get | View aggregate interface information |
| acli network bond list | View aggregate interface list |
| acli network bond mode get | View the networking mode of aggregate interface |
| acli network bond set | Update aggregate interface |
| acli network cli get | Execute the read-only show query commands of SDN cli inside the vn-agent container. |
| acli network faultdomain list | List fault domains |
| acli network ip route get | Get routing information to the specified destination address |
| acli network mgmt switch | Switch management interface role to the specified interface |
| acli network nettools iptables list | Query the list of iptables firewall rules, supports filtering by chain name and table name, displayed in numeric format by default |
| acli network nettools iptables rule check | Check whether the specified iptables rule exists on a chain, supports filtering by protocol, port, and target action |
| acli network nettools netstat connection check | Check the number of network connections on a specified port, supports filtering by connection state |
| acli network nettools netstat list | List network connections and port listening status, supports filtering by TCP/UDP, listening, numeric format, and process |
| acli network nettools netstat port check | Check whether a specified port is in listening state, supports TCP/UDP protocols |
| acli network nic down | Disable physical interface |
| acli network nic get | View node interface information |
| acli network nic irqcpu list | Display the information on CPU cores for handling interface interrupts |
| acli network nic list | View node interface list |
| acli network nic lldp disable | Disable interface LLDP |
| acli network nic lldp enable | Enable interface LLDP |
| acli network nic lldp get | View interface LLDP |
| acli network nic mtu get | View interface MTU |
| acli network nic mtu set | Configure interface MTU |
| acli network nic queue get | View the number of interface queues |
| acli network nic queue set | Configure the number of interface queues |
| acli network nic rdma disable | Disable RDMA for the specified IB NIC from the specified vendor |
| acli network nic rdma enable | Enable RDMA for the specified IB NIC from the specified vendor |
| acli network nic rdma get | Obtain information about the specified IB NIC from the specified vendor |
| acli network nic rdma list | Obtain information about all IB NICs from the specified vendor |
| acli network nic rdma whitelist check | Check RDMA whitelist configuration |
| acli network nic rdma whitelist set | Update RDMA whitelist configuration |
| acli network nic reorder | Adjust interface order |
| acli network nic ring get | View the ring buffer parameters for the current interface |
| acli network nic ring set | Configure ring buffer parameters for the current interface |
| acli network nic set | Set host network port |
| acli network nic up | Enable physical interface |
| acli network pfc create | Create a Priority Flow Control (PFC) configuration (asynchronous task, returns taskId) |
| acli network pfc delete | Delete a Priority Flow Control (PFC) configuration (asynchronous task, returns taskId) |
| acli network pfc get | Query a single Priority Flow Control (PFC) configuration (filtered by domainId, returns the first match; backend has no get-by-id endpoint) |
| acli network pfc list | Query the list of Priority Flow Control (PFC) configurations |
| acli network pfc set | Update a Priority Flow Control (PFC) configuration (asynchronous task, returns taskId) |
| acli network port check | Check network port status |
| acli network sfd_bytools | sfd_byTools.sh script for the data plane |
| acli network vlink check | Check vlink configuration status |
| acli network vxlan list | Query the cluster VXLAN information list |
| acli network vxlan set | Update cluster VXLAN configuration |
| acli platform arbiter get | Check whether the current node is an arbiter |
| acli platform backup bcfg get | View the backup point config file \{$vmid\}.conf.bcfg content |
| acli platform backup cbt file cbtinfo get | Display CBT information for all disks under the VM directory |
| acli platform backup cbt file dump | Display CBT file content in hexadecimal format |
| acli platform backup cbt file verify | Verify the integrity and consistency of the CBT file |
| acli platform backup config get | Get the content of the backup task configuration |
| acli platform backup config set | Set the content of backup task configuration file backup.json |
| acli platform backup datamover config get | get datamover config file |
| acli platform backup datamover config set | set datamover config file |
| acli platform backup datamover performancedetect set | Enable or disable datamover performance bottleneck detection |
| acli platform backup datamover performanceindicator get | Query performance indicators and running status during datamover operation |
| acli platform backup datamover performancereport get | Get the performance bottleneck detection report during datamover operation |
| acli platform backup mergedata config get | Get the content of the data merge task configuration file merge_data.json |
| acli platform backup mergedata config set | Set data merge task configuration file merge_data.json content |
| acli platform backup region config set | Set runtime parameter configuration for region snapshots |
| acli platform cfs admin status set | Set the value of /cfs/disable_admin.conf to control the disabled status of the platform admin user |
| acli platform cfs status | Check the write permissions for the /cfs directory |
| acli platform datareport set | Set the config of datareport |
| acli platform info get | Get platform information |
| acli platform info system_language get | Get system language |
| acli platform mysql config get | Get MySQL configuration |
| acli platform mysql-manager-cli | Platform mysql-manager-cli tool |
| acli platform node cert get | Obtain the certificate MD5 value |
| acli platform node cert list | List node certificates |
| acli platform node get | View node information |
| acli platform node list | View node list |
| acli platform patches alert get | Get patch service alert info |
| acli platform patches list | List patched patches on this host |
| acli platform port list | List platform ports |
| acli platform redis redis-cli | Platform redis-cli tool |
| acli platform scheduler quota get | Query scheduler quota |
| acli platform scheduler quota set | Modify scheduler quota |
| acli platform sn get | Get cluster serial number and component authorization info |
| acli platform snapshot mysql get | Snapshot database information query |
| acli platform syncvmtime get | Get cluster VM time sync configuration |
| acli platform syslog config get | Get syslog forwarding configuration |
| acli platform system_config get | Get cluster system configuration |
| acli platform vcpu_type list | List supported and all vCPU models of the cluster |
| acli platform version get | Obtain platform version |
| acli platform version info | Get API version details |
| acli platform version security verify | Check whether the platform is a security version |
| acli platform vssn verify | Verify integrity and authorization limits of all VS serial numbers on this host |
| acli platform vtsn keyid get | Get USB Key ID |
| acli platform vtsn owner get | Get USB Key owner info |
| acli platform zookeeper zkcli | Platform zkcli-c tool |
| acli plugin cleanup | Clean up the directory and kill related processes for the specified plugin |
| acli plugin info | Retrieve specified plugin information |
| acli plugin install | Plugin installation/update |
| acli plugin list | Get the list of installed plugins |
| acli plugin sync | Sync all installed plugins and their configuration to specified cluster nodes |
| acli plugin uninstall | Plugin uninstallation |
| acli plugins asan_ops asan_ops | Execute virtual storage detection tool |
| acli plugins asys asys | Run the system check tool to detect the host |
| acli plugins log_collect cancel | Cancel log collection task |
| acli plugins log_collect create | Create log collection task |
| acli plugins log_collect progress | Query log collection task progress |
| acli plugins netdoctor netdoctor | Network troubleshooting tool that supports two modes: Diagnosis Box (multi-scenario troubleshooting) and Tools Box (quick tools). |
| acli plugins performance_tools analyze | Analyze log data to identify system and virtual machine bottlenecks |
| acli plugins performance_tools check_host | Check host environment information: CPU, memory, hyper-threading, etc. |
| acli plugins performance_tools check_vm | Check virtual machine status (VM configuration file, IO, MEM, CPU), automatically detect the host where the VM is running, must input VM ID |
| acli plugins performance_tools check_vm_model | Check virtual machine business model |
| acli plugins performance_tools collect_log | Collect host performance related logs, configurations, command execution results |
| acli plugins performance_tools combined collect_log | By virtual machine, automatically monitor virtual machines, automatically detect virtual machines and their host machines, and package related logs |
| acli plugins performance_tools isolate list | View CPU isolation status |
| acli plugins performance_tools isolate only_pcpu | Specify CPU core isolation |
| acli plugins performance_tools isolate vs_network_irq | Automatically find storage communication port network card interrupt isolation |
| acli plugins performance_tools monitor clean | Delete monitoring data generated last time |
| acli plugins performance_tools monitor start | Monitoring (disk IO, VS IO, virtual machine IO, pidstat, network) information stored in files |
| acli plugins performance_tools monitor status | Get monitoring data status |
| acli plugins performance_tools monitor stop | Stop monitoring process |
| acli plugins performance_tools shell | The program has some built-in script files that can be executed when they don't exist in the environment |
| acli plugins performance_tools unisolate | Cancel CPU isolation, restore settings; cancel virtual machine isolation |
| acli plugins performance_tools update | Update program |
| acli plugins performance_tools version | Version information |
| acli plugins vm_start vm_start | VM start failure detection |
| acli plugins vm_suspend vm_suspend | VM suspend detection |
| acli service anet kafka-consumer-groups get | Query detailed information of Kafka consumer groups, including topic, partition, offset, lag, etc. |
| acli service anet sdn status | Query the running status of the SDN (Software Defined Network) service |
| acli service anet vn-cluster-service-api rps disable | Disable RPS on the node |
| acli service anet vn-cluster-service-api rps enable | Enable RPS on the node |
| acli service anet vn-cluster-service-api rps status | Obtain the RPS status on the node |
| acli service anet vn-manager-service-api restart | Restart the vn-manager-service-api service |
| acli service anet vn-manager-service-api start | Start the vn-manager-service-api service |
| acli service anet vn-manager-service-api status | View the vn-manager-service-api service status |
| acli service anet vn-manager-service-api stop | Stop the vn-manager-service-api service |
| acli service anet vn-node-agent-api restart | Restart the vn-node-agent-api service |
| acli service anet vn-node-agent-api start | Start the vn-node-agent-api service |
| acli service anet vn-node-agent-api status | View the vn-node-agent-api service status |
| acli service anet vn-node-agent-api stop | Stop the vn-node-agent-api service |
| acli service asv apache2 restart | Restart the Apache2 service |
| acli service asv apache2 start | Start the Apache2 service |
| acli service asv apache2 status | View the apache2 service status |
| acli service asv apache2 stop | Stop the Apache2 service |
| acli service asv authorize_client restart | Restart the authorize_client service |
| acli service asv authorize_client start | Start the authorize_client service |
| acli service asv authorize_client status | View the authorize_client service status |
| acli service asv authorize_client stop | Stop authorize_client service |
| acli service asv authorize_server restart | Restart authorize_server service |
| acli service asv authorize_server start | Start authorize_server service |
| acli service asv authorize_server status | View the authorize_server service status |
| acli service asv authorize_server stop | Stop authorize_server service |
| acli service asv corosync restart | Restart the corosync service |
| acli service asv corosync start | Start corosync service |
| acli service asv corosync status | View the corosync service status |
| acli service asv corosync stop | Stop corosync service |
| acli service asv exporter restart | Restart the exporter service |
| acli service asv exporter start | Start the exporter service |
| acli service asv exporter status | View the exporter service status |
| acli service asv exporter stop | Stop the exporter service |
| acli service asv loadman config get | Obtain loadman service configuration |
| acli service asv loadman config set | Update loadman service configuration |
| acli service asv loadman maintenance get | Get maintenance information related to overload protection |
| acli service asv loadman maintenance set | Maintenance operations related to overload protection |
| acli service asv loadman restart | Restart the loadman service |
| acli service asv loadman start | Start the loadman service |
| acli service asv loadman status | Query the loadman service status |
| acli service asv loadman stop | Stop the loadman service |
| acli service asv mgmt-node-agent-api get | Request API data from mgmt-node-agent-api |
| acli service asv mgmt-node-agent-api restart | Restart mgmt-node-agent-api service |
| acli service asv mgmt-node-agent-api start | Start mgmt-node-agent-api service |
| acli service asv mgmt-node-agent-api status | Check mgmt-node-agent-api service status |
| acli service asv mgmt-node-agent-api stop | Stop mgmt-node-agent-api service |
| acli service asv mgmt-node-agent-periodic restart | Restart mgmt-node-agent-periodic service |
| acli service asv mgmt-node-agent-periodic start | Start mgmt-node-agent-periodic service |
| acli service asv mgmt-node-agent-periodic status | Check mgmt-node-agent-periodic service status |
| acli service asv mgmt-node-agent-periodic stop | Stop mgmt-node-agent-periodic service |
| acli service asv mysql restart | Restart the MySQL service |
| acli service asv mysql start | Start the MySQL service |
| acli service asv mysql status | View the MySQL service status |
| acli service asv mysql stop | Stop mysql service |
| acli service asv mysql-managerd restart | Restart the mysql-managerd service |
| acli service asv mysql-managerd start | Start the mysql-managerd service |
| acli service asv mysql-managerd status | View the mysql-managerd service status |
| acli service asv mysql-managerd stop | Stop the mysql-managerd service |
| acli service asv perl-services restart | Restarting the basic perl services. |
| acli service asv pmxcfs restart | Restart the pmxcfs service |
| acli service asv pmxcfs start | Start the pmxcfs service |
| acli service asv pmxcfs status | View pmxcfs service status |
| acli service asv pmxcfs stop | Stop pmxcfs service |
| acli service asv redis restart | Restart redis service |
| acli service asv redis start | Start redis service |
| acli service asv redis status | View the Redis service status |
| acli service asv redis stop | Stop the Redis service |
| acli service asv rrdcached restart | Restart the rrdcached service |
| acli service asv rrdcached start | Start rrdcached service |
| acli service asv rrdcached status | View rrdcached service status |
| acli service asv rrdcached stop | Stop rrdcached service |
| acli service asv rsyncd restart | Restart rsyncd service |
| acli service asv rsyncd start | Start rsyncd service |
| acli service asv rsyncd status | View the rsyncd service status |
| acli service asv rsyncd stop | Stop rsyncd service |
| acli service asv sangfor_waf restart | Restart sangfor_waf service |
| acli service asv sangfor_waf start | Start sangfor_waf service |
| acli service asv sangfor_waf status | View the sangfor_waf service status |
| acli service asv sangfor_waf stop | Stop the sangfor_waf service |
| acli service asv vtpalertd restart | Restart vtpalertd service |
| acli service asv vtpalertd start | Start the vtpalertd service |
| acli service asv vtpalertd status | View the vtpalertd service status |
| acli service asv vtpalertd stop | Stop the vtpalertd service |
| acli service asv vtpcron restart | Restart vtpcron service |
| acli service asv vtpcron start | Start the vtpcron service |
| acli service asv vtpcron status | View vtpcron service status |
| acli service asv vtpcron stop | Stop vtpcron service |
| acli service asv vtpdaemon opqueue config get | Get process op queue config |
| acli service asv vtpdaemon opqueue config set | Set process op queue config |
| acli service asv vtpdaemon restart | Restart vtpdaemon service |
| acli service asv vtpdaemon start | Start the vtpdaemon service |
| acli service asv vtpdaemon status | View the vtpdaemon service status |
| acli service asv vtpdaemon stop | Stop vtpdaemon service |
| acli service asv vtplogd restart | Restart the vtplogd service |
| acli service asv vtplogd start | Start the vtplogd service |
| acli service asv vtplogd status | View vtplogd service status |
| acli service asv vtplogd stop | Stop vtplogd service |
| acli service asv vtpperlproxy restart | Restart the vtpperlproxy service |
| acli service asv vtpperlproxy start | Start the vtpperlproxy service |
| acli service asv vtpperlproxy status | View vtpperlproxy service status |
| acli service asv vtpperlproxy stop | Stop vtpperlproxy service |
| acli service asv vtpstatd restart | Restart vtpstatd service |
| acli service asv vtpstatd start | Start the vtpstatd service |
| acli service asv vtpstatd status | View vtpstatd service status |
| acli service asv vtpstatd stop | Stop the vtpstatd service |
| acli service asv zk restart | Restart the ZooKeeper service |
| acli service asv zk start | Start zk service |
| acli service asv zk status | View the ZooKeeper service status |
| acli service asv zk stop | Stop the ZooKeeper service |
| acli service host hostd restart | Restart hostd service |
| acli service host hostd start | Start hostd service |
| acli service host hostd status | Check hostd service status |
| acli service host hostd stop | Stop hostd service |
| acli service host lsud restart | Restart lsud service |
| acli service host lsud start | Start lsud service |
| acli service host lsud status | Check lsud service status |
| acli service host lsud stop | Stop lsud service |
| acli storage asan brick iostat | View brick iostat |
| acli storage asan disk list | Display disk information of the virtual datastore |
| acli storage asan disk residual clean | Clear residual disk information |
| acli storage asan io_uring sqpoll disable | Disable io_uring sqpoll mode in the cache service of a virtual datastore |
| acli storage asan io_uring sqpoll enable | Enable io_uring sqpoll mode in the cache service of a virtual datastore |
| acli storage asan io_uring sqpoll precheck | Check whether hosts in a virtual datastore support enabling the io_uring sqpoll feature |
| acli storage asan io_uring sqpoll status | View the io_uring sqpoll mode status in the cache service of a virtual datastore |
| acli storage asan version get | Obtain virtual storage version |
| acli storage asan volume iostat | Obtain iostat information of virtual datastore |
| acli storage asan volume list | Obtain the virtual datastore information list |
| acli storage asan vs_disk_scan | disk_scan.sh command |
| acli storage asan vs_hotplug | vs_hotplug.sh command |
| acli storage asan vs_json_rw | vs_json_rw.py command |
| acli storage asan vs_rpc_tool | vs_rpc_tool command |
| acli storage asan vs_tier | vs_tier_cli.py command |
| acli storage asan vs_update_nfs | vs_update_nfs.sh command |
| acli storage asan vs_vginfo | vs_vginfo.sh command |
| acli storage backuppool list | List backup pool storage |
| acli storage display config get | Get whether to display Local system disks with available space >= 100G |
| acli storage display config set | Set whether to display Local system disks with available space >= 100G |
| acli storage fc host list | FC HBA list information |
| acli storage fc host statistics get | FC HBA statistics |
| acli storage mount | View the mounting information of the specified storage ID |
| acli storage other list | Display a list of storage information, excluding virtual storage |
| acli storage sffsck | sffsck command |
| acli storage umount | Unmount the mount point of the specified datastore |
| acli storage vs_status volume list | List VS virtual storage volumes |
| acli storage vsmgr fault-domains list | List fault domains of the specified volume |
| acli storage vsmgr host-in-volume get | Query whether a host is in a VS volume |
| acli storage vsmgr ippool ip get | Query IPs allocated to a host in a specified-type IP pool |
| acli storage vsmgr ippool used-net get | Query the network segment configured for the IP pool |
| acli storage vsmgr volume get | Get VS virtual storage volume details |
| acli storage vsmgr volume has-stretch-volume | Check whether a stretch volume exists |
| acli system arp | View the ARP table (Address Resolution Protocol cache, read-only). |
| acli system arping | Send an ARP request to the specified node to detect its online status. |
| acli system blkid | Query the UUID, file system type and other attributes of block devices (read-only). |
| acli system cat | Read and view contents of specified files in the system whitelist. |
| acli system cgroup cpu list | List all files in /cgroup/cpu |
| acli system cgroup cpu tree | Display the subgroup structure of the cpu cgroup subsystem |
| acli system cgroup get | Display all parameter information for the specified cgroup |
| acli system cgroup memory tree | Display the subgroup structure of the memory cgroup subsystem |
| acli system chkconfig | View the runlevel configuration of system services (read-only). |
| acli system chping | chping command |
| acli system cpu info | System CPU information |
| acli system curl | Call the GET APIs of HCI platform services in a controlled manner via the `acli system curl` subcommand (read-only), carrying the 100 GET APIs allowed for KB troubleshooting. |
| acli system date | date command, used to get the current system time (read-only). |
| acli system df | df command |
| acli system diff | Compare the content differences of two files (read-only). |
| acli system dig | Perform DNS queries and get domain resolution records (read-only). |
| acli system dmesg | View kernel ring buffer logs (read-only). |
| acli system dmidecode | dmidecode command, reads and displays DMI/SMBIOS hardware information (read-only; dumping DMI data |
| acli system du | Estimate the disk space usage of the specified directory or file (read-only). |
| acli system ethtool | Ethtool command |
| acli system fdisk | View disk partition information (read-only). |
| acli system file sqlite3 backup | Backup a SQLite database to a specified output file |
| acli system file sqlite3 integrity-check | Check the integrity of a SQLite database (PRAGMA integrity_check and quick_check) |
| acli system file sqlite3 query | Execute a SQLite database SQL query, supports three output formats: csv, column, list |
| acli system file test exist | Check whether a specified path exists, can specify type as file, directory, or any |
| acli system file test read | Check whether a specified file is readable |
| acli system file test socket exist | Check whether a specified Unix socket exists |
| acli system file test write | Check whether a specified file is writable |
| acli system file touch create | Create an empty file or update the timestamp of an existing file |
| acli system file wget download | Download a file from a specified URL, supports timeout setting, SSL skip, output to file or stdout |
| acli system find | Search for files in a specified directory by criteria (read-only). |
| acli system fio | fio command |
| acli system free | free command |
| acli system grep | Search for matching lines by keyword in configuration or system files that are whitelisted. |
| acli system hostname | View node name and domain name (only read-only forms are available; rewriting the node name is not supported). |
| acli system hosts get | Obtain node information |
| acli system hwclock | Get hardware clock time |
| acli system id | Query user identity information (uid/gid/groups) of the current or a specified user (read-only). |
| acli system ifconfig | View node NIC configuration information |
| acli system iostat | iostat command |
| acli system ip | View node network information, which supports read-only queries of address, route, link, and neighbor information. |
| acli system iperf3 | Network bandwidth measurement diagnostic tool for TCP/UDP throughput testing (read-only, does not change system state). The command runs inside the vs-cp-manager container (which shares the network namespace with the vs container). |
| acli system ipmitool | ipmitool command |
| acli system iptables | View system firewall rules (iptables, read-only). |
| acli system kill | Kill command |
| acli system lldptool | lldptool command |
| acli system ls | List files in the specified directory within the whitelist. |
| acli system lsblk | lsblk command |
| acli system lscpu | View CPU architecture information (architecture, model, cores, threads, etc., read-only). |
| acli system lsmod | lsmod command for viewing kernel modules |
| acli system lsof | lsof command |
| acli system lspci | View node PCIe device information |
| acli system lsusb | List USB devices |
| acli system mcelog | Query CPU Machine Check Exception hardware error logs |
| acli system md5sum | Calculate the MD5 checksum of a specified file (read-only). |
| acli system memory ce_count get | Obtain memory ce_count data |
| acli system memory dump | System memory usage |
| acli system memory ecc_data get | Obtain ECC data from system memory |
| acli system memory info | View detailed system memory information |
| acli system memory usage get | sfd_ps_mem.py command |
| acli system mounts get | View system mounts information |
| acli system mpstat | mpstat command |
| acli system multipath | multipath command |
| acli system multipathconfig clear | Clear multipath policy |
| acli system multipathconfig devicepolicy clear | Clear device-level multipath custom configuration for the specified vendor/product on the specified node. |
| acli system multipathconfig devicepolicy list | List all device-level multipath custom policies on the specified node, each with custom params and matched storages. |
| acli system multipathconfig devicepolicy set | Set device-level multipath custom configuration for the specified vendor/product on the specified node. |
| acli system multipathconfig get | Query the effective multipath policy for the specified storage on the specified node |
| acli system multipathconfig reload | Rescan disks to apply multipath configuration, default FC |
| acli system multipathconfig set | Modify multipath policy |
| acli system netstat | netstat command |
| acli system nslookup | Perform DNS queries and get resolution records of a domain or IP (read-only). |
| acli system numactl | Query NUMA topology and policy |
| acli system perf | perf command |
| acli system pidstat | pidstat command, used to view system process resources |
| acli system ping | Ping command |
| acli system proc cgroup get | Get the cgroup information for the specified process |
| acli system proc fuser check | Query processes occupying a specified file or directory |
| acli system proc stack get | Get the stack info of the process |
| acli system proc starttime get | Get the start time of a specified process |
| acli system ps | ps command |
| acli system qemu-img | Query disk image information and check image consistency (read-only, no repair). |
| acli system realethtool | realethtool command |
| acli system rm | rm command, only deletes files inside the specified directories (only files under whitelisted |
| acli system route | View the system routing table (read-only). |
| acli system sar | Collect and view system activity reports (CPU, memory, IO, etc., read-only). |
| acli system sensors | sensors command, used to view information collected by sensors |
| acli system smartctl | smartctl command |
| acli system smartpqi version get | Obtain smartpqi version information |
| acli system ss | View network socket statistics (TCP/UDP connections, etc.; read-only). |
| acli system stat | stat command |
| acli system strace | strace command, only supports tracing system calls of acli commands (read-only, does not modify |
| acli system tail | View the end content of specified files in the whitelist and support realtime tracking. |
| acli system tcpdump | tcpdump command |
| acli system top | top command, used to view real-time process information |
| acli system traceroute | Trace the network path of packets to a destination host (read-only). |
| acli system turbostat | View CPU topology, frequency and power consumption statistics (read-only). The command runs inside the asv-con container, with a maximum execution time of 15 seconds. |
| acli system uname | uname command |
| acli system uniq | Filter and output adjacent duplicate lines from a file or input stream; piped input is supported (read-only). |
| acli system uptime | View system uptime, current time, number of logged-in users and system load (read-only). |
| acli system vtpclustat local-id get | Get the local host's node ID in the VTP cluster |
| acli system vtpclustat online list | Get the list of all online nodes in the VTP cluster |
| acli system vtpclustat status | Query the overall status of the VTP cluster |
| acli system which | Query the path of the executable file of a specified command (read-only). |
| acli system who | View information about users currently logged into the system (read-only). |
| acli system who boot-time get | Query the most recent system boot time |
| acli task get | Query operation task information |
| acli task list | Display operation tasks of the current day |
| acli vm advcfg disktype get | Query the driver type of the specified disk of the virtual machine |
| acli vm advcfg disktype list | List all disks and their driver types of the virtual machine (including the master switch status) |
| acli vm advcfg disktype set | Modify the driver type of the virtual machine disk (cold edit, only supported when the VM is powered off; if --disk-id is not specified, all ide-family disks will be modified) |
| acli vm advcfg nictype get | Query the model of the specified NIC on the virtual machine |
| acli vm advcfg nictype list | List all NICs and their models of the virtual machine |
| acli vm advcfg nictype set | Modify the model of the specified NIC on the virtual machine (only supported when the VM is powered off) |
| acli vm advcfg wwn get | Query the WWN (World Wide Name, a unique disk identifier) of the specified virtual machine disk |
| acli vm advcfg wwn list | List all disks of the virtual machine and their WWNs |
| acli vm advcfg wwn set | Modify the WWN of the virtual machine disk (cold edit, only supported when the VM is powered off; only virtio-scsi bus disks support setting a non-empty WWN) |
| acli vm config get | Obtain VM configuration information |
| acli vm config pending delete | Delete VM pending configuration |
| acli vm config pending get | Query VM pending configuration |
| acli vm cpu consistency get | Get CPU consistency status, compare CPU sockets, cores per socket, and total vCPUs across DB, CFS, and Qemu |
| acli vm cpu consistency set | Set CPU consistency, modify DB and CFS config based on the specified sockets and cores per socket (Dangerous operation: will overwrite existing configuration) |
| acli vm delete | Delete VM |
| acli vm disk aio get | Check the AIO info of the specified disk of virtual machine |
| acli vm disk check | Check whether the disk image is damaged by using the qcow2-dump tool |
| acli vm disk consistency check | Check disk consistency, compare path and size_gib fields between database and CFS config |
| acli vm disk consistency sync | Sync disk configuration, modify CFS and DB simultaneously based on the provided path and size (Dangerous operation: will overwrite existing configuration) |
| acli vm disk io_uring get | Check the virtual machine io_uring status |
| acli vm disk list | Display the disk image list of the target VM |
| acli vm disk path get | Get virtual machine disk path |
| acli vm dr config import | Import VM configuration from the replica datastore by reading the conf file of the source VM, generating disk mappings according to the user-specified datastore mapping, and calling the vmman import-config API to issue an import command. |
| acli vm dr placeholder convert | Convert ordinary VMs to placeholder VMs. Convert ordinary VMs in the replica datastore to placeholder VMs. The datastores for placeholder VMs are specified by users. The vmman convert-to-placeholder API is called to issue a conversion command. |
| acli vm hotplug whitelist add | Allow CPU/memory hot-add for specified OSes or all unknown OSes |
| acli vm hotplug whitelist delete | Delete the configuration of allowing specified OSes or disable the global default policy |
| acli vm hotplug whitelist list | Query the OS whitelist for CPU/memory hot-add and global default policy status |
| acli vm hotplug whitelist reset | Restore all custom OS whitelists (factory settings retained) |
| acli vm hotplug whitelist set | Modify the capability of allowing CPU/memory hot-add for the specified OS |
| acli vm int3 | Dump guest memory using the INT3 instruction |
| acli vm list | Obtain information of all VMs |
| acli vm lock clean | 删除特定虚拟机锁文件 |
| acli vm lock list | Display the VM lock list |
| acli vm memory consistency get | Get memory consistency status, compare memory configuration (MB) across DB, CFS, and Qemu |
| acli vm memory consistency set | Set memory consistency, modify DB and CFS config based on the specified memory size (Dangerous operation: will overwrite existing configuration) |
| acli vm memory dump cancel | Cancel the guest memory dump task |
| acli vm memory dump create | Create a guest memory dump task |
| acli vm memory dump progress | Query the progress of the guest memory dump task |
| acli vm nic consistency get | Get NIC consistency status, compare MAC address and interface ID across Qemu, VN, CFS, and DB |
| acli vm nic consistency set | Set NIC consistency, modify VN and CFS config based on the specified MAC address (Dangerous operation: will overwrite existing configuration) |
| acli vm nic queuecount get | Obtain the number of VM NIC queues |
| acli vm nic queuecount set | Update the number of VM NIC queues |
| acli vm sagaflow branch rollback skip | Skip sagaflow branch rollback |
| acli vm sagaflow get | Query sagaflow information |
| acli vm sagaflow workflow rollback list | Get sagaflow workflow rollback list |
| acli vm sagaflow workflow rollback set | Set sagaflow workflow rollback |
| acli vm shareddisk repair | Fix shared disk expansion abnormality |
| acli vm shutdown | Power off VM |
| acli vm start | Power on VM |
| acli vm status get | Get the VM status by VM ID |
| acli vm status set | Set the VM status |
| acli vm vnc all disable | Disable access to all VM consoles |
| acli vm vnc all enable | Enable access to all VM consoles |
| acli vm vnc clean close | Disable revocation of VM console access permissions |
| acli vm vnc clean open | Enable daily revocation of VM console access permissions |
| acli vm vnc disable | Disable access to the VM console |
| acli vm vnc enable | Enable access to the VM console |
| acli vm vnc get | Obtain the VM console configuration |
