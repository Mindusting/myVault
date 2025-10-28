---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Ejecutar archivos de SQL en SQLite3
---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para poder ejecutar en archivo `.sql` en nuestra base de datos podemos usar el comado `.read`, una vez ayamos abrierto nuestra base de datos, tendremos que escribir la siguiente sintaxis:

> [!abstract] SINTAXIS
> .read ***\[sql_file_name\]***

También existe al posibilidad de, teniendo la base de datos cerrada, podemos segir la siguiente sintaxis:

> [!abstract] SINTAXIS
> sqlite3 ***\[db_name\]*** < ***\[sql_file_name\]***

