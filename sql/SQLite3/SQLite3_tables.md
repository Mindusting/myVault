---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Tablas en SQLite3
---

<h1 style="text-align:center;">TABLAS EN SQLITE3</h1>

---

# REFERENCIAS WEB

- [SQLite3](https://sqlite.org/lang_createtable.html)

# VÍDEOS

- [Aaron Francis](https://youtu.be/sgVpOaJLoG0)

# TABLAS EN SQLITE3

%%
ESQUEMA DE CREACIÓN DE UNA TABLA

```txt
o─>(CREATE)┬────────────┬>(TABLE)┬>(IF)─>(NOT)─>(EXISTS)┐
           ├>(TEMP)─────┤        │                      │
           └>(TEMPORARY)┘        │                      │
┌─────────────────<──────────────┴─────────────<────────┘
├─>(schema-name)─>(.)┬>(table-name)┬>(AS)─>[select-stmt]───────>─────┐
└───────>────────────┘             │                                 │
┌───────────────────<──────────────┘                ┌────────>───────┼>o
└─>(()┬>[column-def]┬>┬────────────────────────┬>())┴>[table-options]┘
      └──────(,)<───┘ └[table-constraint]<─(,)<┘
```
%%

La creación de una tabla en *SQLite3* puede ser un poco complicado si pretendemos verlo todo de golpe, por tanto vamos a ir viendo las cosas paso a paso.

```sql
/*
Aquí indicamos la creación
de la tabla y su nombre.
*/
CREATE TABLE "users" (

    /*
    Entre los paréntesis indicaresmos
    los nombres de las comlumnas
    seguidos del tipo de dato que
    queremos guardar en la columna.
    */

    "first_name" TEXT, -- Coma para separar columnas.
    "last_name"  TEXT

    /*
    Como se puede ver, las columnas
    "first_name" y "last_name", son
    las dós de tipo "TEXT", esto
    quiere decir que vamos a guardar
    texto en ellas.
    */
);
```

Como se puede ver en el ejemplo, la tabla que hemos creado está hecha para guardar registros de usuarios, de momento solo hemos indicado que se va a guardar el nombre y el apellido, ahora, dos registro podrían coincidir con el mismo nombre y apellido por lo que no podríamos identificar cual es cual a la hora de hacer una búsqueda, o querer relacionar alguna otra información a la persona que a la que hace referencia el registro, para solucionar este problema usaremos otra columna, esta almacenará un número que identifique de forma única a cada registro.

### TIPOS DE DATO

- [SQLite3 DataTypes](https://www.sqlite.org/datatype3.html)

## CLAVE PRIMARIA

```sql
CREATE TABLE "users" (
 -- "id"         INTEGER
    "id"         INTEGER PRIMARY KEY,

    /*
    Como se puede ver en la línea anterior
    tenemos una línea comentada que indica
    la culumna "id" de tipo integer, ahora
    esa línea está comentada para que
    podais ver como sería la instrucción
    sin ningun extra, pero en este caso
    después de indicar el tipo (integer),
    indicamos que esta columna va a ser la
    clave primaria (PRIMARY KEY).
    */

    "first_name" TEXT,
    "last_name"  TEXT
)
```

La columna que va a ser usada como clave primaria, también se puede indica de la siguiente manera:

```sql
CREATE TABLE "users" (
    "id"         INTEGER,
    "first_name" TEXT,
    "last_name"  TEXT,
    PRIMARY KEY("id")

    /*
    En este caso podemos ver como en la
    última línea indicamos que la columna
    con el nombre "id" debe ser clave
    primaria.
    */
);
```

## VALOR NO NULO

Si queremos que una columna sea obligatoria, podemos indicar que sea de tipo ´NOT NULL´, esto nos obligará algún valor diferente de nulo (´null´), el uso que se le puede dar sería por ejemplo, si tenemos una tabla de usuarios, estos deben tener como mínimo un nombre, en ese caso sí nos sirve esta propiedad.

```sql
CREATE TABLE "users" (
    "id"         INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    -- Al ser "NOT NULL" el nombre es obligatorio.

    "last_name"  TEXT
)
```

## CLAVE EXTRANJERA

El uso que tienen las claves extranjeras podremos ver lo con un ejemplo sencillo, imaginaros que queremos hacer un programa el cual va ha almacenar notas, las cuales van a estar asociadas a diferentes usuarios, para esto, necesitaremos crear dos tablas ´users´ y ´notes´, cada registro de la tabla ´users´ tendrá una clave primaria que le identificará de forma inequíboca y cada registro de la tabla ´notes´ tendrá una clave extranjera que hará referencia a las claves primarias de los usuarios, esto permitirá identificar el propietario de una nota, simplemente tendremos que comparar la clave extranjera de la nota y buscar al usuarios con ese mismo *id*, a su vez, también podremos hacerlo en sentido contrario, si quisieramos ver las notas de un usuario en concreto, tendremos que comparar el *id* de cada nota con el usuario del cual queremos localizar las notas.

```sql
CREATE TABLE "users" (
    "id"         INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name"  TEXT
);

CREATE TABLE "notes" (
    "id" INTEGER PRIMARY KEY,

    /*
    La siguiente línea indica que el valor
    que se va ha introducir en esa columna
    va a ser un id existente en la columna
    "id" de la tabla "users".
    */

    "id_user" INTEGER FROREIGN KEY REFERENCES "users"("id"),
    "note" TEXT
);
```

## AUTOINCREMENTAR

- [SQLite3 AUTOINCREMENT](https://www.sqlite.org/autoinc.html)

---

Para crear una [tablas](../SQL_tables.md) básica en SQLite con la que podremos guardar datos de usuarios, podremos seguir el siguiente ejemplo.

```sql
CREATE TABLE "users" (
    "id"         INTEGER,
    "first_name" TEXT
);
```

Como se puede ver en el ejemplo, esta tabla tendrá dos columnas (`id` y `first_name`), con sus respectivos [tipos de datos](SQLite3_data_types.md).

Un cambio que podemos hacerle a este diseño de tabla sería hacer que el identificador del registro no se pueda repetir, sea [único](SQLite3_unique.md) y [clave primaria](../SQL_primary_key.md) auto [incremental](SQLite3_autoincrement.md), y ya de paso, que el nombre [no pueda ser `null`](SQLite3_not_null.md), ya que queremos que cada usuario tenga su propio nombre.

```sql
CREATE TABLE "users" (
    "id"         INTEGER NOT NULL UNIQUE,
    "first_name" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

También podemos dar a cada columna un [valor por defecto](SQLite3_default.md).

---

https://youtu.be/sgVpOaJLoG0

```
STRICT
ANY
```
