---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Letra de las columnas de EXCEL en Python
---

Para convertir el número de la columna en la letra que corresponde se puede usar el la [función](../py_function.md) `get_column_letter`, esta recibe un valor de tipo [int](../variables/py_int.md) como argumento:

```py
from openpyxl import utils

for i in range(1, 10):
    print(utils.get_column_letter(i), end=" ")
# SALIDA:
# A B C D E F G H I
```

La utilidad de esto es poder automatizar la escritura de valores en las celdas:

```py
from openpyxl import (
    Workbook,
    utils
)

wb: Workbook = Workbook()
ws = wb.active

for x in range(1, 10):
    for y in range(1, 10):
        cl = utils.get_column_letter(x)
        ws[f"{cl}{y}"].value = x * y

wb.save("main.xlsx")
```