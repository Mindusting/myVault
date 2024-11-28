---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: DB en MySQL
---

# DB EN MYSQL

> [!faq] FAQ
> - [¿Qué es una DB?](../sql_db.md)

## CREAR UNA DB

> [!abstract] SINTAXIS
> CREATE DATABASE ***\[db\_name]***;

```sql
CREATE DATABASE my_db;
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

## BORRA DB

Para poder borra una DB esta no deber estar establecida como área de trabajo.

> [!warning] ANTES DE BORRAR
> Cuidado al borra una DB, ya que se perderá todo su contenido, asegura te de que realmente quieres borrar la DB antes de ejecutar la instrucción (Una vez borrado no se podrá recuperar el contenido).

> [!abstract] SINTAXIS
> DROP DATABASE ***\[db\_name\]***;

```sql
DROP DATABASE my_db;
```