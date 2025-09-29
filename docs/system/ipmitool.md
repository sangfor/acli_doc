---
sidebar_position: 10
---

# ipmitool
操作概述: 调用系统ipmitool命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system ipmitool
```

结果示例:
```bash
ipmitool version 1.8.17

usage: ipmitool [options...] <command>

       -h             This help
       -V             Show version information
       -v             Verbose (can use multiple times)
       -c             Display output in comma separated format
       -d N           Specify a /dev/ipmiN device to use (default=0)
       -I intf        Interface to use
       -H hostname    Remote host name for LAN interface
       -p port        Remote RMCP port [default=623]
       -U username    Remote session username
       -f file        Read remote session password from file
       -z size        Change Size of Communication Channel (OEM)
       -S sdr         Use local file for remote SDR cache
       -D tty:b[:s]   Specify the serial device, baud rate to use
                      and, optionally, specify that interface is the system one
       -4             Use only IPv4
       -6             Use only IPv6
       -a             Prompt for remote password
       -Y             Prompt for the Kg key for IPMIv2 authentication
       -e char        Set SOL escape character
       -C ciphersuite Cipher suite to be used by lanplus interface
       -k key         Use Kg key for IPMIv2 authentication
       -y hex_key     Use hexadecimal-encoded Kg key for IPMIv2 authentication
       -L level       Remote session privilege level [default=ADMINISTRATOR]
                      Append a '+' to use name/privilege lookup in RAKP1
       -A authtype    Force use of auth type NONE, PASSWORD, MD2, MD5 or OEM
       -P password    Remote session password
       -E             Read password from IPMI_PASSWORD environment variable
       -K             Read kgkey from IPMI_KGKEY environment variable
       -m address     Set local IPMB address
       -b channel     Set destination channel for bridged request
       -t address     Bridge request to remote target address
       -B channel     Set transit channel for bridged request (dual bridge)
       -T address     Set transit address for bridge request (dual bridge)
       -l lun         Set destination lun for raw commands
       -o oemtype     Setup for OEM (use 'list' to see available OEM types)
       -O seloem      Use file for OEM SEL event descriptions
       -N seconds     Specify timeout for lan [default=2] / lanplus [default=1] interface
       -R retry       Set the number of retries for lan/lanplus interface [default=4]
```