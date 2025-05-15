---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Swith en Python
---

# SWITCH EN PYTHON

> [!help]- REFERENCIAS WEB
> - [El libro de Python](https://ellibrodepython.com/switch-python)

En Python no existe como tal el *switch*, pero gracias a los [diccionarios](py_dict.md) y/o las [listas](py_list.md) podemos recrear la estructura *switch*:

## SWITCH CON DICCIONARIO

A la hora de crear un *switch* lo más seguro es que terminemos usando esta opción de usar el [diccionario](py_dict.md) ya que es más versátil, las claves del serán las opciones del *switch* mientras que en los valores guardaremos las referencias a las funciones que queremos que se ejecute cuando coincida en la condición del *switch*:

El tiempo de complejidad para encontrar el caso de búsqueda es `O(log n)`.

```py
def main() -> None:
    print(switch("pitagoras", 3, 4)())
    print(switch("normalize", 3, 2)())
    print(switch("sum", 3, 2)())
    # SALIDA:
    # 1.9036539387158786
    # (1.0, 0.6666666666666666)
    # None

def switch(operator: str, a: float, b: float):
    return { # Opciones del switch
        "pitagoras": lambda: pitagoras(a, b),
        "normalize": lambda: normalize(a, b),
    }.get(operator, lambda: None) # Default


def pitagoras(dx: float, dy: float) -> float:
    return ((dx * dx) + (dy * dy)) ** 0.2


def normalize(dx: float, dy: float) -> tuple:
    max_value: float = max(dx, dy)
    return (dx / max_value, dy / max_value)


main()
```

## SWITCH CON LISTA

Para crear un *switch*, tenemos una forma alternativa y es a través de de una [lista](py_list.md) (*se puede sustituir la [lista](py_list.md) con una [tupla](py_tuple.md)*), en este caso los valores a buscar solo podrán ser [números enteros](py_int.md) consecutivos.

El tiempo de complejidad para encontrar el caso de búsqueda es `O(1)`.

```py
def main() -> None:
    print(switch(0, 3, 4)())
    print(switch(1, 3, 2)())
    print(switch(2, 3, 2)())
    # SALIDA:
    # 1.9036539387158786
    # (1.0, 0.6666666666666666)
    # None


def switch(option: int, a: float, b: float):
    cases: list = [ # Opciones del switch
        lambda: pitagoras(a, b),
        lambda: normalize(a, b),
    ]
    # Default
    return cases[option] if option < len(cases) else lambda: None


def pitagoras(dx: float, dy: float) -> float:
    return ((dx * dx) + (dy * dy)) ** 0.2


def normalize(dx: float, dy: float) -> tuple:
    max_value: float = max(dx, dy)
    return (dx / max_value, dy / max_value)


main()
```
