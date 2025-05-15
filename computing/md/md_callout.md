---
author: Mindusting
corrected: false
tags:
  - MarkDown
title: Anoraciones en Markdown
---

# ANOTACIONES

> [!help]- REFERENCIAS WEB
> - [Obsidian doc (callout)](<https://help.obsidian.md/Editing+and+formatting/Callouts>)

Las anotaciones en *MarkDown* sirven para agrupar el texto dentro de un bloque usando una sintaxis similar a la de las [citas](md_quotes.md) con la diferencia que a edtas le podemos dar colores dependiendo del mensaje que queramos transmitir con el contenido de su interior el color y el icono dependeren del tipo de anotación que indiquemos (*Los tipos de indican en el apartado [tipos de anotaciones](<## TIPOS DE ANOTACIONES>)*), además, se puede añadir un guión entre los corchetes que indican el tipo y el título alternativo un guión para que está anotación aparezca plegada.

> [!abstract] SINTAXIS
> \> \[!***\[type\]***\]***\[fold\]*** ***\[title\]***
> \> ***\[content\]***

```md
> [!note] Este es el título de mi anotación.
> Este es el contenido de mi nota.
> > [!tip]- Esta es mi anotación indexada y plegada.
> > Se puede hacer que una anotación esté plegada de forma predeterminada añadiendo un guion tras la declaración de la misma.
```

# TIPOS DE ANOTACIONES

> [!note]
> - note

> [!info]
> - info

> [!todo]
> - todo

> [!abstract]
> - abstract
> - summary
> - tldr

> [!tip]
> - tip
> - hint
> - important

> [!success]
> - success
> - check
> - done

> [!question]
> - question
> - help
> - faq

> [!warning]
> - warning
> - caution
> - attention

> [!failure]
> - failure
> - fail
> - missing

> [!danger]
> - danger
> - error

> [!bug]
> - bug

> [!example]
> - example

> [!quote]
> - quote
> - cite
