---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Clase Tk Python
---

# TK

Esta [clase](../py_class.md) se usa para crear la ventana con la que interactuará el usuario, tenemos que crear un [objeto](../py_class.md) de tipo `Tk` instanciando esta [clase](../py_class.md):

```python
import tkinter as tk

# Aquí creamos el objeto Tk.
root: tk.Tk = tk.Tk()

# Mantenemos la ventana abierta
# hasta que el usuario pulse la
# equis de cierre gracias al
# método "mainloop".
root.mainloop()
```

Cuando empecemos a crear *elementos* ([`widget`](./py_tk.md#WIDGETS)) para nuestra ventana, estos se declararán entre la declaración de la ventana y la llamada al `mainloop`.

---

Como se puede ver en el ejemplo superior, primero creamos el [objeto](../py_class.md) de tipo `Tk` y luego llamamos al [método](../class/py_method.md) `mainloop`, este indica que queremos que la ventana se mantenga activa hasta que se cierre.

Cuando empecemos a crear *elementos* (`widget`) para nuestra ventana, estos se declararán entre la declaración de la ventana y la llamada al `mainloop`.

## GEOMERÍA DE LA VENTANA

Para cambiar el **tamaño** de la ventana se usa al [método](../class/py_method.md) `geometry`, esta recibe un argumento de tipo [`str`](../py_str.md) con las medidas y la posición de la ventana:

> [!abstract] SINTAXIS
> ***\[width\]***x***\[height\]\{***+***\[posX\]***+***\[posY\]\}***

```python
import tkinter as tk

root: tk.Tk = tk.Tk()
# Indicamos que queremos que la ventana
# tenga unas dimensiones de 360 píxeles
# de ancho por 240 píxeles de alto.
root.geometry("360x240")

root.mainloop()
```

Como se puede ver en el ejemplo superior, hemos indicado que queremos que la ventana sea `360` pixeles de ancho y `240` pixeles de alto.

---

Si queremos indicar también la posición de la ventana lo haremos de la siguiente forma:

```python
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

Las coordenadas de la ventana funcionan desde su punto origen, este se encuentra arriba a la izquierda de esta, por lo que en este caso, la ventana se situará a `300` pixeles desde la izquierda de la pantalla y a `200` pixeles desde el techo de la pantalla.

> [!note] NOTE
> Nota que la separación entre los valores del tamaño de la página se separan con una `x`, mientras que la separación entre el tamaño y la posición y los valores de la posición se separan con un `+`.

---

Esto también se puede hacer mediante el [`f-str`](../py_str.md#F-STRING) para no tener un valor predeterminado, si no que podemos modificarlo mediante una variable o un calculo previo a la creación de la ventana:

```python
import tkinter as tk

root: tk.Tk = tk.Tk()

# Aquí declaramos las variables y les
# asignamos los valores para la indicación
# del tamaño y posición de la ventana.
width:  int = 360
height: int = 240
pos_x:  int = 100
pos_y:  int = 100

# Mediante un f-str indicamos los valores
# de las variables de forma ordenada para
# que la ventana coja el aspecto que
# hayamos indicado.
root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

root.mainloop()
```

## REDIMENSIONABLE

De forma predeterminada, las ventanas de `Tk` son redimensionables, esto quiere decir que el usuario puede cambiar el tamaño de esta manteniendo el clic y arrastrando en uno de sus bordes, si queremos que esto no sea posible tendremos que usar el [método](../class/py_method.md) `resizable`, este recibe dos argumentos de tipo [`bool`](../py_bool.md) siendo el primero para el eje en `x` y el segundo en `y`, si el valor que indicamos es igual a `False`, ese eje no se podrá redimensionar, si es `True` sí se podrá.

```python
import tkinter as tk

root: tk.Tk = tk.Tk()
root.geometry("360x240")

# Indicamos que ninguno de los
# ejes es redimensionable.
root.resizable(False, False)

root.mainloop()
```

## TÍTULO

Se puede cambiar el título de la ventana mediante el [método](../class/py_method.md) `title`, este recibe un único argumento de tipo [`str`](../py_str.md), el texto que se indique será el que reciba la ventana como título.

```python
import tkinter as tk

root: tk.Tk = tk.Tk()
root.geometry("360x240")
root.resizable(False, False)

# Aquí se le da un nuevo título
# a la ventana.
root.title("Título de mi ventana")

root.mainloop()
```

## ICONO

Para cambiar el icono de la ventana se usa el [método](../class/py_method.md) `iconbitmap`, este recibe un argumento de tipo [`str`](../py_str.md) con la ruta del archivo `.ico` que va a ser usado como icono.

```python
import tkinter as tk

root: tk.Tk = tk.Tk()
root.geometry("360x240")
root.resizable(False, False)
root.title("Título de mi ventana")
root.iconbitmap("./imgs/logos/main.ico")

root.mainloop()
```

## CONFIGURACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```python
import tkinter as tk

root: tk.Tk = tk.Tk()
root.geometry("360x240")
root.config()

root.mainloop()
```

> [!info] INFO
> En vez de pasarle cada argumento mediante los argumentos connombre, se le puede pasar de forma directa un diccionario con la fonfiguración.

Lista de atributos del [método](../class/py_method.md) `config`:
- `background`: Recibe un [`str`](../py_str.md) con el código hexadecimal con una almohadilla (***\#***) por delante, del color con el que se va a rellenar el fondo de la ventana.
- `menu`: Recibe un objeto de tipo [`menu`](./py_tk_menu.md).
