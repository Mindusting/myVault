---
author: Mindusting
corrected: false
tags:
  - Programming/Python/OS
title: Función cpu_count del módulo OS en Python
---

La [función](../py_function.md) `cpu_count` del [módulo](../py_module.md) [`OS`](py_os.md) devuelve el un [`integer`](../variables/py_int.md) indicando el número de procesadores lógicos que tienen la máquina en la que se está ejecutando el programa.

```py
import os

print(f"CPUs: {os.cpu_count()}")
```
