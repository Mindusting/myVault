---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Consultas en MySQL
---

# CONSULTAS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Re estructurar todo el documento.
> >     - [x] Indicar que para poder hacer consultas primero se deben introducir datos.
> >     - [ ] Hacer un apartado de consultas simples.
> >         - [ ] Documentar el `AS`.
> >         - [ ] Documentar el `WHERE`.
> >             - [ ] Explicar los operadores lógicos en el `WHERE`.
> >             - [ ] Explicar los operadores aritméticos en el `WHERE`.
> >             - [ ] Explicar los operadores relacionales en el `WHERE`.
> >             - [x] Explicar los operador `LIKE` en el `WHERE`.
> >             - [ ] Explicar los operador `BETWEEN` en el `WHERE`.
> >             - [ ] Explicar los operador `IN` en el `WHERE`.
> >             - [ ] Explicar los operador `IS` en el `WHERE`.
> >             - [ ] Explicar la prioridad de los operadores en el `WHERE`.
> >         - [x] Documentar el `ORDER BY`.
> >         - [ ] Documentar el `JOIN`.
> >     - [ ] Hacer un apartado de consultas complejas.

> [!warning] AVISO
> Para poder obtener datos, primero tendremos que crear por lo menos una [tabla](mysql_table.md) e [insertar datos](mysql_insert.md), es por eso que recomiendo mirar primero esos dos apartados.

Las consultas en [SQL](../sql.md) sirven para obtener información de la **tablas**, para poder hacer la consulta más básica tendremos que usar las palabras clave `SELEC` y `FROM`.

- `SELECT`: Permite indicar que **columnas** queremos obtener de la consulta, mediante sus *nombres*.
- `FROM`: Permite indicar la tabla de la que queremos obtener la información.

> [!abstract] SINTAXIS
> SELECT ***\[col\_name\], ...***
> FROM ***\[table\_name\]***;

```sql
-- Creación de la tabla.
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    sex  INTEGER
    CHECK (sex IN (0, 1))
);

-- Inserción de datos.
INSERT INTO users (name, sex)
VALUES
    ("Adelio", 1),
    ("Adelia", 0),
    ("Jon",    1),
    ("Sara",   0);

-- Consulta.
SELECT id, name
FROM users;
/*
RESULTADO DE LA CONSULTA
+----+--------+
| id |  name  |
+----+--------+
| 1  | Adelio |
| 2  | Adelia |
| 3  | Jon    |
| 4  | Sara   |
+----+--------+
*/
```

Como se puede ver en este ejemplo, como en la consulta hemos indicado que queremos obtener las *columnas* `id` y `name`, se nos ha mostrado esa información.

> [!important] IMPORTANTE
> Si seguido al `SELECT` ponemos un **asterisco** (\*), esto indica que queremos la totalidad de las *columnas*.

## WHERE

Si queremos hacer un cribado de la consulta, podemos usar la palabra clave `WHERE` (*Del inglés "dónde"*), siguiendo la lógica de "_muestra me los datos en **dónde** se cumplan las siguientes condiciones_", esto es debido a que tras indicar el `WHERE` tendremos que especificar las condiciones bajo las que obtendremos la información.

> [!abstract] SINTAXIS
> SELECT ***\[col\_name\], ...***
> FROM ***\[table\_name\]***
> WHERE ***\[condition\]***;

```sql
-- Creación de la tabla.
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    sex  INTEGER
    CHECK (sex IN (0, 1))
);

-- Inserción de datos.
INSERT INTO users (name, sex)
VALUES
    ("Adelio", 1),
    ("Adelia", 0),
    ("Jon",    1),
    ("Sara",   0);

-- Primera consulta.
SELECT id, name, sex
FROM users
WHERE sex = 0;
/*
RESULTADO DE LA CONSULTA
+----+--------+-----+
| id |  name  | sex |
+----+--------+-----+
| 2  | Adelia | 0   |
| 4  | Sara   | 0   |
+----+--------+-----+
*/

-- Segunda consulta.
SELECT id, name, sex
FROM users
WHERE sex = 1;
/*
RESULTADO DE LA CONSULTA
+----+--------+-----+
| id |  name  | sex |
+----+--------+-----+
| 1  | Adelio | 1   |
| 3  | Jon    | 1   |
+----+--------+-----+
*/
```

### OPERADORES RELACIONALES

| OPERADOR | SIGNIFICADO   |
|:--------:|:------------- |
|    <     | Menor que     |
|    <=    | Menor o igual |
|    >     | Mayor         |
|    >=    | Mayor o igual |
|    =     | Igual a       |
|  != <>   | Distinto de   |

### OPERADORES ARITMÉTICOS

| OPERADOR | SIGNIFICADO                        |
|:--------:|:---------------------------------- |
|    +     | Suma                               |
|    -     | Resta o cambio de signo (*unario*) |
|    \*    | Multiplicación                     |
|    /     | División                           |
|   div    | División entera                    |
|  \% mod  | Resto de división entera           |

### OPERADORES LÓGICOS

|    AND    | TRUE  | FALSE | NULL  |
|:---------:|:-----:|:-----:|:-----:|
| **TRUE**  | TRUE  | FALSE | NULL  |
| **FALSE** | FALSE | FALSE | FALSE |
| **NULL**  | NULL  | FALSE | NULL  |

|    OR     | TRUE | FALSE | NULL |
|:---------:|:----:|:-----:|:----:|
| **TRUE**  | TRUE | TRUE  | TRUE |
| **FALSE** | TRUE | FALSE | NULL |
| **NULL**  | TRUE | NULL  | NULL |

|    NOT    |  RES  |
|:---------:|:-----:|
| **TRUE**  | FALSE |
| **FALSE** | TRUE  |
| **NULL**  | NULL  |

### LIKE

El operador `LIKE` permite hacer consultas sobre texto de una forma más sencilla, ya que podemos indicar un formato, para ello, podemos usar dos caracteres especiales:

- `%`: indica un texto de *0* a *n* caracteres.
- `_`: indica un carácter obligatorio.

> [!abstract] SINTAXIS
> ***\[col\_name\]*** LIKE ***\[pattern\]***

```sql
-- Creación de la tabla.
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    sex  INTEGER
    CHECK (sex IN (0, 1))
);

-- Inserción de datos.
INSERT INTO users (name, sex)
VALUES
    ("Adelio", 1),
    ("Adelia", 0),
    ("Jon",    1),
    ("Sara",   0);

-- Consulta.
SELECT id, name, sex
FROM users
WHERE name LIKE "%li_";
/*
RESULTADO DE LA CONSULTA
+----+--------+-----+
| id |  name  | sex |
+----+--------+-----+
| 1  | Adelio | 1   |
| 2  | Adelia | 0   |
+----+--------+-----+
*/
```

## ORDER BY

Para ordenar el resultado de una consulta se usa la sentencia `ORDER BY`, seguido a esta pondremos los nombres de las *columnas* que usará como referencia para ordenar, pudiendo indicar incluso el orden de preferencia y si queremos que sea de forma *ascendente* o *descendente*.

- `ASC`: (*por defecto*) indica que se debe ordenar de forma *ascendente*.
- `DESC`: indica que se debe ordenar de forma *descendente*.

> [!note] NOTA
> El orden se realizará en caso de ser valores numéricos, desde el más pequeño al más grade, en caso de ser texto, irá ordenado alfabéticamente, y si son fechas irá de la más antigua a la más moderna.
> 
> Ten en cuanta que el orden se invierte si indicamos `DESC`.

> [!abstract] SINTAXIS
> SELECT ***\[col\_name\], ...***
> FROM ***\[table\_name\]***
> ORDER BY ***\[col\_name\] \{ASC/DESC\}, ...***;

```sql
-- Creación de la tabla.
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    sex  INTEGER
    CHECK (sex IN (0, 1))
);

-- Inserción de datos.
INSERT INTO users (name, sex)
VALUES
    ("Adelio", 1),
    ("Adelia", 0),
    ("Jon",    1),
    ("Sara",   0);

-- Consulta.
SELECT id, name, sex
FROM users
ORDER BY sex, name DESC;
/*
RESULTADO DE LA CONSULTA
+----+--------+-----+
| id |  name  | sex |
+----+--------+-----+
| 4  | Sara   | 0   |
| 2  | Adelia | 0   |
| 3  | Jon    | 1   |
| 1  | Adelio | 1   |
+----+--------+-----+
*/
```

En este ejemplo se puede ver como el resultado se ha ordenado primero en base al sexo del registro, este al ser numérico (*y de forma `ASC` por defecto*) se ha ordenado de forma que las mujeres salen primero y luego los hombres, y estos se han ordenado en base al nombre, esta vez de forma `DESC`, por lo que están de forma inversa al alfabeto.

---

También es posible usar el número de la *columna* del `SELECT` para indicar el orden, de forma que no tengamos que poner le nombre de la *columna*, para hacer el mismo ejemplo de antes de esta nueva forma se hace así:

```sql
--      1,   2 ,  3
SELECT id, name, sex
FROM users
ORDER BY 3, 2 DESC;
```

## ALIAS

Para poner un *alias* a las **tablas** o **columnas** se usa la sentencia `AS`, a su vez, esta tiene dos formas de formularse, *implícita* y *explícita*, primero veremos la *explicita*.

> [!abstract] SINTAXIS
> ***\[old\_name\]*** AS ***\[new\_name\]***

```sql
-- Creación de la tabla.
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    sex  INTEGER
    CHECK (sex IN (0, 1))
);

-- Inserción de datos.
INSERT INTO users (name, sex)
VALUES
    ("Adelio", 1),
    ("Adelia", 0),
    ("Jon",    1),
    ("Sara",   0);

-- Consulta.
SELECT
    u.id   AS number,
    u.name AS "first name",
    u.sex  AS gender
FROM users AS u;
/*
RESULTADO DE LA CONSULTA
+--------+--------+--------+
| number |  name  | gender |
+--------+--------+--------+
| 1      | Adelio | 1      |
| 2      | Adelia | 0      |
| 3      | Jon    | 1      |
| 4      | Sara   | 0      |
+--------+--------+--------+
*/
```

Como se puede ver en este ejemplo se le da un *alias* a la **tabla** y luego se hace referencia a las **columnas** mediante el *alias*, esto se verá más en el apartado [`UNION`](#UNION), ya que se usan múltiples **tablas** y se debe indicar de que **tabla** queremos la **columna**.

---
---
---
---
---
---
---

## UNION

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```sql
----------------------------
-- CREACIÓN DE LAS TABLAS --
----------------------------
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(16) NOT NULL,
    dni  CHAR(9) NOT NULL CHECK (LENGTH(dni) = 9)
);

CREATE UNIQUE INDEX "i_dni_users" ON "users" (
    "dni"
);

CREATE TABLE notes (
    id      INTEGER PRIMARY KEY,
    id_user INTEGER,
    note    VARCHAR(255),
    
    CONSTRAINT fk_id_user_notes
    FOREIGN KEY (id_user) REFERENCES users(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

------------------------
-- INSERCIÓN DE DATOS --
------------------------
INSERT INTO users (name, dni)
VALUES
    ('Adelio', '12345678A'),
    ('Adelia', '23456789B');

INSERT INTO notes (id_user, note)
VALUES
    (1, 'Esta es la primera nota de Adelio.'),
    (1, 'Esta es la segunda nota de Adelio.'),
    (2, 'Esta es la primera nota de Adelia.'),
    (2, 'Esta es la segunda nota de Adelia.');
```

### UNION ON

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```sql
SELECT *
FROM users
JOIN notes
ON users.id = notes.id_user;
```
