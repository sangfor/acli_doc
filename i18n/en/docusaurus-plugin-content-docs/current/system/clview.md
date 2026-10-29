---
sidebar_position: 1
---

# clview

### Overview

Inspect heartbeat headers, heartbeat blocks, lock blocks on a device, and lock holders of a file.

### Command Parameters

Command format:

```bash
acli system clview [OPTION]* DEVICE
```

`DEVICE` is required and specifies the device to query, for example, `/dev/sdc`. Refer to the tool's help output below for option descriptions.

Data is displayed in hexadecimal and decimal formats. Pay attention to status information in parentheses, such as `right`, `wrong`, `free`, `sh`, and `ex`.

### Usage Example

```bash
acli system clview
```

### Output Example

When no device is specified, the following message and help are returned. `cl_tool_view` is the underlying tool name:

```text
No device specified
Usage: cl_tool_view [OPTION]* DEVICE

Options:
  -p, --pno=N                The address of disk, it's unit is m.
  -s, --sector=N             Read N-th sector (default: 4096)
  -n, --count=N             how many sectors to show(default: 1)
  -t, --type=TYPE           The type of the block data. There are three values, h(heartbeat header), b(heartbeat block), l(lock block). If it is not specified, the application will judge it based on sector block data by self
  -q, --query-lock-holders    Query the lock-holders of the given file
  -h, --help                 Show this message and exit

It uses two types of formats to display data, hexadecimal and decimal. And you need to note the parentheses prompted state information, such as "right" or "wrong", "free", "sh", "ex" and so on.

Simple example: Read the third sector block data on /dev/sdc
  cl_tool_view -s 3 /dev/sdc
```
