---
aliases:
  - Pointers in programing
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Variables en la programación
---

> [!fail] ESTE ARCHIVO ESTÁ INCOMPLETO

Una variable no es más que un espacio reservado de la memoria RAM para poder guardar un valor, estando este asociado a un nombre.

Dependiendo del lenguaje, las variables pueden ser de tipazo fuerte o débil, el tipado fuerte implica que una vez se declara una variable el tipo de esta no se puede cambiar, el tipado débil implica lo contrario.

# TIPOS DE VARIABLE

Las variables pueden ser principalmente de cuatro tipos, teniendo esto a su vez subcategorías.

- Entero (`int`)
- Decimal (`float`)
- Booleano (`boolena`)
- Carácter (`char`)

## ENTEROS

En una variable entera se puede guardar por ejemplo el número de clientes de una empresa, ya que sería imposible que tuviéramos medio cliente.

### TIPOS DE ENTEROS

Los esteros suelen estar subdivididos en las siguientes categorías:

| SPACE   | NAME   |
|:------- |:------ |
| 1 byte  | `byte` |
| 2 bytes | short  |
| 4 bytes | int    |
| 8 bytes | long   |

Dependiendo del número que queramos almacenar tendremos que usar un tipo u otro para escoger el número de bytes que nos permita realizar la función que queremos pero que al mismo tiempo consuma la menor cantidad de bytes por cuestiones de optimización.

### CON O SIN SIGNO

>[!fail] HAY QUE AÑADIR UN ENLACE AL APARTADO EN EL QUE SE EXPLICA CÓMO SE ALMACENA EL BINARIO

Los números enteros puedes o no tener signo, esto afectará a la forma en la que se guardan los números, un entero sin signo solo podrá almacenar el cero y número naturales, mientras que los que tienen signo podrán almacenar números enteros (Tanto positivos como negativos incluyendo el cero).

Como se ha mencionado anteriormente, los números, dependiendo de si tienen signo o no, se almacenan de forma distinta, para poder visualizarlo mejor, veremos el ejemplo de como se almacena el número 5 en binario.

Si es *unsigned* (**sin signo**), se almacenará de la siguiente forma:

```txt
╔════╦════╦════╦════╗
║  8 ║  4 ║  2 ║  1 ║
╠════╬════╬════╬════╣
│  0 │  1 │  0 │  1 │
└────┴────┴────┴────┘
```

En este caso, ya que tenemos cuatro bits, el rango de número que podremos almacenar será entre cero y quince, sin embargo, si el número es *signed* (**con signo**) podremos almacenar tanto el número cinco como el menos cinco, sacrificando la mitad de los números positivos para poder almacenar los número negativos.

```txt
╔════╦════╦════╦════╗
║ -8 ║  4 ║  2 ║  1 ║
╠════╬════╬════╬════╣
│  0 │  1 │  0 │  1 │
└────┴────┴────┴────┘

╔════╦════╦════╦════╗
║ -8 ║  4 ║  2 ║  1 ║
╠════╬════╬════╬════╣
│  1 │  0 │  1 │  1 │
└────┴────┴────┴────┘
```

En este ejemplo de encima, se pueden ver los dos números en decimal, tanto el cinco como el menos cinco.

### CAPACIDAD DE LOS ENTEROS

Si quieres saber hasta qué número podemos almacenar en cada uno de estos tipos, primero tendremos que saber el número de bits que usa, para ello seguimos la siguiente fórmula.

`n_bytes * 8 = n_bits`

Un ejemplo de ello es el siguiente:

`2 * 8 = 16`

---

Después de saber el número de bits usaremos la siguiente fórmula para saber el número de combinaciones que podemos hacer con ese número de bits.

`2 ^ n_bites = n_combinaciones`

Un ejemplo de ello es el siguiente:

`2 ^ 16 = 65536`

---

Ahora, dependiendo de si el número tiene signo o no, tendremos que seguir una fórmula u otra.

#### SIN SIGNO

Si el número no tiene signo se usa la siguiente fórmula.

`n_combinaciones - 1 = max_num`

Un ejemplo de ello es el siguiente:

`65536 - 1 = 65535`

Esta fórmula nos otorga el número más alto que podemos obtener (En el caso del ejemplo es `65535`), siendo el más bajo el cero.

#### CON SIGNO

Si el número tiene signo se usan las siguientes fórmulas:

```txt
0 - (n_combinaciones / 2) = min_num

-1 - min_num = max_num
```

Un ejemplo de ello es el siguiente:

```txt
0 - (65536 / 2) = -32768

-1 - (-32768) = 32767
```

Estas fórmulas nos otorgan el número más alto (En el caso del ejemplo es `32767`) y más bajo (En el caso del ejemplo es `-32768`) que podemos obtener.

## DECIMALES

En una variable decimal podríamos almacenar por ejemplo la altura de una persona en metros (Ej.: `1.75` metros).

### TIPOS DE DECIMALES

Los decimales suelen estar subdivididos en las siguientes categorías:

- (**4 bytes**) float
- (**8 bytes**) double

%%
Dependiendo del número que queramos almacenar tendremos que usar un tipo u otro para escoger el número de bytes que nos permita realizar la función que queremos pero que al mismo tiempo consuma la menor cantidad de bytes por cuestiones de optimización.
%%

Dependiendo de la precisión que queramos tener tendremos que usar un tipo u otro, tendremos que tener en cuenta que cuanta más precisión queramos más espacio ocupará.

>[!warning]
>>[!fail] HAY QUE AÑADIR EL ENLACE AL APARTADO EN EL QUE SE EXPLICA CÓMO SE ALMACENA EL BINARIO DECIMAL
>
>Los número decimales tienen un pequemos margen de error, el porqué de esto se explica más a fondo en la [documentación del funcionamiento del binario](), por lo que siempre recomiendo que a la hora de comparar dos número decimales y queremos saber si son iguales, deberemos redondear los decínales a una cifra que sea segura.

### SOLUCIONAR PROBLEMA DE PRECISIÓN

>[!fail] AÑADIR LINK A LOS OPERADORES

A la hora de comparar dos números decimales con los [operadores](), el margen de error nos puede pasar malas jugadas por lo qué recomiendo redondear los números antes de hacer la comparación, en el caso de ser de tipo `float` recomiendo redondear al decimal seis mientras que los `doubles` al quince.

## BOOLEANO

## CARÁCTER