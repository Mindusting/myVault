---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Comment
title: Comentarios en Python
---

<h1 style="text-align:center;">COMENTARIOS EN PYTHON</h1>

---

# REFERENCIAS WEB

- [W3](https://www.w3schools.com/python/python_comments.asp)

# COMENTARIOS EN PYTHON

[¿Qué es un comentario en programación?](../pc/pc_comment.md)

Los comentarios sirven para dar una **descripción** de lo que hace una **parte del código** o dar **indicaciones**. Esto nos puede servir para en un futuro, cuando ya no nos acordemos de qué hace dicha parte del código, y así **no tener que interpretarlo**, sino que podemos ver la descripción que hayamos dejado, también **puede ayudar a otras personas** que estén trabajando con nosotros a entender como funciona lo que estamos haciendo.

Debido a que el texto que esté marcado como comentario no se ejecuta, nos puede servir para **inhabilitar código sin necesidad de borrarlo**, por si nos pudiera ser útil en un futuro.

## COMENTARIOS DE UNA LÍNEA

Para escribir un comentario de una sola línea, tenemos que escribir **un numeral** (`#`) seguido del comentario, esto es debido a que a partir de la dicha **almohadilla** hasta el final de línea será un comentario.

%%
SINTAXIS

```py
# [comment]
```
%%

> [!abstract] SINTAXIS
> <span class="comment-color">#<span class="italic">[comment]</span></span>

Esto es un ejemplo de un comentario:

```py
# Esto es un comentario.
```

## COMENTARIOS MULTILÍNEA

Para escribir un comentario multilínea se puede usar las **seis comillas** (`""""""`), todo lo que se escriba entre estas comillas da igual cuantas líneas haya entre ellas, todo será considerado un comentario.

%%
SINTAXIS

```py
"""[comment]"""
```
%%

> [!abstract] SINTAXIS
> <span class="comment-color">"""<span class="italic">[comment]</span>"""</span>

Este es un ejemplo de como hacer un comentario multilínea:

```py
"""
Esto es un
comentario de
múltiples líneas.
"""
```

> [!info]
> Yo no suelo usar las triples comillas para escribir comentarios, ya que las suelo usar para [comentar código](<## COMENTAR CÓDIGO>).

## COMENTAR CÓDIGO

A la hora de comentar código lo que suelo hacer es meterlo entre seis comillas como se explica en el apartado de [comentarios multilínea ](<## COMENTARIOS MULTILÍNEA>), pero antes de las tres últimas comillas pongo un **numeral** (`#`), esto permite que el código que se encuentre dentro de las comillas esté comentado, pero si quiero des comentarlo, simplemente tengo que añadir un nuevo **numeral** (`#`) en frente de las tres primeras comillas, de esta forma, tanto las comillas de apertura y cierre de comentario se comentan con el **numeral** (`#`) y todo el contenido que se encuentre entre las comillas dejará de ser un comentario.

%%
SINTAXIS

```py
#"""
[code]
#"""
```
%%

>[!abstract] SINTAXIS
> <span class="comment-color">#"""</span><br><span class="italic grey">[code]</span><br><span class="comment-color">#"""</span>

Aquí tienes un ejemplo de código comentado.

```py
# Este primer print está comentado.
"""
print("Este es mi primer print")
#"""

# Este segundo print no está comentado.
#"""
print("Este es mi segundo print")
#"""
```

Lo que se ve en este ejemplo no tiene demasiado sentido ya que al ser una línea se podría hacer lo mismo usando el **numeral** (`#`) en frente del [print](py_print.md), pero sí nos serviría para comentar un gran bloque de código, ya que si no, las opciones que tenemos es, o ir comentando todas las líneas con  **numerales** (`#`) lo cual es un horror de hacer, o comentarlo con las seis comillas, pero en este último caso tendremos que quitarlas tanto de arriba como de debajo del bloque de código y esta forma de hacerlo nos permite poder comentar o descomentar todo un bloque de código con solo un carácter.
