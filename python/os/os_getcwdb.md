---
author: Mindusting
corrected: false
tags:
  - Programming/Python/OS
title: Función getcwd del módulo OS en Python
---

La [función](../py_function.md) `getcwdb` del [módulo](../py_module.md) [`OS`](py_os.md) devuelve el un [`bytes`](../variables/py_byte.md) con la ruta desde la que se a ejecutado el primer archivo.

La [función](../py_function.md) `getcwdb` funciona de la misma forma que la [función](../py_function.md) [`getcwd`](os_getcwd.md), con la diferencia que esta en vez de devolver un valor de tipo [`string`](../variables/py_str.md) devuelve una secuencia de [`bytes`](../variables/py_byte.md) con la misma información.

En el caso de las contra barras (`\`) salen por duplicado en el caso de esta [función](../py_function.md).
