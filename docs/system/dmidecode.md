---
sidebar_position: 1
---

# dmidecode

### 操作概述

dmidecode 命令，读取并展示 DMI/SMBIOS 硬件信息（只读，禁止把 DMI 数据转储为文件）。

### 命令参数

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-u|--dump            禁止参数，把 DMI 数据转储为二进制文件（写操作），拒绝执行
--dump-bin=<file>    禁止参数，把 DMI 数据转储为二进制文件（写操作），拒绝执行；
                     因 GNU getopt 支持唯一前缀缩写，--du 开头的写法（--du / --dum / --dump）同样命中拒绝；
                     注意 --dev-mem 不受影响（其最短唯一前缀为 --de）
```

### 使用示例

```bash
acli system dmidecode
```

### 结果示例

```bash
# dmidecode 3.4
Getting SMBIOS data from sysfs.
SMBIOS 2.7 present.
620 structures occupying 29188 bytes.
Table at 0x000E0010.

Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
        Vendor: Phoenix Technologies LTD
        Version: 6.00
        Release Date: 11/12/2020
        Address: 0xEA480
        Runtime Size: 88960 bytes
        ROM Size: 64 kB
        Characteristics:
                ISA is supported
                PCI is supported
                PC Card (PCMCIA) is supported
                PNP is supported
                APM is supported
                BIOS is upgradeable
                BIOS shadowing is allowed
                ESCD support is available
                Boot from CD is supported
                Selectable boot is supported
                EDD is supported
                Print screen service is supported (int 5h)
                8042 keyboard services are supported (int 9h)
                Serial services are supported (int 14h)
                Printer services are supported (int 17h)
                CGA/mono video services are supported (int 10h)
                ACPI is supported
                Smart battery is supported
                BIOS boot specification is supported
                Function key-initiated network boot is supported
                Targeted content distribution is supported
        BIOS Revision: 4.6
        Firmware Revision: 0.0
```