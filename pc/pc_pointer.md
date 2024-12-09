---
aliases:
  - Pointers in programing
author: Mindusting
corrected: true
tags:
  - Programming/Concept
title: Punteros en la programación
---

# POINTERS

Los **punteros** en programación se entienden como una [variable](pc_variable.md) que almacena una **dirección de memoria RAM**, sencillamente eso.

Debido al objetivo que tiene este tipo de dato su tamaño es dependiente del número de bits del sistema en el que se esté ejecutando el programa, esto es por que en un sistema de **32 bits** únicamente necesitamos 4 [`bytes`](pc_byte.md) para alcanzar a cubrir todas las direcciones de memoria, y en los sistemas de **64 bits** son necesarios 8 [`bytes`](pc_byte.md).

Por lo general cuando se trabaja con **punteros** se suele decir que tiene una **dirección** y un **valor**:
- **Dirección**: es el número almacenado en el **puntero**, representando este una dirección de memoria.
- **Valor**: es el número del [`byte`](pc_byte.md) almacenado en la posición de memoria al que apunta la *dirección* del puntero, en el caso de que se quiera obtener un tipo más grande que el [`byte`](pc_byte.md), se entenderá como *valor* el conjunto de [`bytes`](pc_byte.md) seguidos al que está siendo apuntado, incluyendo este último (*un `long` en [C](../c/c.md) serían 8 [`bytes`](pc_byte.md)*).

## POINTER A NULL

Cuando un **puntero** almacena la dirección de memoria `0` se dice que apunta a `null` (*"no apunta a ningún sitio"*), suele representar que aún no se le a asignado ninguna **dirección** al **puntero**. Es por esto que la primera **dirección** de memoria nunca se usa.

## ACTIVIDADES

|  RAM  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  A  |  B  |  C  |  D  |  E  |  F  |
|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | 00  | B6  | 66  | C1  | 27  | D1  | AE  | C9  | 59  | DA  | 37  | DC  | 7F  | 20  | DB  | 97  |
| **1** | 10  | E1  | 71  | 9B  | 16  | 9C  | 19  | 2F  | 8F  | C2  | ED  | 5C  | 85  | 34  | 61  | 5F  |
| **2** | 90  | B2  | 21  | BD  | 5D  | F0  | 74  | F8  | EA  | 30  | FC  | 3A  | 1D  | 63  | 87  | 3D  |
| **3** | A0  | BE  | C6  | D2  | A8  | 48  | F6  | 4D  | 22  | 80  | 84  | AA  | E9  | 2D  | B9  | 32  |
| **4** | FD  | F2  | 46  | 7A  | 2E  | AB  | C3  | 39  | C0  | 40  | C0  | 50  | 56  | C8  | 9E  | 45  |
| **5** | 3E  | 2B  | 15  | 70  | 72  | 10  | D9  | 3B  | 78  | E5  | F1  | 23  | 60  | 25  | 67  | 86  |
| **6** | EF  | 38  | DF  | D8  | FB  | 5A  | D4  | BB  | F3  | 52  | 40  | FF  | 8D  | DE  | D5  | A5  |
| **7** | 1A  | 4B  | 7D  | 9D  | 49  | 91  | BA  | 68  | 24  | B3  | A0  | FE  | 82  | 29  | 2A  | D0  |
| **8** | 62  | AD  | 80  | 65  | 92  | 41  | 33  | B0  | 90  | BF  | FA  | 44  | 4F  | 9F  | B5  | 96  |
| **9** | 47  | 8B  | 58  | 75  | 57  | 99  | 3F  | 79  | 12  | E0  | 8E  | A1  | 5B  | A9  | 76  | EE  |
| **A** | 7C  | 9A  | 7B  | E8  | 1B  | E7  | B4  | 36  | 42  | BC  | 6D  | A6  | A3  | 4E  | 60  | E4  |
| **B** | 35  | 4A  | 73  | 11  | 1E  | 81  | 6C  | 77  | 30  | 98  | 1C  | 20  | B0  | CE  | 70  | 26  |
| **C** | 31  | 4C  | C4  | 6F  | 8C  | D7  | CB  | 93  | 89  | D6  | 17  | CA  | 43  | 88  | 3C  | A4  |
| **D** | B8  | 64  | 94  | 54  | 7E  | E2  | 83  | B7  | 18  | 51  | F7  | 13  | CF  | 69  | D0  | C5  |
| **E** | EC  | AF  | CD  | 6E  | AC  | 5E  | 53  | E0  | F9  | A2  | 6B  | A7  | 95  | DD  | 6A  | 55  |
| **F** | D3  | 8A  | EB  | E3  | 2C  | 50  | E6  | CC  | F5  | 28  | C7  | 1F  | 14  | B1  | F0  | F4  |
^random-table

> [!example] Ejemplo
> Imaginemos que tenemos un **puntero** con la dirección `236`, para poder encontrar la posición en la tabla tendremos que convertir el número a [hexadecimal](pc_number_system#HEXADECIMAL), siendo este `EC`, por lo que apunta a la fila `E` columna `C`, tendiendo este el valor `95`, siendo en decimal `149`.
>
> Y si interpretamos el **valor** de nuestro **puntero** lo interpretamos como si fuese otro **puntero** este nos daría el valor `99`, siendo en decimal `153`.

> [!exercise] Ejercicios
> 1. Descubre cuál es el **valor** del de la **dirección** `6F`, luego interpreta el **valor** como una nueva **dirección** y encuentra el **valor** de esta.
> 2. Encuentra la **dirección** del **valor** `FF`.

> [!note] Nota
> Si has terminado de entender el funcionamiento de los punteros te recomiendo que vayas al apartado de [arrays en la programación](pc_array.md) para que puedas ver uno de los usos más comunes que se le puede dar a un **puntero**.
