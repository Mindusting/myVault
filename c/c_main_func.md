---
author: Mindusting
corrected: false
tags:
  - Programming/C
title: C
---

<h1 style="text-align:center;">FUNCIÓN MAIN C</h1>

---

# FUNCIÓN MAIN EN C

La función `main` es por donde nuestro programa va a empezar a ejecutarse, si nuestro archivo no tiene función `main` el compilador nos dará un error.

```c
// Incluimos en nuestro programa la librería "stdio"
#include <stdio.h>

// Declaramos la función "main".
int main() {
    // Imprimimos un mensaje en consola.
    printf("Hola mundo");

    // La función "main" devuelve 0 si no ocurren errores.
    return 0;
}
```

La librería `stdio` (*STanDar Input Output*) agrega a nuestro programa varias funciones, entre ellas tenemos la función `printf`, la cual nos permite imprimir texto por consola.
