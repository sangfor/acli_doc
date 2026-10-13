---
sidebar_position: 1
---

# list

### Overview

List fault domains

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli network faultdomain list
```

### Output Example

```bash
{
  "fault_domains": [
    {
      "id": "0671d49e-388d-47f0-b556-bdd5b4ef0185",
      "name": "test-fault-domain",
      "type": "storage",
      "revision_number": 1,
      "hosts": [
        {
          "id": "8976be83-beaf-4b93-8a3a-ea5165e15197",
          "hostids": [
            "host-105056913a04",
            "host-105056913a05"
          ]
        },
        {
          "id": "9976be83-beaf-4b93-8a3a-ea5165e15198",
          "hostids": [
            "host-105056913a06",
            "host-105056913a07"
          ]
        }
      ]
    }
  ]
}
```
