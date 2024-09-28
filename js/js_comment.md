---
author: Mindusting
corrected: false
tags:
  - Programming/JS/Comment
title: Comentarios en JS
---

[¿Qué es un comentario?](../pc/pc_comment.md)

Los comentarios en JS permiten hacer anotaciones y/o comentar un trozo del código, que consisten en hacer que una parte del código ya no se ejecute, ya que deja de considerarse parte del código.

# COMENTARIOS DE UNA LÍNEA

Para escribir un comentario de una línea se usa dos veces el carácter *barra* (`/`), a partir de ese punto, hasta el final de la línea, se considerará un comentario.

>[!abstract] SINTAXIS
>//***\[comment\]***

Este es un ejemplo de un comentario de una sola línea:

```js
// Esto es un comentario de una línea.
```

# COMENTARIOS MULTI LÍNEA

Para escribir un comentario de múltiples líneas se usa la *barra* (`/`) y el *asterisco* (`*`) para indicar donde comienza el comentario y donde termina.

El inicio se hace con 

>[!abstract] SINTAXIS
>/\*
>***\[comment\]***
>\*/

Este es un ejemplo de un comentario de múltiples líneas:

```js
/*
Esto es
un comentario
de varias
líneas.
*/
```
