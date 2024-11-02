---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
title: Importar elementos de módulos en Python
---

Al igual que nosotros podemos elegir qué módulo importar, también podemos elegir que elementos de este queremos importar, esto nos puede servir cuando queremos usar una (o unas pocas) [variable](../py_variable.md) o [función](../py_function.md) de un módulo, siendo completamente innecesaria la importación del resto de elementos de ese módulo, para ello haremos uso de la palabra clave `from`.

>[!abstract] SINTAXIS
>from ***\[module_name\]*** import ***\[element_name\]***

```py
from math import e, pi

print(f"PI = {pi}")
print(f"E  = {e}")

""" SALIDA:
PI = 3.141592653589793
E  = 2.718281828459045
"""
```

Como se puede ver en este ejemplo, esta vez importamos las [variables](../py_variable.md) “e” y “pi” exclusivamente del [módulo math](https://docs.python.org/3/library/math.html), también tiene un matiz extra, y es que al importar las [variables](../py_variable.md) en vez de el módulo, cuando queramos usarlas no hará falta que nombremos al módulo como ocurre en el ejemplo anterior a este.

Ten en cuenta que también existe la posibilidad de importar todas las [variables](../py_variable.md) y [funciones](../py_function.md) de un método poniendo un asterisco tras la palabra clave `import`, pero esto se suele considerar una mala práctica por lo mismo de antes, es raro que vayas a usar todas las [variables](../py_variable.md) y [funciones](../py_function.md), y en el caso de que si las vayas a usar, sigue siendo recomendable escribirlos de forma individual para poder ver que se a importado y por que si se modifica el módulo bien por que se añada algo o se quite, lo vas a notar (Sí se quita uno que quieres usar ocurrirá un error y si se añade uno, no se importará), en cualquier caso, para lo que si va bien es cuando estamos probando el módulo por primera vez y queremos ver que nos ofrece.

```PY
from math import *
```
