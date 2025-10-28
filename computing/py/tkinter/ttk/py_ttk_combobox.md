---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: ComboBox en TKinter en Python
---

# COMBOBOX EN TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```python
import tkinter as tk
from tkinter import ttk

root = tkTk()

cb = ttk.Combobox(root)
cb["state"] = "readonly"
cb["values"] = (
    "Opción 1",
    "Opción 2",
    "Opción 3",
    "Opción 4",
)
cb.current(0)
cb.pack()

cb.bind(
    "<<ComboboxSelected>>",
    lambda: print(cb.get())
)

root.mainloop()
```
