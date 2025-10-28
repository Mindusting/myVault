---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable
title: Variables en Python
---

# INT EN PYTHON

>[!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Releer la documentación del `int` para ver que se podría mejorar.

> [!help]- REFERENCIAS WEB
> - [Python doc (int)](https://docs.python.org/3/library/functions.html#int)

Un ejemplo de la declaración de variables de números enteros sería el siguiente:

```python
num1 = 3
num2: int = 2
```

Los números enteros están representados por la clase `int`, esta permite por ejemplo, transformar un valor de tipo [string](#STRING) a uno entero.

```python
num1: int = int("3")
num2: int = 2

print(f"{num1 + num2 = }")
# SALIDA:
# num1 + num2 = 5
```

En el ejemplo anterior se puede ver cómo se transforma el **texto** `3` al **número entero** `3`, gracias a esto es por lo que se pueden sumar los dos números, ya qué los textos no se suman, se unen, si quieres comprobar esto último puedes ejecutar el siguiente código.

```python
num1: str = "3"
num2: str = "2"

print(f"{num1 + num2 = }")
# SALIDA:
# num1 + num2 = '32'
```

## DE OTRAS BASES AL DECIMAL

La clase `int` permite transformar un texto que represente un valor que no sea de *base 10* en *base 10*, esto se puede hacer pasándole a esta clase dos argumentos, el texto con el valor a combertir a decimal y la base del valor introducido.

```python
byte_in_hex: str = "ff"

print(int(byte_in_hex, 16))
# SALIDA:
# 255
```

En el anterior ejemplo se puede ver cómo se transforma el valor `ff` en `255`, pasando del **hexadecimal** al **decimal**, también podríamos hacer lo mismo con el binario.

```python
num_in_bin: str = "10010"

print(int(num_in_bin, 2))
# SALIDA:
# 18
```

## REPRESENTACIÓN EN FORMA DE FRACCIÓN

Se puede convertir un número entero en una fracción representada con una [tupla](py_tuple.md), la cual contendrá el **dividendo** (`numerator`) y el **divisor** (`denominator`), para ello deberemos hacer uso de la función `as_integer_ratio`.

```python
int_ratio: tuple = int.as_integer_ratio(3)

print(int_ratio)
# SALIDA:
# (3, 1)
```

En este ejemplo podemos ver cómo se obtiene la [tupla](py_tuple.md) con el **dividendo** (`numerator`) y **divisor** (`denominator`) del números entero.

En el caso de los número enteros, por sí solos, este método no tiene mucho sentido, es cuando se combina este método con el de los valores [float](#FLOAT) cuando podemos darle un mejor uso.

#### PROPIEDADES

Para obtener los valores de forma fraccionaria, no hace falta usar el método `as_integer_ratio`, ya que se puede obtener estos valores en forma de propiedades del número entero.

```python
print((8).numerator)
print((8).denominator)
# SALIDA:
# 8
# 1

######################

num: int = 8

print(num.numerator)
print(num.denominator)
# SALIDA:
# 8
# 1
```

## INT BIT

>[!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Revisar toda la documentación y ver que se puede mejorar.
> > - [ ] Reparar los enlaces rotos.

> [!tip]
> Para poder manejar estos métodos primero debes saber somo funcionan los [bytes](#BYTES) en python.

Para convertir un número entero a un conjunto de **bytes**, se puede usar el método `to_bytes`.

```python
print((18).to_bytes())
print(int.to_bytes(18))

print((360).to_bytes(2))
print(int.to_bytes(360, 2))
```

Sí el número entero es demasiado grande, tendremos que indicar el número de **bytes** que requiere, como se puede ver en el segundo grupo de `print`s del ejemplo.

Para poder transformar un grupo de bytes a un número entero se usa el método `from_bytes`.

```python
int_in_bytes: bytes = (360).to_bytes(2)

print(int.from_bytes(int_in_bytes))
```

> [!info]
> Por cierto, estos métodos por sí solos no pueden transformar número negativos a bytes y viceversa, para ello se usa el parámetro `signed`, siendo este de tipo [booleano](#BOOLEAN).

```python
int_in_bytes: bytes = (-360).to_bytes(2, signed=True)

print(int.from_bytes(int_in_bytes, signed=True))
```

### CONTAR BITS

El método `bit_count` cuenta el número de bits `True` qué usa un número en [binario](#BINARY).

```python
header: str = "| NUM | BIN | COUNT |"

print(header)
print("-" * len(header))
for i in range(8):
    binary: str = f"{bin(i)[2:]:>03}"
    count: int = i.bit_count()
    print(f"|{i:^5}|{binary:^5}|{count:^7}|")
```

| NUM |  BIN  | COUNT |
|:---:|:-----:|:-----:|
|  0  |  000  |   0   |
|  1  |  001  |   1   |
|  2  |  010  |   1   |
|  3  |  011  |   2   |
|  4  |  100  |   1   |
|  5  |  101  |   2   |
|  6  |  110  |   2   |
|  7  |  111  |   3   |

```python
num: int = 8

print(f"bin({num}) = {bin(num)[2:]}")
print(f"bit_count({num}) = {num.bit_count()}")
# SALIDA:
# bin(8) = 1000
# bit_count(8) = 1
```

### LONGITUD DE BITS

El método `bit_length` cuenta el número de bits qué usa un número en [binario](#BINARY).

```python
header: str = "| NUM | BIN | LENGTH |"

print(header)
print("-" * len(header))
for i in range(8):
    binary: str = f"{bin(i)[2:]:>03}"
    count: int = i.bit_length()
    print(f"|{i:^5}|{binary:^5}|{count:^8}|")
```

| NUM |  BIN  | COUNT |
|:---:|:-----:|:-----:|
|  0  |  000  |   0   |
|  1  |  001  |   1   |
|  2  |  010  |   2   |
|  3  |  011  |   2   |
|  4  |  100  |   3   |
|  5  |  101  |   3   |
|  6  |  110  |   3   |
|  7  |  111  |   3   |

```python
num: int = 8

print(f"bin({num}) = {bin(num)[2:]}")
print(f"bit_length({num}) = {num.bit_length()}")
# SALIDA:
# bin(8) = 1000
# bit_length(8) = 4
```

## INT BYTES

>[!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Revisar toda la documentación y ver que se puede mejorar.
> > - [ ] Reparar los enlaces rotos.

> [!tip]
> Para poder manejar estos métodos primero debes saber somo funcionan los [bytes](#BYTES) en python.

Para convertir un número entero a un conjunto de **bytes**, se puede usar el método `to_bytes`.

```python
print((18).to_bytes())
print(int.to_bytes(18))

print((360).to_bytes(2))
print(int.to_bytes(360, 2))
```

Sí el número entero es demasiado grande, tendremos que indicar el número de **bytes** que requiere, como se puede ver en el segundo grupo de `print`s del ejemplo.

Para poder transformar un grupo de bytes a un número entero se usa el método `from_bytes`.

```python
int_in_bytes: bytes = (360).to_bytes(2)

print(int.from_bytes(int_in_bytes))
```

> [!info]
> Por cierto, estos métodos por sí solos no pueden transformar número negativos a bytes y viceversa, para ello se usa el parámetro `signed`, siendo este de tipo [booleano](#BOOLEAN).

```python
int_in_bytes: bytes = (-360).to_bytes(2, signed=True)

print(int.from_bytes(int_in_bytes, signed=True))
```
