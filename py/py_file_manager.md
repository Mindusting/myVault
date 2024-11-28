---
author: Mindusting
corrected: false
tags:
  - Programming/Python/File
title: Archivos externos en Python
---

# ARCHIVO EXTERNOS

> [!help] REFERENCIAS WEB
> - [Python doc](https://docs.python.org/es/3/library/io.html)

El manejo de archivos externos, nos permitirá guardar información de forma permanente, estos archivos se quedarán guardados en el disco duro una vez el programa se termine de ejecutar, permitiendo poder acceder en el futuro a esa información guardada.

Para ello usaremos la [función](py_function.md) `open` (*Abrir en Ingles*), esta [función](py_function.md), en las últimas versiones de Python ya viene incluida de forma automática, en el caso en el que no tengamos acceso a ella, podremos importarla desde el [módulo](py_module.md) `io`.

%%
SINTAXIS

```python
open([file_name], [mode])
```
%%

> [!abstract] SINTAXIS
> <span class="function-color">open</span>(<span class="italic grey">[file_name]</span>, <span class="italic grey">[mode]</span>)

Esta [función](py_function.md) nos devuelve un [objeto](py_class.md) de tipo `TextIOWrapper`, del [módulo](py_module.md) `io`, para qué nos entendamos, es un [objeto](py_class.md) de tipo "*archivo*", este [objeto](py_class.md) no guarda el contendido del archivo, si no que es una referencia a este, de forma que cuando nosotros queramos obtener su contenido u modificar lo, podremos hacerlo a trabes de este sin necesidad de cargar todo el archivo en memoria, ya que podría ocupar mucho espacio, veamos un ejemplo de esto:

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
