---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OS
title: Módolo OS en Python
---

# OS

> [!fail] ESTA APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [Python Doc (os)](https://docs.python.org/3.11/library/os.html)

Para obtener el ancho y alto de caracteres en el terminal, podemos usar la [función](py_function.md) `get_terminal_size`.

---

La función `walk` crea una estructura de árbol respecto a un directorio.

## FUNCIONES

### CONTAR CPUS

La [función](py_function.md) `cpu_count` del [módulo](py_module.md) [`OS`](py_os.md) devuelve el un [`integer`](variables/py_int.md) indicando el número de procesadores lógicos que tienen la máquina en la que se está ejecutando el programa.

```python
import os

print(f"CPUs: {os.cpu_count()}")
```

### CWD

La [función](py_function.md) `getcwd` del [módulo](py_module.md) [`OS`](py_os.md) devuelve el un [`string`](variables/py_str.md) con la ruta desde la que se a ejecutado el primer archivo.

Imaginemos que tenemos la siguiente estructura de nuestro proyecto:

```txt
C:\
  └─\my_project
    ├─ main.py
    └─\modules
      └─ my_module.py
```

Si nos situamos en el directorio `my_project` y ejecutamos el archivo `main.py`, si este tiene el código:

```python
import os

print(os.getcwd())
# SALIDA:
# C:\my_project
```

Podremos ver como nos imprime la ruta en donde se encuentra el archivo, ahora si el código del archivo `main.py` es:

```python
from modules import my_module

my_module.my_func()
```

Y el código del archivo `my_module.py` es:

```python
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

Existe otra [función](py_function.md) similar que devuelve el mismo resultado en [bytes](variables/py_byte.md), esta es [`getcwdb`](#CWDB).

### CWDB

La [función](py_function.md) `getcwdb` del [módulo](py_module.md) [`OS`](py_os.md) devuelve el un [`bytes`](variables/py_byte.md) con la ruta desde la que se a ejecutado el primer archivo.

La [función](py_function.md) `getcwdb` funciona de la misma forma que la [función](py_function.md) [`getcwd`](#CWD), con la diferencia que esta en vez de devolver un valor de tipo [`string`](variables/py_str.md) devuelve una secuencia de [`bytes`](variables/py_byte.md) con la misma información.

En el caso de las contra barras (`\`) salen por duplicado en el caso de esta [función](py_function.md).

### SYSTEM

La [función](py_function.md) `system` del [módulo](py_module.md) [`OS`](py_os.md) recibe un argumento de tipo [`string`](variables/py_str.md), este [`string`](variables/py_str.md) lo ejecutará como un comando del sistema:

- [CMD](../../os/Windows/Windows_Commands.md)
- [TERMINAL](../../os/Unix/unix_commands.md)

```python
import os

clear = lambda: os.system("cls" if "nt" == os.name else "clear")

print("Esta es la primera impresión.")
clear()
print("Esta es la segudna impresión.")
```

En este ejemplo también se hace uso de la [variable](py_variable.md) [`name`](#NAME).

## VARIABLES

### NAME

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
