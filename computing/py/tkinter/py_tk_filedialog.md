---
author: Mindusting
corrected: false
tags:
  - Programming/Python/TKinter
title: Selección de archivos y directorios en TKinter
---

# FILE DIALOG EN TKINTER

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar pedir directorio.
> > - [ ] Documentar abrir archivo.
> > - [ ] Documentar pedir archivo por nombre.
> > - [ ] Documentar pedir archivos por nombre.
> > - [ ] Documentar guardar archivo.
> > - [ ] Documentar guardar archivo por nombre.

```py
from tkinter import filedialog
```

## PEDIR DIRECTORIO

```py
from tkinter import filedialog

directory = filedialog.askdirectory(
    initialdir="C:/",
    mustexist=True,
    title="Elige la carpeta."
)

print(directory)
```

## ABRIR ARCHIVO

```py
from tkinter import filedialog

file = filedialog.askopenfile(
    mode="rb",
    defaultextension="*.*",
    filetypes=(
        ("Cualquiera", ".*"),
        ("Text",       ".txt"),
        ("MarkDown",   ".md"),
        ("Python",     ".py"),
        ("SQLite",     ".db"),
        ("SQLite",     ".sqlite"),
        ("SQLite",     ".sqlite3")
    ),
    initialdir=".",
    initialfile="main.py",
    title="Elige el archivo."
)
file_paths = filedialog.askopenfilenames(
    defaultextension="*.*",
    filetypes=(
        ("Cualquiera", ".*"),
        ("Text",       ".txt"),
        ("MarkDown",   ".md"),
        ("Python",     ".py"),
        ("SQLite",     ".db"),
        ("SQLite",     ".sqlite"),
        ("SQLite",     ".sqlite3")
    ),
    initialdir=".",
    initialfile="main.db",
    title="Elige el archivo."
)

if file is None:
    print("No has elegido archivo.")
else:
    print(file.read())
```

## PEDIR ARCHIVO POR NOMBRE

```py
from tkinter import filedialog

file_path = filedialog.askopenfilename(
    defaultextension="*.*",
    filetypes=(
        ("Cualquiera", ".*"),
        ("Text",       ".txt"),
        ("MarkDown",   ".md"),
        ("Python",     ".py"),
        ("SQLite",     ".db"),
        ("SQLite",     ".sqlite"),
        ("SQLite",     ".sqlite3")
    ),
    initialdir=".",
    initialfile="main.py",
    title="Elige el archivo."
)

if file_path is None:
    print("No has elegido archivo.")
else:
    print(f"El archivo seleccionado es:\n{file_path}")
```

## PEDIR ARCHIVOS POR NOMBRE

```py
from tkinter import filedialog

file_paths = filedialog.askopenfilenames(
    defaultextension="*.*",
    filetypes=(
        ("Cualquiera", ".*"),
        ("Text",       ".txt"),
        ("MarkDown",   ".md"),
        ("Python",     ".py"),
        ("SQLite",     ".db"),
        ("SQLite",     ".sqlite"),
        ("SQLite",     ".sqlite3")
    ),
    initialdir=".",
    #initialfile="main.py",
    title="Elige unos archivo."
)

if file_paths is None:
    print("No has elegido archivo.")
else:
    print(f"El o los archivos seleccionados son:")
    for path in file_paths:
        print(path)
```

## GUARDAR ARCHIVO

```py
from tkinter import filedialog

file = filedialog.asksaveasfile(
    mode="wb",
    confirmoverwrite=True,
    filetypes=(
        ("Cualquiera", ".*"),
        ("Text",       ".txt"),
        ("MarkDown",   ".md"),
        ("Python",     ".py"),
        ("SQLite",     ".db"),
        ("SQLite",     ".sqlite"),
        ("SQLite",     ".sqlite3")
    ),
    initialdir=".",
    initialfile="main.db",
    title="Elige el archivo."
)

if file is None:
    print("No has elegido archivo.")
else:
    data = str("Este es el contenido del archivo.")
    file.write(data)
```

## GUARDAR ARCHIVO POR NOMBRE

```py
from tkinter import filedialog

file_path = filedialog.asksaveasfilename(
    confirmoverwrite=True,
    filetypes=(
        ("Cualquiera", ".*"),
        ("Text",       ".txt"),
        ("MarkDown",   ".md"),
        ("Python",     ".py"),
        ("SQLite",     ".db"),
        ("SQLite",     ".sqlite"),
        ("SQLite",     ".sqlite3")
    ),
    initialdir=".",
    initialfile="main.db",
    title="Elige el archivo."
)

if file_path is None:
    print("No has elegido archivo.")
else:
    print(f"El archivo seleccionado es:\n{file_path}")
```
