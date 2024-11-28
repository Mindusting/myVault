---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Loop
title: Bucle infinito en Python
---

Para hacer un bucle que se esté repitiendo de forma indefinida tendremos que hacer un bucle [`while`](py_while.md) con la condición valiendo siempre [`True`](../variables/py_bool.md):

```python
while True:
    print("Hola mundo!!!")
```

Por supuesto este bucle siempre se puede romper con un [`break`](py_break.md), o forzando el fin del programa, el crear un bucle infinito no implica que se nos vaya a quedar colgado el ordenador.
