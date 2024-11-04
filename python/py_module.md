---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
title: Módulos de Python
---

# MODULES

> [!help] REFERENCIAS WEB
> - [W3 (modules)](https://www.w3schools.com/python/python_modules.asp)
>
> YouTube:
> - [pildorasinformaticas (modulos)](https://youtu.be/t93x-vnFvP4)

Un módulo podemos entenderlo como un archivo que contiene código, pero este no tiene por qué ejecutarse expresamente por sí solo, sino que puede ser usado como una utilidad para otro archivo, para poder entenderlo mejor, podemos ver el ejemplo del [módulo math](https://docs.python.org/3/library/math.html), el cual forma parte de Python, para poder hacer uso del [módulo math](https://docs.python.org/3/library/math.html) este debe ser importado a nuestro proyecto, para ello usaremos la palabra clave `import` seguida del módulo a importar.

>[!abstract] SINTAXIS
>import ***\[modules_name\]***

Por ejemplo podríamos importar el [módulo math](https://docs.python.org/3/library/math.html):

```py
import math
```

Este módulo contiene [variables](py_variable.md) y [funciones](py_function.md), en esta documentación se van a ver unas cuantas, pero no todas, si quieres ver más a fondo que ofrece este módulo puedes visitar la documentación oficial del [módulo math](https://docs.python.org/3/library/math.html) de Python.

Para poder usar el contenido de un módulo se debe escribir el nombre de este, seguido de un punto y el nombre de la [variable](py_variable.md) o [función](py_function.md) que queramos usar.

```py
import math

print(f"La raíz cuadrada de dos es = {math.sqrt(2)}")
print(f"PI = {math.pi}")
print(f"E = {math.e}")
print(f"El suelo de 0.999 es = {math.floor(0.999)}")
print(f"El techo de 0.001 es = {math.ceil(0.001)}")

""" SALIDA:
La raíz cuadrada de dos es = 1.4142135623730951
PI = 3.141592653589793
E = 2.718281828459045
El suelo de 0.999 es = 0
El techo de 0.001 es = 1
"""
```

En este ejemplo se puede ver como se llama a diferentes [variables](py_variable.md) y [funciones](py_function.md) del [módulo math](https://docs.python.org/3/library/math.html).

Es posible que os preguntéis el por qué estas [variables](py_variable.md) y [funciones](py_function.md) de Python tienen que importarse a diferencia de la [función print](py_print.md) que no necesita ser importada para su uso, esto es debido que la esta última es de uso común, es por así decirlo una parte esencial de Python, y también es por qué sí se cargará en memoria todos los módulos al iniciar un proyecto, este tardaría mucho en empezar a ejecutarse a parte del consumo de memoria que ello implica, es por esto que las [variables](py_variable.md) y [funciones](py_function.md) no tan esenciales de Python en de ser importadas de forma manual, indicado qué es lo que queremos importar.

# OTROS RELACIONADOS

- [IMPORTAR ELEMENTO DE MÓDULO \*️⃣](modules/Modules_Import_Elements.md)
- [RENOMBRAR MÓDULOS 🔤](modules/Modules_Rename.md)
- [CREAR MÓDULO 💽](modules/Modules_Create.md)
- [PAQUETES 📦](modules/Modules_Packages.md)

---

>[!tip]
>Es posible [ver el código fuente de un módulo](modules/Modules_Get_source.md), esto te puede interesar si quieres saber como funciona internamente.