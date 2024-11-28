---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Obtención de datos en Python con SQLite3
---

Si alguna vez habéis ejecutado un [`SELECT`](../../sql/sqlite3/SQLite3_select.md) con el [módulo](../py_module.md) [SQLite3](../py_sqlite3.md) os habréis dado cuenta que no obtenéis los datos, esto es por que cuando ejecutamos un [`SELECT`](../../sql/sqlite3/SQLite3_select.md), el resultado que nos devuelve se guarda dentro del objeto [`cursor`](../py_sqlite3.md) en forma de [lista](../py_list.md) con [tuplas](../py_tuple.md) por cada registro devuelto.

Para poder acceder a esta información se pueden usar tres [métodos](../py_module.md):

- `fetchall`:
    Este devuelve la lista por completo.
<br>
- `fetchmany`:
    Este devuelve una lista con el [número](../variables/py_int.md) de registros que nosotros indiquemos como argumento.
<br>
- `fetchone`:
    Este devuelve el primer registro de la consulta.

> [!warning] WARNING
> Es importante saber que cuando consultamos información de esta [lista](../py_list.md), todas las [tuplas](../py_tuple.md) que recibamos se borrarán de la [lista](../py_list.md), por lo que si por ejemplo usamos el [método](../classes/py_method.md) `fetchone` dos veces, en el segundo caso, nos devolverá el segundo registro.

```python
import sqlite3

connection = sqlite3.connect("main.db")
cursor = con.cursor()

cursor.execute("""\
SELECT
    id,
    first_name,
    last_name
FROM users;""")

print(cursor.fetchall())
# SALIDA:
# [(1, 'Mind', 'Dusting'), (2, 'Adelio', 'Gonzalez'), (3, 'Adelia', 'Rodriguez')]

cursor.commit()

cursor.close()
connection.close()
```

Como se puede ver en el anterior ejemplo, devuelve correctamente el resultado de la consulta, ahora, si nosotros que remos visualizar los datos en vez de trabajar sobre ellos, haciendo lo esta forma es un poco ortopédico, para poder visualizar el contenido de una forma más visual podemos usar el [módulo](../py_module.md) [`pandas`](../py_pandas.md):

```python
import sqlite3
import pandas as pnd

connection = sqlite3.connect("main.db")
cursor = con.cursor()

cursor.execute("""\
SELECT
    id,
    first_name,
    last_name
FROM users;""")

print(pnd.DataFrame(
    cursor.fetchall(),
    columns=("ID", "Nombre", "Apellido")))
# SALIDA:
#    ID  Nombre   Apellido
# 0   1    Mind    Dusting
# 1   2  Adelio   Gonzalez
# 2   3  Adelia  Rodriguez

cursor.commit()

cursor.close()
connection.close()
```

Como se puede ver en este ejemplo, usamos [módulo](../py_module.md) [`pandas`](../py_pandas.md) y le indicamos los nombres de las columnas para poder ver mucho más fácilmente la información.

---

Como extra, el [módulo](../py_module.md) [py_numpy](../numpy/py_numpy.md) tiene muy buenas sinergias con este ya que podemos convertir los resultados de las consultas e matrices y trabajar sobre ellas de esta forma.

Supongamos que queremos obtener tanto los nombre como los apellidos por separado:

```python
import sqlite3
improt numpy as np

connection = sqlite3.connect("main.db")
cursor = con.cursor()

cursor.execute("""\
SELECT
    id,
    first_name,
    last_name
FROM users;""")

res = np.array(cursor.fetchall())

first_names = res[:, 1]
last_names = res[:, 2]

"""
Todos los registros
 v
[:, 1]
    ^
Número de la columna
"""

print(res)
# SALIDA:
# [['1' 'Mind' 'Dusting']
#  ['2' 'Adelio' 'Gonzalez']        
#  ['3' 'Adelia' 'Rodriguez']]

print("-" * 30) # SEPARADOR

print(first_names)
print(last_names)
# SALIDA:
# ['Mind' 'Adelio' 'Adelia']        
# ['Dusting' 'Gonzalez' 'Rodriguez']

cursor.commit()

cursor.close()
connection.close()
```

Como se puede ver en el anterior ejemplo trabajamos sobre los datos como una matriz de [py_numpy](../numpy/py_numpy.md), en este caso puede parecer un poco absurdo el ejemplo, pero imaginemos que tenemos una lista de alumnos con sus respectivas notas, si queremos sacar la media de la clase, gracias a que podemos usar [py_numpy](../numpy/py_numpy.md), podemos extraer de forma sencilla las notas y luego hacer la media de esta.
