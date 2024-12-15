---
author: Mindusting
corrected: true
tags:
  - Programming/Python/File
title: Archivos de Python
---

# ARCHIVOS DE PYTHON

Para poder programar algo en **Python** tenemos que guardar las instrucciones de nuestro programa en un archivo con extensión "`.py`" por lo que para empezar puedes crear una carpeta llamada "***Python***" donde guardarás los diferentes archivos, puedes crear un archivo para cada apartado (Recuerda que deben tener nombres distintos y acabar en "`.py`"), eso ya dependerá de cómo quieras organizarte tú, a medida que vayas aprendiendo a programar irás sabiendo mejor cómo organizar los archivos, pero ahora es momento de trastear e ir probando las cosas a ver que pasa y por qué pasan, no tengas miedo a equivocarte, que salgan errores o que no funcione como quieres las cosas, es el proceso de aprendizaje, si hay algo que no sepas búscalo en internet, no te quedes parado y no pierdas la motivación.

Empecemos situándonos en la carpeta "***Python***" que deberíamos haber creado, y dentro de esta creamos un fichero llamado "`Main.py`" y lo abrimos con nuestro [IDE](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.ii39hp967o1c).

## EJECUTAR ARCHIVOS

Para ejecutar ficheros de **Python** en **Windows** se puede abrir el **administrador de archivos**, ir a la ruta en la que se encuentra el archivo y hacer doble clic sobre él, se debería ejecutar siempre y cuando tengamos [instalado Python](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.5l09os6map1a), si se abre una ventana negra y se cierra automáticamente, es normal, lo que ocurre es que se ejecuta el programa y al terminar se cierra la ventana, para que nos dé tiempo a ver el resultado de nuestro programa, al final de este deberemos escribir "`input()`", ahora mismo puede que no entiendas por qué, si sigues el documento en el apartado **INPUT** entenderás por qué pasa esto, pero de momento solo hace falta que sepas que lo último que debes poner en tu programa es "`input()`".

Para ejecutarlo en **UNIX** tendremos que abrir un terminal, situarnos en la ruta del archivo y ejecutar el comando:

%%
SINTAXIS

```shell
python3 [file_name].py [ARGV(s)]
```
%%

> [!abstract] SINTAXIS
> python3 <span class="italic grey">[file_name]</span>.py <span class="italic grey">[ARGV(s)]</span>

Imaginemos que tenemos el archivo `main.py`, si quisiéramos ejecutarlo tendríamos que escribir el siguiente comando:

```shell
python3 main.py
```

En el caso en el que nuestro archivo `main.py` requiriera de por ejemplo dos *argumentos*, podremos indicarlo como se muestra en el siguiente ejemplo:

```shell
python3 main.py 3 2
```
