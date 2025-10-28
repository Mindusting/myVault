---
author: Mindusting
corrected: false
tags:
  - Programming/C
title: Estructura inicial en C
---

# ESTRUCTURA INICIAL

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/index.php)
> - [W3 Schools (Librería `stdio`)](https://www.w3schools.com/c/c_ref_stdio.php)

Para poder hacer que un programa de **C** funcione, primero tendremos que crear la siguiente estructura.

```c
// Incluimos en nuestro programa la librería "stdio".
#include <stdio.h>

// Declaramos la función "main".
int main() {
    // Imprimimos un mensaje en consola.
    printf("Hola mundo!\n");

    // La función "main" devuelve 0 si no ocurren errores.
    return 0;
}
```

La función `main` es por donde nuestro programa va a empezar a ejecutarse, si nuestro archivo no tiene función `main` el compilador nos dará un error, ya que esta función representa el punto en el que nuestro programa debe iniciar a ejecutarse.

> [!info]
> La librería `stdio` (*STanDar Input Output*) agrega a nuestro programa varias funciones, entre ellas tenemos la función `printf`, la cual nos permite imprimir texto por consola.
> 
> Si quieres saber más a cerca de esta librería te recomiendo revisar el siguiente [enlace](https://www.w3schools.com/c/c_ref_stdio.php).

De momento todo nuestro programa lo escribiremos dentro de esta función, al gula que hemos hecho a la hora de imprimir el "*Hola mundo!*" por consola.

> [!note]
> El `return` al final de la función `main` le sirve a nuestro programa para saber si ha llegado al final de la ejecución sin errores, es por ello que es importante ponerlo.
