---
author: Mindusting
corrected: false
tags:
  - Programming/CS
title: Variables en C#
---

# VARIABLES C\#

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools (Variables)](https://www.w3schools.com/cs/cs_variables.php)
> - [W3 Schools (Consstants)](https://www.w3schools.com/cs/cs_variables_constants.php)
> - [W3 Schools (Display Variables)](https://www.w3schools.com/cs/cs_variables_display.php)
> - [W3 Schools (Multiple Variables)](https://www.w3schools.com/cs/cs_variables_multiple.php)
> - [W3 Schools (Identifiers)](https://www.w3schools.com/cs/cs_variables_identifiers.php)
> - [W3 Schools (Data Types)](https://www.w3schools.com/cs/cs_data_types.php)

https://www.geeksforgeeks.org/c-sharp/data-typesc-in-sharp/

| Tipo     | Tamaño  | Default | Descripción                                |
|:-------- |:------- | ------- |:------------------------------------------ |
| `bool`   | 1 bytes | `0`     | Valores `true` o `false`                   |
| `int`    | 4 bytes | `0`     | Entero entre $-2^{31}$ y $2^{31}-1$        |
| `long`   | 8 bytes | `0`     | Entero entre $-2^{63}$ y $2^{63}-1$        |
| `float`  | 4 bytes | `0`     | Decimal con precisión de $6$ a $7$ dígitos |
| `double` | 8 bytes | `0`     | Decimal con precisión de $15$ dígitos      |
| `char`   | 2 bytes | `0`     | Un carácter                                |
| `string` | 2 bytes | `0`     | Una secuencia de caracteres                |

## NÚMEROS ENTEROS

| Tipo     | Tamaño  | Rango                  | Default | Descripción       |
|:-------- |:------- |:---------------------- |:-------:|:----------------- |
| `sbyte`  | 1 byte  | $-2^7$ a $2^7-1$       |   `0`   | 1 byte con signo  |
| `short`  | 2 bytes | $-2^{15}$ a $2^{15}-1$ |   `0`   | 2 bytes con signo |
| `int`    | 4 bytes | $-2^{31}$ a $2^{31}-1$ |   `0`   | 4 bytes con signo |
| `long`   | 8 bytes | $-2^{63}$ a $2^{63}-1$ |  `0l`   | 8 bytes con signo |
| `byte`   | 1 byte  | $0$ a $2^{8}$          |   `0`   | 1 byte sin signo  |
| `ushort` | 2 bytes | $0$ a $2^{16}$         |   `0`   | 2 bytes sin signo |
| `uint`   | 4 bytes | $0$ a $2^{32}$         |   `0`   | 4 bytes sin signo |
| `ulong`  | 8 bytes | $0$ a $2^{64}$         |  `0ul`  | 8 bytes sin signo |

## NÚMEROS DECIMALES

| Tipo      |     Tamaño | Default | Descripción               |
|:--------- | ----------:|:-------:|:------------------------- |
| `float`   |  $4$ bytes |  `0f`   | Precisión de  $6$ dígitos |
| `double`  |  $8$ bytes |  `0d`   | Precisión de $15$ dígitos |
| `decimal` | $16$ bytes |  `0m`   | Precisión de $28$ dígitos |
