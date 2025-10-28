---
alias: Queue en Programación
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: FIFO en Programación
---

# FIFO EN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar como se hace un FIFO en C como ejemplo.

El término **FIFO** viene del inglés (*First In, First Out*), que significa, el primero en entrar es el primero en salir, esta estructura de datos también se llama **cola**, ya que al igual que en por ejemplo una cola de clientes, el primero en ser atendido (*Y por tanto salir de la cola*) es el primero que llegó, y el último en llegar el el último en salir.

![#center](drawing/fifo.md)

Este tipo de estructuras las podemos encontrar por ejemplo en [Python](../py/py.md):

```python
numbers: list = list()

numbers.append(3)
numbers.append(2)
numbers.append(5)

print(numbers.pop(0))
print(numbers.pop(0))
print(numbers.pop(0))
# SALIDA:
# 3
# 2
# 5
```
