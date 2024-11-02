---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/Int
title: Números enteros en Python
---

# NÚMEROS ENTEROS EN PYTHON

[¿Qué son los número enteros en programación?](../../pc/pc_variable.md#ENTEROS)

Un ejemplo de la declaración de variables de números enteros sería el siguiente:

```py
num1 = 3
num2: int = 2
```

Los números enteros están representados por la clase `int`, esta permite por ejemplo, transformar un valor de tipo [string](py_str.md) a uno entero.

```py
num1: int = int("3")
num2: int = 2

print(f"{num1 + num2 = }")
# SALIDA:
# num1 + num2 = 5
```

En el ejemplo anterior se puede ver cómo se transforma el **texto** `3` al **número entero** `3`, gracias a esto es por lo que se pueden sumar los dos números, ya qué los textos no se suman, se unen, si quieres comprobar esto último puedes ejecutar el siguiente código.

```py
num1: str = "3"
num2: str = "2"

print(f"{num1 + num2 = }")
# SALIDA:
# num1 + num2 = '32'
```

# DE OTRAS BASES AL DECIMAL

La clase `int` permite transformar un texto que represente un valor que no sea de *base 10* en *base 10*, esto se puede hacer pasándole a esta clase dos argumentos, el texto con el valor a combertir a decimal y la base del valor introducido.

```py
byte_in_hex: str = "ff"

print(int(byte_in_hex, 16))
# SALIDA:
# 255
```

En el anterior ejemplo se puede ver cómo se transforma el valor `ff` en `255`, pasando del **hexadecimal** al **decimal**, también podríamos hacer lo mismo con el binario.

```py
num_in_bin: str = "10010"

print(int(num_in_bin, 2))
# SALIDA:
# 18
```

# REPRESENTACIÓN EN FORMA DE FRACCIÓN

Se puede convertir un número entero en una fracción representada con una [tupla](../collections/Collections_tuple.md), la cual contendrá el **dividendo** (`numerator`) y el **divisor** (`denominator`), para ello deberemos hacer uso de la función `as_integer_ratio`.

```py
int_ratio: tuple = int.as_integer_ratio(3)

print(int_ratio)
# SALIDA:
# (3, 1)
```

En este ejemplo podemos ver cómo se obtiene la [tupla](../collections/Collections_tuple.md) con el **dividendo** (`numerator`) y **divisor** (`denominator`) del números entero.

En el caso de los número enteros, por sí solos, este método no tiene mucho sentido, es cuando se combina este método con el de los valores [float](py_float.md) cueando podemos darle un mejor uso.

## PROPIEDADES

Para obtener los valores de forma fraccionaria, no hace falta usar el método `as_integer_ratio`, ya que se puede obtener estos valores en forma de propiedades del número entero.

```py
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

# APARTADOS RELACIONADOS

- [USO DE BITS](Int/Int_Bit.md)
- [USO DE BYTES](Int/Int_Bytes.md)
- [NÚMERO COMPLEJOS](py_complex.md)
