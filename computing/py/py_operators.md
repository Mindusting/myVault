---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Operators
title: Operadores de Python
---

# OPERADORES

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## ARITMÉTICOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

| OPERADOR | DESCRIPCIÓN     | USO      | RES. |
|:--------:|-----------------|----------|-----:|
|     +    | Suma            | 12 + 3   |   15 |
|     -    | Resta           | 12 - 3   |    9 |
|    \*    | Multiplicación  | 12 \* 3  |   36 |
|     /    | División        | 12 / 3   |    4 |
|    \%    | Porcentaje      | 16 \% 3  |    1 |
|    //    | División exacta | 18 // 5  |    3 |
|   \*\*   | Elevación       | 12 \*\* 3| 1728 |
^arithmetic-operators-table

## BIT A BIT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Esta clase de operadores se realizan bit a bit.

| OPER. | HACCIÓN     | USO      | RES. |
|:-----:|:------------|:--------:|:----:|
|   &   | and         |  10 & 11 |  10  |
|  \|   | or          | 10 \| 11 |  11  |
|  \^   | xor         | 10 \^ 11 |  01  |
|  \~   | not         |    ~3    |  -4  |
|  >>   | shift right |  2 >> 3  |   0  |
|  <<   | shift left  |  2 << 3  |  16  |
^bit-operators-table

> [!info]
> En le case del not, hay que tener en cuenta que tiene parte negativa, es por esto que `~3` termina siendo `-4` ya que los resultados serían `00000011` y `11111100`.
>
> En el caso de los shift resulta que se desplaza a la izquierda o a la derecha el número que se encuentra a la izquierda, se desplaza en binario el número de bits que indique el número que se encuentre a la derecha en la dirección que apunte el operador.

```python
x = 16
y = 2
l = x << y
r = x >> y

print(f"{bin(x)[2:]:>08} = x")
print(f"{bin(y)[2:]:>08} = y")
print(f"{bin(l)[2:]:>08} = left")
print(f"{bin(r)[2:]:>08} = right")
# RESULT:
# 00010000 = x
# 00000010 = y
# 01000000 = left
# 00000100 = right
```

## LÓGICOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Para la siguiente tabla, supongamos que `x = 6`.

| OPER. | DESCRIPCIÓN       | USO              | RES.  |
|:-----:|:------------------|:-----------------|------:|
|  and  | Puerta lógica and | 5 < x and x < 10 | True  |
|   or  | Puerta lógica or  | x < 5 or 10 < x  | False |
|  not  | Puerta lógica not | not(5 < x)       | False |
^logical-operators-table

## RELACIONAL

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

| OPER. | DESCRIPCIÓN       | USO       | RES.  |
|:-----:|-------------------|-----------|-------|
|   >   | Mayor qué         | 12 > 3    | True  |
|   <   | Menor qué         | 12 < 3    | False |
| \=\=  | Igual qué         | 12 \=\= 3 | False |
|  >\=  | Mayor o igual qué | 12 >\= 3  | True  |
|  <\=  | Menor o igual qué | 12 <\= 3  | False |
|  !\=  | Diferente qué     | 12 !\= 3  | True  |
^relational-operators-table

## MORSA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
