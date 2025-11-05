---
sidebar_position: 10
---
 
# set
操作概述: 过载保护功能相关维护操作
 
命令参数: 
```bash
-i|--isolation=boolean     必要参数，紧急触发过载保护中的隔离和解除隔离操作，枚举值：true(触发隔离)、false(解除隔离)。仅可用于临时调整，调整后loadman仍会根据主机CPU负载情况触发对应操作
```
 
使用示例:
```bash
acli service asv loadman maintenance set -i false
```
 
结果示例:
```bash
code: 0
message: urgent operation completed successfully
```