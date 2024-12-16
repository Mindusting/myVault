---
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Array(s) en la programación
---

# ARRAYS

> [!help] REFERENCIAS WEB
> - [¿Qué son los punteros en programación?](pc_pointer.md)
> YouTube:
> - [Code Dumped](https://youtu.be/xFMXIgvlgcY)

## BÁSICO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Terminar de explicar lo básico de los arrays.
> > - [ ] Poner ejemplo de array.

> Un **array** es muy similar a las [variables](pc_variable.md) con la diferencia de que estos son capaces de almacenar múltiples valores en secuencia, una forma de entenderlo sería como si tuviéramos una caja con una etiqueta con el nombre de nuestros array y dentro de esta tuviéramos una secuencia de cajas con su propia etiqueta, estás etiquetas indican el número de la caja (*el cual no se puede repetir*) y dentro de estas jamás es donde se guardan los valores.

Un array es un conjunto de valores del mismo tipo, siendo parecidos a las [variables](pc_variable.md), debido a que estos tienen la capacidad de almacenar múltiples valores, para diferenciar cada uno de ellos se usa un "*índice*", este es un número

## AVANZADO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que pasa si te sales del rango de array.

En esencia, cuando declaramos un array lo que estamos haciendo es usar un [`pointer`](pc_pointer.md) con la dirección de memoria del primer [`byte`](pc_byte.md) de la secuencia de [`bytes`](pc_byte.md) reservados para el array.

Por lo que cuando queremos acceder a un elemento del **array** la formula que sigue es la siguiente:

$$
ptr + index * typeSize = newPtr
$$
^array-formula

Es debido a esta formula que los arrays tienen tienen una complejidad de tiempo [`O(1)`](pc_big_o.md), ya que da igual la longitud del array, la formula siempre será la misa y por tanto siempre se tardará lo mismo en calcularla.

## ACTIVIDADES

![](pc_pointer#^random-table)

> [!example] Ejemplo
> Si nuestro [**puntero**](pc_pointer.md) tiene la **dirección** `47` (*`70` en decimal*), cada elemento del **array** ocupa 4 [`bytes`](pc_byte.md) y queremos acceder al elemento 5, haríamos el siguiente cálculo con la [formula de los **array**](#^array-formula):
>
> $$70 + 5 * 4 = 90$$
>
> El resultado es `90` (*`5A` en [hexadecimal](pc_number_system.md#HEXADECIMAL)*), por lo que deberemos obtener su **valor** y la de los tres siguientes [`bytes`](pc_byte.md) para obtener los cuatro del elemento en cuestión, interpretando los como un solo **valor** el resultado es `4045627429`.
>
> ---
>
> Así es como he calculado el **valor** de los cuatro [`bytes`](pc_byte.md) como un único número:
> ```python
> print(int("F1236025", 16))
> # SALIDA:
> # 4045627429
> ```

> [!exercise] Ejercicios
> 1. Obtén el **valor** del elemento 3 del [**puntero**](pc_pointer.md) con **dirección** `B8` (*`184` en decimal*) teniendo en cuanta que cada elemento ocupa 8 [`bytes`](pc_byte.md).
> 2. Obtén el **valor** del elemento 9 del [**puntero**](pc_pointer.md) con **dirección** `16` (*`22` en decimal*) teniendo en cuanta que cada elemento ocupa 2 [`bytes`](pc_byte.md).
