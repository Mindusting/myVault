---
author: Mindusting
corrected: false
tags:
  - Programming/Python/OS
title: Función getcwd del módulo OS en Python
---

La [función](../py_function.md) `getcwd` del [módulo](../py_module.md) [`OS`](py_os.md) devuelve el un [`string`](../variables/py_str.md) con la ruta desde la que se a ejecutado el primer archivo.

Imaginemos que tenemos la siguiente estructura de nuestro proyecto:

```txt
C:\
  └─\my_project
    ├─ main.py
    └─\modules
      └─ my_module.py
```

Si nos situamos en el directorio `my_project` y ejecutamos el archivo `main.py`, si este tiene el código:

```py
import os

print(os.getcwd())
# SALIDA:
# C:\my_project
```

Podremos ver como nos imprime la ruta en donde se encuentra el archivo, ahora si el código del archivo `main.py` es:

```py
from modules import my_module

my_module.my_func()
```

Y el código del archivo `my_module.py` es:

```py
import os

def my_func() -> None:
    print(os.getcwd())
    # SALIDA:
    # C:\my_project
```

Como se puede ver el resultado es el mismo, ya que lo que devuelve esta función, es la ruta hasta el primer archivo que se ha ejecutado del programa.

---

Lo mismo se aplicaría para [Unix](../../os/Unix/Unix.md), con la deferencia que en este caso, en vez de **contra barras** (`\`) es con **barras** (`/`). 

```txt
/
└─/my_project
  ├─ main.py
  └─/modules
    └─ my_module.py
```

---

Existe otra [función](../py_function.md) similar que devuelve el mismo resultado en [bytes](../variables/py_byte.md), esta es [`getcwdb`](os_getcwdb.md).
