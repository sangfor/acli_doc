---
sidebar_position: 1
---

# vm_start

### Overview

VM start failure detection

### Command Parameters

```bash
-i|--vmid=string              Required parameter, faulty vmid, example: 6025407369236
-t|--time=string              Check date, default today, format: YYYY-MM-DD, example: 2026-01-01
-v|--version                  Display current plugin version information
-h|--help                     Display help information for current command
```

### Usage Example

```bash
# Example 1: Check the start status of a specified virtual machine
acli vm_start -i 6025407369236

# Example 2: Check the start status of a specified virtual machine (specify date)
acli vm_start -i 6025407369236 -t 2026-01-01

# Example 3: Display plugin version information
acli vm_start -v

# Example 4: Display help information
acli vm_start --help
```

### Output Example

```bash
-------------------------------------------------------------------------[No VM Start Failure Task - Routine Troubleshooting Process]-------------------------------------------------------------------------
  Target check group [Check VM running storage (virtual storage) abnormality] pre-check: Failed, skip target check group
  Target check group [Check VM running storage (other storage) abnormality] pre-check: Passed, execute target check group
  Target check group [Check VM start or restart stuck] pre-check: Failed, skip target check group
  Target check group [VM start task completed but stuck] pre-check: Passed, execute target check group
  Target check group [Check service abnormality] pre-check: Failed, skip target check group
Task plan:
  1. Execute [Check VM running storage (other storage) abnormality]
  2. Execute [VM start task completed but stuck]
  3. Execute [Check VM running host abnormality]

-------------------------------------------------------------------------[Check VM running storage (other storage) abnormality]-------------------------------------------------------------------------
  Target check group [Insufficient storage space] pre-check: Passed, execute target check group
Task plan:
  1. Execute [Insufficient storage space]
  2. Execute [External storage hardware link abnormality]
  3. Execute [External storage directory split-brain]
  4. Execute [sffs cluster lock 208 error]

-----------------------------------------------------------------------------------[Insufficient storage space]-----------------------------------------------------------------------------------
Pre-check: (None)
Task plan:
  1. Execute [Insufficient capacity]
  Execute check item: Insufficient capacity
    10.131.136.156: Normal - Info: [acli][External storage hardware link check] Check passed, no storage usage exceeds 90%

-------------------------------------------------------------------------------[External storage hardware link abnormality]-------------------------------------------------------------------------------
Pre-check: (None)
Task plan:
  1. Execute [Optical module/fiber/HBA has CRC or optical attenuation]
  2. Execute [Optical module/HBA compatibility]
  Execute check item: Optical module/fiber/HBA has CRC or optical attenuation
    10.131.136.156: Normal - Info: [acli][External storage hardware link check] External storage has no CRC errors or optical attenuation
```
