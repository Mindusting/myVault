---
author: Mindusting
corrected: false
tags:
  - Math/NumberSystem/Binary
title: Binario
---

# BINARIO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar la conversión de decimal a binario.
> > - [ ] Explicar la conversión de binario a decimal.
> > - [ ] Explicar la suma en binario.
> > - [ ] Explicar la resta en binario.
> > - [ ] Explicar la multiplicación en binario.
> > - [ ] Explicar la división en binario.

El **binario** es un *sistema numérico* basado en el uso de dos estados (*generalmente representados con **cero** y **uno***) para contabilizar.

## NÚMEROS ENTEROS

Para empezar a contar en **binario** empezaremos a ver como se representan los primeros números; número 0 en [**decimal**](math_ns_dec.md) es representado en **binario** con un 0, el 1 en en [**decimal**](math_ns_dec.md) también es un 1 en **binario**, sin embargo, a partir de este punto, a diferencia del [**decimal**](math_ns_dec.md) en donde podemos seguir usando el mismo dígito con símbolos distintos, en el **binario** ya nos hemos quedado sin símbolos (*estados*), por lo que necesitaremos nuevos dígitos.

| BINARIO | DECIMAL |
| -------:| -------:|
|       0 |       0 |
|       1 |       1 |
|      10 |       2 |
|      11 |       3 |
|     100 |       4 |
|     101 |       5 |
|     110 |       6 |
|     111 |       7 |
|     ... |     ... |

Si te fijas, el valor de cada dígito el doble respecto al anterior; a continuación puede ver una tabla con los primeros 8 valores de cada dígito:

| ÍNDICE:      |  ...  |   7   |   6   |   5   |   4   |   3   |   2   |   1   |   0   |
|:------------ |:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **VALOR:**   |  ...  |  128  |  64   |  32   |  16   |   8   |   4   |   2   |   1   |
| **FÓRMULA:** | $2^i$ | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |

> [!important] IMPORTANTE
> - Fíjate que el *índice* no es más que la posición del dígito contando desde derecha a izquierda y empezando por 0.
> - Fíjate también que la fórmula siempre es la misma ($2^i$), siendo $i$ el *índice* de la posición del dígito.

### SUMA

```txt
    110 = 6
+   101 = 5
-------
   1011 = 11
```

### MULTIPLICACIÓN

```txt
    11010 = 26
  x   101 = 5
  -------
    11010
   00000
+ 11010
---------
 10000010 = 130
```
