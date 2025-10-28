---
author: Mindusting
corrected: false
tags:
  - OS/Windows/BATCH
title: Archivos BATCH
---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Revisar todo el archivo y subdividirlo.

# PRÓLOGO

Hoy que tener en cuenta que los archivos `.bat` no son más que un archivo que contiene comandos de Windows, los cuales van a ser ejecutados en orden, por lo que escribiendo comandos como `cls`, `mkdir` y demás comandos de Windows, estos se ejecutarás al igual que si los ubiesemos ejecutado nosotros.

# COMENTARIOS

Los comentarios en los archivos `.bat` permiten dejar anotaciones a derca de por ejemplo, que hace nuestro archivo `.bat` por si queremos que otras personas puedan entenderlo, o para que si en algún momento dejamos nuestro archivo por un tiempo y luego queremos volver a retomarlo, los comentarios nos pueden ayudar a comprender el fin del archivo.

> [!abstract] SINTAXIS
> rem ***\[comment\]***

> [!example] Ej. de comentarios en los archivos `.bat`:
> ```bat
> rem Esto es un comentario.
> ```
> Como se puede ver en el ejemplo, para escribir un comentario se usa el comando `rem`, este indica que esa lína no debe ejecutarse ya que es un comentario.

# COMMANDO ECHO (OUTPUT)

Este comando permite imprimir en consola, y configurar la salida de datos por la misma.

## DESACTIVAR LA IMPRESIÓN DE COMANDOS

Cada vez que se ejecute un comando este se imprimirá por consola, si no queremos que nuestro terminal se llene de líneas indicando cada comando que se ejecuta y queremos que se imprima solo lo que nosotros indicquemos, esto se puede hacer de la siguiente forma.

> [!example] Ej. de como desactivar la impresión de comandos:
> ```bat
> @echo off
> ```

Este comando indicará que no queremos que se impriman por consola los comandos que se ejecuten en nuestro archivo `.bat`, si quisieramos volver a activarlo, estan simple como ejecutar el mismo comando, instarcambiando `off` por `on`.

## IMPRESIÓN DE TEXTO

Para poder escribir po consola podremos usar el comando `echo`.

> [!abstract] SINTAXIS
> echo ***\[text\]***

> [!example] Ej. de como imprimir por consola:
> ```bat
> @echo off
> echo Hola mundo!!!
> ```

Si quisieramos hacer un salto de línea es tan facil como escribir un punto pegado al comando `echo`.

> [!example] Ej. de como imprimir un salto de línea:
> ```bat
> @echo off
> echo Hola mundo!!!
> echo.
> echo Hola mundo!!!
> ```

# FIN DEL ARCHIVO

Para poder indicar el fin del archivo se usa el comando `exit`, ahora mismo es posible que no le veas demasiado uso, pero cuandro empecemos a ver los condicionales este comando tendrá un mejor uso.

> [!abstract] SINTAXIS
> exit

> [!example] Ej. de uso del comando `exit`:
> ```bat
> @echo off
> echo Hola mundo!!!
> pause>nul
> exit
> ```

# PAUSAR EJECUCIÓN

Si estás ejecutando los archivos `.bat` desde no tendrás demasiado problema ya que podrás ver el resultado de tu programa, pero si lo estás ejecutando haciendo doble clic sobre el archivo en un entorno gráfico, este se cerrará automaticamente al llegar al final del archivo, si queremos que se detenga el programa, podremos hacer usando el comando `pause`, esto imprimirá un mensage indicando que se debe pulsar 'enter' para continuar.

> [!example] Ej. de uso del comando `pause`:
> ```bat
> @echo off
> echo Hola mundo!!!
> pause
> exit
> ```

---

En el caso de que queramos que no se imprima el mensage y simplemente queremos que el programa espere a que el usuario pulse la tecla enter, podemos usar el comando `pause>nul`.

> [!example] Ej. de uso del comando `pause>nul`:
> ```bat
> @echo off
> echo Debes pulsar enter para continuar...
> pause>nul
> exit
> ```

# VARIABLES

Las varibles permiten almacenar un valor, asociandolo a un "alias", este "alias" es el que usaremos cada vez que queramos hacer referencia a el valor almacenado en esta variable.

Para declarar una variable se usa el comando `set`.

> [!abstract] SINTAXIS
> set ***\[var_name\]***=***\[value\]***

> [!example] Ej. de uso de variables:
> ```bat
> @echo off
> set name=Mindusting
> set age=18
> echo Hola, mi nombre es %name% y tengo %age% años.
> pause>nul
> exit
> ```
> Como se puede ver en este ejeplo, para hacer referencia al valor de una variable, esta debe estar entre caracteres de porcentage.

## OPERADORES

Los operadores permiten hacer calculos matemáticos con número y variables.

| OPERADOR | SIGNIFICADO                     |
|:--------:|:--------------------------------|
|    \+    | Suma entre operadores           |
|    \-    | Resta entre operadores          |
|    \*    | Multiplicación entre operadores |
|    \/    | División entre operadores       |

> [!abstract] SINTAXIS
> ***\[operator_a\] \[operand\] \[operator_b\]***

> [!example] Ej. de uso de operadores:
> ```bat
> @echo off
> set num1=3
> set num2=2
> set/a res=%num1% + %num2%
> echo %num1% + %num2% = %res%
> pause>nul
> exit
> ```
