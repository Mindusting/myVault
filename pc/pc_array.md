---
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Array(s) en la programación
---

# ARRAYS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [Code Dumped](https://youtu.be/xFMXIgvlgcY)

## BASICO

> Un array es muy similar a las [variables](pc_variable.md) con la diferencia de que estos son capaces de almacenar múltiples valores en secuencia, una forma de entenderlo sería como si tuviéramos una caja con una etiqueta con el nombre de nuestros array y dentro de esta tuviéramos una secuencia de cajas con su propia etiqueta, estás etiquetas indican el número de la caja (*el cual no se puede repetir*) y dentro de estas jamás es donde se guardan los valores.

Un array es un conjunto de valores del mismo tipo, siendo parecidos a las [variables](pc_variable.md), debido a que estos tienen la capacidad de almacenar múltiples valores, para diferenciar cada uno de ellos se usa un "*índice*", este es un número

%%
| IDX | VAL |
|:---:|:---:|
|  0  |  5  |
|  1  |  2  |
|  2  |  7  |

```txt
╔═╦╗
║ ║║
╠═╬╣
╚═╩╝

┌─┬┐
│ ││
├─┼┤
└─┴┘
```
%%

```txt
╔═══╦═══╦═══╦═══╦═══╗
║ 0 ║ 1 ║ 2 ║ 3 ║ 4 ║
╠═══╬═══╬═══╬═══╬═══╣
│ 3 │ 2 │ 5 │ 4 │ 9 │
└───┴───┴───┴───┴───┘
```

## AVANZADO

En esencia, cuando declaramos un array lo que estamos haciendo es usar un [`pointer`](pc_pointer.md) con la dirección de memoria del primer [`byte`](pc_byte.md) de la secuencia de [`bytes`](pc_byte.md) reservados para el array.

Por lo que cuando queremos acceder a un elemento del array la formula que sigue es la siguiente:

$$
newPtr = ptr + index * typeSize
$$
^array-formula

> [!example] Ejemplo
> Imaginemos que tenemos un array de tipo `short` (*dos [bytes](pc_byte.md)*), este sería un [`pointer`](pc_pointer.md) el cual por ejemplo puede tener la dirección `102`, si queremos acceder al tercer (*índice `2`*) elemento del array, tendríamos que seguir la [fórmula](#^array-formula) de antes, obteniendo así el resultado $106 = 102 + 2 * 2$, y ya que es de tipo `short`, tendremos que leer los dos [bytes](pc_byte.md), empezando por el resultado de la [fórmula](#^array-formula).
> $$
> \begin{bmatrix}
> 100 & 101 & \begin{bmatrix}102\end{bmatrix} & 103 & 104 & 105 & \begin{bmatrix}106 & 107\end{bmatrix}
> \end{bmatrix}
> $$

Es debido a esta formula que los arrays tienen tienen una complejidad de tiempo [`O(1)`](pc_big_o.md), ya que da igual la longitud del array, la formula siempre será la misa y por tanto siempre se tardará lo mismo en calcularla.

---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

|  RAM   | 00  | 01  | 10  | 11  |
|:------:|:---:|:---:|:---:|:---:|
| **00** |  N  |  2  |  8  |  3  |
| **01** |  F  |  D  |  E  |  C  |
| **10** |  B  |  6  |  A  |  4  |
| **11** |  7  |  5  |  9  |  1  |
