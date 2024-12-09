---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Threading
title: Threading en Python
---

# THREADING

> [!help] REFERENCIAS WEB
> - [Python](https://docs.python.org/3/library/threading.html)
> 
> YouTube:
> - [Bro Code](https://youtu.be/STEOavXqXkQ)
> - [Dave's Space](https://youtu.be/AZnGRKFUU0c)

Para poder crear **hilos** en Python tendremos que importar el [módulo](py_module.md) `threading`:

```python
import threading
```

En esta documentación solo veremos como usar la [clase](py_class.md) `Thread`, por lo que la tendremos que importar de la siguiente forma:

```python
from threading import Thread
```

## CLASE THREAD

Para crear un **hilo** con la [clase](py_class.md) `Thread` tendremos que darle algunos **argumentos**, de los cuales, el primero listado es el obligatorio:

- `target`: nombre de la [función](py_function.md) a ejecutar en el hilo.
- `args`: [tupla](py_tuple.md) con los argumentos que se le debe pasar a la [función](py_function.md) indicada en `target`.
- `kwargs`: [diccionario](py_dict.md) que se le pasará a la [función](py_function.md) indicada en `target`.
- `name`: [string](py_str.md) usado para identificar el **hilo**.
- `daemon`: [booleano](py_bool.md) indicando si el de tipo demonio.

```python
# Importación de los módulos.
from threading import Thread
import time

# Declaración de diferentes funciones.
def f1():
    time.sleep(1)
    print("f1")

def f2():
    time.sleep(2)
    print("f2")

def f3():
    time.sleep(3)
    print("f3")

# Creación de tres hilos.
th1 = Thread(target=f1)
th2 = Thread(target=f2)
th3 = Thread(target=f3)

# Inicio de los tres hilos.
th1.start()
th2.start()
th3.start()

# Espera la finalización de los hilos.
th1.join()
th2.join()
th3.join()

print("Fín de todos los hilos.")

```

### MÉTODOS DE THREAD

Los objetos de tipo `Thread` tienen varios [métodos](py_function.md), veremos los más importantes:

- `start`: hace que comience el proceso de ejecución del hilo.
- `is_alive`: devuelve un valor [booleano](py_bool.md) indicando si sigue vivo (*Si está vivo es que no ha terminado*).
- `join`: la ejecución del programa se detiene hasta que el hilo termine de ejecutarse.
