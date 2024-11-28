---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OpenPyXL
title: Módulo OpenPyXL en Python
---

# OPENPYXL

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> - [ ] Tengo que reorganizar todo el contenido.

> [!help] REFERENCIAS WEB
> - [OPENPYXL Doc](https://openpyxl.readthedocs.io/en/stable/)
> - [Real Python](https://realpython.com/openpyxl-excel-spreadsheets-python/)
>
> YouTube:
> - [Tech With Tim](https://youtu.be/7YS6YDQKFh0)
> - [Bek Brace](https://youtu.be/hFDrWvDOYFA)

[py_openpyxl_sheets](py_openpyxl_sheets.md)

Para poder trabajar sobre un *EXCEL* primero deberemos importar el [módulo](../py_module.md) `openpyxl`, primer tenemos que importarlo.

```python
import openpyxl
```

## CLASES

### WORKBOOK

Para poder trabajar sobre un *EXCEL* primero tendremos que crearlo, para ello usaremos la [clase](../py_class.md) `WorkBook`:

```python
import openpyxl as xl

wb = xl.Workbook()
```

### SHEETS

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

#### CAMBIAR NOMBRE

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

#### CREAR PÁGINAS

Para crear nuevas páginas en nuestro archivo de *EXCEL* se usa el [método](../classes/py_method.md) `create_sheet`, este [método](../classes/py_method.md) requiere de un argumento y puede tener dos, el primero (obligatorio) es el nombre de la nueva página, el segundo es el índice de la página, si no indicamos ninguno, será el valor más alto posible, esto es debido a que las páginas se guardan en forma de [lista](../py_list.md).

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

#### LISTAR PÁGINAS

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

#### ORDENAR PÁGINAS

Para cambiar el orden de las páginas se usa el [método](../classes/py_method.md) `move_sheet`, este recibe dos argumentos, el nombre y el índice de donde lo queremos mover.

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

#### BORRAR PÁGINA

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

### SAVE

Para guardar un [objeto](../py_class.md) `Workbook` se usa el [método](../classes/py_method.md) `save`, este recibe un argumento obligatorio, en este se indica el nombre con el que queremos guardar el archivo.

```python
from openpyxl import Workbook

wb: Workbook = Workbook()

wb.save("main.xlsx")
```

Como se puede ver en el anterior ejemplo, el nombre del archivo tiene la extensión `xlsx`, esto es para que el [os](../../os/os.md) lo reconozca como un *EXCEL* y así se pueda abrir con una herramienta especializada haciendo doble clic sobre el icono del archivo.

---

En el caso en el que queramos guardar el archivo en un directorio distinto al que se encuentra el archivo de Python, se puede indicar la rula tanto relativa como absoluta.

```python
from openpyxl import Workbook

wb: Workbook = Workbook()

direction: str = "C:\\"
file_name: str = "main.xlsx"

wb.save(f"{direction}{file_name}")
wb.close()
```

Una vez hayas guardado un archivo *EXCEL* quizás te interese [cerrarlo](#CLOSE), o [abrirlo](#LOAD%20WORKBOOK) en el futuro para hacer consultas. 

### LOAD WORKBOOK

Para abrir un archivo *EXCEL* que ya esté creado se hace uso de la [función](../py_function.md) `load_workbook`

```python
from openpyxl import (
    Workbook,
    load_workbook
)

wb: Workbook = load_workbook("main.xlsx")
```

Esta [función](../py_function.md) requiere de un argumento obligatorio, este es el nombre del archivo (Y su ruta si hiciera falta).

## LETRA DE COLUMNA

Para convertir el número de la columna en la letra que corresponde se puede usar el la [función](../py_function.md) `get_column_letter`, esta recibe un valor de tipo [int](../variables/py_int.md) como argumento:

```python
from openpyxl import utils

for i in range(1, 10):
    print(utils.get_column_letter(i), end=" ")
# SALIDA:
# A B C D E F G H I
```

La utilidad de esto es poder automatizar la escritura de valores en las celdas:

```python
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
