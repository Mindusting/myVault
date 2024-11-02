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

Debido al objetivo que tiene este tipo de dato su tamaño es dependiente del número de bits del sistema en el que se esté ejecutando el programa, esto es debido a que en un sistema de **32 bits** únicamente necesitamos 4 [`bytes`](pc_byte.md) para alcanzar a cubrir todas las direcciones de memoria, y en los sistemas de **64 bits** se necesitan 8 [`bytes`](pc_byte.md) para abarcar todas las direcciones de memoria disponibles.

Por lo general cuando se trabaja con **punteros** se suele decir que tiene una **dirección** y un **valor**:
- **Dirección**: es el número almacenado en el **puntero**, representando este una dirección de memoria.
- **Valor**: es el número del [`byte`](pc_byte.md) almacenado en la posición de memoria al que apunta la *dirección* del puntero, en el caso de que se quiera obtener un tipo más grande que el [`byte`](pc_byte.md), se entenderá como *valor* el conjunto de [`bytes`](pc_byte.md) seguidos al que está siendo apuntado, incluyendo este último (*un `long` en [C](../c/c.md) serían 8 [`bytes`](pc_byte.md)*).
