---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Módulo ZipFile en Python
---

# ARCHIVOS ZIP EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Explicar el objetivo de este módulo.
> > - [ ] Documentar como saber si un archivo es válido.
> > - [ ] Documentar el problema de los archivo grandes, requiere `ZIP64` a partir de archivo de 4GiB de tamaño.

> [!help]- REFERENCIAS WEB
> - [Python doc](https://docs.python.org/3/library/zipfile.html)
> - [geeksforgeeks](https://www.geeksforgeeks.org/working-zip-files-python/)
> - [Real Python](https://realpython.com/python-zipfile/)
> - [note.nkmk.me](https://note.nkmk.me/en/python-zipfile/)

El objetivo de este [módulo](../py_module.md) es poder trabajar sobre archivo `.zip` con Python, como puede ser crear archivos nuevo, leer ya existentes, modificarlos e incluso obtener información de cada archivo interno comprimido.

> [!info] INFO
> Este módulo está incluido en Python3 por lo que no hace falta instalarlo.

## ÍNDICE

Si quieres seguir una documentación más lineal, te recomiendo lo siguiente:

1. [CLASE `ZipFile`](py_zipfile_zipfile.md)
2. [CLASE `ZipInfo`](py_zipfile_zipinfo.md)

## ARCHIVOS VÁLIDOS

Para comprobar si un archivo es válido como `.zip`, y eso no es si tiene la extensión correcta, sino al contenido del archivo es interpretable como un archivo `.zip`, podemos usar la [función](../py_func.md) `is_zipfile`, este requiere de un argumento indicando la ruta del archivo, esta devolverá un valor [booleano](../py_bool.md) indicando si es válido o no.

> [!abstract] SINTAXIS
> id\_zipfile(***\[path\]***)

```python
import zipfile

# Uso de la función `is_zipfile`.
print(zipfile.is_zipfile("./data.zip"))
```

> [!note] NOTA
> Esta [función](../py_func.md) devolverá `False` si la **ruta** indicada no existe.

