---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Clase Frame en TKinter en Python
---

# CLASE FRAME EN TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```python
import tkinter as tk


def main() -> None:
    root = Window()
    root.mainloop()


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("480x360")
        self.resizable(False, False)
        self.title("My Window")

        self.frames = {
            MainFrame: MainFrame(self),
            SecondFrame: SecondFrame(self)
        }

        for frame in self.frames.values():
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.view_frame(MainFrame)


    def view_frame(self, frame_class: tk.Frame) -> None:

        for frame in self.frames.values():
            frame.grid_remove()

        self.frames[frame_class].grid()
        self.update()


class MainFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#ff0000")

        self.btn = tk.Button(
            master = self,
            text = "Second",
            command = lambda: self.master.view_frame(SecondFrame)
        )
        self.btn.grid(row=0, column=0, sticky="nsew")

        self.a = tk.Label(
            master = self,
            text = "Hola"
        )
        self.a.grid(row=1, column=1, sticky="nsew")


class SecondFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#00ff00")
        
        self.btn = tk.Button(
            master = self,
            text = "Main",
            command = lambda: self.master.view_frame(MainFrame)
        )
        self.btn.grid(row=0, column=0, sticky="nsew")

        self.a = tk.Label(
            master = self,
            text = "Adio"
        )
        self.a.grid(row=1, column=1, sticky="nsew")


if "__main__" == __name__:
    main()
```

```python
import tkinter as tk


def main() -> None:
    root: Window = Window()
    root.mainloop()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.window_default_conf()
        self.create_frames()


    def window_default_conf(self) -> None:
        self.title("My window")
        self.resizable(False, False)


    def create_frames(self) -> None:
        self.frames: dict = dict()

        self.frames[Main_Frame] = Main_Frame(self)
        self.frames[Second_Frame] = Second_Frame(self)

        self.show_frame(Main_Frame)


    def show_frame(self, class_frame) -> None:

        for obj_frame in self.frames.values():
            obj_frame.grid_forget()
        
        
        frame: tk.Frame = self.frames[class_frame]
        frame.grid(
            row=0,
            column=0
        )


class Main_Frame(tk.Frame):
    def __init__(self, root: Window):
        super().__init__()

        self.root: Window = root
        self.create_widgets()


    def create_widgets(self) -> None:
        self.button = tk.Button(
            self,
            text="Cambiar a segundo frame",
            command=lambda: self.root.show_frame(Second_Frame)
        )
        self.button.grid(row=0, column=0)

        self.label = tk.Label(
            self,
            text="Hola mundo!"
        )
        self.label.grid(row=1, column=1)


class Second_Frame(tk.Frame):
    def __init__(self, root: Window):
        super().__init__()

        self.root: Window = root
        self.create_widgets()


    def create_widgets(self) -> None:
        self.button = tk.Button(
            self,
            text="Cambiar a primer frame",
            command=lambda: self.root.show_frame(Main_Frame)
        )
        self.button.grid(row=0, column=0)


if "__main__" == __name__:
    main()
```
