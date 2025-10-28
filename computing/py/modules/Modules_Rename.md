---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
title: Renombrar módulos en Python
---

A la hora de importar módulo podemos encontrarnos con la situación en la que dos o más módulos (O los elementos que contienen) tienen el mismo nombre y por tanto ocurre un conflicto, para evitar esto se puede cambiar el nombre tanto de un módulo como de los elementos que lo componen, para ello se debe hacer uso de la palabra clave “as”.

>[!abstract] SINTAXIS
>import ***\[module_name\]*** as ***\[new_name\]***
>
>from ***\[module_name\]*** import ***\[element_name\]*** as ***\[new_name\]***

A continuación podemos ver un ejemplo de como se le cambia el nombre a un módulo:

```python
import random as rand

print(rand.random())
```

Y aquí podemos ver como se le cambia el nombre a un elemento de un módulo:

```python
from random import random as rand

print(rand())
```

Como se puede ver en el primer ejemplo, se importa el [módulo random](https://docs.python.org/3/library/random.html) cambiándole el nombre a “rand”, en el segundo ejemplo se le cambia a la [función](../py_func.md) `random` el nombre para pasar a ser “rand”.
