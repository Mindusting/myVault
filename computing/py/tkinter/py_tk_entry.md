---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Entradas en Tkinter
alias: w
---

# ENTRADAS EN TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar el `state=tk.DISABLED`.

La [clase](../py_class.md) `Entry` permite crear un campo en donde el usuario podrá escribir.

## ENTRADA BÁSICA

Primero veremos la forma básica de tratar la información que contendrá la *entrada*.

> [!abstract] SINTAXIS
> Entry(***\[master\]***)

```python
import tkinter as tk

def main() -> None:
    root: Window = Window()
    root.mainloop()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0)
```

Para poder interactuar con la inforación usaremos principalmente tres [métodos](../class/py_methods.md):

- `get()`
- `remove(0, tk.END)`
- `insert(0, "Hola")`

### OBTENER TEXTO

Para obtener el texto que contiene la *entrada* se usa el [método](../class/py_methods.md) `get`; este no recive ningún parámetro y nos debolverá en contenido en forma de [texto](../py_str.md).

> [!abstract] SINTAXIS
> ***\[entry\]***.get()

Se suele usar un botón como confirmación a la hora de obtener el contenido del campo.

```python
import tkinter as tk

def main() -> None:
    root: Window = Window()
    root.mainloop()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # Se crea la entrada y el botón.
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0)

        self.button_conf = tk.Button(
            self,
            text="Confirmar",
            command=self.print_entry
        )
        self.button_conf.grid(row=1, column=0)

    def print_entry(self) -> None:
        # Se imprime el texto de la entrada.
        print(self.entry.get())

if "__main__" == __name__:
    main()
```

### BORRAR TEXTO

```python
import tkinter as tk

def main() -> None:
    root: Window = Window()
    root.mainloop()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # Se crea la entrada y dos botones.
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0)

        self.button_conf = tk.Button(
            self,
            text="Confirmar",
            command=self.print_entry
        )
        self.button_conf.grid(row=1, column=0)

        self.button_clear = tk.Button(
            self,
            text="Limpiar",
            command=self.clear_entry
        )
        self.button_clear.grid(row=2, column=0)

    def print_entry(self) -> None:
        # Se imprime el texto de la entrada.
        print(self.entry.get())

    def clear_entry(self) -> None:
        # Se borra todo.
        self.entry.delete(0, tk.END)

if "__main__" == __name__:
    main()
```

### ESCRIBIR TEXTO

```python
import tkinter as tk

def main() -> None:
    root: Window = Window()
    root.mainloop()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # Se crea la entrada y tres botones.
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0)

        self.button_conf = tk.Button(
            self,
            text="Confirmar",
            command=self.print_entry
        )
        self.button_conf.grid(row=1, column=0)

        self.button_clear = tk.Button(
            self,
            text="Limpiar",
            command=self.clear_entry
        )
        self.button_clear.grid(row=2, column=0)

        self.button_default = tk.Button(
            self,
            text="Valor por defecto",
            command=self.default_entry
        )
        self.button_default.grid(row=3, column=0)

    def print_entry(self) -> None:
        # Se imprime el texto de la entrada.
        print(self.entry.get())

    def clear_entry(self) -> None:
        # Se borra todo.
        self.entry.delete(0, tk.END)

    def default_entry(self) -> None:
        # Se borra todo para seguido
        # escribir el valor por defecto.
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Hola")

if "__main__" == __name__:
    main()
```

## ENTRADA ABANZADA

> [!abstract] SINTAXIS
> Entry(***\[master\]***, ***textvariable=\[var\]***)

## ENTRADA DE CONTRASEÑA

- `show`
