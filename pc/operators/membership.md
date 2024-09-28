---
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Operadores de membresía
---

El operador de membresía indica si un valor u objeto se encuentra dentro de un iterable, como se puede ver en el próximo ejemplo, se usa este operador para comprobar si el valor `2` se encuentra dentro de la lista.

```py
x = [3, 2, 7]
y = 2

print(f"{y in x = }")

""" RESULTADO:
y in x = True
"""
```

También existe la posibilidad de usa el operador `not`, invirtiendo el resultado de este.

```py
x = [3, 2, 7]
y = 2

print(f"{y not in x = }")

""" RESULTADO:
y not in x = False
"""
```

%%
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
in y not in son operadores de pertenencia.
in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
%%
