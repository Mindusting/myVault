---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/HEX
title: Hexadecimal en Python
---

# NÚMEROS ENTEROS

Para pasar de un número entero al hexadecimal se usa la función `hex`.

```py
num: int = 255

num_hex: str = hex(num)

print(num_hex)
print(num_hex[2:])
# SALIDA:
# 0xff
# ff
```

Como se puede ver en el ejemplo de arriba, el número es pasado por la función `hex`, el resultado de este (Siendo un [string](py_str.md)) es guardado en una variable, y luego se imprime dos veces, en el primero se imprime el resultado por completo y en el segundo se usa un [slice](../py_slice.md) para quitar los dos primeros caracteres qué indican que es un valor hexadecimal.

Si quisiéramos hacer el proceso contrario para obtener un número entero de un valor hexadecimal tendremos que usar la clase [int](py_int.md).

```py
print(int("0xff", 16))
print(int("ff", 16))
# SALIDA:
# 255
# 255
```

# NÚMEROS DECIMALES

Para transformar un valor decimal a hexadecimal y viceversa, se hace uso de unos métodos de la clase [float](py_float.md).

```py
PI: float = 3.1415926535

PI_HEX: str = float.hex(PI)

print(PI_HEX)
print(PI_HEX[2:])
# SALIDA:
# 0x1.921fb54411744p+1
# 1.921fb54411744p+1
```

En el ejemplo de encima se puede ver cómo se transforma el valor decimal a hexadecimal de una forma muy similar a como se hace con lo [número decimales](<# NÚMEROS ENTEROS>).

```py
print(float.fromhex("0x1.921fb54411744p+1"))
print(float.fromhex("1.921fb54411744p+1"))
# SALIDA:
# 3.1415926535
# 3.1415926535
```
