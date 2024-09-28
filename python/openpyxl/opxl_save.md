---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Guarda el EXCEL en Python
---

Para guardar un [objeto](../py_class.md) `Workbook` se usa el [método](../classes/py_method.md) `save`, este recibe un argumento obligatorio, en este se indica el nombre con el que queremos guardar el archivo.

```py
from openpyxl import Workbook

wb: Workbook = Workbook()

wb.save("main.xlsx")
```

Como se puede ver en el anterior ejemplo, el nombre del archivo tiene la extensión `xlsx`, esto es para que el [os](../../os/os.md) lo reconozca como un [excel](../../office/EXCEL/excel.md) y así se pueda abrir con una herramienta especializada haciendo doble clic sobre el icono del archivo.

---

En el caso en el que queramos guardar el archivo en un directorio distinto al que se encuentra el archivo de Python, se puede indicar la rula tanto relativa como absoluta.

```py
from openpyxl import Workbook

wb: Workbook = Workbook()

direction: str = "C:\\"
file_name: str = "main.xlsx"

wb.save(f"{direction}{file_name}")
wb.close()
```

Una vez hayas guardado un archivo [excel](../../office/EXCEL/excel.md) quizás te interese [cerrarlo](opxl_close.md), o [abrirlo](opxl_load_workbook.md) en el futuro para hacer consultas. 
