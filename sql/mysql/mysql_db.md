---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: DB en MySQL
---

# DB EN MYSQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> - [ ] Escribir una explicación en la creación de la DB.
> - [ ] Escribir una explicación en el apartado de renombrar la DB.
> - [ ] Escribir una explicación en la modificación de la DB.

> [!faq] FAQ
> - [¿Qué es una DB?](../sql_db.md)

## CREAR UNA DB

> [!abstract] SINTAXIS
> CREATE DATABASE ***\[db\_name]***;

```sql
CREATE DATABASE my_db;
```

> [!note]
> También es posible usar `SCHEMA` en sustitución a `DATABASE`.

### CONJUNTO DE CARACTERES

Establecer un conjunto de caracteres correcto para la DB permite que esta sea capaz de interpretas correctamente el texto que se quiere almacenar en ella.

Para poder ver los conjuntos de caracteres permitidos se puede usar la siguiente instrucción:

> [!abstract] SINTAXIS
> SHOW CHARACTER SET;

Una vez hemos elegido un conjunto de datos, para crear una DB con ese conjunto de caracteres específico, tendremos que seguir la siguiente sintaxis:

> [!abstract] SINTAXIS
> CREATE DATABASE ***\[db\_name]***
> COLLATE ***\[character_set]***;

```sql
CREATE DATABASE my_db
COLLATE utf8mb4_spanish_ci;
```

## LISTAR DDBB

Si queremos saber que DB tenemos creadas podremos hacerlo mediante la siguiente instrucción, esta nos listará los nombre de las DB.

> [!abstract] SINTAXIS
> SHOW DATABASES;

```sql
SHOW DATABASES;
```

## ÁREA DE TRABAJO

Para poder trabajar sobre una DB primero debemos establecerla como área de trabajo, para ello seguiremos la siguiente sintaxis:

> [!abstract] SINTAXIS
> USE ***\[db_name]***;

```sql
USE my_db;
```

## RENOMBRAR DB

> [!abstract] SINTAXIS
> RENAME DATABASE ***\[db\_name\]*** TO ***\[new\_db\_name\]***;

```sql
RENAME DATABASE my_db TO test_db;
```

## MODIFICAR DB

> [!abstract] SINTAXIS
> ALTER DATABASE ***\[db\_name\]***
> ***\[modification]***;

```sql
ALTER DATABASE my_db
CHARACTER SET latin1;
```

> [!note]
> También es posible usar `SCHEMA` en sustitución a `DATABASE`.

## BORRA DB

Para poder borra una DB esta no deber estar establecida como área de trabajo.

> [!warning] ANTES DE BORRAR
> Cuidado al borra una DB, ya que se perderá todo su contenido, asegura te de que realmente quieres borrar la DB antes de ejecutar la instrucción (Una vez borrado no se podrá recuperar el contenido).

> [!abstract] SINTAXIS
> DROP DATABASE ***\[db\_name\]***;

```sql
DROP DATABASE my_db;
```