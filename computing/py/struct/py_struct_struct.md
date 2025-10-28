---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Struct
title: Clase Struct del módulo Struct en Python
---

# CLASE STRUCT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!abstract] SINTAXIS
> Struct(***\[formas\]***)

```python
from struct import Struct

s_user: Struct = Struct("B8sB")

print(s_user.pack(1, bytes("Adelio", encoding="ascii"), 20))
print(s_user.pack(2, bytes("Adelia", encoding="ascii"), 22))
# SALIDA:
# b'\x01Adelio\x00\x00\x14'
# b'\x02Adelia\x00\x00\x16'
```
