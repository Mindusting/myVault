---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Módulo TKinter en Python
---

# TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Documentar clase Tk.
> > - [ ] Documentar que son los "widgets".
> > - [ ] Documentar clase Label.
> > - [ ] Documentar clase Button.
> > - [ ] Documentar clase Entry.
> > - [ ] Documentar clase Text.
> > - [ ] Documentar clase Frame.

> [!help]- REFERENCIAS WEB
> - [Python tkinter](https://docs.python.org/3.12/library/tk.html)
> - [TkDocs](https://tkdocs.com/tutorial/index.html)
> - [Real Python](https://realpython.com/python-gui-tkinter/)
> - [Guia Tkinter](https://guia-tkinter.readthedocs.io/es/develop/index.html)
>
> YouTube:
> - [Bro Code](https://youtu.be/TuLxsvK4svQ)
> - [Clear Code](https://youtu.be/mop6g-c5HEY)

> [!warning] ATENCIÓN:
> Para entender bien la documentación de **TKinter** es muy recomendable entender la [OOP de Python](../py_class.md) ya que se utiliza mucho y se trabaja con **herencia**.

El [módulo](../py_module.md) **TKinter** ofrece la posibilidad de crear entornos gráficos (*GUI*) para mejorar la interacción con el usuario que use nuestro programa.

Cabe resaltar que **TKinter** ha sufrido cambios con el paso del tiempo, entre ellos está la adición del nuevo [submódulos](../py_module.md) [`ttk`](./ttk/py_ttk.md) que contiene una versión más avanzada de los elementos de **TKinter**, lo mejor es empezar aprendiendo a usar el antiguo **TKinter** y luego aprender lo nuevo, ya que este último es algo más complejo.

---

Para poder hacer uso de **TKinter**, primero deberemos importar el [módulo](../py_module.md) de la siguiente forma, a este se le suele dar el alias de `tk`:

```python
import tkinter as tk
```

Una vez hayamos importado **TKinter**, podremos crear una ventana con la [clase](../py_class.md) [`Tk`](./py_tk_tk.md).

## CLASES

- [Tk](./py_tk_tk.md)
- [PhotoImage](py_tk_photoimage.md)

%%
[Widget](py_tk_widget.md)

- [Label](ttk/py_ttk_label.md)
- [Entry](ttk/py_ttk_entry.md)
- [Button](py_tk_button.md)
- [Frame](py_tk_frame.md)
- [Text](py_tk_text.md)
- [Menu](py_tk_menu.md)
- [ComboBox](ttk/py_ttk_combobox.md)
- [Scrollbar](ttk/py_ttk_scrollbar.md)
%%

## OTROS SUBMÓDULOS

- [SELECTOR DE COLOR](py_tk_colorchooser.md)
- [VENTANAS POPUP](py_tk_messagebox.md)
- [DIÁLOGOS SIMPLES](py_tk_simpledialog.md)
- [DIÁLOGOS DE FICHERO](py_tk_filedialog.md)
