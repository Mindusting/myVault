---
author: Mindusting
corrected: false
tags:
  - OS/Linux/BASH
title: Comando LS en Linux
---

# COMANDO LS EN LINUX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar el conjunto de caracteres validos e inválidos en un ultimo apartado.
> >     `[...]`, `[^...]`, `[!...]`
> > - [ ] Explicar que con el parámetro `-l`, los directorios son `d`, los archivos son `-`; los siguientes tres bloques son el propietario, el grupo primario y el resto de usuarios.

> [!help]- REFERENCIAS WEB
> - [geeksforgeeks](https://www.geeksforgeeks.org/ls-command-in-linux/)

El comando `ls` (*abreviación del inglés `LiSt`*), sirve para listar el contenido de un directorio, este último puede ser en el que nos encontremos en ese momento y otro.

Listar un directorio consiste en crear una lista de los directorios y archivos que se encuentren dentro del directorio que hayamos especificado.

> [!abstract] SINTAXIS
> ls ***[\[parameters\]](#PARÁMETROS) [\[path\]](#RUTA%20DE%20ACCIÓN)***

## PARÁMETROS

Los parámetros que indiquemos modificarán el comportamiento del comando, pudiendo indicar uno o varios al mismo tiempo.

- `--help`:
    Muestra la ayuda interna del comando `LS`.

- `-a` o `--all`:
    Muestra también los [**archivos ocultos**](../linux_hidden_files.md).

- `-l`:
    Lista los archivos mostrando más datos relevantes acerca de los archivos y directorios, como son los **permisos**, el **creador**, **tamaño en bytes**, la **fecha de modificación** y su **nombre**.

- `-t`:
    Ordena el listado de archivos y directorios en base a su fecha de modificación, poniendo al principio los modificados más recientemente.

- `-r`:
    Invierte el orden de la lista.

- `-S`:
    Ordena el listado de archivos y directorios en base al tamaño, poniendo al principio del listado los más grandes.

- `-R`:
    Lista los archivos y directorios de forma recursiva.

- `-i`:
    Muestra el [`inode`](../linux_inode.md) de cada archivo y directorio.

- `-h`:
    Cambia el formato en el que se muestra el tamaño en bytes, para mostrarlos en distintas unidades de medidas.

- `-F`:
    Nos indica al final de cada nombre que tipo de elemento es mediante unos caracteres especiales:
    - *nada*: Archivo normal.
    - `/`: Directorio.
    - `*`: Ejecutable.
    - `@`: Link a un archivo.

## RUTA DE ACCIÓN

La **ruta de acción** indica sobre qué directorio queremos que se aplique el comando `LS`, si no indicamos nada se efectuará sobre el directorio en el que nos encontremos.

Se puede especificar caracteres especiales para poder buscar de una forma más sencilla archivos o directorios:

- `*`: de cero a varios caracteres.
- `?`: un carácter.

> [!example] EJEMPLO DE USO DEL `*`
> Si quisiéramos encontrar todos los archivos `.c` en un directorio, tendríamos que ejecutar el siguiente comando:
> 
> ```bash
> ls *.c
> ```
> 
> Con esto lo que estamos indicando es que debe buscar todos los archivos que comienzan por cero y múltiples caracteres seguido de `.c`.

> [!example] EJEMPLO DE USO DEL `?`
> Si quisiéramos buscar el archivo de texto de Adelio, pero no recordamos si era un chico o una chica podemos ejecutar lo siguiente:
> 
> ```
> ls adeli?.txt
> ```
> 
> Este buscará todos los archivos que empiecen por `adeli` seguido de un carácter y que termine con `.txt`, pudiendo ser en este caso `adelio.txt` o `adelia.txt`.

> [!exercise] EJERCICIO
> Intenta ejecutar ejecutar un comando que muestre todos los archivos `.c` que contengan un su nombre la palabra `user`.
