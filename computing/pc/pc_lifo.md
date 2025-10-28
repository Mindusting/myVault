---
alias: Stack en Programación
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: LIFO en Programación
---

# LIFO EN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar como se hace un LIFO en C como ejemplo.

El termino **LIFO** viene del inglés (*Last In, Firs Out*), que significa, el último en entrar es el primero en salir, esta estructura de datos también se le llama **stack** (*Significa "pila", como puede ser una pila de platos*), esta estructura de datos en forma de pila sigue la misma lógica que una de la vida real, en el sentido en el que cuando nosotros tenemos una pila de platos si queremos usar uno, cogemos el que está arriba del todo y cuando queremos añadir un nuevo plato a la pila, lo ponemos encima de esta, de esta forma, el último plato que hemos añadido a la pila, es el primero que quitamos de ella.

![#center](drawing/lifo.md)

Este tipo de estructuras las podemos encontrar por ejemplo en [Python](../py/py.md):

```python
numbers: list = list()

numbers.append(3)
numbers.append(2)
numbers.append(5)

print(numbers.pop())
print(numbers.pop())
print(numbers.pop())
# SALIDA:
# 5
# 2
# 3
```
