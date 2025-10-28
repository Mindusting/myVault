---
author: Mindusting
corrected: false
tags:
  - Math/Logarithm
title: Logaritmo
---

# LOGARITMO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

El logaritmo de un número consistiría en hacer el proceso inverso a la elevación, la fórmula que se utiliza es la siguiente:

$$
log_{b}(x)
$$

Donde $b$ es la *base* en la que se quiere hacer la operación y $x$ es el número sobre el que queremos aplicar la función.

## LOGARITMO NATURAL

Para calcular el *logaritmo natural* la la base que se utiliza es el número $e$, gracias a este podemos calcular el logaritmo que nosotros queramos.

```java
public class MyMath {
    public static void main(String[] args) {

        //                    x             b
        double res = Math.log(8) / Math.log(2);

        System.out.println(res);
    }
}
```

```python
import math

#              x             b
print(math.log(8) / math.log(2))
```

Como se ha visto en los ejemplos anteriores si dividimos el resultado del logaritmo natural del número que nosotros queramos por otro igual con la base que queramos, el resultado es el número de dígitos que necesitamos para poder almacenar ese número, en este caso se ha usado el 8, y en binario, el si queremos almacenar un número entre el 0 y el 7 (*rango de 8 números*), necesitamos 3 bits, siendo este el resultado de la operación de los ejemplos.
