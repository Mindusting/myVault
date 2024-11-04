---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Ejecuta sentencias de SQLite en Python
---

Una vez nos hemos [conectado a una base de datos](../py_sqlite3.md) podemos trabajar sobre ella con el [método](../classes/py_method.md) `execute`, este puede recibir uno o dos argumentos, siendo el primero la sentencia SQL y el segundo los parámetros (Ya veremos más adelante en qué consiste).

```py
import sqlite3

connection = sqlite3.connect("main.db")
cursor = con.cursor()

cursor.execute("""\
CREATE TABLE users (
    id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY(id)
);""")

cursor.commit()

cursor.close()
connection.close()
```

Como puedes ver en el ejemplo, tras conectarnos a la base de datos, [creamos una tabla](../../sql/SQLite3/SQLite3_tables.md) a nombre de `users` y después es hacemos uso del [método](../classes/py_method.md) `commit`, este es el encargado de guardar los cambios en la base de datos.

> [!question] ¿Es necesario usar `commit`?
> No siempre es necesario usar `commit` ya que cosas como la creación de una tabla (Como es este caso) sí se guarda pese a que no ejecutemos ningún `commit`, ahora, cambios en los registros (líneas) de las tablas entre otras cosas no se guardarán en el archivos de la base de datos hasta que ejecutemos el `commit`, por ello es buena practica ejecutarlo siempre al final para no perder los cambios.

---

El segundo argumento del [método](../classes/py_method.md) `execute` sirve para indicar valor que nosotros queramos insertar de forma dinámica, con un ejemplo se entenderá mejor:

```py
import sqlite3

connection = sqlite3.connect("main.db")
cursor = con.cursor()

data: tuple = ("Mind", "Dusting")

cursor.execute("""\
INSERT INTO users (
    first_name,
    last_name
) VALUES (?, ?);""",
    data)

cursor.commit()

cursor.close()
connection.close()
```

Como se puede ver en este ejemplo, antes de ejecutar la sentencia creamos una [tupla](py_tuple.md) (también se puede hacer con una [lista](../py_list.md)), dentro de esta guardamos los datos (ordenados) que queremos insertar en la tabla, después de esto ejecutamos el [`INSERT`](../../sql/SQLite3/SQLite3_insert.md) con unos interrogantes, estos indican en donde van a ir los valores que se van a insertar a través del segundo argumento.

# EJECUTA MÚLTIPLES SENTENCIAS EN UNA

Es posible que hayas intentado ejecutar varias sentencias SQL en un solo `execute`, esto no es posible de hacer, para en los casos que queramos ejecutar varias sentencias iguales, pero cambiado ciertos datos como podría ser ejecutar varios [`INSERT`](../../sql/SQLite3/SQLite3_insert.md) podemos hacerlo con el [método](../classes/py_method.md) `executemany`:

```py
import sqlite3

connection = sqlite3.connect("main.db")
cursor = con.cursor()

data: tuple[tuple] = (
    ("Mind", "Dusting"),
    ("Adelio", "Gonzalez"),
    ("Adelia", "Rodriguez")
)

cursor.executemany("""\
INSERT INTO users (
    first_name,
    last_name
) VALUES (?, ?);""",
    data)

cursor.commit()

cursor.close()
connection.close()
```

El [`INSERT`](../../sql/SQLite3/SQLite3_insert.md) que se ve en el ejemplo se ejecutará tres veces ya que es el número de elementos que tiene la [tupla](py_tuple.md) `data`, este [método](../classes/py_method.md) sería el equivalente a hacer un [bucle for-each](../loops/py_for_each.md):

```py
import sqlite3

connection = sqlite3.connect("main.db")
cursor = con.cursor()

data: tuple[tuple] = (
    ("Mind", "Dusting"),
    ("Adelio", "Gonzalez"),
    ("Adelia", "Rodriguez")
)

for line in data:
    cursor.execute("""\
    INSERT INTO users (
        first_name,
        last_name
    ) VALUES (?, ?);""",
        line)

cursor.commit()

cursor.close()
connection.close()
```

> [!question] ¿Cómo puedo obtener los datos después de un [`SELECT`](../../sql/SQLite3/SQLite3_select.md)?
> Para ello te recomiendo leer la [documentación correspondiente](SQLite3_fetch.md).
