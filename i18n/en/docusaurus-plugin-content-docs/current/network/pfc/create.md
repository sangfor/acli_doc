---
sidebar_position: 3
---

# create

### Overview

Create a Priority Flow Control (PFC) configuration (asynchronous task, returns taskId)

### Command Parameters

```bash
-d|--data=object    Required parameter, parameters for creating flow control configuration (JSON object)
                    Fields:
                      domainId    string  Required, network plane ID (UUID)
                      enable      bool    Required, whether to enable
                      trust       string  Required, trust mode, values: pcp / dscp (lowercase)
                      pcpTag      int     Optional, required when trust=pcp, range 0-7
                      dscpTag     int     Optional, required when trust=dscp, range 0-63
                      cnpPrio     int     Optional, RoCE scenario, range 0-7
                      cnpDscp     int     Optional, RoCE scenario, range 0-63
                    Example: {"domainId":"960d7a90-aad3-4f5c-b57f-5e3f61098ae2","enable":true,"trust":"dscp","dscpTag":46}
```

### Usage Example

```bash
# DSCP mode
acli network pfc create -d '{"domainId":"960d7a90-aad3-4f5c-b57f-5e3f61098ae2","enable":true,"trust":"dscp","dscpTag":46}'

# PCP mode (business plane, non-VS)
acli network pfc create -d '{"domainId":"ff348d34-e4ed-40bb-a0ab-0ba24523eda7","enable":true,"trust":"pcp","pcpTag":3}'

# With CNP fields (RoCE flow control scenario)
acli network pfc create -d '{"domainId":"960d7a90-aad3-4f5c-b57f-5e3f61098ae2","enable":true,"trust":"dscp","dscpTag":26,"cnpPrio":3,"cnpDscp":48}'
```

### Output Example

```bash
taskId: host-0050568ecad9:1703505443:0
```
