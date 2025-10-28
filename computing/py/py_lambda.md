---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Lambda
title: Funciones lambda en Python
---

# FUNCIÓN LAMBDA EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Revisar y rehacer toda la documentación, añadir más ejemplos, poner casos de uso etc.

> [!faq]- FAQ
> - [¿Qué es un if ternario?](py_conditionals.md#IF-TERNARIO)

Las [funciones](py_func.md) `lambda` tienen el mismo objetivo que una [función](py_func.md) normal, con la diferencia que esta se declara en una única línea, y su objetivo es realizar operaciones simples.

> [!abstract] SINTAXIS
> ***\[func_name]*** = lambda ***\[args]***: ***\[func_code]***

> [!note] Nota
> Una [función](py_func.md) `lambda` puede no tener *argumentos*.

```python
import os

# Se usa un if ternario.
cls = lambda: os.system("cls" if "nt" == os.name else "clear")
cubed = lambda x: x ** 3

cls()
print(cubed(3))
```
