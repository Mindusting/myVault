---
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Operadores de identidad
---

El operador de identidad compara el contenido de dos variables, si el contenido de estos es el mismo objeto, el resultado será `true`.

```py
x = [3, 2, 7]
y = x
z = [3, 2, 7]

print(f"{x is y = }")
print(f"{x is z = }")

""" RESULTADO:
x is y = True
x is z = False
"""
```

También existe la posibilidad de usa el operador `not`, invirtiendo el resultado de este.

```py
x = [3, 2, 7]
y = x

print(f"{x is not y = }")

""" RESULTADO:
x is not y = False
"""
```

%%
Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.
is y is not son operadores de identidad.
is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.
is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.
Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.
%%
