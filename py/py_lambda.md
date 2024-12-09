---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Lambda
title: Funciones lambda en Python
---

# LAMBDA

> [!faq] FAQ
> - [¿Qué es un if ternario?](py_flow_control.md#IF-TERNARIO)

Las [funciones](py_function.md) `lambda` tienen el mismo objetivo que una [función](py_function.md) normal, con la diferencia que esta se declara en una única línea, y su objetivo es realizar operaciones simples.

> [!abstract] SINTAXIS
> ***\[func_name]*** = lambda ***\[args]***: ***\[func_code]***

> [!note] Nota
> Una [función](py_function.md) `lambda` puede no tener *argumentos*.

```python
import os

# Se usa un if ternario.
cls = lambda: os.system("cls" if "nt" == os.name else "clear")
cubed = lambda x: x ** 3

cls()
print(cubed(3))
```
