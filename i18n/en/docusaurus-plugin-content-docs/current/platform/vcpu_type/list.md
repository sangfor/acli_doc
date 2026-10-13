---
sidebar_position: 1
---

# list

### Overview

List supported and all vCPU models of the cluster

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli platform vcpu_type list
```

### Output Example

```bash
{
  "all_vcpu": [
    {
      "description": "The basic feature set of Intel Core 2 Duo processors will be used as the default vCPU feature set of newly created VMs. Nodes with the following types of processors can be added to the cluster: Intel Merom (Xeon Core 2), Intel Penryn (Xeon 45nm Core 2), Intel Nehalem (Xeon Core i7), Intel Westmere (Xeon 32nm Core i7), Intel Sandy Bridge, Intel Ivy Bridge, Intel Haswell, Intel Broadwell, Intel Skylake, Intel Cascade Lake, Intel Ice Lake, Intel Sapphire Rapids, and future Intel processors.",
      "vcpu": "core2duo"
    },
    {
      "description": "The basic feature set of Intel Haswell processors will be used as the default vCPU feature set of newly created VMs. Nodes with the following types of processors can be added to the cluster: Intel Haswell, Intel Broadwell, Intel Skylake, Intel Cascade Lake, Intel Ice Lake, Intel Sapphire Rapids, and future Intel processors. Compared with the Intel Core 2 Duo mode, the Intel Haswell mode provides more CPU features, including RDRAND, MOVBE, INVPCID, XSAVEOPT, PCLMULQDQ, ARAT, AVX2, MAC, and TSX.",
      "vcpu": "Haswell-noTSX"
    },
    {
      "description": "The basic feature set of Intel Cascade Lake processors will be used as the default vCPU feature set of newly created VMs. Nodes with the following types of processors can be added to the cluster: Intel Cascade Lake, Intel Ice Lake, Intel Sapphire Rapids, and future Intel processors. Compared with the Intel Haswell mode, the Intel Cascade Lake mode provides more CPU features, including PDPE1GB, RDSEED, CLWB, VNNI, TSX, SMAP, PREFETCHW, AVX-512, PMem, MPK, XSAVEC, XSAVE, and XGETBV with ECX = 1.",
      "vcpu": "Cascadelake-Server-noTSX"
    },
    {
      "description": "The basic feature set of Intel Ice Lake processors will be used as the default vCPU feature set of newly created VMs. Nodes with the following types of processors can be added to the cluster: Intel Ice Lake, Intel Sapphire Rapids, and future Intel processors. Compared with the Intel Cascade Lake mode, the Intel Ice Lake mode provides more CPU features, including SHA extensions, Vectorized AES, UMIP, Read Processor ID, Fast Short REP MOV, WBNOINVD, GFNI, AVX512_IFMA, Vectorized Bit Manipulation, and Bit Algorithms Instructions.",
      "vcpu": "Icelake-Server-v4"
    }
  ],
  "supported_vcpu": [
    "core2duo",
    "Haswell-noTSX",
    "Cascadelake-Server-noTSX"
  ],
  "vcpu_unsupported_nodes": {
    "Icelake-Server-v4": [
      {
        "nodeid": "host-0050568e74c8",
        "nodeip": "10.131.136.197",
        "nodename": "10.131.136.197"
      },
      {
        "nodeid": "host-0050568ec35e",
        "nodeip": "10.131.137.114",
        "nodename": "10.131.137.114"
      },
      {
        "nodeid": "host-0050568e3fe4",
        "nodeip": "10.131.137.124",
        "nodename": "10.131.137.124"
      }
    ]
  }
}
```
