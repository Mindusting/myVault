---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Clase Tk Python
---

# CLASE TK EN TKINTER

> [!important] IMPORTANTE
> La [clase](../py_class.md) `Tk` es la encargada de crear la ventana que usaremos para mostrar información, en mucha de la documentación que podrás encontrar por internet que enseñan a usar esta [clase](../py_class.md) de forma directa, en esta documentación no se mostrará así, ya que para hacer pruebas o proyectos pequeños puede venir bien, pero si tu intención es escalarlo a un programa más complejo, el orden y claridad del código es importante, para ello haremos uso de la [herencia](../class/py_inheritance.md) entre [clases](../py_class.md), por lo que si no entiendes bien estos conceptos, te recomiendo que primero consultes al documentación de este mismo tema.

Hago un pequeño adelanto de a lo que me refiero con como organizar el código, a continuación tienes un ejemplo de como suelen ser los ejemplos sencillos (*para hacer pruebas*):

```python
import tkinter as tk

# Se crea la ventan.
root: tk.Tk = tk.Tk()

# Se establecen las propiedades.
root.title("Mi ventana.")
root.geometry("360x240")
root.resizable(False, False)

# Se muestra la ventana.
root.mainloop()
```

Y aquí tienes un ejemplo de como hacer el código organizado para poder escalarlo fácil mente, a medida que vayamos viendo cosas más complicadas, verás que la escalabilidad de los proyectos es mucho más sencilla de esta forma a pesar de que tengamos que escribir más código al principio:

```python
import tkinter as tk


def main() -> None:
    # Se crea la ventan.
    root: Window = Window()
    # Se muestra la ventan.
    root.mainloop()

# La clase Window hereda de Tk de esta
# forma podremos manejar la ventan de
# una forma más sencilla y estará
# todo más organizado.
class Window(tk.Tk):

    def __init__(self):
        # Ejecutamos el contructor
        # de la clase Tk.
        super().__init__()

        # Se establecen las propiedades.
        self.title("Mi ventana.")
        self.geometry("360x240")
        self.resizable(False, False)


if "__main__" == __name__:
    main()
```

## COMO CREAR UNA VENTANA

Para crear una venta usaremos la [clase](../py_class.md) `Window` (*ventana en inglés*) la cual es hija (*[herede](../class/py_inheritance.md)*) de la [clase](../py_class.md) `Tk`.

Si ejecutamos este código, deberíamos ver una pequeña ventana cuadrada y vacía, la cual podremos cerrar al igual que lo haríamos con cualquier otra.

```python
import tkinter as tk


def main() -> None:
    # Creación del bojeto ventana.
    root: Window = Window()
    # Mostramos la ventan con
    # método mainloop.
    root.mainloop()


# La clase Window que hereda de Tk.
#              v
class Window(tk.Tk):

    def __init__(self):
        # Llamamos al constructor
        # de la clase padre (Tk)
        # para que se cree corectamente.
        super().__init__()


if "__main__" == __name__:
    main()
```

Al ejecutar este programa, nos tiene que aparecer una ventana pequeña y cuadrada con el título "tk", pudiendo cerrarla cuando pulsamos el botón de cerrar (*generalmente la "X"*).

### BUCLE PRINCIPAL DE UNA VENTANA

Cuando terminamos de crear una ventana indicando todas las cosas que queremos que aparezcan en ella, tenemos que llamar al [método](../class/py_method.md) `mainloop`, este hará que se pare la ejecución de nuestro código ya que se mantendrá actualizando la ventana, comprobando si el usuario interactúa con ella, esto ocurrirá hasta que el usuario cierre la ventana, a partir de ahí, nuestro código continuará ejecutándose.

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()
    #       ^
    # Aquí el código se ha parado
    # y no va a imprimir el mensage
    # hasta que se cierre la ventana.
    #            v
    print("Se cerró la ventana.")


class Window(tk.Tk):

    def __init__(self):
        super().__init__()


if "__main__" == __name__:
    main()
```

## GEOMETRÍA DE LA VENTANA

Para cambiar el **tamaño** y/o **posición** de la ventana se usa el [método](../class/py_method.md) `geometry`, esta recibe un argumento de tipo [`str`](../py_str.md) con las **medidas** y/o **posición** en píxeles de la ventana.

Para indicar el tamaño de la ventana se hace siguiendo la siguiente sintaxis; en donde se indica el número de píxelex de ancho y alto separados por una `x`:

> [!abstract] SINTAXIS (tamaño)
> ***\[width\]***x***\[height\]***

Para indicar la posición de la ventana se hace siguiendo la siguiente sintaxis; en donde se indica el número de píxeles en el eje `X` y en el eje `Y`, siendo los dos precedidos por un `+`:

> [!abstract] SINTAXIS (posición)
> \+***\[posX\]***+***\[posY\]***

También existe la posibilidad de indicar el tamaño y la posición en un solo paso; esto se hace combinando las dos sintaxis anteriores:

> [!abstract] SINTAXIS (posición)
> ***\[width\]***x***\[height\]***\+***\[posX\]***+***\[posY\]***

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        # se establece el tamaño de la ventana
        # en 480 por 360 píxeles y la posición
        # en las coordenadas (200, 100).
        self.geometry("480x360+200+100")

        # También se puede hacer por separado:
        # self.geometry("480x360")
        # self.geometry("+200+100")


if "__main__" == __name__:
    main()
```

## REDIMENSIONABILIDAD

La redimensionabilidad de una venta indica si esta puede cambiar de tamaño tanto en el eje `X` como en el `Y`; por ello para indicar que ejes queremos permitir que cambien de tamaño o no, lo haremos con el [método](../class/py_method.md) `resizable`; este recibe dos argumentos de tipo [bool](../py_bool.md), indicando primero el eje `X` y luego el `Y`.

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        # Indicamos que no se puede
        # cambiar el tamaño de la ventana
        # en ninguno de sus ejes.
        self.resizable(False, False)


if "__main__" == __name__:
    main()
```

## TÍTULO DE LA VENTAN

Para indicar el título que queremos que tenga nuestra ventana tendremos que usar el [método](../class/py_method.md) `title`; este recibe un argumento de tipo [`str`](../py_str.md) con el título en cuestión.

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        # Establecemos el título de la ventan.
        self.title("Este es mi título")


if "__main__" == __name__:
    main()
```

## ICONO DE LA VENTANA

Dependiendo de si queremos establecer una imagen como icono o un archivo de tipo `.ico`, tendremos que usar un [método](../class/py_method.md) distinto.

Para los archivo `.ico` se usa el [método](../class/py_method.md) `iconbitmap`; este recibe un argumento de tipo [`str`](../py_str.md) con la ruta de en donde se encuentra el archivo.

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> #TODO
> Para usar una imagen como icono tendremos que usar la [clase](../py_class.md) [`PhotoImage`](./py_tk_photoimage.md) y el [método](../class/py_method.md) `iconphoto`


## CONFIGURACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > Se puede obtener los argumentos de la configuración con `config().keys()`.

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
- `menu`: Recibe un objeto de tipo [`menu`](py_tk_menu.md).
