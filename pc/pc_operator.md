---
author: Mindusting
corrected: false
tags:
  - Programming/Concept
title: Operadores en la programación
---

# OPERADORES

## ARTIMÉTICOS

> [!fail] ESTE APARTADO ESTÁ COMPLETO

| OPER. | DESCRIPCIÓN     | USO      | RES. |
|:-----:|-----------------|----------|-----:|
|   +   | Suma            | 12 + 3   |   15 |
|   -   | Resta           | 12 - 3   |    9 |
|  \*   | Multiplicación  | 12 \* 3  |   36 |
|   /   | División        | 12 / 3   |    4 |
|  \%   | Porcentaje      | 16 \% 3  |    1 |
|  //   | División exacta | 18 // 5  |    3 |
| \*\*  | Elevación       | 12 \*\* 3| 1728 |

## ASIGNACIÓN

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

| OPER. | EJEMPLO   | LO MISMO QUÉ  |
|:-----:|:----------|:--------------|
|    \= | x \= 5    | x \= 5        |
|   +\= | x +\= 3   | x \= x + 3    |
|   -\= | x -\= 3   | x \= x - 3    |
|  \*\= | x \*\= 3  | x \= x \* 3   |
|   /\= | x /\= 3   | x \= x / 3    |
|  \%\= | x \%\= 3  | x \= x \% 3   |
|   //= | x //\= 3  | x \= x // 3   |
| \*\*= | x \*\*= 3 | x \= x \*\* 3 |
|    &= | x &= 3    | x \= x & 3    |
|  \|\= | x \|\= 3  | x \= x \| 3   |
|  \^\= | x \^\= 3  | x \= x \^ 3   |
|  >>\= | x >>\= 3  | x \= x >> 3   |
|  <<\= | x <<\= 3  | x \= x << 3   |

> [!info]
> También existe el operador morsa.

## BIT A BIT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Esta clase de operadores se realizan bit a bit.

| OPER. | HACCIÓN     | USO      | RES. |
|:-----:|:------------|:---------|-----:|
|   &   | and         | 10 & 11  |   10 |
|  \|   | or          | 10 \| 11 |   11 |
|  \^   | xor         | 10 \^ 11 |   01 |
|  \~   | not         | ~3       |   -4 |
|  >>   | shift right | 2 >> 3   |    0 |
|  <<   | shift left  | 2 << 3   |   16 |

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

""" RESULT:
00010000 = x
00000010 = y
01000000 = left
00000100 = right
"""
```

## IDENTIDAD

El operador de identidad compara el contenido de dos variables, si el contenido de estos es el mismo objeto, el resultado será `true`.

```python
x = [3, 2, 7]
y = x
z = [3, 2, 7]

print(f"{x is y = }")
print(f"{x is z = }")

""" RESULTADO:
x is y = True
x is z = False
"""
```

También existe la posibilidad de usa el operador `not`, invirtiendo el resultado de este.

```python
x = [3, 2, 7]
y = x

print(f"{x is not y = }")

""" RESULTADO:
x is not y = False
"""
```

%%
Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.
is y is not son operadores de identidad.
is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.
is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.
Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.
%%

## LÓGICOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

| OPER. | DESCRIPCIÓN       | USO              | RES.  |
|:-----:|:------------------|:-----------------|:------|
|  not  | Puerta lógica not | not(5 < x)       | False |
|  and  | Puerta lógica and | 5 < x and x < 10 | True  |
|   or  | Puerta lógica or  | x < 5 or 10 < x  | False |

[Puertas lógicas](../../Binary/bin.md#%20PUERTAS%20LÓGICAS PUERTAS LÓGICAS>).

## MEMBRESÍA

El operador de membresía indica si un valor u objeto se encuentra dentro de un iterable, como se puede ver en el próximo ejemplo, se usa este operador para comprobar si el valor `2` se encuentra dentro de la lista.

```python
x = [3, 2, 7]
y = 2

print(f"{y in x = }")

""" RESULTADO:
y in x = True
"""
```

También existe la posibilidad de usa el operador `not`, invirtiendo el resultado de este.

```python
x = [3, 2, 7]
y = 2

print(f"{y not in x = }")

""" RESULTADO:
y not in x = False
"""
```

%%
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
in y not in son operadores de pertenencia.
in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
%%

## RELACIONALES

| OPER. | DESCRIPCIÓN       | USO       | RES.  |
|:-----:|-------------------|-----------|-------|
|   >   | Mayor qué         | 12 > 3    | True  |
|   <   | Menor qué         | 12 < 3    | False |
| \=\=  | Igual qué         | 12 \=\= 3 | False |
|  >\=  | Mayor o igual qué | 12 >\= 3  | True  |
|  <\=  | Menor o igual qué | 12 <\= 3  | False |
|  !\=  | Diferente qué     | 12 !\= 3  | True  |
