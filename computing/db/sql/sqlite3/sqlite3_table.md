---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Tablas en SQLite3
---

# TABLAS EN SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar como crear una tabla.
> >     - [ ] Documentar los tipos de datos.
> >     - [ ] Documentar el atributo `NOT NULL`.
> >     - [ ] Documentar el atributo `UNIQUE`.
> >     - [ ] Documentar el atributo `DEFAULT`.
> >     - [ ] Documentar el atributo `CHECK`.
> >     - [ ] Documentar el atributo `PRIMARY KEY`.
> >         - [ ] Documentar el atributo `AUTOINCREMENT`.
> >     - [ ] Documentar el atributo `FOREIGN KEY`.
> > - [ ] Documentar como modificar las tablas.
> >     - [ ] Documentar como renombrar una tabla.
> >     - [ ] Documentar como renombrar una columna.
> >     - [ ] Documentar como añadir una columna.
> >     - [ ] Documentar como borrar una columna.
> >     - [ ] Documentar como intercambiar los valores de las columnas.

> [!help]- REFERENCIAS WEB
> - [SQLite3](https://sqlite.org/lang_createtable.html)
> 
> YouTube:
> - [Aaron Francis](https://youtu.be/sgVpOaJLoG0)

> [!faq]- FAQ
> - [¿Qué son las tablas en SQL?](../sql_table.md)

En las **tablas** es en donde se va a almacenar la información de forma estructurada, más adelante veremos como relacionarlas entre sí.

## CREAR TABLA

Para crear una **tabla** tendremos que seguir la siguiente sintaxis; esta se constitulle de la declaración de creación de la **tabla** ensí junto con sunombre, seguido de la definición de las columnas que la fan a confirmar (*esto último se ve un poco más adelante*):

> [!abstract] SINTAXIS
> CREATE TABLE ***\[table\_name\]*** ([***\[col\_def\]***](#DEFINCIÓN%20DE%20COLUMNA));

```sql
-- Indicamos la creación
-- de la tabla "users".
CREATE TABLE users (
    -- La tabla tendrá dos columnas,
    -- siendo estas "id" y "name".
    id   INTEGER PRIMARY KEY,
    name TEXT
);
```

> [!warning] CUIDADO
> Si ya existe una **tabla** con el mismo nombre nos dará un error.
> Para evitarlo podemos usar la sentencia `IF NOT EXISTS`, haciendo así que solo se cree si no hay ninguna con ese nombre ya creada:
> ```sql
> -- Aquí se encuentra la indicación.
> --           v           v
> CREATE TABLE IF NOT EXISTS users (
>     id   INTEGER PRIMARY KEY,
>     name TEXT
> );
> ```

### DEFINCIÓN DE COLUMNA

La especificación de las **columnas** generalmente se indican a la hora de crear una **tabla** (*también puede ser al ser modificada*); esta se consitulle del nombre de la **columna** en cuestión, su [tipo de dato](sqlite3_datatypes.md), si puede ser un valor nulo, si es único o no y las restricciones de esta.

> [!abstract] SINTAXIS
> ***\[col\_name\] [\[data\_type\]](sqlite3_datatypes.md) [\{NOT NULL\}](#NOT%20NULL) [\{UNIQUE\}](#UNIQUE) [\{CHECK\}](#CHECK)***

#### NOT NULL

El valor **nulo** (`NULL`) se usa en los campos cuando desconocemos el valor que debería ir en dicho campo; indicar que una **columna** es `NOT NULL` quiere decir que no se pueden dejar campos vacios, oseasé, hace que la **columna** sea obligatoria; el uso que se le puede dar sería por ejemplo, si tenemos una **tabla** de usuarios, estos deben tener como mínimo un *nombre*, en ese caso sí nos sirve esta propiedad.

```sql
CREATE TABLE users (
    id    INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT
)
```

Si trataramos de introducir un registro sin indicar un valor nos dará un error debido a la restricción `NOT NULL`.

#### UNIQUE

#### DEFAULT

En la creación de una tabla, si indicamos un valor `DEFAULT` este será el que asigne en ese campo cuando creemos un nuevo registro y el valor de este no sea especificado, por defecto el valor es `NULL`, pero podemos cambiarlo de esta forma.

```sql
CREATE TABLE "users" (
    "id"         INTEGER NOT NULL UNIQUE,
    "first_name" TEXT NOT NULL DEFAULT "No-Name",
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

Como se puede ver en este ejemplo, en el caso de que se cree un registro en esta tabla y no se especifique ningún nombre, este obtendrá el valor por defecto, siendo en este caso `"No-Name"`.

#### CHECK

#### CLAVE PRIMARIA

Cada [tabla](sqlite3_table.md) solo puede tener una clave primaria, esta será una de las columnas y el valor que contenga no se podrá repetir entre los diferentes registros, por lo que tendrá el atributo [`unique`](SQLite3_unique.md) de forma implícita.

```sql
CREATE TABLE "users" (
    "id"         INTEGER,
    "first_name" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

En la declaración de la clave primaria, se puede ver como al final, se indica el atributo [`AUTOINCREMENT`](SQLite3_autoincrement.md), esto es para que cuando [insertemos](sqlite3_insert.md) un registro sin indicar el valor de la clave primaria, esta se adquiera automáticamente, cogiendo el valor más grande que se encuentre en esta columna y sumándo le `1`, en el caso en el que no haya ningún registro, el primer valor que obtendrá es `1`.

---

Para entender esto, imaginemos que tenemos la tabla `users` con los siguientes registros:

| id | first_name |
|---:|:-----------|
|  1 | admin      |
|  2 | Mindusting |
|  4 | Adelio     |

Si te fijas en los `id`, podrás ver que falta el registro `3`, esto puede ser por qué este registro ha sido [eliminado](sqlite3_delete.md) después de [insertar](sqlite3_insert.md) el registro `4` o por qué el registro cuatro se a [insertado](sqlite3_insert.md) indicando específicamente que se quería que tuviera ese `id`, en cualquier caso, cuando nosotros hagamos una nueva [inserción](sqlite3_insert.md) sin indicar un `id`, lo que hará SQLite3 será buscar el valor más grande, siendo en este caso `4`, para luego sumarle `1` e insertar el nuevo registro con el resultado de la operación anterior, quedando algo como esto:

| id | first_name |
|---:|:-----------|
|  1 | admin      |
|  2 | Mindusting |
|  4 | Adelio     |
|  5 | Adelia     |

---
---
---
---

ESQUEMA DE CREACIÓN DE UNA TABLA

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

%%
INFORMACIÓN DE LA TABLA
#TODO

Para consultar la información de las columnas de una tabla se puede usar la instrucción `PRAGMA table_info();`.

%%
SINTAXIS

```txt
PRAGMA table_info([table_name]);
```
%%

> [!abstract] SINTAXIS
> <span class="key-word-color">PRAGMA</span> <span class="flow-word-color">table_info</span>(<span class="italic class-color">[table_name]</span>);
%%

##### AUTOINCREMENTO

- [SQLite3 AUTOINCREMENT](https://www.sqlite.org/autoinc.html)

---

El atributo `AUTOINCREMENT` es utiliza en las [claves primarias](sqlite3_primary_key.md), este, la especificarlo, cambia ligeramente el comportamiento de la [clave primaria](sqlite3_primary_key.md):

Imaginemos que tenemos una tabla sin ningún registro al meter uno nuevo, este tendrá la clave primaria con el valor `1` y la siguiente con el valor `2`, ahora, si borramos la que tiene la clave primaria `2`.

- SIN `AUTOINCREMENT`:
    E [insertamos](sqlite3_insert.md) una nueva, esta tendrá de nuevo el valor `2`, ya que simplemente busca el valor más grande que se encuentre en la columna que sea [clave primaria](sqlite3_primary_key.md) y le suma uno.
- CON `AUTOINCREMENT`:
    E [insertamos](sqlite3_insert.md) una nueva, esta tendrá el valor `3`, ya que aunque el valor `2` ya no esté en uso, la tabla tiene un contador interno para la [clave primaria](sqlite3_primary_key.md), este contador indica que valor debe obtener el siguiente registro en la [clave primaria](sqlite3_primary_key.md).

---

Para crear una [tablas](../sql_table.md) básica en SQLite con la que podremos guardar datos de usuarios, podremos seguir el siguiente ejemplo.

```sql
CREATE TABLE "users" (
    "id"         INTEGER,
    "first_name" TEXT
);
```

Como se puede ver en el ejemplo, esta tabla tendrá dos columnas (`id` y `first_name`), con sus respectivos [tipos de datos](#TIPOS%20DE%20DATOS).

Un cambio que podemos hacerle a este diseño de tabla sería hacer que el identificador del registro no se pueda repetir, sea [único](#ÚNICO) y clave primaria auto [incremental](#AUTOINCREMENTO), y ya de paso, que el nombre [no pueda ser `null`](#NOT%20NULL), ya que queremos que cada usuario tenga su propio nombre.

```sql
CREATE TABLE "users" (
    "id"         INTEGER NOT NULL UNIQUE,
    "first_name" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

También podemos dar a cada columna un [valor por defecto](#DEFAULT).

#### CLAVE EXTRANJERA

El uso que tienen las claves extranjeras podremos ver lo con un ejemplo sencillo, imaginaros que queremos hacer un programa el cual va ha almacenar notas, las cuales van a estar asociadas a diferentes usuarios, para esto, necesitaremos crear dos tablas ´users´ y ´notes´, cada registro de la tabla ´users´ tendrá una clave primaria que le identificará de forma inequívoca y cada registro de la tabla ´notes´ tendrá una clave extranjera que hará referencia a las claves primarias de los usuarios, esto permitirá identificar el propietario de una nota, simplemente tendremos que comparar la clave extranjera de la nota y buscar al usuarios con ese mismo *id*, a su vez, también podremos hacerlo en sentido contrario, si quisiéramos ver las notas de un usuario en concreto, tendremos que comparar el *id* de cada nota con el usuario del cual queremos localizar las notas.

```sql
CREATE TABLE "users" (
    "id"         INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name"  TEXT
);

CREATE TABLE "notes" (
    id     INTEGER PRIMARY KEY,
    userId INTEGER
    note   TEXT,

    FOREIGN KEY (userId)
    REFERENCES users(id),
);
```

## MODIFICAR TABLA

> [!help]- REFERENCIAS WEB
> - [SQLite3 (`ALTER TABLE`)](https://sqlite.org/lang_altertable.html)

### RENOMBRAR TABLA

### RENOMBRAR COLUMNA

### AÑADIR COLUMNA

### BORRAR COLUMNA

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name\]*** DROP ***\[col\_name\]***;

### INTERCAMBIAR VALORES

```sql
UPDATE t
SET
    c0 = c1,
    c1 = c0;
```

## BORRAR TABLA

Para borrar una tabla se usa la instrucción `DROP TABLE` pudiendo complementarlo con `IF EXISTS` de forma opcional para finalmente indicar el *nombre de la tabla*.

> [!abstract] SINTAXIS
> DROP TABLE ***\{IF EXISTS\} \[table\_name\]***;

Creamos como ejemplo la tabla `users`.

```sql
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

Borramos la tabla con la sentencia `DROP TABLE`.

```sql
DROP TABLE users;
```

Si añadimos `IF EXISTS` a la sentencia al ejecutarla si la tabla no existe, no tendremos ningún error.

```sql
DROP TABLE IF EXISTS users;
```
