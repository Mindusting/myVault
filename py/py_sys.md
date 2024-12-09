---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/SYS
title: Módulo SYS en Python
---

# REFERENCIAS WEB

- [Python SYS Doc](https://docs.python.org/3.11/library/sys.html)

# SYS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> Hay que cambiarlo ya que tiene que formar parte de la documentación del módulo `SYS` por lo que se debe quitar información redundante que vaya a haber entre los dos apartados.

Para poder hacer uso de los argumentos introducidos al ejecutar el comando [`python`](py_files.md) o [`python3`](py_files.md) se usa el [módulo](py_module.md) `sys`.

```python
import sys

print(sys.argv)
```

En el ejemplo que se encuentra encima, se muestra como se importa el módulo `sys` y luego se imprime la [lista](py_list.md) `argv`, siendo el elemento `0` el nombre del archivo que hemos ejecutado.

Un ejemplo simple del uso que se le puede dar sería la suma entre dos números:

```python
import sys

x: int = int(sys.argv[1])
y: int = int(sys.argv[2])

print(x + y)
```

Si ejecutamos este script de python con el comando `python3 main.py 3 2`, el valor de `x` será `3` y el de `y` será `2`, luego, se guardan estos valores en unas [variables](py_variable.md) transformándolos en tipo `int`, esto es debido que que estos argumentos siempre son de tipo `str`.

> [!info] INFO
> El módulo `sys` provee muchas más cosas, estas tienen su propia explicación en su respectiva documentación.
