---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Menús en Tkinter
---

# MENÚ EN TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [TkDocs (Menus)](https://tkdocs.com/tutorial/menus.html)

```py
import tkinter as tk
from tkinter import filedialog


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("TK Menu")
        self.geometry("360x240")
        self["menu"] = TopMenu(self)


class TopMenu(tk.Menu):

    def __init__(self, master = None):
        super().__init__(master)
        self.menu_file = tk.Menu(self, tearoff=0)
        self.menu_edit = tk.Menu(self, tearoff=0)
        self.add_cascade(
            menu=self.menu_file,
            label="Archivo"
        )

        self.menu_file.add_command(
            label="Nuevo",
            command=self.new_file
        )
        self.menu_file.add_command(
            label="Abrir",
            command=self.open_file
        )

    def new_file(self) -> None:
        file = filedialog.asksaveasfile()
        if file is None:
            return
        file.write("Nuevo archivo.")
        file.close()
    
    def open_file(self) -> None:
        file = filedialog.askopenfile()
        if file is None:
            return
        print(file.read())
        file.close()


if "__main__" == __name__:
    main()

```
