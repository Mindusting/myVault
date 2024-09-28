---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Columnas de EXCEL en Python
---

# INSERTAR

Para insertar una columna en la [página de trabajo](opxl_sheets.md) se usa el [método](../classes/py_method.md) `insert_cols`, este recibe dos argumentos, el primero indica el índice la columna en la que queremos insertar la columna, el segundo indica el número de columnas que queremos insertar.

```
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = Workbook()
ws = wb.active

ws["A1"] = 10
ws["B1"] = 20

ws.insert_cols(2, 3)

wb.save("main.xlsx")
wb.close()
```

Si abres el [excel](../../office/EXCEL/excel.md) podrás ver que entre el número `10` y el `20` hay `3` columnas de separación.

# ELIMINAR

Para eliminar columnas en la [página de trabajo](opxl_sheets.md) se usa el [método](../classes/py_method.md) `delete_cols` este recibe dos argumentos, el primero indica el índice la columna que queremos eliminar, el segundo indica el número de columnas que queremos eliminar después de esta.

```
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")
ws = wb.active

ws.delete_cols(2, 3)

wb.save("main.xlsx")
wb.close()
```

Si abres el [excel](../../office/EXCEL/excel.md) podrás ver que entre el número `10` y el `20` hay `0` columnas de separación ya que las hemos eliminado.
