---
author: Mindusting
corrected: false
tags:
  - MarkDown
title: Código en Markdown
---

<h1 style="text-align:center;">CÓDIGO EN MARKDOWN</h1>

---

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR

Los archivos de MarkDown suelen estar relacionados a la programación, esto es debido a que los archivo MarkDown contienen texto plano, siendo estos archivos, ligeros y sencillo, con ciertas ventajas como puede ser la posibilidad de escribir código en el propio archivo de MarkDown, para ello se hace uso del carácter *acentuación grave* (`<code></code>`).

## LÍNEA DE CÓDIGO

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR

Para poder escribir una sola línea de código, se debe poner una *acentuación grave* para escribir el código y otra *acentuación grave* para cerrar el código.

> [!example] Ej. de uso de línea de código con sintaxis de MD:
> ```md
> Para imprimir en Python se usa la función `print()`.
>
> **Ej:**
> `print("Hola mundo!!!")`
> ```
>
> > [!quote] Así es como se la línea de código:
> > Para imprimir en Python se usa la función `print()`.
> >
> > **Ej:**
> > `print("Hola mundo!!!")`

## BLOQUE DE CÓDIGO

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR
> - [ ] Comprobar si se puede poner el ejemplo de forma que las etiquetas estén inveticas, en el sentido de MD a HTML y HTML a MD.

Para poder escribir un bloque de código, se debe poner tres *acentuaciones graves* para escribir el bloque de código y otras tres *acentuaciones graves* para cerrar el bloque de código.

> [!example] Ej. de bloque de código con sintaxis de MD:
> <pre>
> <code>```python
> import math
>
> def distance(dx: float, dy:float):
>     return math.sqrt((dx * dx) + (dy * dy))
>
> print(distance(1, 1))
> ```</code>
> </pre>
>
> > [!quote] Así es como se ve el bloque de código con sintaxis de MD:
> > ```python
> > import math
> >
> > def distance(dx: float, dy:float):
> >     return math.sqrt((dx * dx) + (dy * dy))
> >
> > print(distance(1, 1))
> > ```
