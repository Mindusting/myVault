---
author: Mindusting
corrected: false
tags:
  - MarkDown/List
title: Listas en Markdown
---

# LISTAS EN MARKDOWN

Las **listas** son un conjunto de elementos consecutivos los cuales pueden estar ordenados o no, pero estos últimos estarán marcados con un punto por delante para indicar que es un nuevo elemento de la **lista**.

## LISTAS ORDENADAS

Las **listas ordenadas** son un conjunto de **elementos** enumerados, para crear una de estas **listas** se a de escribir un **número** seguido de un **punto**, un **espacio** y el **elemento** (***Texto***).

%%
> [!abstract] SINTAXIS
> 1\. ***\[element\]***
%%

```md
1. Primer elemento.
2. Segundo elemento.
    1. Tercer elemento.
    2. Cuarto elemento.
3. Quinto elemento.
```

## LISTAS DESORDENADAS

Las **listas desordenadas** son un conjunto de **elementos** no enumerados, para crear una de estas **listas** se a de escribir un **guión** (`-`), seguido de un **espacio** y el **elemento** (***Texto***).

> [!info]
> El **guión** (`-`) puede ser sustituido por un **más** (`+`) o un asterisco (`*`).

%%
> [!abstract] SINTAXIS
> \- ***\[element\]***
%%

```md
- Primer elemento.
- Segundo elemento.
    - Tercer elemento.
    - Cuarto elemento.
- Quinto elemento.
```

## LISTAS DE TAREAS

Las listas de tareas funcionan de la misma forma que las [listas desordenadas](<md_list.md#LISTAS DESORDENADAS>), con la diferencia que estas tendrán un *check box* con el cual podremos marcar si la tarea está terminada o no, este *check box* se consigue escribiendo unos corchetes y añadiendo un espacio entre estos, de esta forma la tarea estará como *no terminada*, si en vez de un espacio ponemos una *x* esta tarea quedará marcada como terminada y tanto esta como las subtareas quedarán marcadas, sin embargo, si lo sustituimos por cualquier otro carácter, esta tarea quedará marcada como terminada, pero no se tachará, ni esta ni las subtareas.

%%
> [!abstract] SINTAXIS
> \- \[***\[stade\]***\] ***\[task\]***
%%

```md
- [ ] Compra.
    - [M] Comida.
        - [ ] Pan.
        - [ ] Manzana.
    - [x] Libros.
        - [ ] El quijote.
- [ ] Deberes.
    - [ ] Matemáticas.
        - [?] Vectores.
    - [x] Historia.
        - [ ] Segunda guerra mundial.
```
