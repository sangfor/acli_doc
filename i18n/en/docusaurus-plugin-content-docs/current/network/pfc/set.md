---
sidebar_position: 4
---

# set

### Overview

Update a Priority Flow Control (PFC) configuration (asynchronous task, returns taskId)

### Command Parameters

```bash
-f|--flowcontrol-id=string    Required parameter, Flow control configuration ID (UUID), e.g. 6728081d-cb8b-4be1-ba35-28158e150dd4
-d|--data=object              Required parameter, parameters for updating flow control configuration (JSON object)
                                Fields:
                                  enable      bool    Required, whether to enable
                                  trust       string  Required, trust mode, values: pcp / dscp (lowercase)
                                  pcpTag      int     Optional, required when trust=pcp, range 0-7
                                  dscpTag     int     Optional, required when trust=dscp, range 0-63
                                  cnpPrio     int     Optional, RoCE scenario, range 0-7
                                  cnpDscp     int     Optional, RoCE scenario, range 0-63
                                Example: {"enable":true,"trust":"dscp","dscpTag":46}
```

### Usage Example

```bash
# First list to get the id
acli network pfc list -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2

# Update (disable enable, change dscpTag)
acli network pfc set -f 215613f8-4ee3-4d56-a602-d05fe9cd484c -d '{"enable":false,"trust":"dscp","dscpTag":30}'

# Update cnp fields
acli network pfc set -f 215613f8-4ee3-4d56-a602-d05fe9cd484c -d '{"enable":true,"trust":"dscp","dscpTag":30,"cnpPrio":3,"cnpDscp":48}'
```

### Output Example

```bash
taskId: host-0050568ecad9:1703505460:1
```
