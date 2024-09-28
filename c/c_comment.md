---
author: Mindusting
corrected: false
tags:
  - Programming/C
title: Comentarios en C
---

<h1 style="text-align:center;">COMENTARIOS EN C</h1>

---

# COMENTARIOS EN C

[¿Qué es un comentario en programación?](../pc/pc_comment.md)

## COMENTARIOS DE UNA LÍNEA

Para crear un comentario de una línea tendremos que poner dos barras (`//`), el comentario se extiende hasta el final de la línea.

```c
// Esto es un comentario de una línea.
```

## COMENTARIOS MULTILÍNEA

Para crear un comentario multilínea tendremos que poner una barra y un asterisco (`/*`) este conjunto representa el comienzo del comentario, este comentario termina con el conjunto asterisco y barra (`*/`) o sé acabe d, todo el texto que se encuentre entre estos dos conjuntos será un comentario.

```c
/*
Esto es un
comentario
multilína.
*/
```

# COMENTARIOS TEMPORALES

Los comentarios temporales se pueden usar para *desactivar* código deforma temporal, permitiendo activar y desactivar código para hacer pruebas:

```c
/* <-- La diferencia está aquí.
Este texto está comentado.
//*/

//* <-- La diferencia está aquí.
Este texto no está comentado.
//*/
```
