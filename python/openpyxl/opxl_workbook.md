---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Objeto EXCEL en Python
---

Para poder trabajar sobre un [`EXCEL`](../../office/EXCEL/excel.md) primero tendremos que crearlo, para ello usaremos la [clase](../py_class.md) `WorkBook`:

```py
import openpyxl as xl

wb = xl.Workbook()
```

Una vez creado, te puede interesar las siguientes cosas:

- [GUARDAR EL EXCEL](opxl_save.md)
- [CARGAR UN EXCEL](opxl_load_workbook.md)
- [ABRIR UN APÁGINA DE EXCEL](opxl_sheets.md)
