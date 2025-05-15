---
author: Mindusting
corrected: true
tags:
  - Programming/Python/TKinter
title: PopUps en TKinter
---

# POPUPS EN TKINTER

> [!help]- REFERENCIAS WEB
> - [Python doc (messagebox)](https://docs.python.org/3/library/tkinter.messagebox.html)
> 
> YouTube:
> - [Bro Code](https://youtu.be/SGTtoHO6loo)

El [módulo](../py_module.md) [`tkinter`](py_tk.md) contiene el [submódulo](../py_module.md) `messagebox`, este se usa para poder mostrar los característicos mensajes de *popup* en pantalla, de los cuales tenemos dos tipos, los que sencillamente muestran información y los que reciben información por parte del usuario.

Para importar este [módulo](../py_module.md) lo podremos hacer de la siguiente forma:

```python
from tkinter import messagebox
```

Este [módulo](../py_module.md) contiene múltiples [funciones](../py_function.md) para mostrar los diferentes tipos de mensajes, pero todos tienen una característica en común y es que reciben los mismos argumentos:

- `title`: con este argumento indicaremos el título que queremos que tenga el mensaje *popup*.
- `message`: con este argumento indicaremos el mensaje del *popup*.

## MOSTRAR INFORMACIÓN

- `showinfo`: este *popup* tiene una estética de *información*.
- `showwarning`: este *popup* tiene una estética de *aviso*.
- `showerror`: este *popup* tiene una estética de *error*.

## RECIBIR INFORMACIÓN

- `askokcancel`: ofrece dos botones (`Ok` y `Cancel`), este *popup* devolverá un valor [booleano](../py_bool.md) (*`True` con `Ok` y `False` con `Cancel`*), si se cierra la ventana, devuelve `False`.
- `askquestion`: ofrece dos botones (`Yes` y `No`), este *popup* devolverá un [string](../py_str.md) (*`yes` con `Yes` y `no` con `No`*), si se cierra la ventana, devuelve `no`.
- `askretrycancel`: ofrece dos botones (`Retry` y `Cancel`), este *popup* devolverá un valor [booleano](../py_bool.md) (*`True` con `Retry` y `False` con `Cancel`*), si se cierra la ventana, devuelve `False`.
- `askyesno`: ofrece dos botones (`Yes` y `No`), este *popup* devolverá un valor [booleano](../py_bool.md) (*`True` con `Yes` y `False` con `No`*), si se cierra la ventana, devuelve `False`.
- `askyesnocancel`: ofrece tres botones (`Yes`, `No` y `Cancel`), este *popup* devolverá un valor [booleano](../py_bool.md) (*`True` con `Yes` y `False` con `No`*) o `None` si se pulsa `Cancel`, si se cierra la ventana, devuelve `None`. 
