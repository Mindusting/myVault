---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Struct
title: Módulo Struct en Python
---

# STRUCT

> [!help] REFERENCIAS WEB
> - [Python doc](https://docs.python.org/3/library/struct.html)
> 
> YouTube:
> - [NeuralNine](https://youtu.be/gViM3ZuDQrw)

Este módulo es usado para transformar los valores de Python en [`byte`](variables/py_byte.md) y viceversa, permitiendo así guardar información de forma compacta en archivos

## STRING DE FORMATO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

| Character | Byte order             | Size     | Alignment |
| --------- | ---------------------- | -------- | --------- |
| `@`       | native                 | nativew  | native    |
| `=`       | native                 | standard | none      |
| `<`       | little-endian          | standard | none      |
| `>`       | big-endian             | standard | none      |
| `!`       | network (= big-endian) | standard | none      |

| Format | C Type             | Python type       | TAMAÑO EN BYTES |
|:------:|:------------------ |:----------------- |:---------------:|
|  `x`   | pad byte           | no value          |                 |
|  `c`   | char               | bytes of length 1 |        1        |
|  `b`   | signed char        | integer           |        1        |
|  `B`   | unsigned char      | integer           |        1        |
|  `?`   | _Bool              | bool              |        1        |
|  `h`   | short              | integer           |        2        |
|  `H`   | unsigned short     | integer           |        2        |
|  `i`   | int                | integer           |        4        |
|  `I`   | unsigned int       | integer           |        4        |
|  `l`   | long               | integer           |        4        |
|  `L`   | unsigned long      | integer           |        4        |
|  `q`   | long long          | integer           |        8        |
|  `Q`   | unsigned long long | integer           |        8        |
|  `n`   | `ssize_t`          | integer           |                 |
|  `N`   | `size_t`           | integer           |                 |
|  `e`   | (6)                | float             |        2        |
|  `f`   | float              | float             |        4        |
|  `d`   | double             | float             |        8        |
|  `s`   | char\[\]           | bytes             |                 |
|  `p`   | char\[\]           | bytes             |                 |
|  `P`   | void*              | integer           |                 |

## FUNCIONES

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
