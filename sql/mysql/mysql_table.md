---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: Tablas en MySQL
---

# TABLA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo]
> > - [ ] Documentar la creación de una tabla.
> > - [ ] Documentar listado de tablas.
> > - [ ] Documentar `CHECK`.
> >     - [ ] Documentar rango de valores.
> > - [ ] Documentar claves.
> >     - [ ] Clave primaria.
> >     - [ ] Clave foránea.
> > - [ ] Documentar restricciones (`CONSTRAINT`).
> > - [ ] Documentar tipos de datos.
> >     - [ ] Tipo de dato `TIMESTAMP`.
> >     - [ ] Tipo de dato `ENUM`.
> >     - [ ] Tipo de dato `SET`.
> > - [ ] Actualización en borrado.
> > - [ ] Actualización en edición.
> > - [ ] Documentar comentarios de columna (`COMMENT`).
> > - [ ] Valor por defecto.
> > - [ ] Repasar todo para comprobar que falta y si debo cambiar el texto.
> > - [ ] Comprobar faltas de ortografía.

> [!faq] FAQ
> - [¿Qué son las tablas en SQL?](../sql_table.md)

Una tabla nos permite almacenar información de forma ordenada dentro de nuestra DB, una DB puede albergar múltiples tablas, las cuales pueden estar relacionadas entre sí.

## CREAR TABLA

> [!abstract] SINTAXIS
> CREATE TABLE ***\[table\_name\]*** (***\[field\_name\]***);

```sql
-- Indicamos que la DB en la que queremos trabajar es "my_db".
use my_db;

-- Indicamos la creación de la DB.
CREATE TABLE users (
    -- La DB tendrá un solo campo, siendo este "id".
    id   INTEGER PRIMARY KEY,
    name VARCHAR(16)
);
```

Una tabla requiere de al menos un campo en el que se pueda guardar información, el campo indicado en este ejemplo es "*id*", este almacenará un valor entero y se usará para identificar cada [registro](#^Crear-registros)[^registro] (*Por así decirlo, es una matrícula para cada [registro](#^Crear-registros)*), dando le un valor distinto a cada uno, pero tal y como está ahora, diferentes [registro](#^Crear-registros) pueden tener el mismo valor en este capo, para evitar esto hay que [modificarlo](#^Modificar-una-tabla) para convertirlo en un valor *key*.

[^registro]: Un registro es un objeto donde se guardan los datos de por ejemplo un cliente, si creamos una tabla llamada "*clientes*", dentro de estas se guardarán los *registros* "*cliente*", a su vez, cada uno de estos almacenará el \[nombre, apellidos, DNI, email, ...\] del cliente por cada registro (*Objeto "cliente"*).

## LISTAR TABLAS

%%
> [!abstract] SINTAXIS
> SHOW FULL TABLES FROM ***\[db_name\]***;
%%

> [!abstract] SINTAXIS
> SHOW TABLES;

```sql
SHOW TABLES;
```

## RENOMBRAR TABLA

Renombrar una tabla nos permite corregir un erro que hayamos cometido a la hora de crear la tabla.

> [!abstract] SINTAXIS
> RENAME TABLE ***\[table\_name]*** TO ***\[new\_table\_name]***;

```sql
RENAME TABLE users TO my_users;
```

No es recomendable tener nombres tan poco descriptivos, simplemente es un ejemplo de como se puede hacer.

## MODIFICAR TABLA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Modificar un capo de una tabla nos puede servir para cambiar las propiedades de estos en sado de que nos hayamos equivocado o queramos darle otro uso.

[^1]: Nota al pie.

> [!abstract] SINTAXIS
> ALTER TABLE ***\[table\_name]***
> MODIFY COLUMN ***\[field\_name] \[type] \[propeties]***;

## CAMPOS OBLIGATORIO

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

## DATOS AUTO INCREMENTALES

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

## LLAVES

En las tablas de *SQL* existen lo que se conoce como **llaves**, estos son campos campos que lo que tienen de especial es que no se pueden repetir, ya que por lo general son **auto incrementales**, existen dos tipos de **llaves**, las **primarias** y las **extranjeras**.

### PRIMARIAS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

Para indicar que un **atributo** del registro tiene que ser una **llave primaria** se usa la **palabra clave** "**primary**" seguido de la **palabra clave** "**key**" y unos paréntesis, dentro de estos deberemos escribir el nombre de **atributo** que queramos que sea la **llave primaria** de nuestra tabla.

```sql
CREATE TABLE users (
    id    INT NOT NULL AUTO_INCREMENT
    name  VARCHAR(16) NOT NULL,
    edad  INT NOT NULL,
    email VARCHAR(128) NOT NULL,

    PRIMARY KEY(id);
);
```

En este ejemplo se puede ver como al final de la creación de la tabla, se indica que el atributo "`id`" el cual es de tipo "`AUTO_INCREMENT`" será la llave primaria de esta tabla.

### EXTRANJERAS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

Una llave de tipo "`FOREIGN`" (**Del Inglés "Extranjero"**) es un atributo donde se va a guardar la llave primaria de otra tabla, pudiendo enlazar de esta forma los contenidos de las tablas.

```sql
CREATE TABLE products (
    id         INT NOT NULL AUTO_INCREMENT,
    name       VARCHAR(16) NOT NULL,
    created_by INT NOT NULL,
    marca      varchar(64) not NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(created_by) REFERENCES users(id)
);
```

En este ejemplo se puede ver como en al final de la creación de esta de esta tabla se  indica que el atributo "*created_by*" contendrá una **llave extranjera**, seguido de la **palabra clave** `reference` (**Del Inglés "Referencia"**) seguido por el nombre de la tabla a la cual queramos que esté vinculada junto con unos paréntesis, indicando entre estos el atributo que se va a usar como **llave extranjera**.

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