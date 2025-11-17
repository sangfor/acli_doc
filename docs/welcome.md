---
slug: /
sidebar_position: 1
title: aCLI排障
sidebar_label: 介绍
---

## 欢迎使用aCLI排障服务命令行工具

欢迎使用aCLI排障服务命令行工具，aCLI（Admin CLI）是专为HCI平台设计的命令行排障工具，旨在为技术支持和运维人员提供便捷、高效的系统诊断和问题解决手段。aCLI通过封装复杂的底层操作，提供标准化的命令接口，使排障工作更加规范和高效。

```shell
support/host-005056b237a6(acli) ~ # acli --help
用法：acli [参数] {命名空间}+ {命令} [命令参数]

参数：
  --help, -?           展示工具用法
  --version            展示版本信息
  --debug              打开debug级别日志
  --cluster            用于遍历集群主机执行acli命令
  --timeout            用于设置命令的超时时间（秒）
  --force              强制模式：忽略交互确认，直接执行操作（使用前请确认风险）
  --formatter          用于命令的格式化参数。枚举值：xml、csv、keyvalue、json
  --container          用于命令的全局容器指定参数，仅对system下的命令生效。枚举值：asv-con、vn-con、vn-agent、vs-cp-manager

可用命名空间：
  acli                 acli说明，允许用户获取附加信息
  alert                告警相关命令
  task                 任务相关命令
  log                  平台日志相关命令
  service              服务相关命令
  vm                   虚拟机相关命令
  system               系统相关命令
  network              网络相关命令
  storage              存储相关命令
  platform             平台相关命令
  hardware             硬件相关命令
```

---

**技术支持说明**：如在使用过程中遇到问题，请联系深信服技术支持团队获取专业协助。

## 下载与安装

:::warning 使用提醒
当前aCLI排障服务命令行工具处于preview试点阶段，请谨慎使用。  
请勿随意使用变更命令修改系统环境与配置，否则可能造成不可预知的后果。
:::

### 下载

请根据您的 HCI 版本架构选择对应的安装器进行安装，通常情况下，使用Intel、AMD等品牌处理器的系统请选择 x86/64 版本下载，使用海光、飞腾、鲲鹏、兆芯等品牌处理器的请选择 arm/aarch64 版本下载。

<a
  href="http://acli.sangfor.com.cn:1110/api/public/download/4jotgyfk/latest?architecture=x86_64&api_key=QRlZXabZ8sOrFKtgs1VIfkHJZYQ3QNrcETXgsJaiX9Svz1pjFj"
  className="download-btn"
>
  下载 x86/64 版本
</a>
<a className="link-spacer"></a>
<a
  href="http://acli.sangfor.com.cn:1110/api/public/download/4jotgyfk/latest?architecture=aarch64&api_key=QRlZXabZ8sOrFKtgs1VIfkHJZYQ3QNrcETXgsJaiX9Svz1pjFj"
  className="download-btn"
>
  下载 arm/aarch64 版本
</a>

### 安装

:::info 安装提醒
安装前，请先检查 /sf/data/local 分区可用容量是否大于 1GB ，否则可能安装失败。
:::

1. 上传安装包

    将下载的安装包上传至 HCI 环境的 `/sf/data/local/` 目录

2. 添加执行权限

    ```shell
    chmod +x acli-installer_x86_64_YYYY-MM-DD_HH-mm-ss.acli
    ```

3. 执行安装

    ```shell
    ./acli-installer_x86_64_YYYY-MM-DD_HH-mm-ss.acli --install
    ```

4. 启用自动补全

    ```shell
    source ~/.profile
    ```

5. 验证安装

    ```shell
    acli --version
    ```

## 使用说明

### 命令说明

1. 命令格式

    ```shell
    acli   [options]     {namespace}+      {cmd}+      [cmd options]+
     |         |              |              |              |
    主程序 全局参数（可选） 命名空间（多个） 参数（多个）  参数选项（多个）
    ```

    <details>
      <summary>展开查看-示例：查询 '登录' 字样操作日志</summary>
      <pre><code> 
        support/host-005056b237a6(acli) ~ # acli task get -k 登录 -l 1
        [0]:
          action_type: 0
          bcancel: 0
          log_id: host-005056b237a6:198461:1763024338:1381504498768
          object_name: admin
          pid:
          reserved2:
          reserved3:
          hostname: 10.131.134.160
          object_id:
          user: admin (10.131.112.176)
          end: 2025-11-13 16:58:58
          errcode_tracing: null
          host: 10.131.134.160
          module_type: 5
          ha_handle_result:
          description: 执行（登录）完成
          dest_host:
          event_id: 5373997
          otype: 用户
          sched_effect:
          start: 2025-11-13 16:58:58
          status: 2
          hostid: host-005056b237a6
          risk_level: 2
          sched_reason:
          type: 登录
          upid:
          alert_type: 登录
          sysloged: 0
          target: admin
          ha_handle_action:
          id: 64
          object_type: 用户
          process: 完成
          request_id: ,9159dd2398fe3ac38bef4e6c6346ee4a
          vm:
      </code></pre>
    </details>

2. 命名空间

    acli的命令空间一般按照业务或操作对象进行严格划分，按照层级深入，直到最小操作单元。

    例如查看FC存储的相关统计信息：

    ```shell
    acli storage fc host statistics get
    ```

    例如上述命令则是按照 存储 - 存储类型 - 对象 - 事件/子对象 - 操作 进行严格编排得出。

3. 外置插件

    ```shell
    support/host-005056b237a6(acli) ~ # acli
    用法：acli [参数] {命名空间}+ {命令} [命令参数]

    参数：
      --help, -?           展示工具用法
      --version            展示版本信息
      --debug              打开debug级别日志
      --cluster            用于遍历集群主机执行acli命令
      --timeout            用于设置命令的超时时间（秒）
      --force              强制模式：忽略交互确认，直接执行操作（使用前请确认风险）
      --formatter          用于命令的格式化参数。枚举值：xml、csv、keyvalue、json
      --container          用于命令的全局容器指定参数，仅对system下的命令生效。枚举值：asv-con、vn-con、vn-agent、vs-cp-manager

    可用插件：
      vm_suspend           虚拟机异常挂起场景排障
      vm_start             虚拟机开关机场景排障
      netdoctor            网络异常场景排障
      performance_tools    性能异常场景排障
      host_offline         主机离线场景排障
    ......
    ```

    acli支持安装与卸载各类官方或第三方开源插件，目前preview版本预装了部分插件用以体验，后续将会上新更多的插件以供自由选择安装。

### 参数说明

1. 全局参数

    在acli命令体系中，将能够作用于任何命令的参数称之为全局参数。

    使用 acli --help 查看当前支持的所有全局参数

    ```shell
    support/host-005056b237a6(acli) ~ # acli
    用法：acli [参数] {命名空间}+ {命令} [命令参数]

    参数：
      --help, -?           展示工具用法
      --version            展示版本信息
      --debug              打开debug级别日志
      --cluster            用于遍历集群主机执行acli命令
      --timeout            用于设置命令的超时时间（秒）
      --force              强制模式：忽略交互确认，直接执行操作（使用前请确认风险）
      --formatter          用于命令的格式化参数。枚举值：xml、csv、keyvalue、json
      --container          用于命令的全局容器指定参数，仅对system下的命令生效。枚举值：asv-con、vn-con、vn-agent、vs-cp-manager
    ......
    ```

    通过灵活使用全局参数，实现对命令的精细化控制与强大执行能力。

    例如：acli命令默认在主控节点执行，但可以通过全局参数等方式实现集群执行。

2. 命令参数

    绝大多数命令需要输入参数进行控制执行逻辑，命令本身的参数被称之为命令参数。

    在有命令参数的命令后面使用 --help 或 直接回车 即可以看到其命令参数，例如：acli alert get --help

    ```shell
    support/host-005056b237a6(acli) ~ # acli alert get --help
    用法：acli alert get [命令参数]

    描述：
      get                                 查询告警信息

    命令参数：
      -k|--keyword=string                 搜索告警对象、事件和描述，示例：虚拟机异常挂起
      -e|--event=string                   指定事件，示例：免key序列号异常
      -o|--object-name=string             指定告警对象，示例：10.134.244.34
      -T|--object-type=string             指定告警对象类型，枚举值：host(主机),storage_obj(存储),vm(虚拟机),vnet(虚拟网络),sn(序列号),others(其他)
      -t|--time=string                    指定时间，格式：'YYYY-MM-DD HH:MM:SS'、'YYYY-MM-DD HH'
      -L|--level=integer                  指定级别，枚举值：1（紧急），0（普通）
      -l|--limit=integer                  指定展示记录的数目（默认值为50），示例：1，2等
    ```

## 使用案例

### 故障诊断

acli命令通过组合可以实现多种故障诊断功能，当然更推荐你使用外置插件进行一键诊断。

例如：使用插件 performance_tools 进行虚拟机性能异常场景排障（以下仅为示例，具体使用方式请参考插件文档）

<details>
  <summary>展开查看</summary>
  ```shell
    support/host-005056b237a6(acli) ~ # acli performance_tools check_host
    欢迎使用虚拟机检测工具！当前时间 2025-11-14 17:15:10
    正在进行主机检测...
    主机名: host-005056b237a6
    CPU型号: Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
    CPU核心数: 8
    CPU使用率: 51.24
    主机总内存大小: 41.67GB
    主机剩余内存大小 26.44GB
    运行虚拟机数量: 0
    集群类型: HCI
    -----------------------------------------------------------------------------------------------------------------------------------

    一、检查主机CPU信息
    1.1 CPU超线程 √
    详细信息: 物理主机未开启CPU超线程

    1.2 CPU使用率 √
    详细信息: 物理主机的CPU使用率为51.24%，检测阈值为65.00%
    当时CPU占用最高的10个进程为：
    PID        %CPU  MEM      STAT  START    TIME     COMMAND                                           
    37861      50.7  1.16GB   S<Ll  07:42    290:35   /sf/sdn/bin/dataplane --proc-type secondary -l 0,1...
    49470      7.2   32.21MB  S<l   07:42    41:15    -w                                                
    37872      7.2   11.52MB  R     07:42    41:33    /sf/sdn/bin/dhcp6d                                
    1745237    5.0   461.63MB S     17:15    0:00     start                                             
    8947       3.6   114.98MB Ssl   07:40    21:04    /usr/local/sf/container/bin/kubelet --config /sf/e...
    37529      3.6   21.02MB  S<l   07:42    21:04    /sf/sdn/bin/dpp -l 2 --proc-type primary --iova-mo...
    190410     3.6   499.55MB S     07:49    20:38    vtpalertd                                         
    5621       3.4   25.86MB  Ssl   07:40    19:47    /usr/local/sf/container/bin/containerd-squashfs-gr...
    110094     3.1   137.53MB S     07:45    17:50    WSGI                                              
    1744467    2.6   461.59MB S     17:15    0:00     start                                             


    1.3 CPU sys使用率 ×
    告警等级:中
    详细信息:物理主机的CPU sys使用率为25.55%，检测阈值为20.00%
    建议: 如果物理主机的CPU sys使用率比较高，请检查是否存在进程异常占用，是否存在内存降频，时钟源不正确等问题，参考https://support.sangfor.com.cn//cases/list?product_id=26&category_id=29936&type=2

    1.4 SPDK 转发核占用情况 √ 
    详细信息: SPDK 转发核核使用率为0.00%，检测阈值为90.00%

    1.5 CPU超配比检测 √
    详细信息: 主机CPU超配比为100.00%，检测阈值为0.00%

    1.6 CPU降频检查 √ 
    详细信息: 无法获取当前环境睿频信息

    1.7 非转发核单核CPU使用率 √
    详细信息: 非转发核单核CPU使用率最高为55.56%，检测阈值为95.00%

    1.8 CPU主频检测 × 
    告警等级:中
    详细信息:CPU主频为2.2GHz，检测阈值为2.4GHz
    建议: CPU基准频率为2.2GHz，如果CPU主频较低，会导致单核性能不足，桌面云场景建议使用主频超过2.4GHz的CPU，参考 https://support.sangfor.com.cn/cases/list?product_id=26&type=2&category_id=29936

    1.9 CPU时钟源检测 √
    详细信息: CPU时钟源为tsc，X86和C86架构检测时钟源需要是tsc

    -----------------------------------------------------------------------------------------------------------------------------------

    二、检查主机内存信息
    2.1 内存频率一致 √
    详细信息: 内存条频率一致

    2.2 内存条运行频率和物理频率一致 √
    详细信息: 内存条运行频率和物理频率一致

    2.3 Percpu内存泄漏检测 √
    详细信息: Percpu内存占用为264.00MB，检测阈值为10.00GB

    2.4 Slab内存泄漏检测 √
    详细信息: SReclaim内存占用为1.43GB，检测阈值为10.00GB

    2.5 NUMA节点内存均衡检测 √
    详细信息: 系统只有一个NUMA节点，无需检查内存均衡性

    2.6 可用内存大小检测 √
    详细信息: 物理主机的可用内存为26.44GB，占总内存比值为63.46%，检测阈值为剩余不足10GB或可用内存比值不足10.00%
    当时内存占用最高（不包含大页内存）的10个进程为：
    PID        %CPU  MEM      STAT  START    TIME     COMMAND                                           
    37861      50.7  1.16GB   S<Ll  07:42    290:35   /sf/sdn/bin/dataplane --proc-type secondary -l 0,1...
    182799     2.3   628.37MB Sl    07:49    13:26    kafka-server -Xmx512M -Xms512M -server -XX:+UseG1G...
    203235     0.8   522.71MB Sl    07:50    4:49     vn-ccp -Xms512m -Xmx1g -XX:+HeapDumpOnOutOfMemoryE...
    198849     0.0   510.16MB Ss+   07:50    0:01     menuconfigd                                       
    184417     0.1   509.81MB S     07:49    0:47     vtplogd                                           
    190410     3.6   499.55MB S     07:49    20:38    vtpalertd                                         
    114527     0.0   498.04MB S     07:45    0:06     vtpperlproxy                                      
    198473     0.9   497.92MB S     07:50    5:07     vtpcron                                           
    198566     0.9   497.74MB S     07:50    5:05     vtpcron                                           
    198270     0.8   497.35MB S     07:50    4:42     vtpcron                                           


    2.7 Swap使用情况 √
    详细信息: Swap内存占用大小为0.00B，检测阈值为0.00GB

    2.8 配置内存占用情况 √
    详细信息: 实际总的配置内存为%.2fGB，剩余配置内存为%.2fGB，配置内存占用率为%s，检测阈值为配置内存占用率超过%s

    2.9 内存降频检测 √ 
    详细信息: 不存在内存降频

    2.10 内存插法检测 √
    详细信息: 内存条数7，内存通道数14，未插内存通道：RAM slot #5、NVD #4、RAM slot #1、RAM slot #3、NVD #3、NVD #2、RAM slot #4、RAM slot #2、RAM slot #6、NVD #5、NVD #1、NVD #、NVD #6

    三、检查主机磁盘信息
    3.1 磁盘延迟检测 √
    详细信息: 不存在时延超过阈值的磁盘，检测阈值SSD磁盘10ms，HDD磁盘50ms
    当时的磁盘时延为：
    sda               0.55   101.11    1.84   23.25    68.52   272.55    27.19     0.07    2.63    1.50    2.72   0.56   1.40
    sdb               0.00     0.00    0.02    0.00     0.25     0.00    30.56     0.00    0.61    0.61    0.00   0.34   0.00
    sdc               0.00     0.00    0.02    0.00     0.29     0.00    30.62     0.00    0.35    0.35    0.00   0.18   0.00
    sdd               0.00     0.06    0.02    0.02     0.23     0.04    12.47     0.00    1.24    0.24    2.65   0.76   0.00
    sda               0.00     4.00    0.00    6.00     0.00    40.00    13.33     0.00    0.67    0.00    0.67   1.33   0.80
    sdb               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
    sdc               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
    sdd               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00


    3.2 VS卡慢盘日志检测 √
    详细信息: 不存在VS卡慢盘日志

    3.3 内核卡慢盘日志检测 √
    详细信息: 不存在内核卡慢盘日志
    ......

    主机检测异常项总结
    1. CPU sys使用率 ×
    告警等级:中
    详细信息:物理主机的CPU sys使用率为25.55%，检测阈值为20.00%
    建议: 如果物理主机的CPU sys使用率比较高，请检查是否存在进程异常占用，是否存在内存降频，时钟源不正确等问题，参考https://support.sangfor.com.cn//cases/list?product_id=26&category_id=29936&type=2

    2. CPU主频检测 × 
    告警等级:中
    详细信息:CPU主频为2.2GHz，检测阈值为2.4GHz
    建议: CPU基准频率为2.2GHz，如果CPU主频较低，会导致单核性能不足，桌面云场景建议使用主频超过2.4GHz的CPU，参考 https://support.sangfor.com.cn/cases/list?product_id=26&type=2&category_id=29936

    3. 网络转发核独占检测 × 
    告警等级:中
    详细信息:网络转发核独占情况：未独占
    建议: 网络转发核独占性能较高，如果网络转发性能存在瓶颈或需要达到更高的网络转发性能，请在主机详情页启用网络转发核独占。

    4. 内核异常日志检测 ×
    告警等级:中
    详细信息:内核存在以下异常日志：
    /sf/log/today/kernel.log
    2025-11-14 07:40:37.749677 err [kernel:] [    6.604250] integrity: Unable to open file: /etc/keys/x509_ima.der (-2)
    2025-11-14 07:40:37.749683 err [kernel:] [    6.604270] integrity: Unable to open file: /etc/keys/x509_evm.der (-2)
    2025-11-14 07:40:37.749894 err [kernel:] [    8.378681] piix4_smbus 0000:00:07.3: SMBus Host Controller not enabled!
    2025-11-14 07:40:37.750909 err [kernel:] [   53.418485] kvm_amd: CPU 7 isn't AMD or Hygon
    建议: 该检测项检测内核日志中emerg、alert、crit、err等级的日志，可以初步观察是否存在明显的异常，大部分情况下不需要处理。

    检测完成！结果同时输出在了文件 /sf/data/local/performance_tools/check_result/output.txt 中。
    ```

    使用排障插件，你可以轻松获得某个场景的检查结果以及排障指导。
</details>

### 日志收集

acli工具提供强大的日志收集能力，能够收集 HCI 上任意日志并使用高效的压缩算法进行压缩。

<details>
  <summary>展开查看</summary>
    ```shell
    support/host-005056b237a6(acli) ~ # acli log collection --help
    用法：acli log collection  {命令} [命令参数]

    可用命令：
      cancel               取消日志收集任务
      create               创建日志收集任务
      progress             查询日志收集任务


    support/host-005056b237a6(acli) ~ # acli log collection create --help
    用法：acli log collection create [命令参数]

    描述：
      create                              创建日志收集任务

    命令参数：
      -s|--save-filename=string           必要参数，收集文件命名（无需文件后缀），使用icare单号，示例：Q2025052718316
      -m|--modules=string                 日志收集专项，使用英文逗号拼接指定的专项，示例：vm_suspend,network
                                          可供选择的专项，不设置则默认other，枚举值：
                                          vm_suspend（虚拟机挂起专项）  vm_start（虚拟机开机失败专项）
                                          host_offline（主机离线专项）  network（网络专项）
                                          storage（虚拟存储专项）       slowdisk（卡慢盘专项，单天收集时间约4min）
                                          performance（性能专项）       other（默认收集专项，不收集上述n个场景日志）
      -d|--date-range=string              指定日期范围（使用英文逗号拼接起始日期，示例：2025-06-25,2025-06-27）
                                          指定某个日期（举例：2025-06-25），不设置则默认今天
      -i|--ips=string                     指定主机ip，使用英文逗号拼接指定的ip，举例：1.1.1.1,1.2.3.4   不设置则默认收集当前主机日志，设置all表示收集所有主机
      -p|--paths=string                   指定收集额外的目录或者文件，最终压缩成extra_tar.tar.gz压缩包，可以使用英文逗号拼接多个路径，比如：/sf/data/local/you,/sf/ls.txt
      -c|--config=string                  JSON配置文件路径，用于使用配置文件更高级的控制日志收集，举例：--config /sf/data/local/config.json
      -u|--remote-url=string              远程目标地址（使用前请检查网络连通性），示例：http://acli.sangfor.com.cn:5888/
      -H|--header=string                  HTTP请求头，对全局有效，格式：Header-Name: value
      -L|--url-header=string              URL特定请求头，优先级大于--header，格式：index:Header-Name:value，注意：index从0开始
      -U|--auth-username=string           认证用户名，注意：如果有多个目标地址请先将具有auth-username的地址先进行配置
      -P|--auth-password=string           认证密码，注意：必须和auth-username同时出现，如果有多个目标地址请先将具有auth-password的地址先进行配置

                                          说明：
                                          -s 为必要参数；后接ICare单号
                                          建议先探测hci是否可以ping通过日志服务地址;若可访问建议使用 -u 参数收集完可直接上传
                                          可选节点为：
                                          国内节点：acli.sangfor.com.cn
                                          马来节点：acli.sea.sangfor.com
                                          德国节点：acli.eu.sangfor.com

                                          示例1：收集网络专项，1.1.1.1主机，2025-06-25,2025-06-28时间段日志
                                          acli log collection create -s Q2025052777777 -m network -i 1.1.1.1 -d 2025-06-25,2025-06-28

                                          示例2：通过ping发现HCI可以ping通过acli.sangfor.com.cn；收集虚拟机挂起专项，所有主机今天的日志并在收集完成后自动上传至日志服务器
                                          acli log collection create -s Q2025062888888 -m vm_suspend -i all -u http://acli.sangfor.com.cn:5888/

                                          示例3：未指定专项，收集所有主机当前日期的other日志（other为默认收集专项，不收集当前所有已提供场景的相关日志）
                                          acli log collection create -s Q2025072999999 -i all
    ```
</details>

你可以使用 acli log collection create 命令创建日志收集任务，并指定收集专项、主机、时间范围等参数，并可以轻松获得日志文件列表。

```shell
support/host-005056b237a6(acli) ~ # acli log collection create -s Q202511111200 -m vm_suspend -i all
日志收集任务下发成功！

support/host-005056b237a6(acli) ~ # acli log collection progress
状态：收集任务已完成！
压缩包路径（完成日志下载后请手动删除压缩包）：/sf/data/local/private/Q202511111200.zip
总进度：100% - 1/1（已收集完成/收集总数）
总耗时：00:00:37.4
10.131.134.160  收集完成  100%
日志收集记录：
  IP：10.131.134.160
    x /sf/log/14.tar.gz
    x /sf/log/14.tar.zst
    x /sf/log/14.zst
    √ /sf/log/14/
    x /sf/log/blackbox/20251114.tar.gz
    x /sf/log/blackbox/20251114.zst
    √ /sf/log/blackbox/20251114/
    x /sf/log/vn-blackbox/20251114.tar.gz
    x /sf/log/vn-blackbox/20251114.zst
    x /sf/log/vn-blackbox/20251114/LOG_ping_statistic.txt
    x /sf/log/vn-blackbox/20251114/LOG_ping_statistic.txt.zip
    x /sf/log/vn-blackbox/20251114/LOG_tcpstat.txt
    x /sf/log/vn-blackbox/20251114/LOG_tcpstat.txt.zip
    √ /boot/firmware/current/package/meta-inf/kernel_version
    √ /boot/firmware/current/package/meta-inf/version
    √ /boot/firmware/history
    x /boot/firmware/nvidia-vgpu-mgr/sgax-install.md5sum
    √ /cfs/
    √ /etc/hosts
    √ /proc/cpuinfo
    √ /sf/cfg/
    √ /sf/etc/
    √ /sf/kernel_version
    √ /sf/log/checkitem/
    x /sf/log/compress_today_log.log
    √ /sf/log/log_new.db
    √ /sf/log/rd_rsync_check.log
    x /sf/log/rd_switch_today_log.log
    √ /sf/log/sdn/
    √ /sf/log/switch_today_log.log
```

日志默认存放目录为：`/sf/data/local/private/`，同时深信服技术支持提供了统一的 [日志上传平台](http://acli.sangfor.com.cn:5888) 进行日志管理分析。

你可以随时上传并于 CTI 或 官方技术支持取得联系，以寻求最佳问题解决方式。

### 运维监控

通过组合acli命令，设置定时或者阈值，则可以实现自动化与高级排障检查等能力。后续官方会将支持自由编排acli命令的开发框架与SDK包进行开源，届时，所有开发者与客户都可以根据自身的需求进行客制化开发。

## 技术特点

<div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginTop: '1rem'}}>

- ✅ **集群支持**：主机级和集群级操作
- ✅ **异步处理**：长时间运行的任务支持后台执行
- ✅ **安全可控**：专用排障环境，命令执行可审计
- ✅ **生态完善**：丰富的社区文档和持续维护
- ✅ **体验优化**：智能补全、详细帮助、操作指引

</div>

## 适用人群

<div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginTop: '1rem'}}>

- ✅ **开发技术人员**
- ✅ **技术支持工程师**
- ✅ **CTI/TAC 技术专家**
- ✅ **一线技术支持**
- ✅ **总代技术团队**
- ✅ **渠道合作伙伴**
- ✅ **客户运维人员**
- ✅ **......**

</div>
