---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Clase ZipFile en el módulo ZipFile en Python
---

# CLASE ZIPFILE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Documentar la compresión de los archivo:
> >     - [x] Documentar el modo.
> >     - [x] Documentar el método de compresión.
> >         - [x] `ZIP_STORED`: sin compresión (*por defecto*).
> >         - [x] `ZIP_DEFLATED`: compresión normal de ZIP.
> >         - [x] `ZIP_BZIP2`: compresión BZIP2.
> >         - [x] `ZIP_LZMA`: compresión LZMA.
> >     - [x] Documentar la habilitación del ZIP64.
> >     - [x] Documentar el nivel de compresión.
> > - [ ] Documentar la excepción `BadZipFile`.
> > - [ ] Documentar `namelist`.
> > - [ ] Documentar `infolist`.
> > - [ ] Documentar `filelist`.
> > - [x] Documentar `printdir`.
> > - [ ] Documentar `testzip`.
> > - [ ] Documentar `getinfo`.
> > - [ ] Documentar `setpassword`.
> > - [x] Documentar `read`.
> > - [ ] Documentar `open`.
> > - [ ] Documentar `extract`.
> > - [ ] Documentar `extractall`.
> > - [x] Documentar `write`.
> > - [ ] Documentar `close`.

> [!help]- REFERENCIAS WEB
> - [Python doc (`ZipFile`)](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile)

La [clase](../py_class.md) `ZipFile` se comporta de una forma similar a la [función](../py_func.md) [`open`](../py_open.md), con la diferencia principal que esta está pensada para trabajar sobre archivo `.zip` en vez de archivos de texto.

## CONEXIÓN A ARCHIVO ZIP

> [!abstract] SINTAXIS
> ZipFile(***\[file\]***, [***\[mode\]***](#MODO%20DE%20CONEXIÓN), [***\[compression\]***](#MÉTODO%20DE%20COMPRESIÓN), [***\[allowZip64\]***](#HABILITAR%20ZIP64), [***\[compresslevel\]***](#NIVEL%20DE%20COMPRESIÓN))

### MODO DE CONEXIÓN

Dependiendo del modo de trabajo que elijamos para el archivo `.zip`, podremos hacer unas cosas u otras.

| MODOS | SIGNIFICADO | DESCRIPCIÓN                            |
|:-----:| ----------- |:-------------------------------------- |
|  `w`  | Write       | Escribir de cero el archivo.           |
|  `r`  | Read        | Leer un archivo existente.             |
|  `a`  | Append      | Crear o añadir a un archivo existente. |
|  `x`  | Exclusive   | Crear archivo no existente.            |
^table-acciess-modifiers

- `w`: Permite crear archivos `.zip` nuevos, si se indica un archivo ya existente se sobrescribirá los datos que introduzcamos.
- `r`: Permite leer archivos `.zip`, si el archivo indicado no existe, lanza una [excepción](../py_exceptions.md) de tipo `FileNotFoundError`.
- `a`: Permite crear archivos `.zip` nuevos, si se indica un archivo ya existente se añadirá los cambios que indiquemos.
- `x`: Permite crear archivos `.zip` nuevos, si se indica un archivo ya existente se lanzará una [excepción](../py_exceptions.md) de tipo `FileExistsError`.

### MÉTODO DE COMPRESIÓN

Existen cuatro tipos de compresión, siendo `ZIP_STORED` el formato por defecto:

| COMPRESIÓN     | VALOR | DESCRIPCIÓN                     |
|:-------------- |:-----:|:------------------------------- |
| `ZIP_STORED`   |  `0`  | Sin compresión (*por defecto*). |
| `ZIP_DEFLATED` |  `8`  | Compresión normal de ZIP.       |
| `ZIP_BZIP2`    | `12`  | Compresión BZIP2.               |
| `ZIP_LZMA`     | `14`  | Compresión LZMA.                |

- `ZIP_STORED`: (*es la opción por defecto*) no comprime el contenido, simplemente lo agrupa dentro del archivo `.zip`.
- `ZIP_DEFLATED`: es la compresión estándar de ZIP.
- `ZIP_BZIP2`: es el método de compresión BZIP2.
- `ZIP_LZMA`: es el método de compresión LZMA.

### HABILITAR ZIP64

A la hora de abrir un archivo `.zip` este utiliza el método por defecto que es con 32 bits, este tiene un defecto y es que no puede manejar archivo de un tamaño mayor a 4 GiB de peso, es por eso que existe esta opción la cual por defecto está activada que permite usar el método de 64 bits.

### NIVEL DE COMPRESIÓN

El nivel de compresión se aplica sobre el [método de compresión](#MÉTODO%20DE%20COMPRESIÓN) e indica la dureza de este último, a menor dureza menor compresión y por tanto menos tiempo de calculo, y a mayor dureza mayor compresión y por tanto más tiempo de calculo, el rango de valores es de [`[0, 9]`](../../../math/math_range_notation.md), siendo el nivel `0` sin compresión, `1` el nivel más bajo de compresión y `9` el nivel más grade de compresión.

Este argumento tiene como valor por defecto `-1`, el cual es interpretado como un punto medio entre nivel de compresión y tiempo de calculo, dando como resultado el nivel `6`.

## ARCHIVO ZIP MALO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

- `BadZipFile`: clase de tipo excepción para cuando el archivo a abrir no es válido como `.zip`.

## COMENTARIO DEL ARCHIVO

Para pode establecer o leer el comentario del archivo usaremos la [variable](../py_variable.md) `comment`, este almacena el comentario en forma de [`bytes`](../py_bytes.md).

Este comentario es simplemente para poder darle una descripción al archivo, para poder ejemplo indicar de forma general el contendido del archivo, pudiendo así hacernos una idea de que es lo que contiene sin tener que revisar el resto del contenido comprimido.

```python
from zipfile import ZipFile

zipf = ZipFile("data.zip", "a")

# Establecemos el comentario del archivo.
zipf.comment = b"Este es el comentario del archivo `.zip`."

# Leemos el comentario del archivo.
print(zipf.comment)

zipf.close()
```

## ESCRIBIR ARCHIVO

Para añadir un nuevo archivo al archivo `.zip` se usa el [método](../class/py_methods.md) `write`, esta tiene un argumento obligatorio en donde indicaremos la ruta del archivo que queremos agregar al `.zip` y otro opcional en donde indicaremos la ruta en donde queremos guardar el archivo dentro del `.zip`.

> [!abstract] SINTAXIS
> ***\[zipf\]***.write(***\[path\]\{***, ***\[new_path\]\}***)

```python
from zipfile import ZipFile

zipf = ZipFile("data.zip", "r")

# Guardamos el archivo "text.txt" en
# la carpeta "docs" con el nombre
# "doc.md".
zipf.write("./text.txt", "./docs/doc.md")

zipf.close()
```

## LEER ARCHIVOS

Para obtener el contendido de uno de los archivos contenidos dentro del archivo `.zip`, se usa el [método](../class/py_methods.md) `read`, este recibe la ruta y nombre del archivo que queramos consultar y devuelve el conjunto de [bytes](../py_bytes.md) del contenido del archivo.

> [!abstract] SINTAXIS
> ***\[zipf\]***.read(***\[path\]***)

```python
from zipfile import ZipFile

zipf = ZipFile("data.zip", "r")

# Imprime el contenido del
# archivo en forma de texto.
print(zipf.read("README.md").decode())

zipf.close()
```

## INPRIMIR DIRECTORIO

Si queremos ver el contendido del archivo `.zip` de forma rápida y sencilla, podemos usar el [método](../class/py_methods.md) `printdir`.

```python
from zipfile import ZipFile

zipf = ZipFile("data.zip", "r")

# Se inprime la información del archivo.
zipf.printdir()

zipf.close()
```

## LISTA DE INFORMACIÓN

Para obtener información de los archivo con la que podremos operar se usa el [método](../class/py_methods.md) `infolist`, este devuelve una [lista](../py_list.md) de [objetos](../py_class.md) [`ZipInfo`](py_zipfile_zipinfo.md).

```python
from zipfile import ZipFile

zipf = ZipFile("data.zip", "r")

# Se obtiene la lista de información.
for info in zipf.infolist():
    # Se imprime la información.
    print(info)

zipf.close()
```

> [!info] INFO
> Este [método](../class/py_methods.md) devuelve el contenido de la [variable](../py_variable.md) `filelist`.
