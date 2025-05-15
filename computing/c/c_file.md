---
author: Mindusting
corrected: false
tags:
  - Programming/C/File
title: Archivos de C
---

# ARCHIVOS DE C

Compilar nuestro programa permite ejecutarlo, por lo que hasta que no escribas nada en un archivo "`.c`" no le vas a poder dar mucha utilidad a este apartado, por lo que si quieres salta al apartado =="OUTPUT"== y cuando hayas seguido los ejemplos de ese apartado y quieras compilar el archivo, vuelves a este apartado.

## WINDOWS

Para poder ejecutar programas escritos en **C** tendremos que descargar el compilador de **C** desde internet e instalarlo.

En **Windows** deberemos crear una archivo "`.exe`" a partir del archivo "`.c`", para ello desde el **CMD** deberemos ir a la ruta donde se encuentra el archivo "`.c`" y seguir la siguiente sintaxis:

```cmd
gcc [file_name].c
```

El archivo "`.exe`" que nos crea tendrá el nombre "`a.exe`" este podrá ser cambiado sin problema, pero manteniendo la extensión "`.exe`", para ejecutarlo desde el terminal tendremos que estar en la ruta en la que se encuentra y seguir la siguiente sintaxis:

```cmd
[file_name].exe
```

## LINUX

Para poder ejecutar programas escritos en **C** tendremos que descargar el compilador desde internet e instalarlo, para ello escribimos en un terminal los siguientes comandos:

```sh
sudo apt-get update
sudo apt-get install build-essential gdb
```

En Linux deberemos ir en un terminal a la ruta en la que se encuentra el archivo y ejecutaremos el siguiente comando para compilar el archivo:

```sh
cc [file_name].c -o [compiled_file_name]
```

Esto nos creará un archivo en el mismo directorio con el nombre que hayamos indicado, y ya compilado (*Listo para ejecutarse*).

Una vez tengamos el archivo compilado para ejecutarlo deberemos escribir un punto y una barra para indicar que queremos ejecutar algo del directorio actual, seguido del nombre que le hayamos dado al archivo compilado.

```sh
./[compiled_dile_name]
```
