---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Páginas de EXCEL en Python
---

# SHEETS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> - [ ] Tengo que reorganizar todo el contenido.

Para trabajar sobre las páginas de *EXCEL* tenemos que crear un [objeto](../py_class.md) `Worksheet`, sobre este es sobre el que se va a trabajar:

```python
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")

ws = wb.active

wb.save("main.xlsx")
wb.close()
```

Como se puede ver en el ejemplo, para poder trabajar sobre una página de *EXCEL* se usa la propiedad `active`, por comodidad, se crea un alias como `ws` (`Worksheet`).

## CAMBIAR NOMBRE

Por defecto al crear un archivo *EXCEL* este tiene una sola página con el nombre `Sheet`, si queremos cambiarle el nombre podemos hacer de la siguiente forma:

```python
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

## CREAR PÁGINAS

Para crear nuevas páginas en nuestro archivo de *EXCEL* se usa el [método](../class/py_method.md) `create_sheet`, este [método](../class/py_method.md) requiere de un argumento y puede tener dos, el primero (obligatorio) es el nombre de la nueva página, el segundo es el índice de la página, si no indicamos ninguno, será el valor más alto posible, esto es debido a que las páginas se guardan en forma de [lista](../py_list.md).

```python
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

## LISTAR PÁGINAS

Para poder ver los nombre de las páginas que tiene nuestro archivos, podemos usar la propiedad `sheetnames`, esta nos devolverá una [lista](../py_list.md) con los nombres y en su respectivo orden:

```python
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

## ORDENAR PÁGINAS

Para cambiar el orden de las páginas se usa el [método](../class/py_method.md) `move_sheet`, este recibe dos argumentos, el nombre y el índice de donde lo queremos mover.

```python
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

## BORRAR PÁGINA

Si queremos borrar alguna página de nuestro archivo podemos usar la palabra lave `del` seguido de la página que remos borrar:

```python
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

## MÉTODOS

### INSERTAR LÍNEA

Para insertar una línea en la [página de trabajo](py_openpyxl_sheets.md) se usa el [método](../class/py_method.md) `insert_rows`, este recibe dos argumentos, el primero indica el índice la línea en la que queremos insertar la línea, el segundo indica el número de líneas que queremos insertar.

```python
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

Si abres el *EXCEL* podrás ver que entre el número `10` y el `20` hay `3` líneas de separación.

### ELIMINAR LÍNEA

Para eliminar líneas en la [página de trabajo](py_openpyxl_sheets.md) se usa el [método](../class/py_method.md) `delete_cols` este recibe dos argumentos, el primero indica el índice la línea que queremos eliminar, el segundo indica el número de líneas que queremos eliminar después de esta.

```python
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

Si abres el *EXCEL* podrás ver que entre el número `10` y el `20` hay `0` líneas de separación ya que las hemos eliminado.

### INSERTAR COLUMNA

Para insertar una columna en la [página de trabajo](py_openpyxl_sheets.md) se usa el [método](../class/py_method.md) `insert_cols`, este recibe dos argumentos, el primero indica el índice la columna en la que queremos insertar la columna, el segundo indica el número de columnas que queremos insertar.

```python
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

Si abres el *EXCEL* podrás ver que entre el número `10` y el `20` hay `3` columnas de separación.

### ELIMINAR COLUMNA

Para eliminar columnas en la [página de trabajo](py_openpyxl_sheets.md) se usa el [método](../class/py_method.md) `delete_cols` este recibe dos argumentos, el primero indica el índice la columna que queremos eliminar, el segundo indica el número de columnas que queremos eliminar después de esta.

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

Si abres el *EXCEL* podrás ver que entre el número `10` y el `20` hay `0` columnas de separación ya que las hemos eliminado.

## CELDAS

Las celdas son los [objetos](../py_class.md) que guardan los valores del *EXCEL*), para acceder a ello se hace de la siguiente forma:

```python
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

También se puede recibir una matriz hecha de [tuplas](../py_tuple.md) con los [objetos](../py_class.md) de celda en cada elemento, para obtener los valores de cada celda he usado la [clase map](../py_map.md), he guardado los datos en una matriz de [py_numpy](../numpy/py_numpy.md) y he impreso los datos con [Pandas](../py_pandas.md).

```python
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
