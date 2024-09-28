---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Páginas de EXCEL en Python
---

Para trabajar sobre las páginas de [excel](../../office/EXCEL/excel.md) tenemos que crear un [objeto](../py_class.md) `Worksheet`, sobre este es sobre el que se va a trabajar:

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

ws = wb.active

wb.save("main.xlsx")
wb.close()
```

Como se puede ver en el ejemplo, para poder trabajar sobre una página de [excel](../../office/EXCEL/excel.md) se usa la propiedad `active`, por comodidad, se crea un alias como `ws` (`Worksheet`).

# CAMBIAR NOMBRE

Por defecto al crear un archivo [excel](../../office/EXCEL/excel.md) este tiene una sola página con el nombre `Sheet`, si queremos cambiarle el nombre podemos hacer de la siguiente forma:

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

ws = wb.active

ws.title = "Main"

print(ws.title)
# SALIDA:
# Main

wb.save("main.xlsx")
wb.close()
```

Como se puede ver en el ejemplo, después de cambiarle el nombre a la página, se consulta su nombre y se imprime para demostrar que se a realizado con éxito, ahora, el nombre que se cambia es el de la página activa (Sobre la que se está trabajando), más adelante veremos como crear más páginas y como seleccionar otra como página de trabajo.

> [!note] NOTE
> Al abrir un archivo la página de trabajo por defecto es siempre la primera.

# CREAR PÁGINAS

Para crear nuevas páginas en nuestro archivo de [excel](../../office/EXCEL/excel.md) se usa el [método](../classes/py_method.md) `create_sheet`, este [método](../classes/py_method.md) requiere de un argumento y puede tener dos, el primero (obligatorio) es el nombre de la nueva página, el segundo es el índice de la página, si no indicamos ninguno, será el valor más alto posible, esto es debido a que las páginas se guardan en forma de [lista](../collections/py_list.md).

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

ws = wb.active

ws.create_sheet("ultima_pagina")
ws.create_sheet("primera_pagina", 1)

print(ws¡b.sheetnames)
# SALIDA:
# ["primera_pagina", "Main", "ultima_pagina"]

wb.save("main.xlsx")
wb.close()
```

# LISTAR PÁGINAS

Para poder ver los nombre de las páginas que tiene nuestro archivos, podemos usar la propiedad `sheetnames`, esta nos devolverá una [lista](../collections/py_list.md) con los nombres y en su respectivo orden:

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

ws = wb.active

print(wb.sheetnames)
# SALIDA:
# ["primera_pagina", "Main", "ultima_pagina"]

wb.save("main.xlsx")
wb.close()
```

# ORDENAR PÁGINAS

Para cambiar el orden de las páginas se usa el [método](../classes/py_method.md) `move_sheet`, este recibe dos argumentos, el nombre y el índice de donde lo queremos mover.

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

ws = wb.active

ws.move_sheet("Main", 1)

print(wb.sheetnames)
# SALIDA:
# ["Main", "primera_pagina", "ultima_pagina"]

wb.save("main.xlsx")
wb.close()
```

# BORRAR PÁGINA

Si queremos borrar alguna página de nuestro archivo podemos usar la palabra lave `del` seguido de la página que remos borrar:

```py
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

del wb["primera_pagina"]
del wb["ultima_pagina"]

ws = wb.active

print(wb.sheetnames)
# SALIDA:
# ["Main"]

wb.save("main.xlsx")
wb.close()
```
