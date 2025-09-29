---
sidebar_position: 10
---

# dmidecode
操作概述: 调用系统dmidecode命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system dmidecode
```

结果示例:
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