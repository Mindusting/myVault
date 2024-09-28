---
author: Mindusting
corrected: false
tags:
  - MarkDown
title: Anoraciones en Markdown
---

<h1 style="text-align:center;">TABLAS EN MARKDOWN</h1>

---

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR
> - [ ] Hacer un ejemplo de tabla con sintaxis de HTML.

[Obsidian doc](<https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax#Tables>)

Una lista está compuesta por títulos, justificación y celdas de contenido.

> [!example] Ej. 1 de uso de la tabla con sintaxis de MD:
> ```md
> | C. A | C. B | C. C |
> |:-----|:----:|-----:|
> |  A1  |  B1  |  C1  |
> |  A2  |  B2  |  C2  |
> |  A3  |  B3  |  C3  |
> ```
> ^ejemplo-1-de-tablas
>
> > [!quote] Así es como se ve la tabla:
> >
> > | C. A | C. B | C. C |
> > |:-----|:----:|-----:|
> > |  A1  |  B1  |  C1  |
> > |  A2  |  B2  |  C2  |
> > |  A3  |  B3  |  C3  |

Como se puede ver en el ejemplo, la primera columna está justificada a la izquierda, la segunda está centrada y la tercera está justificada a la derecha, esto es debido a los guiones y doble puntos que se encuentran en la segunda línea.

| Just. izc. | Centrado | Just. der. |
|:----------:|:--------:|:----------:|
|    :--     |    :-:   |     --:    |

El número mínimo de caracteres para indicar la justificación es de un mínimo de tres, pero a este se le puede añadir guiones para hacer la tabla más estética, esto se puede ver en el anterior [ejemplo](<#^ejemplo-1-de-tablas>).

> [!example] Ej. 2 de uso de la tabla con sintaxis de MD:
> En este ejemplo se puede ver el uso que se le puede dar a las tablas, almacenando una lista de usuarios con su respectivo **ID**.
> ```md
> | ID | NOMBRE |
> |---:|:-------|
> |  0 | admin  |
> |  1 | Adelio |
> |  2 | Jon    |
> |  3 | Alex   |
> ```
>
> > [!quote] Así es como se ve la tabla:
> >
> > | ID | NOMBRE |
> > |---:|:-------|
> > |  0 | admin  |
> > |  1 | Adelio |
> > |  2 | Jon    |
> > |  3 | Alex   |
