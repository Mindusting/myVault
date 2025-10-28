---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Etiquetas en Tkinter
---

# ETIQUETAS EN TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Documentar como comstrar texto.
> > - [ ] Documentar como comstrar imágenes.

El [**widget**](./py_tk_widget.md) `Label` sirve principalmente para mostrar texto o imágenes, con la intención de mostar información al usuario.

## USO CON TEXTO

Para mostrar texto mediante un `Label` primero tendremos que crear lo indicando cual va a ser su `master` (*elemento padre, generalmente la [ventana](./py_tk_tk.md) o un [`Frame`](./py_tk_frame.md)*), seguido del texto que contrendrá este `Label`.

> [!abstract] SINTAXIS
> Label(***\[master\]***, text=***\[text\]***)

Una vez creado el `Label` se debe indicar de que forma queremos colocarlo al igual que concualquier [`Widget`](./py_tk_widget.md).

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("480x360")
        self.create_widgets()


    def create_widgets(self) -> None:
        self.my_label = tk.Label(
            self,
            text="Este es mi texto"
        )
        self.my_label.grid(
            row=0,
            column=0
        )


main()
```

En caso de querer tanto modificar como acceder al texto que contiene el `Label` se puede hacer al igual que con un [**diccionario**](../py_dict.md), como veremos en el próximo ejemplo haciendo uso de un [botón](./py_tk_button.md).

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("480x360")
        self.create_widgets()


    def create_widgets(self) -> None:
        self.my_label = tk.Label(
            self,
            text="Este es mi texto"
        )
        self.my_label.grid(
            row=0,
            column=0
        )

        self.my_button = tk.Button(
            self,
            text="Actualiza",
            command=self.update_label
        )
        self.my_button.grid(
            row=1,
            column=0
        )


    def update_label(self) -> None:
        text = self.my_label["text"]

        print(f"El anterior texto era \"{text}\".")

        self.my_label["text"] = "Este es el último texto"


main()
```

## USO CON IMÁGENES

> [!abstract] SINTAXIS
> Label(***\[master\]***, image=***\[image\]***)
