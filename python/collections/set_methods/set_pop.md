---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

En el caso de qué queramos borrar el último elemento del set se puede usar el [método](../../classes/py_method.md) `pop`, este también devuelve el último valor, por lo que, como se puede ver en el ejemplo, se puede guardar el valor guardado:

```py
my_set: set = {"Manzana", "Naranja", "Platano"}
last_element: str = my_set.pop()

print(my_set)
print(last_element)
# SALIDA:
# {'Naranja', 'Manzana'}
# Platano
```

>[!warning]
>Cuidado con este [método](../../classes/py_method.md), como el contenido del set no tiene por qué estar ordenado siempre de la misma forma, el resultado de este ejemplo puede cambiar cada vez que se ejecute.
