---
author: Mindusting
corrected: false
tags:
  - Programming/Python/OS
title: Función system del módulo OS en Python
---

La [función](../py_function.md) `system` del [módulo](../py_module.md) [`OS`](py_os.md) recibe un argumento de tipo [`string`](../variables/py_str.md), este [`string`](../variables/py_str.md) lo ejecutará como un comando del sistema:

- [CMD](../../os/Windows/Windows_Commands.md)
- [TERMINAL](../../os/Unix/unix_commands.md)

```py
import os

clear = lambda: os.system("cls" if "nt" == os.name else "clear")

print("Esta es la primera impresión.")
clear()
print("Esta es la segudna impresión.")
```

En este ejemplo también se hace uso de la [variable](../py_variable.md) [`name`].
