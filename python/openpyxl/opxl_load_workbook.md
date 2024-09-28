---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Abre un EXCEL en Python
---

Para abrir un archivo [excel](../../office/EXCEL/excel.md) que ya esté creado se hace uso de la [función](../py_function.md) `load_workbook`

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")
```

Esta [función](../py_function.md) requiere de un argumento obligatorio, este es el nombre del archivo (Y su ruta si hiciera falta).
