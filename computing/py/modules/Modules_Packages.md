---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
title: Paquetes en Python
---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

[Curso de Python. Paquetes. Vídeo 35](https://youtu.be/nRieWujis4s?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

Un paquete en Python no es más que un directorio (Carpeta) con módulos en su interior.

En este caso tenemos en el directorio activo el archivo `main.py` y el directorio (Carpeta) `modules`, dentro de esta nos encontramos los archivos `__init__.py`, `ask.py` y `console.py`, los cuales serán los módulos que importaremos desde el archivo `main.py`.

> [!quote] ESTRUCTURA DE DIRECTORIO
> ```txt
> /.
> ├─ main.py
> └─/modules
>   ├─ __init__.py
>   ├─ ask.py
>   └─ console.py
> ```

```txt
/src
├─ main.py
├─/popos
| ├─ __init__.py
| └─ user.py
└─/managers
  ├─ __init__.py
  └─ userManager.py
```

Contenido del archivo: `main.py`
```python
from modules.ask import ask_int
from modules.console import clear

clear()

x = ask_int("Valor de X")
y = ask_int("Valor de Y")

clear()

print(f"{x} + {y} = {x + y}")
```

Contenido del archivo: `__init__.py`
```python
import ask
import console

print("Se ha realizado una importación del paquete \"modules\".")
```

Contenido del archivo: `__init__.py`
```python
############
# ASK BOOL #
############

def ask_bool(question: str) -> bool:
    answer = input(f"{question} [Y/N]: ")
    match answer.upper():
        # TRUE
        case "YES":   return True
        case "Y":     return True
        case "SI":    return True
        case "S":     return True
        case "TRUE":  return True
        case "T":     return True
        case "1":     return True

        # FALSE
        case "NO":    return False
        case "N":     return False
        case "FALSE": return False
        case "F":     return False
        case "0":     return False

        # NONE
        case _:
            print(f"\"{answer}\" is not bool value")

#############
# ASK FLOAT #
#############

def ask_float(question: str) -> float:
    while True:
        answer = input(f"{question} [float]: ")
        try:
            return float(answer.replace(",", "."))
        except ValueError:
            print(f"\"{answer}\" is not float value.")

###########
# ASK INT #
###########

def ask_int(question: str) -> int:
    while True:
        answer = input(f"{question} [int]: ")
        try:
            return int(answer)
        except ValueError:
            print(f"\"{answer}\" is not int value.")

```

Contenido del archivo: `console.py`
```python
from os import (
    name   as __name,
    system as __system
)

# CLEAR CONSOLE
clear = lambda: __system("cls" if "nt" == __name else "clear")
```

Como se puede ver en el ejemplo, desde el archivo `main.py` indicamos que queremos importar dos módulos que se encuentran en el paquete `modules`, poniendo el nombre de este, seguido de un punto y el nombre del módulo, y dentro de estos se importan las [funciones](../py_function.md) `ask_int` y `clear`, pero hay que tener una cosa en cuenta, para que Python en tienda que el directorio `modules` es un paquete se ha añadido dentro de este el archivo `__init__.py` el cual contiene el código que queremos que se ejecute cuando se hace uso de este paquete, en este ejemplo simplemente imprime un mensaje en consola para mostrar el funcionamiento de este.

# ESTRUCTURA DE RUTAS DE PAQUETES

En el apartado anterior hemos visto cómo importar módulos de un paquete que se encuentra dentro del directorio activo, pero…

¿Qué pasaría si quisiéramos importar desde un módulo que se encuentra dentro de un paquete, a otro módulo que se encuentra dentro de otro paquete?

Para esto, primero debemos entender que representa el punto entre los nombre de los paquetes y módulos a la hora de importar uno, bien pues cuando ponemos un solo punto estamos indicando el directorio actual, a partir de ahí cada punto que pongamos indicará el directorio padre, por lo que si ponemos dos punto indica el directorio padre, y sí ponemos tres, indicamos el directorio padre del padre.

>[!quote] ESTRUCTURA DE DIRECTORIO
```txt
.
├─ main.py
├─/dir_a
│ ├─/dir_a1
│ │ ├─ __init__.py
│ │ └─ archivo_a1.py
│ ├─ __init__.py
│ └─ archivo_a.py
└─/dir_b
  ├─ __init__.py
  └─ archivo_b.py
```

Si desde el archivo `archivo_a1.py` quisiéramos importar el módulo `archivo_b.py`, tendríamos que hacerlo de la siguiente forma.

Contenido del archivo: `archivo_a1.py`
```python
from ...dir_b.archivo_b import mi_funcion
```

## PAQUETES REDISTRIBUIDOS

[Curso de Python. Paquetes distribuibles. Vídeo 36](https://youtu.be/Zf9sN-w0BVE?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

>[!fail] Este apartado está incompleto, intentaremos completarlo lo antes posible, disculpen las molestias.
