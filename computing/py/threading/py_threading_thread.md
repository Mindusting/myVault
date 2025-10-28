---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Threading
title: Hilos en Python
---

# HILOS EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> No me gusta como ha quedado la documentación, quiero volver a hacerla, hacer mejores ejemplos, una explicación más extensa, etc.
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué son los hilos en programación?](../../pc/pc_thread.md)

Para crear un **hilo** con la [clase](py_class.md) `Thread` tendremos que darle algunos **argumentos**, de los cuales, el primero listado es el obligatorio:

> [!abstract] SINTAXIS
> Thread(target=**\[target\]**)

- `target`: referencia a la [función](../py_func.md) que ejecutará el hilo una vez se haya iniciado.
- `args`: es una [tupla](py_tuple.md) con los argumentos posicionales que se le debe pasar a la [función](../py_func.md) indicada en `target`.
- `kwargs`: es un [diccionario](py_dict.md) con los argumentos por nombre que se le debe pasar a la [función](../py_func.md) indicada en `target`.
- `name`: es un [string](py_str.md) usado para identificar el **hilo**.
- `daemon`: es un [booleano](py_bool.md) indicando si el de tipo *demonio*.

## DEMONIOS

Los **hilos** de tipo *demonio* son aquellos que se ejecutan como servicio, es decir, que cuando todos los **hilos** que no sean de tipo *demonio* terminen su ejecución, se detendrá todos los **hilos** *demonio*.

> [!example] Ejeplo:
> Si tenemos un programa cullo **hilo** principal crea otro **hilo**, aunque la ejecución del **hilo** principal termine, si el **hilo** secundario no ha terminado su ejecución, el programa no se detendrá hasta que termine; esta 

---
---
---
---
---

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

Los objetos de tipo `Thread` tienen varios [métodos](../py_func.md), veremos los más importantes:

- `start`: hace que comience el proceso de ejecución del hilo.
- `is_alive`: devuelve un valor [booleano](py_bool.md) indicando si sigue vivo (*Si está vivo es que no ha terminado*).
- `join`: la ejecución del programa se detiene hasta que el hilo termine de ejecutarse.
