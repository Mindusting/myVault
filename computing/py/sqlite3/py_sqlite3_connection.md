---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Module
  - Programming/Python/SQLite3
  - DataBase/SQLite3
title: Clase Connection en SQLite3 en Python
---

# CLASE CONNECTION

> [!important] IMPORTANTE
> A lo largo de esta documentación me referiré a la conexión como `cx` en el código.

La clase **`Connection`** en *SQLite3* permite establecer una conexión a una [base de datos](../../db/db.md) para poder operar con ella; al igual que con los [archivos](../py_open.md), estos se deben cerrar al terminar su uso (*con la [función](../py_func.md) `close`*).

Esta **conexión** es la que nos permitirá ejecutar código de [SQLite3](../../db/sql/sqlite3/sqlite3.md) contra la [base de datos](../../db/db.md).

## CREACIÓN DE CURSOR

Para crear [cursores](py_sqlite3_cursor.md) a partir de una conexión se usa el [método](../class/py_methods.md) `cursor`; este nos devolverá un [objeto](../py_class.md) de tipo [`Cursor`](py_sqlite3_cursor.md) el cual no contiene ninguna instrucción [SQLite3](../../db/sql/sqlite3/sqlite3.md).

> [!abstract] SINTAXIS
> ***\[cr\]*** = ***\[cx\]***.cursor()

```python
import sqlite3

cx = sqlite3.connect("./main.db")

# Se crea el cursor virgen.
cu = cx.cursor()

# Se cierra primero el cursor.
cu.close()
# Luego se cierra la conexión.
cx.close()
```

> [!important] IMPORTANTE
> Se debe cerrar antes el cursor que la conexión, básicamente se deben cerrar en el orden inverso al que se han creado.

## EJECUCIÓN DE SQL

Para ejecutar SQL podemos usar los [métodos](../class/py_methods.md) [`execute`](py_sqlite3_cursor.md#EJECUTA%20UNO), [`executemany`](py_sqlite3_cursor.md#EJECUTA%20VARIOS) y [`executescript`](py_sqlite3_cursor.md#EJECUTA%20SCRIPT) las cuales funcionan prácticamente igual (*por no decir igual*) a las que tienen los [cursores](py_sqlite3_cursor.md).

> [!abstract] SINTAXIS
> ***\[cr\]*** = ***\[func\]***(***\[args\]***)

---

Imaginemos que tenemos la siguiente [base de datos](../../db/db.md) a la que nos conectaremos con el nombre `main.db`:

```sql
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INTEGER
);

INSERT INTO users (name, age)
VALUES
    ('Adelio', 20),
    ('Adelia', 22);
```

Aquí en Python podemos ver como obtenemos un [cursor](py_sqlite3_cursor.md) de el [método](../class/py_methods.md) `execute` y luego imprimimos cada una de las [tuplas](../py_tuple.md) que obtenemos como resultado:

```python
import sqlite3

sql: str = "SELECT * FROM users;"

cx = sqlite3.connect("main.db")
cr = cx.execute(sql)

for row in cr:
    print(row)
# SALIDA:
# (1, 'Adelio', 20)
# (2, 'Adelia', 22)

cr.close()
cx.close()
```

## COMMITS Y ROLLBACKS

Cuando ejecutamos código de [SQLite3](../../db/sql/sqlite3/sqlite3.md) de tipo [`CRUD`](../../db/sql/sql_crud.md) no se aplican los cambios sobre la [base de datos](../../db/db.md) de forma automática, sino que los cambios se realizan en forma de transacción en la **memoria RAM** por lo que para bien aplicar o cancelar la transacción tendremos que indicarlo mediante alguno de los [métodos](../class/py_methods.md) [`commit`](#COMMIT) (*para confirmar*) o [`rollback`](#ROLLBACK) (*para cancelar*).

Ten en cuenta que si se cierra la conexión sin haber realizado un `commit` la transacción no se efectuará.

### COMMIT

El [método](../class/py_methods.md) `commit` sirve para aplicar todas las transacciones que se realizado hasta el momento desde el inicio de la última transacción; hay que tener en cuenta que al crear una conexión se ejecuta el inicio de una transacción de forma automática.

```python
import sqlite3

sql: str = """
INSERT INTO users (name, age)
VALUES
    ('Adelio', 20),
    ('Adelia', 22);
"""

cx = sqlite3.connect("main.db")
cx.execute(sql)

# Se aplican los cambios sobre la DB.
cx.commit()

cr.close()
cx.close()
```

### ROLLBACK

Para cancelar la transacción que quede pendiente en la conexión se usa el [método](../class/py_methods.md) `rollback`, no recibe ningún argumento simplemente cancela la transacción pendiente, si no hay ninguna transacción pendiente este [método](../class/py_methods.md) no hace nada.

```python
import sqlite3

script: str = """
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INTEGER
);

INSERT INTO users (name, age)
VALUES
    ('Adelio', 20),
    ('Adelia', 22);
"""

cx = sqlite3.connect("main.db")
cr = cx.cursor()

# Se crea la tabla y se inserta un registro.
# confirmando la transacción.
cr.executescript(script)
cx.commit()

# Se borran todos los usuarios de la tabla.
cr.execute("DELETE FROM users")

# Se muestra que se han borrado los usuarios.
print("Primera impresión de los usuarios:")
for row in cr.execute("SELECT * FROM users"):
    print(row)
# SALIDA:
# Primera impresión de los usuarios:

# Se revierte la transacción.
cx.rollback()

# Se muestra que los usuarios no han sido borrados.
print("Segunda impresión de los usuarios:")
for row in cr.execute("SELECT * FROM users"):
    print(row)
# SALIDA:
# Segunda impresión de los usuarios:
# (1, 'Adelio', 20)
# (2, 'Adelia', 22)

cr.close()
cx.close()
```

## CREAR UN BACKUP

Si queremos hacer un una copia de seguridad (*backup*) de nuestra [base de datos](../../db/db.md), podremos hacer uso del [método](../class/py_methods.md) `backup`, este recibe otra conexión como argumento y guarda en ella la información actual de la conexión original.

> [!abstract] SINTAXIS
> ***\[cx\]***.backup(***\[backup_cx\]***)

```python
import sqlite3

# Se crean las conexiones.
cx        = sqlite3.connect("./main.db")
backup_cx = sqlite3.connect("./backup.db")

# Se copia los datos de la DB original
# al DB backup.
cx.backup(backup_cx)

# Se cierran las conexiones.
backup_cx.close()
cx.close()
```

## TIPO DE SALIDA

Cuando estamos trabajando con [bases de datos](../../db/db.md) lo normal es que usemos texto, pero hay aveces que tendremos que manejar imágenes, vídeos, audios que tengamos guardados en la [base de datos](../../db/db.md) dentro de una columna de tipo [`BLOB`](../../db/sql/sqlite3/sqlite3_datatypes.md), si intentamos acceder a la información ahí guardada, es bastante probable que nos de una excepción, ya que hay ciertos [`bytes`](../py_bytes.md) que no se pueden transformar a texto de forma correcta, para solucionar esto podemos cambiar en la forma en la que nos devuelve la información de la [base de datos](../../db/db.md) con el atributo `text_factory`, este por defecto tiene la [clase](../py_class.md) [`str`](../py_str.md) y podemos sustituirlo por la [clase](../py_class.md) [`bytes`](../py_bytes.md) y viceversa.

Una vez cambiado, cada vez que hagamos una consulta a la [base de datos](../../db/db.md), en cuyo resultado contenga un [`TEXT`](../../db/sql/sqlite3/sqlite3_datatypes.md) o un [`BLOB`](../../db/sql/sqlite3/sqlite3_datatypes.md), nos lo devolverá en forma de [`bytes`](../py_bytes.md).

```python
import sqlite3

cx = sqlite3.connect("./main.db")

# Establecemos el resultado a bytes.
#                  v
cx.text_factory = byte

cx.close()
```

## ESQUEMA DE LA DB

Para obtener toda la estructura y datos de la [base de datos](../../db/db.md) en forma de texto se usa el [método](../class/py_methods.md) `iterdump`; este nos devolverá un generador con todo el contenido el cual podremos transformar en una [**lista**](../py_list.md) o [**tupla**](../py_tuple.md) si así lo queremos.

A continuación veremos un ejemplo de como guardar todo el contenido en un archivo de texto a modo de esquema:

```python
import sqlite3

cx = sqlite3.connect("main.db")

# Guardamos el generador del esquema.
gen = cx.iterdump()

# Juntamos todas instrucciones del esquema
# con saltos de líneas.
schema = "\n".join(gen)

# Abrimos el archivo en donde guardaremos
# es esquema y escribimos la información.
with open("schema.sql", "w") as file:
    file.write(schema)

cx.close()
```

En este último ejemplo hemos visto cómo guardar todo el esquema de la [base de datos](../../db/db.md) en un archivo, pero si por ejemplo quisiéramos filtrar todas las inserciones para así solo guardar la estructura y no los datos, podremos hacer lo de la siguiente forma:

```python
import sqlite3

cx = sqlite3.connect("main.db")

# Guardamos el generador del esquema.
gen = cx.iterdump()

rows = list()

# Filtramos todas las instrucciones que
# comiencen por "INSERT".
for row in gen:
    if not row[:6] == "INSERT":
        rows.append(row)

# Juntamos todas líneas restantes
# del esquema.
schema = "\n".join(rows)

# Abrimos el archivo en donde guardaremos
# es esquema y escribimos la información.
with open("schema.sql", "w") as file:
    file.write(schema)

cx.close()
```

## CREAR FUNCIONES

Para crear una función dentro de una conexión se usa el [método](../class/py_methods.md) `create_function`, este recibe tres argumentos, siendo primero el nombre que tendrá la susodicha función, luego el número de argumentos que recibirá y por último una referencia a una función de Python, esta última puede ser una que ya contiene Python o una que hayamos creado nosotros.

> [!abstract] SINTAXIS
> create_function(***\[name\]***, ***\[num\_args\]***, ***\[func\]***)

Como se puede ver en el siguiente ejemplo se crea una función que se encarga de capitalizar todas las palabras de una frase y devolver ese valor; este es un caso didáctico, por lo que no tiene mucho sentido el uso que se le está dando, ya que solo estamos haciendo un `SELECT` para ver el resultado:

```python
import sqlite3

def capitalize(text: str) -> str:
    words: list = text.split(" ")
    res:   list = list()

    for word in words:
        res.append(word[0].upper() + word[1:])

    return " ".join(res)

cx = sqlite3.connect("main.db")

cx.create_function("capitalize", 1, capitalize)

cr = cx.execute("SELECT capitalize(?)", ("hola mundo",))

for row in cr:
    print(row)
# SALIDA:
# ('Hola Mundo',)

cr.close()
cx.close()
```

> [!example] EJEMPLO
> Un ejemplo más realista de el uso de estas funciones sería cuando queremos hacer un filtrado de usuarios comprobando que el [DNI](../../../dump/dni.md) está bien escrito obteniendo así los que estén mal.

```sql
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    dni  TEXT
);

INSERT INTO users (name, dni)
VALUES
    ('Adelio', '00000000A'),
    ('Adelia', '00000001B');
```

Para el siguiente bloque de código de Python usaremos las funciones de cálculo de [DNI](../../../dump/dni.md):

![](../../../dump/dni.md#^dni-funcs)

```python
import sqlite3

cx = sqlite3.connect("main.db")

cx.create_function("valid_dni", 1, valid_dni)

cr = cx.execute("SELECT * FROM users WHERE NOT valid_dni(dni)")

for row in cr:
    print(row)
# SALIDA:
# ('Adelio', '00000000A')
# ('Adelia', '00000001B')

cr.close()
cx.close()
```

Como ninguno de los dos [DNIs](../../../dump/dni.md) es correcto obtenemos los dos registros.
