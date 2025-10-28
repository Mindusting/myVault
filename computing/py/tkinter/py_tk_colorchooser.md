---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Selector de color en TKinter
---

# SELECTOR DE COLOR EN TKINTER

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtu.be/LI8KQ3pjQug)

El [módulo](../py_module.md) [`tkinter`](py_tk.md) contiene el [submódulo](../py_module.md) `colorchooser`, este se usa para poder pedirle un color al usuario, este [módulo](../py_module.md) contiene una [clase](../py_class.md) ([`Chooser`](#CLASE%20CHOOSER)) y una [función](../py_func.md) ([`askcolor`](#FUNCIÓN%20ASKCOLOR)).

```python
from tkinter import colorchooser as cc

cc.askcolor()

c = cc.Chooser()
c.show()
```

## CLASE CHOOSER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar la clase `Chooser`.

## FUNCIÓN ASKCOLOR

Esta [función](../py_func.md) sirve para pedirle un color al usuario, devolviendo el resultado en forma de [tupla](../py_tuple.md), esta tendrá dos elementos, el primero será otra [tupla](../py_tuple.md) con tres valores numéricos, estos son los valores de *RGB* respectivamente, el segundo elemento será un [string](../py_str.md) con el formato hexadecimal de *RGB* (`#000000`).

```python
from tkinter import colorchooser

data = colorchooser.askcolor()

print(data)
# SALIDA:
# ((0, 0, 0), '#000000')
```

### COLOR POR DEFECTO EN ASKCOLOR

Para establecer un color por defecto en el selector de colores, se puede hacer pasando como primer argumenta de la [función](../py_func.md) una [tupla](../py_tuple.md) con los tres valores *RGB* o un [string](../py_str.md) con el formato hexadecimal (`#000000`).

```python
from tkinter import colorchooser

# Con tupla.
colorchooser.askcolor((255, 0, 0))

# Con string.
colorchooser.askcolor("#ff0000")
```

### TÍTULO EN ASKCOLOR

Para establecer el título del selector de color se puede hacer a través de la opción `title`, este recibirá un [string](../py_str.md):

```python
from tkinter import colorchooser

colorchooser.askcolor(
    title="Elige tu color favorito."
)

```
