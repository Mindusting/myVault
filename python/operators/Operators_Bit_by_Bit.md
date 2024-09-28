---
author: Mindusting
corrected: false
tags:
  - Programming/Python
---

Esta clase de operadores se realizan bit a bit.

| OPER. | HACCIÓN     | USO      | RES. |
|:-----:|:------------|:--------:|:----:|
|   &   | and         |  10 & 11 |  10  |
|  \|   | or          | 10 \| 11 |  11  |
|  \^   | xor         | 10 \^ 11 |  01  |
|  \~   | not         |    ~3    |  -4  |
|  >>   | shift right |  2 >> 3  |   0  |
|  <<   | shift left  |  2 << 3  |  16  |

>[!info]
>En le case del not, hay que tener en cuenta que tiene parte negativa, es por esto que `~3` termina siendo `-4` ya que los resultados serían `00000011` y `11111100`.
>
>En el caso de los shift resulta que se desplaza a la izquierda o a la derecha el número que se encuentra a la izquierda, se desplaza en binario el número de bits que indique el número que se encuentre a la derecha en la dirección que apunte el operador.

```py
x = 16
y = 2
l = x << y
r = x >> y

print(f"{bin(x)[2:]:>08} = x")
print(f"{bin(y)[2:]:>08} = y")
print(f"{bin(l)[2:]:>08} = left")
print(f"{bin(r)[2:]:>08} = right")

""" RESULT:
00010000 = x
00000010 = y
01000000 = left
00000100 = right
"""
```
