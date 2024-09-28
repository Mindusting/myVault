---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/Str
title: R-String en Python
---

<h1 align="center">R-STRING EN PYTHON</h1>

---

# R-STRING EN PYTHON

El término `R-String` es la abreviación de `Raw-String`, siendo *raw*, *crudo* en inglés, la diferencia entre este y un [`str`](py_str.md), es que este, no tiene caracteres de escape, esto podemos verlo mejor con un ejemplo:

```py
print("\tHola mundo!!!")
print(r"\tHola mundo!!!")
# SALIDA:
#     Hola mundo!!!
# \tHola mundo!!!
```

Como se puede ver en el ejemplo, en el [`print`](../py_print.md) que hemos usado el [`str`](py_str.md) normal al haber indicado la tabulación con el `\t` se ha impreso en el resultado la tabulación como corresponde, sin embargo, en el caso del [`print`](../py_print.md) con el `R-String` se ha impreso tal cual los caracteres de **contra barra** y **te** (`\t`).

Para este punto ya te habrás dado cuenta gracias al ejemplo, y es que para indicar que queremos que un [`str`](py_str.md) se interprete de forma cruda, simplemente tendremos que poner una `r` por delante de las comillas que conformen el [`str`](py_str.md).
