---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Menús en Python
---

# MENÚ

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```python
import tkinter as tk

root: tk.Tk = tk.Tk()
root.geometry("360x240")
root.resizable(False, False)

save = lambda x: x
load = lambda x: x
new = lambda x: x
modify = lambda x: x
delete = lambda x: x
help_this_program = lambda x: x

menu = tk.Menu(root)
menu_file = tk.Menu(menu, tearoff=0)
menu_file.add_command(label="Save", command=save)
menu_file.add_command(label="Load", command=load)
menu.add_cascade(label="File", menu=menu_file)
menu_edit = tk.Menu(menu, tearoff=0)
menu_edit.add_command(label="New", command=new)
menu_edit.add_command(label="Modify", command=modify)
menu_edit.add_command(label="Delete", command=delete)
menu.add_cascade(label="Edit", menu=menu_edit)
menu_help = tk.Menu(menu, tearoff=0)
menu_help.add_command(label="Help", command=help_this_program)
menu_help.add_separator()
menu_help.add_command(label="This program", command=help_this_program)
menu.add_cascade(label="Help", menu=menu_help)

root.config(menu=menu)

root.mainloop()
```
