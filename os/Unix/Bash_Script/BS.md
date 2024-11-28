---
author: Mindusting
corrected: false
tags:
  - OS/Linux/BASH
title: Bash Script
---

# BASH SCRIPT

> [!help] REFERENCIAS WEB
> - [GNU doc](https://www.gnu.org/software/bash/manual/bash.html)
> 
> YouTube:
> - [Fazt](https://youtu.be/H4ayPYcZEfI)

![](BS_files.md)

# VARIABLES DE ENTORNO

Para poder visualizar las varibles de entorno se usa el comando `env`.

## AÑADIR VARIABLES DE ENTORNO

En la carpeta `home` podemos encontrar el archivo `.bashrc` este contiene las varibles de entorno, si quisieramos agregar una nueva, tendríasmos que editar este archivo y escribir lo siguiente:

```txt
NOMBRE="Jaime"
export NOMBRE
```

En este ejemplo se muestra como se añade una nueva varible de entorno.

Hay que tener en cuenta que en nuestro terminal no se habrán añadido las varibles especificadas ya que este archivo no se habrá ejecutado, por ello, debemos ejecutar el comando `source .bashsc` para ejecutar este archivo o `bash` para refrescar el terminal de forma completa.

# ARCHIVOS SH

Para poder crear un archivo `sh` este debe tener esta misma extensión, como por ejemplo `mi_archivo.sh`.

Dentro de este podremos escribir comandos de **Unix** pudiendo así ejecutarlos de forma automática con uno de estos archivos.

Para  poder empezar con un archivo `sh` primero deberemos escribir en encabezado del archivo, este se hace midiante comentarios, primero tendremos que indicar que es un tipo de archivo `hs`, para ello escibimos un cierre de esclamación seguido de la ruta `/bin/bash`, en la segunda línea podremos especificar un autor, y en la tercera una descripción a cerca de lo que hace nuestro archivo.

```bash
# !/bin/bash
# Author: Jaime
# Esta es la descripción
```

A este archivo podremos indicarle unas primeras instrucciones, como pueden ser las siguientes:

```bash
# !/bin/bash
# Author: Jaime
# Esta es la descripción

echo "Hola mundo!!!"
```

El comando `echo` lo que indica es que queremos que nos imprima en la siguiente información que nosotro indiquemos.

## EJECUTAR ARCHIVOS SH

Para poder ejecutar archivos `sh` estos deben tener los permisos` para ello, esto se consigue cambiandoselos una vez ayamos guardado el archivo.

`chmod +x mi_archivo.sh`

Una vez nuestro archivo tenga el permiso de ejecución podremos ejecutarlo haciendo referencia a el archivo.

`./mi_archivo.md`

## DECLARACIÓN DE VARIABLES

Para decrarar una varible debemos escribir el nombre de la variable, seguida de un signo igual (`=`) y el valor que queramos que tenga la variable.

```bash
pi=3.1415926535
name="Jaime"
```

Una vez declarada una variable, podemos hacer referencia a esta escribiendo un signo de dolar y el nombre de la variable.

```bash
pi=3.1415926535
name="Jaime"

echo "PI =" $pi
echo "Name =" $name
```

## OPERADORES ARITMÉTICOS

Estos operadores nos permitirán hacer operaciones con números.

```bash
x=2
y=2

echo "x =" $x
echo "y =" $y
echo
echo "x + y =" $((x + y))
echo "x - y =" $((x - y))
echo "x * y =" $((x * y))
echo "x / y =" $((x / y))
```

## OPERADORES RELACIONALES

Estos operadores nos permitirán hacer operaciones lógicas, siendo el cero `0` igual a `False` y el uno `1` igual a `True`.

```bash
x=2
y=2

echo "x =" $x
echo "y =" $y
echo
echo "x == y =" $((x == y))
echo "x != y =" $((x != y))
echo "x >= y =" $((x >= y))
echo "x <= y =" $((x <= y))
echo "x > y =" $((x > y))
echo "x < y =" $((x < y))
```

## OPERADORES DE ASIGNACIÓN

Estos operadores permite hacer un cálculo y asignar el resulado a una variable de una forma compacta.

```bash
x=2
y=2

echo "x =" $x
echo "y =" $y
echo
echo "x += y =" $((x += y))
echo "x -= y =" $((x -= y))
echo "x *= y =" $((x *= y))
echo "x /= y =" $((x /= y))
```

## ARGUMENTOS DE EJECUCIÓN

Al ejecutar el
