---
slug: /
sidebar_position: 1
title: aCLI Troubleshooting
sidebar_label: Introduction
---

## Welcome to aCLI Troubleshooting CLI Tool

Welcome to the aCLI troubleshooting service command-line tool. aCLI (Admin CLI) is a command-line troubleshooting tool specifically designed for the HCI platform, aiming to provide technical support and operation and maintenance personnel with convenient and efficient means for system diagnosis and problem resolution. By encapsulating complex underlying operations, aCLI provides a standardized command interface, making troubleshooting more standardized and efficient.

```shell
support/host-005056b237a6(acli) ~ # acli --help
Usage: aCLI [parameter] {namespace}+ {command} [command parameter]

Parameters:
  --help, -?           Display tool usage
  --version            Display version information
  --debug              Enable debug logs
  --cluster            Traverse all nodes in the cluster to execute the aCLI command
  --timeout            Set the command timeout (seconds)
  --force              Force Mode: Bypasses interactive confirmation and executes operations directly (please confirm the risks before use).
  --formatter          Parameters for command formatting. Enumeration values: xml, csv, keyvalue, json
  --container          Specify the global container for commands, applicable only to commands under the system. Enumeration values: asv-con, vn-con, vn-agent, vs-cp-manager


Available namespaces:
  acli                 aCLI description. Provide additional information to users.
  alert                Alert commands
  task                 Task commands
  log                  Log related commands
  service              Service related commands
  system               System commands
  vm                   VM commands
  network              Network commands
  storage              Storage commands
  platform             Platform commands
  plugin               Plugin lifecycle related commands
  hardware             Hardware commands
```

---

TODO 待更新