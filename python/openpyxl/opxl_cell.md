---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Celdas de EXCEL en Python
---

Las celdas son los [objetos](../py_class.md) que guardan los valores del [excel](../../office/EXCEL/excel.md), para acceder a ello se hace de la siguiente forma:

```py
from openpyxl import Workbook

wb: Workbook = Workbook()

ws = wb.active

# Objeto "cell"
print(ws["A1"])
# SALIDA:
# <Cell 'Sheet'.A1>

# Escritura de información
ws["A1"].value = 10

# Lectura de información
print(ws["A1"].value)
# SALIDA:
# 10

wb.save("main.xlsx")
wb.close()
```

También se puede recibir una matriz hecha de [tuplas](../collections/Collections_tuple.md) con los [objetos](../py_class.md) de celda en cada elemento, para obtener los valores de cada celda he usado la [clase map](../py_map.md), he guardado los datos en una matriz de [py_numpy](../numpy/py_numpy.md) y he impreso los datos con [Pandas](../py_pandas.md).

```py
from openpyxl import Workbook
import numpy as np
import pandsa as pnd

wb: Workbook = Workbook()
ws = wb.active

(
    ws["A1"], ws["B1"],
    ws["A2"], ws["B2"],
) = (
    1, 3,
    2, 4,
)

# Debuelve una matriz hecha
# de tuplas con las celdas.
data = ws["A1:B2"]

# Creamos un array con los
# valores de las celdas.
arr = np.array(
    list(map(
        lambda row: list(map(
            lambda col: col.value,
            row)
        ),
        data)
    )
)

print(pnd.DataFrame(arr))
```
