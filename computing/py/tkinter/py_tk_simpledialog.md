---
author: Mindusting
corrected: true
tags:
  - Programming/Python/TKinter
title: Diálogos simples en TKinter
---

# DIÁLOGOS SIMPLES EN TKINTER

El [módulo](../py_module.md) [`tkinter`](py_tk.md) contiene el [submódulo](../py_module.md) `simpledialog`, este se usa para poder pedirle un [entero](../py_int.md), [real](../py_float.md) o [texto](../py_str.md) al usuario, este [módulo](../py_module.md) contiene tres [funciones](../py_function.md) ([`askinteger`](#ASK%20INTEGER), [`askfloat`](#ASK%20FLOAT) y [`askstring`](#ASK%20STRING)).

Para importar este [submódulo](../py_module.md) se hace de la siguiente forma:

```py
from tkinter import simpledialog
```

> [!info] INFO
> Si el usuario pulsa el botón de cancelar en cualquiera de las ventanas popup, se devolverá `None`.

## ASK INTEGER

La [función](../py_function.md) `askinteger` permite preguntarle al usuario mediante una ventana popup un [entero](../py_int.md), esta requiere de dos argumentos y tiene otros tres opcionales:

> [!abstract] SINTAXIS
> askinteger(***\[title\], \[prompt\], \{\[initialvalue\], \[minvalue\], \[maxvalue\]\}***)

- `title`: sirve para establecer con un [string](../py_str.md) el título de la ventana.
- `prompt`: sirve para establecer con un [string](../py_str.md) el mensaje de la ventana.
- `initialvalue`: sirve para indicar con un [entero](../py_int.md) el valor predeterminado de la respuesta.
- `minvalue`: sirve para establecer con un [entero](../py_int.md) el valor mínimo que puede introducir el usuario.
- `maxvalue`: sirve para establecer con un [entero](../py_int.md) el valor máximo que puede introducir el usuario.

```py
from tkinter import simpledialog

# Se pregunta la edad con el diálogo
age = simpledialog.askinteger(
    title="Selector de edad",
    prompt="Introduce tu edad:",
    initialvalue=18,
    minvalue=0,
    maxvalue=120
)

# Se comprueba si ha cancelado
if age is None:
    print("Has cancelado.")
else:
    print(f"Tienes {age} años.")
```

## ASK FLOAT

La [función](../py_function.md) `askfloat` permite preguntarle al usuario mediante una ventana popup un [real](../py_float.md), esta requiere de dos argumentos y tiene otros tres opcionales:

> [!abstract] SINTAXIS
> askfloat(***\[title\], \[prompt\], \{\[initialvalue\], \[minvalue\], \[maxvalue\]\}***)

- `title`: sirve para establecer con un [string](../py_str.md) el título de la ventana.
- `prompt`: sirve para establecer con un [string](../py_str.md) el mensaje de la ventana.
- `initialvalue`: sirve para indicar con un [real](../py_float.md) el valor predeterminado de la respuesta.
- `minvalue`: sirve para establecer con un [real](../py_float.md) el valor mínimo que puede introducir el usuario.
- `maxvalue`: sirve para establecer con un [real](../py_float.md) el valor máximo que puede introducir el usuario.

```py
from tkinter import simpledialog

# Se pregunta la latura con el diálogo
age = simpledialog.askinteger(
    title="Selector de edad",
    prompt="Introduce tu edad:",
    initialvalue=18,
    minvalue=0,
    maxvalue=120
)

# Se comprueba si ha cancelado
if age is None:
    print("Has cancelado.")
else:
    print(f"Tienes {age} años.")
```

## ASK STRING

La [función](../py_function.md) `askstring` permite preguntarle al usuario mediante una ventana popup un [texto](../py_str.md), esta requiere de dos argumentos y tiene otros dos opcionales:

> [!abstract] SINTAXIS
> askfloat(***\[title\], \[prompt\], \{\[initialvalue\], \[show\]\}***)

- `title`: sirve para establecer con un [string](../py_str.md) el título de la ventana.
- `prompt`: sirve para establecer con un [string](../py_str.md) el mensaje de la ventana.
- `initialvalue`: sirve para indicar con un [texto](../py_str.md) el valor predeterminado de la respuesta.
- `show`: sirve para establecer como queremos que se muestre el [texto](../py_str.md) que escriba el usuario, si no se especifica nada se verá el [texto](../py_str.md) normal, pero si queremos que nos se vea lo que escribe el usuario como puede ser una contraseña, se puede especificar por ejemplo `*`.

```py
from tkinter import simpledialog

# Se pregunta la contraseña con el diálogo
pw = simpledialog.askstring(
    title="Contraseña",
    prompt="Introduce tu contraseña:",
    initialvalue="",
    show="*"
)

# Se comprueba si ha cancelado
if pw is None:
    print("Has cancelado.")
else:
    print(f"Tu contraseña es '{pw}'.")
```
