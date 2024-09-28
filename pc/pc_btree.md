---
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Árbol binario en programación
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

# VÍDEO TUTORIALES

[Spanning Tree](https://youtu.be/K1a2Bk8NrYQ)

# B-TREE

Un árbol binario es similar a las [listas](pc_list.md) en el sentido de que sirven para guardar valores, pero su comportamiento cambia bastante.

Los árboles binarios tienen las siguientes características:

- Se pueden guardar elementos siempre y cuando no se repitan.
- Se pueden borrar elementos.
- No está indexado.
- Se pueden hacer consultas de si existe o no un elemento.

---

```py
from time import time

def find(value, set_lits):
    i_init: int = 0
    i_end:  int = len(set_lits)

    max_i_init: int = i_end - 1
    max_i_end:  int = 0

    while True:
        i_cursor: int = (i_end - i_init) // 2 + i_init
        if set_lits[i_cursor] == value:
            return True
        elif value < set_lits[i_cursor]:
            i_end = i_cursor
        else:
            i_init = i_cursor
        if i_init == max_i_init or i_end == max_i_end:
            return False


y = 9999999
x = [i for i in range(y)]

old_time = time()
y in x
print(time() - old_time)

old_time = time()
find(y, x)
print(time() - old_time)
```
