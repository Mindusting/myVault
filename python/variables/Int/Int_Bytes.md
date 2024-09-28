---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable
title: Uso de bytes de los ints en Python
---

>[!tip]
>Para poder manejar estos métodos primero debes saber somo funcionan los [bytes](../py_byte.md) en python.

Para convertir un número entero a un conjunto de **bytes**, se puede usar el método `to_bytes`.

```py
print((18).to_bytes())
print(int.to_bytes(18))

print((360).to_bytes(2))
print(int.to_bytes(360, 2))
```

Sí el número entero es demasiado grande, tendremos que indicar el número de **bytes** que requiere, como se puede ver en el segundo grupo de `print`s del ejemplo.

Para poder transformar un grupo de bytes a un número entero se usa el método `from_bytes`.

```py
int_in_bytes: bytes = (360).to_bytes(2)

print(int.from_bytes(int_in_bytes))
```

>[!info]
>Por cierto, estos métodos por sí solos no pueden transformar número negativos a bytes y viceversa, para ello se usa el parámetro `signed`, siendo este de tipo [booleano](../py_bool.md).

```py
int_in_bytes: bytes = (-360).to_bytes(2, signed=True)

print(int.from_bytes(int_in_bytes, signed=True))
```
