---
author: Mindusting
corrected: false
tags:
  - MarkDown
title: Formatos de texto en Markdown
---

# FORMATO DE TEXTO

## ITÁLICA

Para poder escribir texto en *itálica* se puede hacer de varias formas, pero la recomendada es usando el **asterisco** (`*`) por delante y detrás del texto que queramos tener en *itálica*, la otra opción es con **barra baja** (`_`).

%%
SINTAXIS

*[italic_text]*

_[italic_text]_
%%

> [!abstract] SINTAXIS
> \*___\[italic_text\]___\*
>
> \_***\[italic_text\]***\_

```md
El próximo texto está en *itálica*.

El próximo texto también está en _itálica_.
```

## NEGRITA

Para poder escribir texto en *negrita* se puede hacer de varias formas, pero la recomendada es usando doble **asterisco** (`*`) por delante y detrás del texto que queramos tener en *negrita*, también se puede hacer con **barra baja** (`_`).

%%
SINTAXIS

**[bold_text]**

__[bold_text]__
%%

> [!abstract] SINTAXIS
> \*\*___\[bold_text\]___\*\*
>
> \_\_***\[bold_text\]***\_\_

```md
El próximo texto está en **negrita**.

El próximo texto también está en __negrita__.
```

## ITÁLICA Y NEGRITA

Para poder escribir texto en *itálica* y *negrita* se puede hacer de varias formas, pero la recomendada es usando triple **asterisco** (`*`) por delante y detrás del texto que queramos tener en *itálica* y *negrita*, también se puede hacer con **barra baja** (`_`).

%%
SINTAXIS

***[bold_text]***

___[bold_text]___
%%

> [!abstract] SINTAXIS
> \*\*\*___\[italic_bold_text\]___\*\*\*
>
> \_\_\_***\[italic_bold_text\]***\_\_\_

```md
El próximo texto está en ***itálica y negrita***.

El próximo texto también está en ___itálica y negrita___.
```

## TACHADO

Para poder escribir texto *tachado* se hace usando la **doble virgulilla** (`~`) por delante y por detrás del texto que queramos tener *tachado*.

%%
SINTAXIS

~~[deleted_text]~~
%%

> [!abstract] SINTAXIS
> \~\~___\[deleted_text\]___\~\~

```md
El próximo texto está ~~tachado~~.
```

## MARCADO

Para poder escribir texto *marcado* se hace usando el **doble igual** (`=`) por delante y por detrás del texto que queramos tener *marcado*.

%%
SINTAXIS

==[marked_text]==
%%

> [!abstract] SINTAXIS
> \=\=___\[marked_text\]___\=\=

```md
El próximo texto está ==marcado==.
```
