---
sidebar_position: 1
---

# curl

### Overview

Call the GET APIs of HCI platform services in a controlled manner via the `acli system curl` subcommand (read-only), carrying the 100 GET APIs allowed for KB troubleshooting.

### Command Parameters

This is a controlled passthrough command. Only the GET method is allowed, and it follows the curl security restrictions (closed set):

Command format:

```bash
acli system curl -X <method> <url>    (<method> must be GET, -X may be omitted; <url> is required)
```

Parameter description:

```bash
<method>  Optional parameter. HTTP method; -X may be omitted (defaults to GET). The value must be GET; POST/PUT/DELETE etc. are rejected.
<url>     Required parameter. Target URL; only http:// and https:// are supported (protocol whitelist, https by default). The URL must be a single token without spaces, and may be wrapped in single or double quotes.
```

Security restrictions (rejected on match):

```bash
host whitelist: only 127.0.0.1, localhost, and cluster management network IPs are allowed
Path template: must exactly match one of the 100 GET API path whitelist templates (<name> placeholder occupies one segment)
Flag whitelist: only -X -k|--insecure -s|--silent -S|--show-error -h|--help --manual -V|--version --connect-timeout --max-time -m --retry --retry-delay --retry-max-time --url
Port whitelist: explicit ports must be 443/20030/20220/15001/23030/22030/20210; if no port is given, the implicit port of the protocol is used
Timeout: --max-time/-m <= acli MaxCmdTimeout (defaults to 60 seconds if not specified); --connect-timeout <= 5s
Multiple URLs / chaining: only one URL per command; --next, -:, &&, ;, | are forbidden
Charset: UTF-8, Chinese characters allowed
```

### Usage Example

```bash
acli system curl -skX GET https://127.0.0.1/vapi/json/vtpstorage/storagetree
```

Or omit `-X` (defaults to GET):

```bash
acli system curl -sk https://127.0.0.1/vapi/json/vtpstorage/storagetree
```

### Output Example

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