---
author: Mindusting
corrected: false
tags:
  - Programming/Python/File
title: Archivos externos en Python
---

# ARCHIVO EXTERNOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Replantear por completo esta documentación.
> > - [ ] Explicar como usar la palabra clave `with`.

> [!help]- REFERENCIAS WEB
> - [Python doc (open)](https://docs.python.org/3/library/functions.html#open)
> - [Python doc (io)](https://docs.python.org/es/3/library/io.html)
> - [TpointTech (File Handling)](https://www.tpointtech.com/python-files-io)

Para trabajar sobre otros archivos

> [!abstract] SINTAXIS
> open(***\[path\]***, ***\[mode\]***, encoding=***\[encoding\]***)

`seek(x)`
`truncate(x)`
`write(x)`
`read(x)`
`flush()`
`tell()`

## MODOS DE TRABAJO

| MODE | READ  | WRITE | CREATES | SEEK  | OVERWRITE |
|:----:|:----- |:----- |:------- |:----- |:--------- |
| `r`  | True  | False | False   | Start | False     |
| `w`  | False | True  | True    | Start | True      |
| `x`  | False | True  | True    | Start | False     |
| `a`  | False | True  | True    | End   | False     |

`r`: el *seek* se sitúa al principio, no puede escribir, si no existe el archivo lanza `FileNotFoundError`.
`x`: el *seek* se sitúa al principio, crea el archivo, si ya existe lanza `FileExistsError`, permite escribir.
`a`: el *seek* se sitúa al final, permite escribir.
`r+`: el *seek* se sitúa al principio, escribe al final.
`w+`: el *seek* se sitúa al principio, escribe al principio.
`a+`: el *seek* se sitúa al final, escribe al final.

## FUNCIONES PROPIAS

### BORRADO SEGURO DE ARCHIVOS

```python
import os


def sremove(path: str | bytes, layers: int = 1) -> None:

    if layers <= 0:
        raise ValueError("layers must by greater than 0")

    if not os.path.exists(path):
        raise FileNotFoundError

    number_of_bytes: int = os.path.getsize(path)

    with open(path, "wb") as file:
        for _ in range(layers):
            file.write(os.urandom(number_of_bytes))
            file.flush()
            file.seek(0)

    os.remove(path)
```

---
---
---
---
---

El manejo de archivos externos, nos permitirá guardar información de forma permanente, estos archivos se quedarán guardados en el disco duro una vez el programa se termine de ejecutar, permitiendo poder acceder en el futuro a esa información guardada.

Para ello usaremos la [función](py_func.md) `open` (*Abrir en Ingles*), esta [función](py_func.md), en las últimas versiones de Python ya viene incluida de forma automática, en el caso en el que no tengamos acceso a ella, podremos importarla desde el [módulo](py_module.md) `io`.

%%
SINTAXIS

```python
open([file_name], [mode])
```
%%

> [!abstract] SINTAXIS
> <span class="function-color">open</span>(<span class="italic grey">[file_name]</span>, <span class="italic grey">[mode]</span>)

Esta [función](py_func.md) nos devuelve un [objeto](py_class.md) de tipo `TextIOWrapper`, del [módulo](py_module.md) `io`, para qué nos entendamos, es un [objeto](py_class.md) de tipo "*archivo*", este [objeto](py_class.md) no guarda el contendido del archivo, si no que es una referencia a este, de forma que cuando nosotros queramos obtener su contenido u modificar lo, podremos hacerlo a trabes de este sin necesidad de cargar todo el archivo en memoria, ya que podría ocupar mucho espacio, veamos un ejemplo de esto:

```python
# Creamos la conexión con el archivo.
file = open("main.txt", "w")

# Escribimos texto en el archivo.
file.write("Este es mi archivo de texto.")

# Cerramos la conexión con el archivo.
file.close()
```

Si ejecutamos el anterior ejemplo podremos ver que en el mismo directorio en el que se encuentra nuestro programa podremos encontrar un archivo llamado `main.txt`, si lo abrimos podremos ver que el texto "`Este es mi archivo de texto.`" se ha guardado correctamente.

Más adelante veremos que modos de apertura tenemos para los archivos, pero antes veremos otra forma de abrir archivos.

```python
# Creamos la conexión con el archivo.
with open("main.txt", "w", encoding="utf-8") as file:

    # Escribimos texto en el archivo.
    file.write("Este es mi archivo de texto.")

# Se cierra auromáticamente al terminar
# la sangría del with.
```

Es importante cerra los archivo una vez vamos a dejar de usarlos, ya que estos consumen memoria RAM y también podrían no guardarse los cambios que le hayamos hecho.

## MODOS DE APERTURA

Los modos se separan en dos partes que son combinables, un indica como se va a interpretar el contenido del archivo y el otro indica como se va a trabajar sobre el archivo.

### INTERPRETACIÓN DEL CONTENIDO

| MODO | DEFINICIÓN                   |
|:----:|:---------------------------- |
| `t`  | Texto (Por defecto).         |
| `b`  | Binario.                     |

#### TEXTO

#### BINARIO

### MODO DE TRABAJO

| MODO | DEFINICIÓN                   |
|:----:|:---------------------------- |
| `w`  | Escritura.                   |
| `r`  | Lectura (Por defecto).       |
| `a`  | Añadir.                      |
| `x`  | Crear archivo para escribir. |
| `+`  | Lectura escritura.           |

#### ESCRITURA

#### LECTURA

#### AÑADIR

#### CREAR ARCHIVO

`FileExistsError`

### LECTURA ESCRITURA
