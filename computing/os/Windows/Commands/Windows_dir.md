---
author: Mindusting
corrected: false
tags:
  - OS/Windows
title: Comando DIR en Windows
---

# COMANDO DIR EN WINDOWS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

El comando `dir` (*DIRectory*) muestra una lista de los archivos y carpetas que se encuentren en el directorio especificado.

%%
SINTAXIS

```cmd
dir [parametres] [path][file_name]
```
%%

> [!abstract] SINTAXIS
> <span class="function-color">dir</span> <span class="italic grey">[parametres] [path][file_name]</span>

> [!quote] PARÁMETROS
> - `A`: Muestra los atributos especificados:
>     - `D`: Directorios.
>     - `R`: Archivos de solo lectura.
>     - `H`: Archivos ocultos.
>     - `A`: Archivos listos para el archivado.
>     - `S`: Archivos del sistema.
>     - `I`: Archivos indizados que no son de contenido.
>     - `L`: Puntos de reanálisis.
>     - `O`: Archivos sin conexión.
>     - `-`: Prefijo de exclusión.
> - `B`: Muestra solo los nombres (Y extensión).
> - `C`: Aplica el separador de millares en el tamaño del archivo (Está por defecto), para desactivarlo se usa `-C`.
> - `D`: Listado ancho (Arriba -> Abajo) (Similar al de Linux).
> - `L`: Usar letras minúsculas.
> - `N`: Por defecto.
> - `O`: Ordenado por:
>     - `N`: Nombre.
>     - `S`: Tamaño.
>     - `E`: Extensión.
>     - `D`: Fecha y hora.
>     - `G`: Agrupa primero los directorios.
>     - `-`: Prefijo para invertir el orden.
> - `P`: Pausa por cada impresión completa de pantalla.
> - `Q`: Muestra el propietario del archivo.
> - `R`: Muestra las secuencias alternativas de datos del archivo.
> - `S`: Muestra el directorio especificado y sus subdirectorios.
> - `T`: Campo de hora.
>     - `C`: Creación.
>     - `A`: Último acceso.
>     - `W`: Última Modificación.
> - `W`: Formato de listado ancho (Izquierda -> Derecha).
> - `X`: Muestra los nombres cortos generados para los nombres de archivo sin formato 8dot3. El formato es el mismo que para /N, con el nombre corto especificado antes del nombre largo. Si no existe ningún nombre corto, se muestran espacios en blanco en su lugar.
> - `4`: Muestra los años con 4 dígitos.

> [!fail] SE DEBE TERMINAR EL EJEMPLO

Ejemplo:

```cmd
dir /BOS code
```
