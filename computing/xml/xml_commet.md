---
author: Mindusting
corrected: true
tags:
  - Programming/XML
title: Comentarios en XML
---

# COMENTARIOS EN XML

> [!faq]- FAQ
> - [¿Qué son los comentarios en la programación?](../pc/pc_comment.md)

Una vez hayamos abierto nuestro archivo `.html` con un IDE, podremos empezar a escribir nuestras primeras líneas de código, pero antes aprenderemos a escribir comentarios, los comentarios sirven para dar una descripción de lo que hace una parte del código o dar indicaciones. Esto nos puede servir para en un futuro, cuando ya no nos acordemos de qué hace dicha parte del código, y así no tener que interpretarlo, sino que podemos ver la descripción que hayamos dejado, también puede ayudar a otras personas que estén trabajando con nosotros a entender como funciona lo que estamos haciendo. Debido a que el texto que esté marcado como comentario no se ejecuta, nos puede servir para inhabilitar código sin necesidad de borrarlo, por si nos pudiera ser útil en un futuro.

%%
SINTAXIS

```html
<!--[comment]-->
```
%%

>[!abstract] SINTAXIS
><span class="comment-color">\<!\--</span><span class="italic bold comment-color">[comment]</span><span class="comment-color">--></span>

Aquí podemos ver un ejemplo de un comentario de una línea:

```html
<!-- Esto de aquí es un comentario -->
```

Como se puede ver en la sintaxis, se ha de escribir un signo menor que (`<`), seguido de un signo de cierre de exclamación (`!`), seguido de dos guiones o menos (`-`), escribimos el comentario y como cierre se vuelve a escribir dos guiones o menos (`-`), seguidos de un signo de mayor que (`>`), las dos partes que se encuentran a los lados del `[comment]` se les puede llamar "apertura de comentario" y "cierre de comentario", estos no tienen porqué estar en la misma línea, pueden englobar un conjunto de líneas permitiendo escribir párrafos de texto.

Un ejemplo de cómo se puede escribir un comentario de múltiples líneas es el siguiente:

```html
<!--
    Esto de aquí es
    un comentario
    multi línea y
    solo me hace
    falta escribir
    una apertura y
    un cierre de
    comentario.
-->
```
