---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Líneas de EXCEL en Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

# INSERTAR

Para insertar una línea en la [página de trabajo](opxl_sheets.md) se usa el [método](../classes/py_method.md) `insert_rows`, este recibe dos argumentos, el primero indica el índice la línea en la que queremos insertar la línea, el segundo indica el número de líneas que queremos insertar.

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = Workbook()
ws = wb.active

ws["A1"] = 10
ws["A2"] = 20

ws.insert_rows(2, 3)

wb.save("main.xlsx")
wb.close()
```

Si abres el [excel](../../office/EXCEL/excel.md) podrás ver que entre el número `10` y el `20` hay `3` líneas de separación.

# ELIMINAR

Para eliminar líneas en la [página de trabajo](opxl_sheets.md) se usa el [método](../classes/py_method.md) `delete_cols` este recibe dos argumentos, el primero indica el índice la línea que queremos eliminar, el segundo indica el número de líneas que queremos eliminar después de esta.

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")
ws = wb.active

ws.delete_rows(2, 3)

wb.save("main.xlsx")
wb.close()
```

Si abres el [excel](../../office/EXCEL/excel.md) podrás ver que entre el número `10` y el `20` hay `0` líneas de separación ya que las hemos eliminado.
