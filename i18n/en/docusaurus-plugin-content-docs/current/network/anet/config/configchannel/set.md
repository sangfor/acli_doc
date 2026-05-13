---
sidebar_position: 1
---

# set

### Overview

Set network configuration channel detection module settings

### Command Parameters
```bash
-p|--periodic-detect-enable=boolean    Enable scheduled detection for network configuration channel, Example: true to enable, false to disable
-r|--recovery-enable=boolean           Enable automatic recovery for network configuration channel, Example: true to enable, false to disable
-a|--alert-enable=boolean              Enable alarm notifications for network configuration channel, Example: true to enable, false to disable
```

### Usage Example

```bash
acli network anet config configchannel set --periodic-detect-enable false --recovery-enable true --alert-enable true
```

### Output Example

```bash
periodicDetectEnable: false
recoveryEnable: true
alertEnable: true
```