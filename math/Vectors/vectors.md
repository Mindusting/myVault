---
author: Mindusting
corrected: false
tags:
  - Math/Vector
title: Vectores
---

# VÍDEO TUTORIALES

[3Blue1Brown (Vectors)](https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&si=9YzrArg_yeN4oTzZ)
[El traductor de ingeniería (Vectors)](https://youtu.be/eXA4806YuqY)

# VECTORES

Un vector es un conjunto de números ordenados.

---

- Magnitud.
- Dirección.
- Sentido.

---

La magnitud del vector `(3, 4)` tiene una magnitud de `5`.

---

```txt
SUMA DE VECTORES

->  ->  ->
A + B = C

----->   ------>   ----->
(3, 4) + (1, -3) = (4, 1)

RESTA DE VECTORES

->  ->  ->
A - B = C

----->   ------>   ----->
(3, 4) - (1, -3) = (2, 7)
```

## MAGNITUD

| CALCULAR MAGNITUD  |
|:------------------:|
| `sqrt(x^2 + y^2)` |

```py
import math

def calculate_dis(x: float, y: float) -> float:
    return math.sqrt((x ** 2) + (y ** 2))
```



|    CALCULAR MAGNITUD     |
|:------------------------:|
| `sqrt(x^2 + y^2 + z^2)` |

```py
import math

def calculate_dis(x: float, y: float, z: float) -> float:
    return math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
```

## DIRECCIÓN

| CALCULAR DIRECCIÓN |
|:------------------:|
|   `atan(y / x)`   |

```py
import math

def calculate_dir(x: float, y: float) -> float:
    if x == 0:
        return math.pi * (0.5 if y > 0 else 1.5)
    else:
        return math.atan(y / x)
```

```py
def point_to(
    self,
    coordenates: tuple[float, float] | list[float, float] | np.ndarray[np.float64]
) -> None:
    v_direction: np.ndarray = coordenates - self.position
    if v_direction[0] == 0:
        self.direction: float = math.degrees(math.pi * (0.5 if v_direction[1] > 0 else 1.5))
    else:
        self.direction: float = (math.degrees(math.atan(v_direction[1] / v_direction[0])) + (180 if v_direction[0] < 0 else 0)) % 360
```

## TRANSFORMACIÓN

![dibujo_tranformacion_de_vectores](dibujo_tranformacion_de_vectores.md)
