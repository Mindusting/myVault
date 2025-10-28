---
author: Mindusting
corrected: false
tags:
  - Mermaid/QuadrantChart
title: Diagrama de quadrantes en Mermaid
---

# DIAGRAMA CIRCULAR EN MERMAID

> [!fail]- ESTE APATADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [Mermaid doc (Quadrant Chart)](https://mermaid.js.org/syntax/quadrantChart.html)

Cuadrantes:
1. Arriba a la derecha.
2. Arriba a la izquierda.
3. Abajo a la izquierda.
4. Abajo a la derecha.

```mermaid
quadrantChart
    title Mapa político
    x-axis Poca livertad social --> Mucha livertad social
    y-axis Poca livertad eco. --> Mucha livertad eco.
    quadrant-1 Liveralismo
    quadrant-2 Derecha
    quadrant-3 Totalitarismo
    quadrant-4 Izquierda
    Adelio: [0.65, 0.80]
    Adelia: [0.80, 0.65]
```
