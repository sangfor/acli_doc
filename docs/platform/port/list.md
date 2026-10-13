---
sidebar_position: 1
---

# list

### 操作概述

查询平台端口列表

### 命令参数

```bash
-s|--service-ids=string   指定要查询的服务ID列表，多个用逗号分隔。不传则返回所有服务端口，示例：ssh,agentless_backup
```

### 使用示例

```bash
acli platform port list --service-ids ssh
```

### 结果示例

```bash
[
  {
    "description": "用于无代理备份数据传输，第三方备份管理平台可以对虚拟机进行备份和恢复",
    "disable_desc": "禁用后，第三方备份管理平台无法对虚拟机执行备份与恢复",
    "port": "40809-40824",
    "protocol": "tcp",
    "service_id": "agentless_backup",
    "service_name": "无代理备份数据传输服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "用于集群添加主机时自动发现环境中的新服务器",
    "disable_desc": "禁用后在添加新主机时将不会自动发现新服务器",
    "port": "4099",
    "protocol": "udp",
    "service_id": "host_found",
    "service_name": "新主机发现服务",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "用于集群内、跨集群虚拟机迁移；当集群被云管平台纳管后此端口将自动开启",
    "disable_desc": "禁用后您只能在集群内迁移虚拟机，将无法使用跨集群迁移功能",
    "port": "7001-7019",
    "protocol": "tcp",
    "service_id": "migrate_live",
    "service_name": "虚拟机迁移服务",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "用于其他设备同步时间",
    "disable_desc": "禁用后将停止与其他设备同步时间",
    "port": "123",
    "protocol": "udp",
    "service_id": "ntp_svr",
    "service_name": "NTP服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "用于执行p2v任务时，处理迁移请求任务和迁移数据传输",
    "disable_desc": "禁用后您将无法使用p2v迁移服务",
    "port": "4000-4010,10809-10900",
    "protocol": "tcp/udp",
    "service_id": "p2v_svr",
    "service_name": "p2v迁移服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "Samba共享目录管理服务，提供文件共享功能",
    "disable_desc": "禁用后将无法使用存储文件共享功能",
    "port": "139,445",
    "protocol": "tcp",
    "service_id": "samba",
    "service_name": "Samba服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "用于桌面云、云内建安全、第三方合作伙伴接入",
    "disable_desc": "禁用后将停止桌面云、云内建安全、第三方合作伙伴服务接入",
    "port": "4433",
    "protocol": "tcp",
    "service_id": "sf_sdk",
    "service_name": "合作伙伴服务",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "通过SNMP服务可帮助管理员了解运行时的物理资源使用情况，需要通过独立的账号和密码来使用服务",
    "disable_desc": "禁用后您将无法通过SNMP服务管理物理主机",
    "port": "161",
    "protocol": "udp",
    "service_id": "snmp",
    "service_name": "SNMP服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "用于协助解决技术问题、问题诊断、排查与恢复等，改善系统运行情况；当集群被云管平台纳管后此端口将自动开启",
    "disable_desc": "禁用后将无法远程登录您的深信服科技信云物理主机协助解决技术问题等，同时其他集群虚拟机迁入功能、云管平台镜像分发功能也将受到影响",
    "port": "22",
    "protocol": "tcp",
    "service_id": "ssh",
    "service_name": "远程协助服务",
    "status": "enable",
    "status_modifiable": "1"
  },
  {
    "description": "用于桌面云接入业务",
    "disable_desc": "禁用后您将无法使用桌面云接入相关服务，桌面云接入服务依赖合作伙伴服务，若无其他合作伙伴服务诉求，可以手动关闭",
    "port": "5500,8888,13500-13999",
    "protocol": "tcp/udp",
    "service_id": "vdi_access",
    "service_name": "桌面云接入服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "用于web访问VMware虚拟机控制台",
    "disable_desc": "禁用后您将不能通过web控制台访问VMware虚拟机",
    "port": "4481",
    "protocol": "tcp",
    "service_id": "vmware_console_proxy",
    "service_name": "VMware虚拟机控制台代理服务",
    "status": "disable",
    "status_modifiable": "1"
  },
  {
    "description": "用于问题诊断与故障恢复；在云管平台开启aCLI排障服务后此端口将自动开启",
    "disable_desc": "",
    "port": "11022",
    "protocol": "tcp",
    "service_id": "acli_ssh",
    "service_name": "排障服务",
    "status": "enable",
    "status_modifiable": "0"
  },
  {
    "description": "提供对外的iscsi盘和共享盘使用。iscsi协议解析、数据传输、共享盘的实现和存储",
    "disable_desc": "",
    "port": "3260",
    "protocol": "tcp",
    "service_id": "iscsi_svr",
    "service_name": "iscsi服务",
    "status": "enable",
    "status_modifiable": "0"
  },
  {
    "description": "用于虚拟网络设备web控制台管理页面，由SANGFOR-waf进行防护",
    "disable_desc": "",
    "port": "4480",
    "protocol": "tcp",
    "service_id": "sso_proxy",
    "service_name": "虚拟网络设备web控制台管理服务",
    "status": "enable",
    "status_modifiable": "0"
  },
  {
    "description": "用于访问深信服科技信云平台Web管理页面",
    "disable_desc": "",
    "port": "80,443",
    "protocol": "tcp",
    "service_id": "web_svr",
    "service_name": "web管理页面服务",
    "status": "enable",
    "status_modifiable": "0"
  }
]
```
