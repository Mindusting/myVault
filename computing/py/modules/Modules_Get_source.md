---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
title: Conseguir el código fuente de un módulo
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Para guardar el código fuente de un [módulo](../py_module.md) en un archivo que podamos consultar de forma fácil, podemos seguir el siguiente ejemplo:

```python
import random
import inspect
src = inspect.getsource(random)
with open("info_random.py", "w") as FILE:
    FILE.write(src)
```

El ver el código fuente de un [módulo](../py_module.md) permite por ejemplo, ver como funciona internamente la generación de números aleatorios, he copiado el mínimo código necesario para generar [números decimales](../py_float.md) aleatorios y lo he metido en una [función](../py_func.md):

```python
import os

def rand() -> float:
    BPF = 53 # Número de bits en los float
    RECIP_BPF = 2 ** -BPF
    return (int.from_bytes(os.urandom(7)) >> 3) * RECIP_BPF

for _ in range(10):
    print(rand())
```

>[!info]
>Cabe resaltar que ciertas [funciones](../py_func.md) no se encuentran en el [módulo](../py_module.md) de forma directa, como puede ser este caso, a medida que indaguemos en los [módulos](../py_module.md) nos encontraremos que faltan algunas [funciones](../py_func.md), esto es debido a que parte del código está escrito en [c](../../c/c.md) o [C++](../../cpp/cpp.md), por lo que, para acceder a ese código se hace de forma distinta.
