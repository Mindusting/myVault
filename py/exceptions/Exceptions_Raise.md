---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Exception
title: Lanzamiento de errores
---

El lanzamiento de excepciones permite al programador provocar de forma voluntaria una excepción, la cual puede ser creada con una clase como se ve en el ejemplo.

%%
SINTAXIS

```
raise [exception_name] ([error_mensage])
```
%%

> [!abstract] SINTAXIS
> <span class="flow-word-color">raise</span> <span class="italic class-color">[exception_name]</span> (<span class="string-color">[error_mensage]</span>)

```python
# Esta es la ejecución de la excepción
raise ValueError ("Mensage de la excepción.")
```

```python
# Esta es mi clase de tipo excepción.
class my_exception(Exception):
    pass

# Esta es la ejecución de la excepción personalizada
raise my_exception ("Mensage de la excepción.")
```

Ejecutar una excepción por sí sola no tiene mucho sentido, pero más adelante en el documento, al combinarlo con otros elementos del lenguaje, el ejecutar una excepción tiene utilidad.
