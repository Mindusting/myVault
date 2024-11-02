---
author: Mindusting
corrected: false
tags:
  - Math/Trigonometry
title: Trigonometría
---

# TRIGONOMETRÍA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> PI / 2 radianes = 90°
> PI radianes = 180°
> 1.5 PI radianes = 270°
> 2 PI radianes = 360°
> 
> `cos(h / a)`
> `sin(h / b)`
> `tan(b / a)`

![#center](trig_draw.md)

%%
```java
public static double vectorDirection(double[] vector) {
    double res = 0.0; // Direction in Radians
    if (vector[0] == 0 && vector[1] == 0) {
        res = 0;
    } else {
        res = Math.atan(vector[1] / vector[0]);
        if (vector[0] < 0) {
            res += Math.PI;
            if (vector[1] > 0) {
                res -= HALF_PI;
            }
        }
    }
    return trueMod(res, TWO_PI);
}
```
%%

## GRADOS Y RADIANES
`α`
https://es.wikipedia.org/wiki/Alfabeto_griego