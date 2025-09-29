---
sidebar_position: 10
---

# create
操作概述: 创建日志收集任务

命令参数:
```bash
-s|--save-filename=string   必要参数，收集文件命名（无需文件后缀），使用icare单号，示例：Q2025052718316
-m|--modules=string         日志收集专项，使用英文逗号拼接指定的专项，示例：compute,network
                            可供选择的专项，不设置则默认all，枚举值：
                            all（所有日志及配置）   slowdisk（卡慢盘专项，单天收集时间约4min）
                            compute（计算专项 - 适用于VT）     network（网络专项 - 适用于VN）
                            storage（存储专项 - 适用于VS）     system （系统专项 - 适用于中台）
                            storage（存储专项 - 适用于VS）     system （系统专项 - 适用于中台）
-d|--date-range=string      指定日期范围（使用英文逗号拼接起始日期，示例：2025-06-25,2025-06-27）
                            指定某个日期（举例：2025-06-25），不设置则默认今天
-i|--ips=string             主机ip，使用英文逗号拼接指定的ip，举例：1.1.1.1,1.2.3.4   不设置则默认收集当前主机日志，设置all表示收集所有主机
-p|--paths=string           指定收集额外的目录或者文件，最终压缩成extra_tar.tar.gz压缩包，可以使用英文逗号拼接多个路径，比如：/sf/data/local/you,/sf/ls.txt
-c|--config=string          JSON配置文件路径，用于使用配置文件更高级的控制日志收集，举例：--config /sf/data/local/config.json
-u|--remote-url=string      远程目标地址（使用前请检查网络连通性），示例：http://acli.sangfor.com.cn:5888/
-H|--header=string          HTTP请求头，对全局有效，格式：Header-Name: value
-L|--url-header=string      URL特定请求头，优先级大于--header，格式：index:Header-Name:value，注意：index从0开始
-U|--auth-username=string   认证用户名，注意：如果有多个目标地址请先将具有auth-username的地址先进行配置
-P|--auth-password=string   认证密码，注意：必须和auth-username同时出现，如果有多个目标地址请先将具有auth-password的地址先进行配置
```

使用示例:
```bash
acli log collection create -s Q2025052718316
```

结果示例:
```bash
日志收集任务下发成功！
```