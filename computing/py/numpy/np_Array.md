---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Numpy
title: Función Array en NumPy
---

La [función](../py_func.md) `array` permite transformar una [lista](../py_list.md) o [tupla](../py_tuple.md) en un [**array**](../../pc/pc_array.md):

```python
my_list:  list  = [3, 2, 5]
my_tuple: tuple = [7, 4, 8]

arr_1: np.ndarray = np.array(my_list)
arr_2: np.ndarray = np.array(my_tuple)

print(arr_1)
print(arr_2)
# SALIDA:
# [3 2 5]
# [7 4 8]
```
