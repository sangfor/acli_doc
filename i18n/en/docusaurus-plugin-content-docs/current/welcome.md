---
slug: /
sidebar_position: 1
title: aCLI Troubleshooting
sidebar_label: Introduction
---

## Welcome to aCLI Troubleshooting Service Command Line Tool

Welcome to the aCLI Troubleshooting Service Command Line Tool. aCLI (Admin CLI) is a command-line troubleshooting tool designed specifically for the HCI platform, aimed at providing convenient and efficient system diagnosis and problem-solving capabilities for technical support and operations personnel. aCLI encapsulates complex low-level operations and provides standardized command interfaces, making troubleshooting work more standardized and efficient.

```shell
support/host-005056b237a6(acli) ~ # acli --help
Usage: aCLI [parameter] {namespace} + {command} [command parameter]

Parameters:
  --help, -?           Display tool usage
  --version            Display version information
  --debug              Enable debug logs
  --cluster            Traverse all nodes in the cluster to execute the aCLI command
  --timeout            Set the command timeout (seconds)
  --force              Force Mode: Bypasses interactive confirmation and executes operations directly (please confirm the risks before use).
  --formatter          Parameters for command formatting. Enumeration values: xml, csv, keyvalue, json
  --container          Specify the global container for commands, applicable only to commands under the system. Enumeration values: asv-con, vn-con, vn-agent, vs-cp-manager

Available namespaces:
  acli                 aCLI description. Provide additional information to users.
  alert                Alert commands
  task                 Task commands
  log                  Log related commands
  service              Service related commands
  vm                   VM commands
  system               System commands
  network              Network commands
  storage              Storage commands
  platform             Platform commands
  hardware             Hardware commands
```

---

**Technical Support Notice**: If you encounter any issues during use, please contact Sangfor Technical Support Team for professional assistance.

## Download and Installation

:::warning Usage Notice
The aCLI Troubleshooting Service Command Line Tool is currently in the preview pilot phase, please use with caution.
Do not arbitrarily use change commands to modify system environment and configuration, otherwise it may cause unpredictable consequences.
:::

### Download

Please select the appropriate installer based on your HCI version architecture. Typically, for systems with Intel, AMD and other brand processors, please download the x86/64 version. For systems with Hygon, Phytium, Kunpeng, Zhaoxin and other brand processors, please download the arm/aarch64 version.

<a
  href="http://acli.sangfor.com.cn:1110/api/public/download/4jotgyfk/latest?architecture=x86_64&api_key=QRlZXabZ8sOrFKtgs1VIfkHJZYQ3QNrcETXgsJaiX9Svz1pjFj"
  className="download-btn"
>
  Download x86/64 Version
</a>
<a className="link-spacer"></a>
<a
  href="http://acli.sangfor.com.cn:1110/api/public/download/4jotgyfk/latest?architecture=aarch64&api_key=QRlZXabZ8sOrFKtgs1VIfkHJZYQ3QNrcETXgsJaiX9Svz1pjFj"
  className="download-btn"
>
  Download arm/aarch64 Version
</a>

### Installation

:::info Installation Notice
Before installation, please check if the available capacity of the /sf/data/local partition is greater than 1GB, otherwise the installation may fail.
:::

1. Upload Installation Package

    Upload the downloaded installation package to the `/sf/data/local/` directory of the HCI environment

2. Add Execute Permission

    ```shell
    chmod +x acli-installer_x86_64_YYYY-MM-DD_HH-mm-ss.acli
    ```

3. Execute Installation

    ```shell
    ./acli-installer_x86_64_YYYY-MM-DD_HH-mm-ss.acli --install
    ```

4. Enable Auto-completion

    ```shell
    source ~/.profile
    ```

5. Verify Installation

    ```shell
    acli --version
    ```

## Usage Instructions

### Command Description

1. Command Format

    ```shell
        acli       [options]     {namespace}+      {cmd}+      [cmd options]+
         |             |              |              |               |
    Main Program   Global opts   Namespace(s)   Parameter(s)   Parameter options
                   (optional)                    (multiple)      (multiple)
    ```

    <details>
      <summary>Expand to View - Example: Query 'HA' Operation Logs</summary>
      <pre><code>
        support/host-005056b237a6(acli) ~ # acli task get -k HA -l 1
        [0]:
          action_type: 10
          bcancel: 0
          description: The VM encountered running error. The HA feature is working to try to recover the VM (vm1).
          dest_host:
          end: 2026-05-14 07:31:33
          errcode_tracing: null
          event_id: 53084160
          ha_handle_action: Restart VM on Healthy Node
          ha_handle_result: Quickly restart VM
          host: 10.131.136.168
          hostid: host-0050568efada
          hostname: 10.131.136.168
          id: 37
          log_id: host-0050568efada:154641:1778715066:778694482582
          module_type: 50
          object_id:
          object_name: vm1
          object_type: VM
          otype: VM
          process: Completed
          request_id: ,a0509b4bdd3e479dd473c91cf3c92142
          reserved2:
          reserved3:
          risk_level: 10
          sched_effect:
          sched_reason:
          start: 2026-05-14 07:31:04
          status: 2
          sysloged: 0
          target: vm1
          type: Recover HA-enabled VM
          upid:
          user: admin (x.x.x.x)
          vm: 1055878891514
      </code></pre>
    </details>

2. Namespace

    The acli command namespace is strictly divided according to business or operation objects, going deeper layer by layer until the smallest operation unit.

    For example, to view FC storage related statistics:

    ```shell
    acli storage fc host statistics get
    ```

    The above command is strictly arranged according to Storage - Storage Type - Object - Event/Sub-object - Operation.

3. External Plugins

    ```shell
    support/host-005056b237a6(acli) ~ # acli
    Usage: aCLI [parameter] {namespace}+ {command} [command parameter]

    Parameters:
      --help, -?           Display tool usage
      --version            Display version information
      --debug              Enable debug logs
      --cluster            Traverse all nodes in the cluster to execute the aCLI command
      --timeout            Set the command timeout (seconds)
      --force              Force Mode: Bypasses interactive confirmation and executes operations directly (please confirm the risks before use).
      --formatter          Parameters for command formatting. Enumeration values: xml, csv, keyvalue, json
      --container          Specify the global container for commands, applicable only to commands under the system. Enumeration values: asv-con, vn-con, vn-agent, vs-cp-manager

    Available plugins:
      asan_ops             Virtual Storage Anomaly Troubleshooting Tool
      asys                 System Check Tool
      log_collect          Log Collect
      netdoctor            Network Troubleshooting
      performance_tools    Performance tools
      vm_start             VM start/stop troubleshooting
      vm_suspend           VM abnormal suspension scenario troubleshooting
    ......
    ```

    acli supports installation and uninstallation of various official or third-party open source plugins. The current preview version comes pre-installed with some plugins for trial. More plugins will be available for free installation later.

### Parameter Description

1. Global Parameters

    In the acli command system, parameters that can act on any command are called global parameters.

    Use `acli --help` to view all currently supported global parameters

    ```shell
    support/host-005056b237a6(acli) ~ # acli
    Usage: aCLI [parameter] {namespace} + {command} [command parameter]

    Parameters:
      --help, -?           Display tool usage
      --version            Display version information
      --debug              Enable debug logs
      --cluster            Traverse all nodes in the cluster to execute the aCLI command
      --timeout            Set the command timeout (seconds)
      --force              Force Mode: Bypasses interactive confirmation and executes operations directly (please confirm the risks before use).
      --formatter          Parameters for command formatting. Enumeration values: xml, csv, keyvalue, json
      --container          Specify the global container for commands, applicable only to commands under the system. Enumeration values: asv-con, vn-con, vn-agent, vs-cp-manager
    ......
    ```

    Through flexible use of global parameters, you can achieve fine-grained control and powerful execution capabilities for commands.

    For example: acli commands execute on the master node by default, but cluster execution can be achieved through global parameters.

2. Command Parameters

    Most commands require input parameters to control execution logic. The parameters of the command itself are called command parameters.

    Use `--help` or press Enter directly after a command with command parameters to see its command parameters, for example: `acli alert get --help`

    ```shell
    support/host-005056b237a6(acli) ~ # acli alert get --help
    Usage: aCLI alert get [command parameter]

    Description:
      get                                 Query alert information

    Command parameters:
      -k|--keyword=string                 Search the alert object, event, and description. Example: VM suspended unexpectedly
      -e|--event=string                   Specify the event. Example: Virtual license key anomaly
      -o|--object-name=string             Specify the alert object. Example: 10.134.244.34
      -T|--object-type=string             Specify the alert object type. Enumeration values: host (Node), storage_obj (Storage), vm (VM), vnet (Virtual Network), sn (Serial Number), others (Others).
      -t|--time=string                    Specify time. Format: 'YYYY-MM-DD HH:MM:SS', 'YYYY-MM-DD HH'
      -L|--level=integer                  Specify the level. Enumeration values: 1 (Critical), 0 (Noncritical)
      -l|--limit=integer                  Specify the number of records to display, such as 1 or 2. Default value: 50
    ```

## Use Cases

### Fault Diagnosis

acli commands can be combined to achieve various fault diagnosis functions. Of course, we recommend using external plugins for one-click diagnosis.

For example: Use the performance_tools plugin for VM performance anomaly scenario troubleshooting (the following is just an example, please refer to the plugin documentation for specific usage)

<details>
  <summary>Expand to View</summary>
  ```shell
    support/host-005056b237a6(acli) ~ # acli performance_tools check_host
    Welcome to the virtual machine detection tool! Current time 2026-05-14 11:45:44
    Performing host detection...
    Hostname: host-0050568efada
    CPU Model: Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
    CPU Core Count: 8
    CPU Usage: 61.47 %
    Host Total Memory Size: 33.28 GB
    Host Remaining Memory Size 17.59 GB
    Running Virtual Machine Count: 1
    Cluster Type: HCI
    -----------------------------------------------------------------------------------------------------------------------------------

    1. Checking Host CPU Information
    1.1 Non-forwarding Core Single-core CPU Usage √
    Detailed Information: Highest non-forwarding core single-core CPU usage is 65.00%, detection threshold is 95.00%

    1.2 SPDK Forwarding Core Usage √
    Detailed Information: SPDK forwarding core usage is 0.00%, detection threshold is 90.00%

    1.3 CPU Main Frequency Detection √
    Detailed Information: CPU main frequency is 2.2GHz, detection threshold is 2.4GHz

    1.4 CPU Clock Source Detection √
    Detailed Information: CPU clock source is tsc, X86 and C86 architectures require the clock source to be tsc

    1.5 CPU Over-allocation Ratio Detection √
    Detailed Information: Host CPU over-allocation ratio is 112.50%, detection threshold is 200.00%
    Host running virtual machine list at that time is as follows:
    VMID                 CPU        MEM        %CPU_UTIL  MEM_USED        VmName
    1055878891514        1          1.00GB     9.90       427.85MB        vm1


    1.6 Host CPU iowait detection √
    Detailed Information: Host CPU iowait usage rate is 0.12%, detection threshold is 10.00%

    1.7 CPU Hyper-threading √
    Detailed Information: Physical host has not enabled CPU hyper-threading

    1.8 CPU Frequency Downgrade Check √
    Detailed Information: Could not retrieve current turbo frequency information.

    1.9 Check Host Non-exclusive CPU Usage √
    Detailed Information: There are no exclusive virtual machines in the environment, no need to detect

    1.10 Check host SMI interrupts √
    Detailed Information: Host CPU does not have SMI interrupts

    1.11 CPU Usage √
    Detailed Information: Physical host CPU usage is 61.47%, detection threshold is 65.00%
    Top 10 processes with highest CPU usage at that time:
    PID        %CPU  MEM      STAT  START    TIME     COMMAND
    39966      65.5  1.29GB   S<Ll  07:24    120:05   /sf/sdn/bin/dataplane --proc-type secondary -l 1,2...
    192868     9.9   427.85MB Sl    07:31    17:31    /usr/bin/kvm -id 1055878891514 -chardev socket,id=...
    40028      8.1   11.57MB  S     07:24    14:52    /sf/sdn/bin/dhcp6d
    114421     7.2   132.73MB S     07:28    13:00    WSGI
    49570      5.4   26.13MB  S<l   07:24    10:03    -w
    39573      4.0   20.85MB  S<Ll  07:24    7:29     /sf/sdn/bin/dpp -l 0 --proc-type primary --iova-mo...
    1722718    4.0   18.89MB  Sl+   10:27    0:00     /sf/data/local/acli/plugins/performance_tools/plug...
    5964       3.3   29.58MB  Ssl   07:21    6:16     /usr/local/sf/container/bin/containerd-squashfs-gr...
    187083     2.9   529.35MB S     07:31    5:15     vtpalertd
    10153      2.5   105.79MB Ssl   07:22    4:41     /usr/local/sf/container/bin/kubelet --config /sf-e...


    1.12 CPU sys Usage ×
    Alarm Level:Medium
    Detailed Information:Physical host CPU sys usage is 37.07%, detection threshold is 15.00%
    Recommendation: If the CPU sys usage of the physical host is relatively high, please check whether there is abnormal process occupation, whether there is memory frequency reduction, incorrect clock source and other issues, refer to https://support.sangfor.com.cn/cases/list?product_id=26&type=1&category_id=30186 , https://support.sangfor.com.cn//cases/list?product_id=26&category_id=29936&type=2 If KB cannot resolve, please contact Cloud BG Middle Platform Technical Support

    -----------------------------------------------------------------------------------------------------------------------------------

    2. Checking Host Memory Information
    2.1 Memory Frequency Downgrade Detection √
    Detailed Information: No memory frequency downgrade

    2.2 Percpu Memory Leakage Detection √
    Detailed Information: Percpu memory usage is 265.50MB, detection threshold is 10.00GB

    2.3 NUMA node memory balance detection √
    Detailed Information: System has only one NUMA node, no need to check memory balance

    2.4 Available Memory Size Detection √
    Detailed Information: Physical host available memory is 17.59GB, accounting for 52.86% of total memory, detection threshold is remaining less than 10GB or available memory ratio less than 10.00%
    Top 10 processes with highest memory usage (excluding huge page memory) at that time:
    PID        %CPU  MEM      STAT  START    TIME     COMMAND
    39966      65.5  1.29GB   S<Ll  07:24    120:06   /sf/sdn/bin/dataplane --proc-type secondary -l 1,2...
    187083     2.9   529.35MB S     07:31    5:15     vtpalertd
    203202     0.6   528.65MB S     07:32    1:11     vtpcron
    203232     0.6   528.44MB S     07:32    1:08     vtpcron
    203154     0.6   528.39MB S     07:32    1:05     vtpcron
    203132     0.6   528.38MB S     07:32    1:13     vtpcron
    203172     0.6   528.29MB S     07:32    1:06     vtpcron
    202311     0.9   527.59MB S     07:31    1:44     vtphwinfod
    204819     0.0   525.68MB Ss    07:32    0:03     backup_clean_schedule
    200337     0.9   524.19MB S     07:31    1:39     vtplogd


    2.5 Configured Memory Usage Status √
    Detailed Information: Actual total configured memory is 6.00GB, remaining configured memory is 17.00GB, configured memory usage rate is 35.29%, detection threshold is configured memory usage rate exceeding 90.00%

    2.6 Memory Frequency Consistent √
    Detailed Information: Memory stick frequencies consistent

    2.7 Memory stick running frequency consistent with physical frequency √
    Detailed Information: Memory stick running frequency consistent with physical frequency

    2.8 Slab Memory Leakage Detection √
    Detailed Information: SReclaim memory usage is 945.23MB, detection threshold is 10.00GB

    2.9 Memory insertion method detection √
    Detailed Information: Memory Modules: 3, Memory Channels: 14, Unpopulated Memory Channels: NVD #、NVD #2、RAM slot #1、RAM slot #2、NVD #3、NVD #1、RAM slot #6、NVD #5、NVD #4、NVD #6、RAM slot #5、RAM slot #4、RAM slot #3

    2.10 Memory ECC Error Detection √
    Detailed Information: Unable to retrieve IPMI logs

    2.11 Swap Usage Status √
    Detailed Information: Swap memory usage size is 0.00B, detection threshold is 0.00GB

    -----------------------------------------------------------------------------------------------------------------------------------

    3. Checking Host Disk Information
    3.1 Disk Latency Detection √
    Detailed Information: No disks with latency exceeding threshold, detection threshold for SSD disks or external storage disks 10ms, HDD disks 50ms
    The disk latency at that time was:

    Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
    sdc               0.00     6.00    0.00    6.00     0.00    48.00    16.00     0.01    0.83    0.00    0.83   0.67   0.40
    sda               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
    sdb               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
    sdd               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00


    3.2 VS Slow Disk Log Detection √
    Detailed Information: No VS slow disk logs exist

    3.3 Kernel Slow Disk Log Detection √
    Detailed Information: No kernel slow disk logs exist

    -----------------------------------------------------------------------------------------------------------------------------------

    4. Checking Host Network Information
    4.1 Network Forwarding Core Usage √
    Detailed Information: Network forwarding core usage is 2.00%, detection threshold is 90.00%

    4.2 Network Traffic Display √
    Detailed Information: Network card traffic at that time is as follows:
    10:28:26 AM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
    10:28:27 AM      eth0   4372.00     46.00    809.39      2.50      0.00      0.00   1738.00
    10:28:27 AM    p_eth1   4364.00      0.00    808.96      0.00      0.00      0.00   1738.00
    10:28:27 AM      eth2   4364.00      0.00    808.96      0.00      0.00      0.00   1738.00
    10:28:27 AM      eth3   4364.00      0.00    808.96      0.00      0.00      0.00   1738.00
    10:28:27 AM      eth4   4364.00      0.00    808.96      0.00      0.00      0.00   1738.00
    10:28:27 AM      eth5   4364.00      0.00    808.96      0.00      0.00      0.00   1738.00
    10:28:27 AM      eth1   4364.00      0.00    799.41      0.00      0.00      0.00   0.00


    4.3 Takeover general mode network card LRO detection √
    Detailed Information: No network adapters taken over in generic mode with LRO enabled were detected.

    4.4 Bonded Network Interface Working Mode √
    Detailed Information: Bonded network interface working mode is normal

    4.5 Network card buffer overflow √
    Detailed Information: Network card has no buffer overflow

    4.6 Network Interface Bandwidth Detection √
    Detailed Information: Storage network interface bandwidth is 0mbps, detection threshold 1,000mbps, terminal communication port eth0 bandwidth is 10,000mbps, detection threshold 1,000mbps
    Network card negotiation information:
    ----------------------------------------
    Network card: eth0            Speed: 10,000 Mbps Mode: Full-duplex (Role: tercom,mgmt)
    Network card: eth1            Speed: 10,000 Mbps Mode: Full-duplex (Role: vxlan)
    Network card: eth2            Speed: 10,000 Mbps Mode: Full-duplex
    Network card: eth3            Speed: 10,000 Mbps Mode: Full-duplex
    Network card: eth4            Speed: 10,000 Mbps Mode: Full-duplex
    Network card: eth5            Speed: 10,000 Mbps Mode: Full-duplex
    ----------------------------------------


    4.7 Network forwarding core exclusive detection ×
    Alarm Level:Medium
    Detailed Information:Network forwarding core exclusive status: Not exclusive
    Recommendation: Network forwarding core exclusive performance is higher. If network forwarding performance has bottlenecks or needs to achieve higher network forwarding performance, please enable network forwarding core exclusive on the host details page. If KB cannot resolve, please contact VN Technical Support

    4.8 Network card interrupt core and network forwarding core conflict detection √
    Detailed Information: No network card with interrupt core and network forwarding core conflict exists

    4.9 VXLAN network port high performance mode detection √
    Detailed Information: VXLAN network interface configured for high-performance mode.

    4.10 VXLAN and business network port DPDK mode detection √
    Detailed Information: VXLAN and service ports not using DPDK mode: eth1

    4.11 Network Packet Loss √
    Detailed Information: No network packet loss

    -----------------------------------------------------------------------------------------------------------------------------------

    5. Checking Other Host Check Items
    5.1 API interface timeout detection √
    Detailed Information: API interface is normal

    5.2 D-state and Z-state process detection √
    Detailed Information: No abnormal D-state or Z-state processes found

    5.3 VS Cache Ratio Detection √
    Detailed Information: VS storage volume cache ratio is: No virtual storage hybrid flash volume, detection threshold 10.00%

    5.4 Kernel Abnormal Log Detection ×
    Alarm Level:Medium
    Detailed Information:Kernel has the following abnormal logs:
    /sf/log/today/kernel.log
    2026-05-14 07:22:59.869618 err [kernel:] [    6.013761] integrity: Unable to open file: /etc/keys/x509_ima.der (-2)
    2026-05-14 07:22:59.869618 err [kernel:] [    6.013777] integrity: Unable to open file: /etc/keys/x509_evm.der (-2)
    2026-05-14 07:22:59.869765 err [kernel:] [    7.676099] piix4_smbus 0000:00:07.3: SMBus Host Controller not enabled!
    2026-05-14 07:22:59.871039 err [kernel:] [   39.628481] kvm_amd: CPU 3 isn't AMD or Hygon
    Recommendation: This check item detects logs of emerg, alert, crit, err levels in kernel logs, which can preliminarily observe if there are obvious abnormalities, in most cases no processing is required.

    5.5 CMCI storm log detection √
    Detailed Information: No CMCI storm log exists

    -----------------------------------------------------------------------------------------------------------------------------------

    Six, Check virtual storage detection items
    6.1 VS tiered cache penetration detection √
    Detailed Information: No cache breakdown logs were recorded.

    6.2 VMP VS data disk remaining space detection √
    Detailed Information: No insufficient remaining space in shards

    6.3 VS client, server, and tiered latency detection √
    Detailed Information: VS no high latency log

    6.4 VS network port latency detection √
    Detailed Information: VS storage network interface latency situation:


    6.5 VS network port historical latency detection in the last day √
    Detailed Information: VS has experienced no high latency or packet loss in the last 24 hours

    6.6 Virtual Storage interface Down Detection √
    Detailed Information: No network interface are down

    6.7 VS Network Port Interrupt Core Usage Detection √
    Detailed Information: VS network port interrupt core usage has been normal in the past day

    -----------------------------------------------------------------------------------------------------------------------------------

    Summary of Host Detection Anomalies  (Please prioritize alert items with high alert levels)
    1. CPU sys Usage ×
    Alarm Level:Medium
    Detailed Information:Physical host CPU sys usage is 37.07%, detection threshold is 15.00%
    Recommendation: If the CPU sys usage of the physical host is relatively high, please check whether there is abnormal process occupation, whether there is memory frequency reduction, incorrect clock source and other issues, refer to https://support.sangfor.com.cn/cases/list?product_id=26&type=1&category_id=30186 , https://support.sangfor.com.cn//cases/list?product_id=26&category_id=29936&type=2 If KB cannot resolve, please contact Cloud BG Middle Platform Technical Support

    2. Network forwarding core exclusive detection ×
    Alarm Level:Medium
    Detailed Information:Network forwarding core exclusive status: Not exclusive
    Recommendation: Network forwarding core exclusive performance is higher. If network forwarding performance has bottlenecks or needs to achieve higher network forwarding performance, please enable network forwarding core exclusive on the host details page. If KB cannot resolve, please contact VN Technical Support

    3. Kernel Abnormal Log Detection ×
    Alarm Level:Medium
    Detailed Information:Kernel has the following abnormal logs:
    /sf/log/today/kernel.log
    2026-05-14 07:22:59.869618 err [kernel:] [    6.013761] integrity: Unable to open file: /etc/keys/x509_ima.der (-2)
    2026-05-14 07:22:59.869618 err [kernel:] [    6.013777] integrity: Unable to open file: /etc/keys/x509_evm.der (-2)
    2026-05-14 07:22:59.869765 err [kernel:] [    7.676099] piix4_smbus 0000:00:07.3: SMBus Host Controller not enabled!
    2026-05-14 07:22:59.871039 err [kernel:] [   39.628481] kvm_amd: CPU 3 isn't AMD or Hygon
    Recommendation: This check item detects logs of emerg, alert, crit, err levels in kernel logs, which can preliminarily observe if there are obvious abnormalities, in most cases no processing is required.

    Detection completed!Results have been output to file /sf/data/local/performance_tools/check_result/output.txt.
    HTML results have been output to file /sf/data/local/performance_tools/check_result/checkhost_output.html.
    ```

    Using troubleshooting plugins, you can easily obtain inspection results and troubleshooting guidance for specific scenarios.
</details>

### Log Collection

The acli tool provides powerful log collection capabilities, capable of collecting any logs on HCI and using efficient compression algorithms for compression.

<details>
  <summary>Expand to View</summary>
    ```shell
    support/host-0050568eb9d8(acli) ~/tmp # acli log_collect --help
    Usage: acli log_collect {command} [command options]

    Available commands:
      cancel               Cancel log collection task
      create               Create log collection task
      progress             Query log collection task progress

    Use "acli log_collect <command> -h" to view help information for specific commands


    support/host-0050568eb9d8(acli) ~/tmp # acli log_collect create --help
    Usage: acli log_collect create [command parameters]

    Description:
      create                              Create log collection task

    Command parameters:
      -s|--save-filename=STRING          Required parameter, collection file name (no file suffix required), use icare ticket number, example: Q2025052718316
      -m|--modules=STRING                Log collection module, use English comma to concatenate specified modules, example: vm_suspend,network
                                         Available modules, default is other, enumerate:
                                            vm_suspend（VM Suspend Issue）             vm_start（VM Start Failure Issue）
                                            host_offline（Host Offline Issue）         network（Network Issue）
                                            storage（Virtual Storage Issue）           slowdisk（Slow Disk Issue, approx. 4min collection time per day）
                                            performance（Performance Issue）           system（Platform Issue）
                                            other（Default Collection Issue, does not collect logs for the above n scenarios）
      -d|--date-range=STRING             Specify date range (use English comma to concatenate start date, example: 2025-06-25,2025-06-27)
                                         Specify a specific date (example: 2025-06-25), default is today if not set
      -i|--ips=STRING                    Specify host ip, use English comma to concatenate specified ips, example: 1.1.1.1,1.2.3.4
                                         Default is collect current host log, set all to collect all hosts
      -p|--paths=STRING                  Specify additional directories or files to collect, will be compressed into extra_tar.tar.gz
                                         Use English comma to concatenate multiple paths, for example: /sf/data/local/you,/sf/ls.txt
      -c|--config=STRING                 JSON configuration file path, used for advanced control of log collection
                                         Example: --config /sf/data/local/config.json
      -u|--remote-url=STRING             Remote target address (check network connectivity before use), example: http://acli.sangfor.com.cn:5888/
      -H|--header=STRING                 HTTP request header, globally valid, format: Header-Name: value
      -L|--url-header=STRING             URL-specific request header, priority higher than --header, format: index:Header-Name:value
                                         Note: index starts from 0
      -U|--auth-username=STRING          Authentication username, note: if multiple target addresses, configure the one with auth-username first
      -P|--auth-password=STRING          Authentication password, note: must appear with auth-username together
                                         If multiple target addresses, configure the one with auth-password first
      -v|--vm-ids=STRING                 Specify virtual machine id, use English comma to concatenate specified vm ids

                                         Note:
                                         -s is required parameter; followed by ICare ticket number
                                         It is recommended to first test if hci can ping the log service address; if accessible, use -u parameter to automatically upload after collection
                                         Available nodes:
                                         China node: acli.sangfor.com.cn
                                         Malaysia node: acli.sea.sangfor.com
                                         Germany node: acli.eu.sangfor.com

                                         Example 1: Collect network module logs, host 1.1.1.1, date range 2025-06-25 to 2025-06-28
                                         acli log collection create -s Q2025052777777 -m network -i 1.1.1.1 -d 2025-06-25,2025-06-28

                                         Example 2: Through ping found HCI can ping acli.sangfor.com.cn; collect vm_suspend module logs, all hosts today's logs
                                         and automatically upload to log server after collection completes
                                         acli log collection create -s Q2025062888888 -m vm_suspend -i all -u http://acli.sangfor.com.cn:5888/

                                         Example 3: No module specified, collect all hosts current date other logs (other is default collection module, does not collect logs for all provided scenarios above)
                                         acli log collection create -s Q2025072999999 -i all
    ```
</details>

You can use the `acli log_collect create` command to create a log collection task, and specify parameters such as collection module, host, date range, etc., to easily obtain a list of log files.

```shell
support/host-005056b237a6(acli) ~ # acli log_collect create -s Q202511111200 -m vm_suspend -i all
Log collection task issued successfully!

support/host-005056b237a6(acli) ~ # acli log_collect progress
Status: Collect task has been completed!
Path to the compressed file (Please manually delete the compressed file after downloading the log): /sf/data/local/acli/tmp/data/log_collect/Q202511111200.zip
Overall progress: 100% - 1/1(Collected/Total collected)
Total time: 00:04:03.0
10.131.136.168  Collection successful  100%
Log collection records:
  IP: 10.131.136.168
    x /sf/log/14.tar.gz
    x /sf/log/14.tar.zst
    x /sf/log/14.zst
    √ /sf/log/14/
    x /sf/log/blackbox/20260514.tar.gz
    x /sf/log/blackbox/20260514.zst
    √ /sf/log/blackbox/20260514/
    x /sf/log/vn-blackbox/20260514.tar.gz
    x /sf/log/vn-blackbox/20260514.zst
    √ /sf/log/vn-blackbox/20260514/
    x /boot/boot/log/install.log
    √ /boot/firmware/current/package/meta-inf/kernel_version
    √ /boot/firmware/current/package/meta-inf/version
    √ /boot/firmware/history
    x /boot/firmware/nvidia-vgpu-mgr/sgax-install.md5sum
    √ /cfs/
    √ /etc/hosts
    √ /sf/cfg/
    √ /sf/data/local/dump/
    x /sf/data/local/kdump/*.kernel_core
    x /sf/data/local/sgax/md5file
    √ /sf/etc/
```

The default log storage directory is: `/sf/data/local/acli/tmp`. Sangfor Technical Support also provides a unified [Log Upload Platform](http://acli.sangfor.com.cn:5888) for log management and analysis.

You can upload at any time and contact CTI or official technical support to seek the best problem resolution.

### Operations and Maintenance Monitoring

By combining acli commands and setting timers or thresholds, you can achieve automation and advanced troubleshooting capabilities. Later, the official will open source the development framework and SDK package that supports free orchestration of acli commands. At that time, all developers and customers will be able to carry out customized development according to their own needs.

## Technical Features

<div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginTop: '1rem'}}>

- ✅ **Cluster Support**: Host-level and cluster-level operations
- ✅ **Asynchronous Processing**: Long-running tasks support background execution
- ✅ **Secure and Controllable**: Dedicated troubleshooting environment, auditable command execution
- ✅ **Complete Ecosystem**: Rich community documentation and continuous maintenance
- ✅ **Optimized Experience**: Intelligent completion, detailed help, operation guidance

</div>

## Target Audience

<div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginTop: '1rem'}}>

- ✅ **Development Technical Personnel**
- ✅ **Technical Support Engineers**
- ✅ **CTI/TAC Technical Experts**
- ✅ **Frontline Technical Support**
- ✅ **Distributor Technical Teams**
- ✅ **Channel Partners**
- ✅ **Customer Operations Personnel**
- ✅ **......**

</div>
