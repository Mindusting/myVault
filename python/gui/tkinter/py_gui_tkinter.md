---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Módulo TKinter en Python
---

<h1 align="center">TKINTER EN PYTHON</h1>

---

# REFERENCIAS WEB

- [Python tkinter](https://docs.python.org/3.12/library/tkinter.html)
- [Real Python](https://realpython.com/python-gui-tkinter/)

# VÍDEOS

- [Bro Code](https://youtu.be/TuLxsvK4svQ)

# TKINTER

Para poder hacer uso de `tkinter`, primero deberemos importar el [módulo](../../py_module.md):

```py
import tkinter as tk
```

## CLASE TK

Esta clase se usa para crear la ventana con la que interactuará el usuario, tenemos que crear un [objeto](../../py_class.md) de tipo `Tk` instanciando esta [clase](../../py_class.md):

```py
import tkinter as tk

# Aquí creamos la clase Tk.
root: tk.Tk = tk.Tk()

# Mantenemos la ventana abierta
# gracias al método "mainloop".
root.mainloop()
```

Cuando empecemos a crear *elementos* (`widget`) para nuestra ventana, estos se declararán entre la declaración de la ventana y la llamada al `mainloop`.

### GEOMERÍA DE LA VENTANA

Para cambiar el **tamaño** de la ventana se usa al [método](../../classes/py_method.md) `geometry`, esta recibe un argumento de tipo [str](../../variables/py_str.md) con las medidas y la posición de la ventana:

```py import tkinter as tk root: tk.Tk = tk.Tk() # Indicamos que queremos que la ventana # tenga unas dimensiones de 360 píxeles # de ancho por 240 píxeles de alto. root.geometry("360x240")

root.mainloop()
```

Si queremos indicar también la posición de la ventana lo haremos de la siguiente forma:

```py
import tkinter as tk

root: tk.Tk = tk.Tk()

# Al igual que en el anterior ejemplo
# indicamos el ancho y el alto de la
# ventana, seguido a esto, indicamos
# la posición en el eje "x" y en el
# eje "y" respecto al punto origen del
# monitor, siendo este la esquina de
# arriba a la izquierda.
root.geometry("360x240+300+200")

root.mainloop()
```

> [!note] NOTE
> Nota que la separación entre los valores del tamaño de la página se separan con una `x`, mientras que la separación entre el tamaño y la posición y los valores de la posición se separan con un `+`.

---

Esto también se puede hacer mediante el [`f-str`](../../variables/py_fstr.md) para no tener un valor predeterminado, si no que podemos modificarlo mediante una variable o un calculo previo a la creación de la ventana:

```py
import tkinter as tk

root: tk.Tk = tk.Tk()

# Aquí declaramos las variables y les
# asignamos los valores para la indicación
# del tamaño y posición de la ventana.
root_x: int = 100
root_y: int = 100
root_width:  int = 360
root_height: int = 240

# Mediante un f-str indicamos los valores
# de las variables de forma ordenada para
# que la ventana coja el aspecto que
# hayamos indicado.
root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")

root.mainloop()
```

### REDIMENSIONABLE

De forma predeterminada, las ventanas de `tkinter` son redimensionables, esto quiere decir que el usuario puede cambiar el tamaño de esta manteniendo el clic y arrastrando en uno de sus bordes, si queremos que esto no sea posible tendremos que usar el [método](../../classes/py_method.md) `resizable`, este recibe dos argumentos de tipo [`bool`](../../variables/py_bool.md) siendo el primero para el eje en `x` y el segundo en `y`, si el valor que indicamos es igual a `False`, ese eje no se podrá redimensionar, si es igual a `True` si se podrá.

```py
import tkinter as tk

root: tk.Tk = tk.Tk()
root.geometry("360x240")

# Indicamos que a ninguno de los ejes
# se les puede cambiar el tamaño.
root.resizable(False, False)

root.mainloop()
```

### TÍTULO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

### ICONO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## WIDGETS

- [Label](Tkinter_Label.md)
- [Button]()
- [Entry]()
- [Text]()
- [Frame]()
