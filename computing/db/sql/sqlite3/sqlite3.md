---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: SQLite3
---

<h1 style="text-align:center;">SQLite3</h1>

![#logo](../../../../img/db.png)

---

# SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Rehacer todo el contenido de esta documentación para tenerlo más organizado y bien estructurado.
> > - [ ] Documentar que en la tabla `sqlite_schema` contiene información de las tablas e índices creados en la DB.
> > - [ ] Documentar que con `PRAGMA table_info([table_name])` obtenemos información de la tabla indicada.
> > - [ ] Ver el [vídeo](https://youtu.be/sgVpOaJLoG0) y documentar lo que enseña.
> > - [ ] Documentar la sentencia `ANY`.
> > - [ ] Documentar la sentencia `STRICT`.
> > - [ ] Checkout what's `WAL`.

> [!help]- REFERENCIAS WEB
> - [SQLite3 doc](https://sqlite.org/)
> - [SQLite Tutorial](https://www.sqlitetutorial.net/)
>
> YouTube:
> - [CS50](https://youtu.be/1RCMYG8RUSE)
> - [Decomplexify](https://www.youtube.com/@decomplexify)

> [!faq]- FAQ
> - [¿Qué es SQL?](../sql.md)

Para poder abrir el entorno de sqlite3 se debe escribir el comando `sqlite3`, tras esto entrarás en el entorno, pudiendo escribir comandos que afectarán a bases de datos.

Este comando nos permite también crear o abrir una base de datos, para ello seguido de este, se escribe al ruta y el nombre de la base de datos.

> [!abstract] SINTAXIS
> sqlite3 ***\[db_name\]***

## DUMP

- [Guardar una base de datos](commands/sqlite3_save_db.md)
- [Abrir una base de datos](commands/sqlite3_open_db.md)
- [Ver las tablas](commands/sqlite3_list_tables.md)
- [Consulta de datos](sqlite3_select.md)
- [Formato de salida de datos](commands/sqlite3_output_formats.md)
- [Ejecutar archivos SQL sobre la base de datos](commands/sqlite3_read_sql_files.md)

---

- [BASES DE DATOS](sqlite3_db.md)
- [TABLAS](sqlite3_table.md)
    - [TIPOS DE DATOS](sqlite3_datatypes.md)
- [INSERTAR REGISTROS](sqlite3_insert.md)
    - [REMPLAZAR](sqlite3_replace.md)
- [LEER REGISTROS](sqlite3_select.md)
- [TRANSACCIONES](sqlite3_transaction.md)
- [OPERADORES](sqlite3_operators.md)
- [PRAGMA](sqlite3_pragma.md)
- [TABLA MASTER](sqlite3_master.md)
- [TRIGGERS](sqlite3_trigger.md)
