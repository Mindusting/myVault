---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
title: Crear módulos en Python
---

A parte de los módulos de Python también podemos crear nuestros propios módulos, para ello deberemos crear un archivo, de momento lo haremos en el directorio activo (El mismo directorio donde se encuentra nuestro archivo principal).

>[!quote] ESTRUCTURA DE DIRECTORIO
>```txt
>main.py
>trigonometry.py
>```

Contenido del archivo: `main.py`
```python
from trigonometry import distance as dis

print(dis(3, 4))
```

Contenido del archivo: `trigonometry.py`
```python
from math import sqrt

def distance(x: float, y: float) -> float:
    return sqrt(pow(x, 2) + pow(y, 2))
```

En este ejemplo se puede ver como desde el archivo “main.py” se importa la [función](../py_function.md) `distance` del módulo `trigonometry` y el contenido de este módulo está en el archivo `trigonometry.py`.
