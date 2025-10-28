---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Tablas en MySQL
---

# TABLA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar la creación de una tabla.
> > - [x] Documentar listado de tablas.
> > - [ ] Documentar `CHECK`.
> >     - [ ] Documentar rango de valores.
> > - [ ] Documentar claves.
> >     - [ ] Clave primaria.
> >     - [ ] Clave foránea.
> > - [ ] Documentar restricciones (`CONSTRAINT`).
> > - [ ] Actualización en borrado.
> > - [ ] Actualización en edición.
> > - [ ] Documentar comentarios de columna (`COMMENT`).
> > - [ ] Valor por defecto.
> > - [ ] Repasar todo para comprobar que falta y si debo cambiar el texto.
> > - [ ] Comprobar faltas de ortografía.
> > - [ ] Explicar como cambiar el set de caracteres de una tabla.
> > - [ ] Explicar que es `ENGINE` de la tabla.
> > - [ ] Explicar que es el `MAX_ROWS` de la tabla.
> > - [ ] Explicar el `COMMENT` de la tabla.
> > - [ ] Explicar el `CHARACTER SET` de la tabla.
> > - [ ] Explicar el `COLLATE` de la tabla.
> > - [ ] Explicar `ON UPDATE`.
> > - [ ] Explicar `ON DELETE`.

> [!help]- REFERENCIAS WEB
> - [W3 (ALTER TABLE)](https://www.w3schools.com/mysql/mysql_alter.asp)

> [!faq]- FAQ
> - [¿Qué son las tablas en SQL?](../sql_table.md)

Una tabla nos permite almacenar información de forma ordenada dentro de nuestra DB, una DB puede albergar múltiples tablas, las cuales pueden estar relacionadas entre sí.

## CREAR TABLA

Para crear una tabla tendremos que seguir la siguiente sintaxis:

> [!abstract] SINTAXIS
> CREATE TABLE ***\[table\_name\]*** ([***\[col\_def\]***](#DEFINICIÓN%20DE%20COLUMNA));

```sql
-- Indicamos que la DB en la que
-- queremos trabajar es "my_db".
USE my_db;

-- Indicamos la creación de la tabla.
CREATE TABLE users (
    -- La tabla tendrá dos columnas,
    -- siendo estas "id" y "name".
    id   INTEGER PRIMARY KEY,
    name VARCHAR(16)
);
```

> [!warning] CUIDADO
> Si ya existe una **tabla** con el mismo nombre nos dará un error.
> Para evitarlo podemos usar la sentencia `IF NOT EXISTS`, haciendo así que solo se cree si no hay ninguna con ese nombre ya creada:
> ```sql
> CREATE TABLE IF NOT EXISTS users (
>     id   INTEGER PRIMARY KEY,
>     name VARCHAR(16)
> );
> ```

### DEFINICIÓN DE COLUMNA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que poner una explicación más extensa.
> > - [ ] Hay que poner un ejemplo de uso.

> [!abstract] SINTAXIS
> ***\[col\_name\] [\[data\_type\]](mysql_data_types.md) [\{modifier\}](#MODIFICADORES) [\{NULL|NOT NULL\}](#NULL%20Y%20NOT%20NULL) [\{DEFAULT \[value\]\}](#DEFAULT) [\{AUTO\_INCREMENT\}](#AUTO%20INCREMENTO) [\{COMMENT '\[comment\]'\}](#COMENTARIO%20DE%20COLUMNA) [\{COLLATE \[character_set\]\}](#SET%20DE%20CARACTERES) [\{ON UPDATE\} \{ON DELETE\}](#EN%20ACTUALIZADO%20Y%20BORRADO)***

#### MODIFICADORES

Los [tipos de datos](mysql_data_types.md) pueden tener modificadores para cambiar su comportamiento:

- `UNSIGNED`: solo se puede aplicar a modificadores numéricos enteros, sirve para que no se puedan almacenar números negativos y no es aplicable a los [tipos de datos](mysql_data_types.md) `FLOAT`, `DOUBLE`, `NUMERIC` y `DECIMAL`.
- `ZEROFILL`: rellena los espacios en blanco a la izquierda de un [tipo de dato](mysql_data_types.md) numérico con ceros, este modificador es obsoleto, no es recomendable usarlo.
- `BINARY`: se aplica a los [tipos de datos](mysql_data_types.md) `CHAR`, `VARCHAR`, `TINYTEXT`, `TEXT`, `MEDIUMTEXT` y `LONGTEXT`, sirve para que **MySQL** distinga entre mayúsculas y minúsculas (*por defecto no lo hace*), este modificador está obsoleto, por lo que no es recomendable usarlo.

#### NULL Y NOT NULL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que poner una explicación más extensa.
> > - [ ] Hay que poner un ejemplo de uso.

- `NULL`: indica que el campo no es requerido.
- `NOT NULL`: indica que el campo es requerido.

#### DEFAULT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que poner un ejemplo de uso.

Permite indicar el valor por defecto que recibe el campo en caso de hacerse una inserción sin especificar el valor del campo en cuestión, por defecto es `NULL`.

> [!abstract] SINTAXIS
> DEFAUTL ***\[value\]***

- Si la columna es de tipo numérico, se indica tal cual el número.
- Si se trata de una cadena de caracteres, se especifica el valor por defecto entre comillas simples.
- Si se trata de una fecha u hora, se indica el valor entre comillas simples, siguiendo el formato `'YYYY-MM-DD'` o `'hh:mm:ss'`.
- Si se trata de un campo enumerado (*`enum`*), hay que indicar un de los disponibles o `NULL`.

#### AUTO INCREMENTO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que poner un ejemplo de uso.

Que una campo sea `AUTO_INCREMENT` quiere decir que `MySQL` se encargará de darle un valor automático que incrementa por cada registro.

---

Tener un capo **auto incremental** en una tabla permite tener un campo que no se va a repetir, esto se suele usar para asignar *ids*, un ejemplo de esto puede ser que creemos dos registro de dos usuarios distintos y estos dos tengan el mismo nombre, sino tivieramos un *id* exclusivo para cada usuario internamente no podríamos diferenciar a los dos usuarios.

> [!abstract] SINTAXIS
> ***\[field_name] \[type] \[not_null]*** AUTO_INCREMENT

```sql
-- Indicamos que la DB en la que queremos trabajar es "my_database".
USE my_db;

-- Indicamos la creación de la DB.
CREATE TABLE users (
    -- La DB tendrá un solo campo, sinedo este "id".
    id INT NOT NULL AUTO_INCREMENT
    -- Este campo no puede ser igual a null y se auto incrementa.
);
```

#### COMENTARIO DE COLUMNA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que poner un ejemplo de uso.

Los comentarios de columna se usan simplemente para añadir una descripción o nota a cerda de para qué está pensada la columna.

> [!abstract] SINTAXIS
> COMMENT '***\[comment\]***'

#### SET DE CARACTERES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que poner un ejemplo de uso.

Sirve para cuando queremos darle un [set de caracteres](mysql_db.md#CONJUNTO%21DE%20CARACTERES) concreto y distinto al de la **tabla**.

> [!abstract] SINTAXIS
> COLLATE ***[\[character_set\]](mysql_db.md#CONJUNTO%20DE%20CARACTERES)***

### RESTRICCIONES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO

#### CLAVES

En las tablas de *SQL* existen lo que se conoce como **clave**, estos son campos campos que lo que tienen de especial es que no se pueden repetir, ya que por lo general son **auto incrementales**, existen dos tipos de **claves**, las [**primarias**](#CLAVE%20PRIMARIA) y las [**extranjeras**](#CLAVE%20EXTRANJERA).

##### CLAVE PRIMARIA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner un ejemplo.

Indica que el atributo o conjunto de atributos son únicos para poder identificar de forma inequívoca cada una de las tuplas.

> [!abstract] SINTAXIS
> PRIMARY KEY (***\[col\_name\] \{, \[col\_name\] ...\}***)

---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Para indicar que un **atributo** del registro tiene que ser una **llave primaria** se usa la **palabra clave** "**primary**" seguido de la **palabra clave** "**key**" y unos paréntesis, dentro de estos deberemos escribir el nombre de **atributo** que queramos que sea la **llave primaria** de nuestra tabla.

```sql
CREATE TABLE users (
    id    INT          NOT NULL,
    name  VARCHAR(16)  NOT NULL,
    edad  INT          NOT NULL,
    email VARCHAR(128) NOT NULL,

    PRIMARY KEY(id);
);
```

> [!error] COMPROBAR ESTE TEXTO YA QUE ESTÁ DESACTUALIZADO DEBIDO AQUE ES DE UNA BERSIÓN MAS ANTIGUA DE ESTE DOCUMENTO
> En este ejemplo se puede ver como al final de la creación de la tabla, se indica que el atributo "`id`" el cual es de tipo "`AUTO_INCREMENT`" será la llave primaria de esta tabla.

##### CLAVE EXTRANJERA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Una llave de tipo "`FOREIGN`" (**Del Inglés "Extranjero"**) es un atributo donde se va a guardar la llave primaria de otra tabla, pudiendo enlazar de esta forma los contenidos de las tablas.

```sql
CREATE TABLE products (
    id         INT         NOT NULL,
    name       VARCHAR(16) NOT NULL,
    created_by INT         NOT NULL,
    marca      varchar(64) NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(created_by) REFERENCES users(id)
);
```

En este ejemplo se puede ver como en al final de la creación de esta de esta tabla se  indica que el atributo "*created_by*" contendrá una **llave extranjera**, seguido de la **palabra clave** `reference` (**Del Inglés "Referencia"**) seguido por el nombre de la tabla a la cual queramos que esté vinculada junto con unos paréntesis, indicando entre estos el atributo que se va a usar como **llave extranjera**.

###### EN BORRADO

> [!abstract] SINSTAXIS
> ON DELETE ***\[RESTRICT|CASCADE|SET NULL|NO ACTION|SET DEFAULT\]***;

###### EN ACTUALIZADO

#### ÚNICO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner un ejemplo.
> > - [ ] Poner sintaxis.

Sirve para indicar que la columna no puede tener valores repetidos, esto se puede emplear como medida de seguridad (*como puede ser el DNI, que no debe repetirse entre personas*) y como creación de claves alternativas, pudiendo identificar de forma única a cada tupla.

---

Tener un capo obligatorio implica que a la hora de crear un nuevo registro este no puede quedar vacío,  esto nos puede servir por ejemplo si queremos que para crear un usuario este debe tener un correo electrónico asociado de forma obligatoria.

> [!abstract] SINTAXIS
> ***\[field_name] \[type]*** NOT NULL

```sql
-- Indicamos que la DB en la que queremos trabajar es "my_db".
USE my_database;

-- Indicamos la creación de la DB.
CREATE TABLE users (
    -- La DB tendrá un solo campo, sinedo este "id".
    id INT NOT NULL
    -- Este campo no puede ser igual a null.
);
```

#### NOMBRAR RESTRICCIONES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner un ejemplo.

Nombrar a las restricciones permite que después podamos buscarlas de forma más sencilla, cabe recalcar que las restricciones no tienen por qué tener nombre.

> [!abstract] SINTAXIS
> CONSTRAINT ***\[constraint\_name\] \[constraint\]***

#### CHEQUEO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner un ejemplo.
> > - [ ] Poner una explicación de `expresion`.
> >     - [ ] Between.
> >     - [ ] And.
> >     - [ ] In.

> [!abstract] SINTAXIS
> CHECK (***\[expresion\]***) ***[\{\{NOT\} ENFORCED\}](#CUMPLIR%20CHEQUEO)***

##### CUMPLIR CHEQUEO

Indicar al final de un [`CHECK`](#CHEQUEO) que es `ENFORCED`, `NOT ENFORCED` especifica el comportamiento de este:

- `ENFORCED`: comprueba que el [`CHECK`](#CHEQUEO) se cumple y no deja introducir datos que no cumplan el [`CHECK`](#CHEQUEO).
- `NOT ENFORCED`: crea el [`CHECK`](#CHEQUEO) pero este no es comprobado a la hora de introducir los datos, por lo que podremos introducirlos aunque no se cumplan.

### EN ACTUALIZADO Y BORRADO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner una mejor explicación.
> > - [ ] Poner algún ejemplo.

El objetivo de estas instrucciones es que el gestos de la **DB**, antes de borrar o modificar una tupla (*padre*), comprueba si hay otras relacionadas a esta (*hija*), en caso de entrar alguna, aplicará las instrucciones indicadas.

> [!abstract] SINTAXIS
> ON DELETE ***\[action\]***
> ON UPDATE ***\[action\]***

- **Padre**: son las tuplas que tiene **hijos** en dependencia a través de las relaciones entre **tablas**.
- **Hijo**: son las tuplas que son dependientes de **padres** través de las relaciones entre **tablas**.

---

- `RESTRICT`: no se permite borra **padres** que tengan **hijos** (*es el valor por defecto*).
- `CASCADE`: borra o modifica los **hijos** cuyos **padres** hayan sido borrados o modificados.
- `SET NULL`: si un **padre** es borrado o modificado, las [claves ajenas](#CLAVE%20EXTRANJERA) del **hijo** se establecerán a `NULL`.
- `NO ACTION`: es equivalente a `RESTRICTA`.
- `SET DEFAULT`: es similar a `SET NULL` con la diferencia de que en este se indica el valor por defecto queremos que se le de en vez de `NULL`.

## LISTAR TABLAS

Para listar todas las tablas que tenemos en la **DB** tenemos que usar la instrucción `SHOW TABLES`.

> [!abstract] SINTAXIS
> SHOW TABLES;

```sql
SHOW TABLES;
```

## DESCRIBIR TABLA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner una explicación más extensa.
> > - [ ] Poner un ejemplo.

Para poder ver como está compuesta una tabla podemos usar la instrucción `DESC` (*abreviación de descripción en inglés*).

> [!abstract] SINTAXIS
> DESC ***\[table\_name\]***;

```sql
CREATE TABLE users (
    id       INTEGER     PRIMARY KEY,
    name     VARCHAR(16) NOT NULL,
    lastName VARCHAR(16),
    dni      CHAR(9)     NOT NULL UNIQUE
    CHECK (LENGTH(dni) = 9)
);

DESC users;
```

> [!quote] Resultado de la descripción de `users`:
| Field    | Type        | Null | Key | Default | Extra |
|:-------- |:----------- |:---- |:--- |:------- |:----- |
| id       | INTEGER     | NO   | PRI | NULL    |       |
| name     | VARCHAR(16) | NO   |     | NULL    |       |
| lastName | VARCHAR(16) | YES  |     | NULL    |       |
| dni      | CHAR(9)     | NO   |     | NULL    |       |

## RENOMBRAR TABLA

Renombrar una tabla nos permite corregir un erro que hayamos cometido a la hora de crear la tabla.

> [!abstract] SINTAXIS
> RENAME TABLE ***\[table\_name]*** TO ***\[new\_table\_name]***;

```sql
RENAME TABLE users TO my_users;
```

No es recomendable tener nombres tan poco descriptivos, simplemente es un ejemplo de como se puede hacer.

## MODIFICAR TABLA

Modificar un capo de una tabla nos puede servir para cambiar las propiedades de estos en caso de que nos hayamos equivocado o queramos darle otro uso.

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name]***
> ***\[modification\]***;

### AÑADIR COLUMNA

Para añadir una **columna** usaremos la instrucción `ADD`:

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name\]***
> ADD ***\[col\_name\] [\[col\_def\]](#DEFINICIÓN%20DE%20COLUMNA)***;

```sql
ALTER TABLE users
ADD dni CHAR(9) CHECK (LENGTH(dni) = 9);
```

### BORRAR COLUMNA

Para borra una **columna** usaremos la instrucción `DROP COLUMN`:

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name\]***
> DROP COLUMN ***\[col\_name\]***;

```sql
ALTER TABLE users
DROP COLUMN dni;
```

---

En el caso de querer borrar la clave primaria se puede hacer de la siguiente manera:

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name\]***
> DROP PRIMARY KEY;

```sql
ALTER TABLE users
DROP PRIMARY KEY;
```

### MODIFICAR COLUMNA

Para modificar una **columna** usaremos la instrucción `MODIFY`:

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name\]***
> MODIFY ***\[col\_name\] [\[col\_def\]](#DEFINICIÓN%20DE%20COLUMNA)***;

```sql
ALTER TABLE users
MODIFY dni CHAR(9) NOT NULL CHECK (LENGTH(dni) = 9);
```

### CAMBIAR COLUMNA

Para cambiar una **columna** usaremos la instrucción `CHANGE`:

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name\]***
> CHANGE ***\[old\_col\_name\]*** ***\[new\_col\_name\] [\[col\_def\]](#DEFINICIÓN%20DE%20COLUMNA)***;

```sql
ALTER TABLE users
CHANGE name fisrtName VARCHAR(16) NOT NULL;
```

## BORRAR TABLAS

> [!warning] ANTES DE BORRAR
>  Cuidado al borra una tabla, ya que se perderá todo su contenido, asegura te de que realmente quieres borrar la tabla antes de ejecutar la instrucción (*Una vez borrado no se podrá recuperar el contenido*).

Para borrar una tabla se usa la instrucción "**drop table**" seguida del nombre de la tabla que se quiera borrar, si se quiere borrar varias tables, estas pueden ser borradas con una sola instrucción separando los nombres con *comas*.

> [!abstract] SINTAXIS
> DROP TABLE ***\[table_name]***, ***\[table_name]*** ...;

```sql
-- Se borra una sola tabla.
DROP TABLE users;

-- Se borran múltiples tablas.
DROP TABLE productos, pedidos;
```
