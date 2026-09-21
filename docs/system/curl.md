---
sidebar_position: 1
---

# curl

### 操作概述

通过 `acli system curl` 子命令受控调用 HCI 平台服务的 GET 接口（只读），承载 KB 排障知识库中的 100 条 GET API 放通。

### 命令参数

本命令为受控透传命令，仅放通 GET 方法，并遵循 curl 安全限制（封闭式）：

命令格式：

```bash
acli system curl -X <method> <url>    （<method> 仅支持 GET，-X 可省略；<url> 为必填项）
```

参数说明：

```bash
<method>  可选参数，HTTP 方法；-X 可省略（默认 GET），值必须为 GET，POST/PUT/DELETE 等拒绝
<url>     必要参数，目标 URL；仅支持 http:// 与 https://（协议白名单，默认 https）；URL 须为单个不含空格的 token，支持单/双引号包裹
```

安全限制（命中即拒绝）：

```bash
host 白名单：仅允许 127.0.0.1、localhost、集群管理网 IP
路径模板：须精确命中 100 条 GET API 路径白名单模板（<名称> 占位符一个占一个段）
flag 白名单：仅允许 -X -k|--insecure -s|--silent -S|--show-error -h|--help --manual -V|--version --connect-timeout --max-time -m --retry --retry-delay --retry-max-time --url
端口白名单：显式端口须命中 443/20030/20220/15001/23030/22030/20210，不带端口按协议隐式端口放行
超时限制：--max-time/-m ≤ acli MaxCmdTimeout（未显式指定默认 60 秒）；--connect-timeout ≤ 5s
多 URL / 串联：一条命令仅一个 URL；禁 --next、-:、&&、;、|
字符集：UTF-8，允许中文
```

### 使用示例

```bash
acli system curl -skX GET https://127.0.0.1/vapi/json/vtpstorage/storagetree
```

或省略 `-X`（默认 GET）：

```bash
acli system curl -sk https://127.0.0.1/vapi/json/vtpstorage/storagetree
```

### 结果示例

```bash
# acli system curl -skX GET https://127.0.0.1/vapi/json/vtpstorage/storagetree
{
  "success": 1,
  "errcode_tracing": "",
  "data": [
    {
      "hosts": 1,
      "maxread": "243560960",
      "status": 1,
      "support_spdk": 0,
      "shared": 0,
      "free": 317639884800,
      "id": "36000c293c31acd40fa7d01471c8d0d9a_0050568991c1",
      "lvtype": "local",
      "support_sriov": 0,
      "alertsize": "285857126809.6",
      "name": "lv_1789039616",
      "total": 317827579904,
      "ats": -1,
      "maxwrite": "394035200",
      "type": "storage",
      "label": ""
    }
  ],
  "errcode": null
}
```
