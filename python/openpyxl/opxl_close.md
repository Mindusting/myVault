---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Cerrar de EXCEL en Python
---

Para cerrar la conexión con un archivo de [excel](../../office/EXCEL/excel.md) se usa el [método](../classes/py_method.md) `close` del [objeto](../py_class.md) `Workbook`:

```py
from openpyxl import Workbook

wb: Workbook = Workbook()

wb.save("main.xlsx")

wb.close()
```

Se suele cerrar el archivo una vez hemos terminado de usarlo y no queremos modificarlo por error.
