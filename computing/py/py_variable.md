---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable
title: Variables en Python
---

# VARIABLES EN PYTHON

>[!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar las variables `gloval` y `nongloval`.
> > - [ ] Documentar como se puede indicar el tipo de una variable (`x: int`).
> > - [ ] Documentar el valor `None`.
> > - [ ] Documentar que las variables en Python son todo pointer.
> > - [ ] Documentar el `del`.
> > - [ ] Documentar el recolector de basura de Python.
> > - [ ] Documentar función `isinstance`.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/python/python_variables.asp)
>
> YouTube:
> - [Sreekanth (Como funcionan internamente las variables en Python)](https://youtu.be/Bz3ir-vKqkk)

> [!faq]- FAQ
> - [¿Qué son las variables en programación?](../pc/pc_variable.md)

Aquí podrás encontrar documentación sobre múltiples tipos de datos, pero hay cuatro que son los más usado, y por tanto lo que deberías saber usar (*El resto está bien que los sepas usar, pero no son tan usados*):

- [Números enteros.](py_int.md)
- [Números decimales.](py_float.md)
- [Cadenas de texto.](py_str.md)
- [Valores booleanos.](py_bool.md)

---

- [Números complejos](py_complex.md)

## BINARY

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar los números en binario (`0b10`).

## OCTAL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar los número en octal (`010`).

## HEX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO

### HEX ENTEROS

Para pasar de un número entero al hexadecimal se usa la función `hex`.

```python
num: int = 255

num_hex: str = hex(num)

print(num_hex)
print(num_hex[2:])
# SALIDA:
# 0xff
# ff
```

Como se puede ver en el ejemplo de arriba, el número es pasado por la función `hex`, el resultado de este (*Siendo un [string](#STRING)*) es guardado en una variable, y luego se imprime dos veces, en el primero se imprime el resultado por completo y en el segundo se usa un [slice](py_slice.md) para quitar los dos primeros caracteres qué indican que es un valor hexadecimal.

Si quisiéramos hacer el proceso contrario para obtener un número entero de un valor hexadecimal tendremos que usar la clase [int](#INT).

```python
print(int("0xff", 16))
print(int("ff", 16))
# SALIDA:
# 255
# 255
```

### HEX DECIMALES

Para transformar un valor decimal a hexadecimal y viceversa, se hace uso de unos métodos de la clase [float](#FLOAT).

```python
PI: float = 3.1415926535

PI_HEX: str = float.hex(PI)

print(PI_HEX)
print(PI_HEX[2:])
# SALIDA:
# 0x1.921fb54411744p+1
# 1.921fb54411744p+1
```

En el ejemplo de encima se puede ver cómo se transforma el valor decimal a hexadecimal de una forma muy similar a como se hace con lo [número decimales](#FLOAT).

```python
print(float.fromhex("0x1.921fb54411744p+1"))
print(float.fromhex("1.921fb54411744p+1"))
# SALIDA:
# 3.1415926535
# 3.1415926535
```
