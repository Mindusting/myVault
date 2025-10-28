---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: String en Java
---

# STRING EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

- [Format String](../java_format_string.md)

| SECUENCIA DE ESCAPE | REPRESENTA            |
|:-------------------:|:--------------------- |
|         \b          | Retroceso             |
|         \t          | Tabulación horizontal |
|         \n          | Nueva line            |
|         \r          | Retorno de carro      |
|         \f          | Salto de página       |
|         \\"         | Dobles comillas       |
|         \\'         | Comilla simple        |
|         \\\         | Contra barra          |

|     |                              |
|:---:|:---------------------------- |
| %d  | boolean                      |
| %d  | byte<br>short<br>int<br>long |

## LONGITUD DE UN STRING

Para obtener el número de caracteres por el que está confirmado un `String` podremos usar el [método](../java_method.md) `length`; este devulve un [`int`](../java_variable.md) indicando la longitud del `String`.

> [!abstract] SINTAXIS
> ***\[string\]***.length()

## A MAYÚSCULAS

> [!abstract] SINTAXIS
> ***\[string\]***.toUpperCase()

## A MINÚSCULAS

> [!abstract] SINTAXIS
> ***\[string\]***.toLowerCase()