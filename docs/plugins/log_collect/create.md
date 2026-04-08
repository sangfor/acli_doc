---
sidebar_position: 1
---

# create

### 操作概述

创建日志收集任务

### 命令参数

```bash
-s|--save-filename=string          （必要参数），收集文件命名（无需文件后缀），使用icare单号，示例：Q2025052718316
-m|--modules=string                日志收集专项，使用英文逗号拼接指定的专项，示例：vm_suspend,network
                                     可供选择的专项，不设置则默认other，枚举值：
                                        vm_suspend（虚拟机挂起专项）      vm_start（虚拟机开机失败专项）
                                        host_offline（主机离线专项）      network（网络专项）
                                        storage（虚拟存储专项）           slowdisk（卡慢盘专项，单天收集时间约4min）
                                        performance（性能专项）          system（中台专项）
                                        other（默认收集专项，不收集上述n个场景日志）
-d|--date-range=string             指定日期范围（使用英文逗号拼接起始日期，示例：2025-06-25,2025-06-27）指定某个日期（举例：2025-06-25），不设置则默认今天
-i|--ips=string                    指定主机ip，使用英文逗号拼接指定的ip，举例：1.1.1.1,1.2.3.4，不设置则默认收集当前主机日志，设置all表示收集所有主机
-p|--paths=string                  指定收集额外的目录或者文件，最终压缩成extra_tar.tar.gz压缩包，可以使用英文逗号拼接多个路径，比如：/sf/data/local/you,/sf/ls.txt
-c|--config=string                 JSON配置文件路径，用于使用配置文件更高级的控制日志收集，举例：--config /sf/data/local/config.json
-u|--remote-url=string             远程目标地址（使用前请检查网络连通性），示例：http://acli.sangfor.com.cn:5888/
-H|--header=string                 HTTP请求头，对全局有效，格式：Header-Name: value
-L|--url-header=string             URL特定请求头，优先级大于--header，格式：index:Header-Name:value，注意：index从0开始
-U|--auth-username=string          认证用户名，注意：如果有多个目标地址请先将具有auth-username的地址先进行配置
-P|--auth-password=string          认证密码，注意：必须和auth-username同时出现，如果有多个目标地址请先将具有auth-password的地址先进行配置
-v|--vm-ids=string                 指定虚拟机id，使用英文逗号拼接指定的vmid
```

### 使用示例

```bash
# 示例1：收集网络专项，1.1.1.1主机，2025-06-25,2025-06-28时间段日志
acli log_collect create -s Q2025052777777 -m network -i 1.1.1.1 -d 2025-06-25,2025-06-28  

# 示例2：通过ping发现HCI可以ping通过acli.sangfor.com.cn；收集虚拟机挂起专项，所有主机今天的日志并在收集完成后自动上传至日志服务器
acli log_collect create -s Q2025062888888 -m vm_suspend -i all -u http://acli.sangfor.com.cn:5888/ 

# 示例3：未指定专项，收集所有主机当前日期的other日志（other为默认收集专项，不收集当前所有已提供场景的相关日志）
acli log_collect create -s Q2025072999999 -i all
```

### 结果示例

```bash
日志收集任务下发成功！
```
