---
author: Mindusting
corrected: false
tags:
  - Math/Trigonometry
title: Trigonometría
---

# TRIGONOMETRÍA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > PI / 2 radianes = 90°
> > PI radianes = 180°
> > 1.5 PI radianes = 270°
> > 2 PI radianes = 360°
> > 
> > `cos(h / a)`
> > `sin(h / b)`
> > `tan(b / a)`

![#center](trig_draw.md)

```python
import math, numpy as np

class Trigonometry:

    @classmethod
    def direction(cls, dx: float, dy: float) -> float:
        """
        Devuelve la dirección del vector de
        dos dimentiones en radianes.
        """
        ret: float = None
        if dx != 0:
            ret: float = math.atan(dy / dx)
            if   dx <  0: ret += math.pi
            elif dy <= 0: ret += math.tau
        else:
            if dy == 0:
                ret = 0
            elif dy >= 0: # PI * 0.5
                ret = 1.5707963267948966
            else: # PI * 1.5
                ret = 4.71238898038469
        return ret
    
    @classmethod
    def distance(cls, dx: float, dy: float) -> float:
        """
        Return de distance of the vector.
        """
        return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    
    @classmethod
    def vectorice(cls, dir_rad: float) -> np.ndarray:
        """
        Devuelve un vector unitario de la
        dirección en radianes.
        """
        return np.array((math.cos(dir_rad), math.sin(dir_rad)))
```

## GRADOS Y RADIANES
`α`
https://es.wikipedia.org/wiki/Alfabeto_griego