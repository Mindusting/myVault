---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Random
title: Random en Python
---

# RANDOM

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo]
> > - [ ] Explicar qué son los números pseudoaleatorios.
> > - [ ] Explicar qué son los las semillas.

> [!help] REFERENCIAS WEB
> - [Python doc (Random)](https://docs.python.org/es/3/library/random.html)
> - [W3 (Random)](https://www.w3schools.com/python/module_random.asp)

El [módulo](py_module.md) **random** contiene varias [funciones](py_function.md), pero en esta documentación solo veremos la [clase](py_class.md) `Random`, y sus utilidades, pero para ello primero deberemos importarla:

```python
from random import Random
```

Para crear un objeto `Random` tenemos que seguir la siguiente sintaxis, en donde el argumento `seed` es opcional.

> [!abstract] SINTAXIS
> Random(***\[seed]***)

```python
rng: Random = Random()
```

## MÉTODOS DE LA CLASE RANDOM

- `random`: devuelve un [float](py_float.md) aleatorio.
- `seed([seed])`: establece el valor indicado como nueva semilla del generador de números aleatorios.
- `choice([iterable])`: se el da como argumento un *iterable* y devuelve un *elemento* aleatorio de este.
- `shuffle([iterable])`: desordena el *iterable* que se le pasa como argumento.
