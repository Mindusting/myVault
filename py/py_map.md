---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Map
title: Map en Python
---

# CLASE MAP 🗺️

>[!fail]- ESTE APARTADO ESTÁ INCOMPLETO

```python
my_list = [
    "1",
    "22",
    "333",
    "4444",
    "55555"
]

nums = [1, 2, 3, 4]

res = map(lambda x: x + x, nums)
print(list(res))

res = map(lambda e: f"{len(e)}: {e}", my_list)

for e in res:
    print(e)
print(list(e))

```
