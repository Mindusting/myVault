---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: SQLite3
---

<h1 style="text-align:center;">SQLite3</h1>

![#logo](../../img/db.png)

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

> [!help]- REFERENCIAS WEB
> YouTube:
> - [CS50](https://youtu.be/1RCMYG8RUSE)

> [!faq]- FAQ
> - [¿Qué es SQL?](../sql.md)

Para poder abrir el entorno de sqlite3 se debe escribir el comando `sqlite3`, tras esto entrarás en el entorno, pudiendo escribir comandos que afectarán a bases de datos.

Este comando nos permite también crear o abrir una base de datos, para ello seguido de este, se escribe al ruta y el nombre de la base de datos.

> [!abstract] SINTAXIS
> sqlite3 ***\[db_name\]***

%%
# DUMP

- [Guardar una base de datos](SQLite3_save_db.md)
- [Abrir una base de datos](SQLite3_open_db.md)
- [Ver las tablas](SQLite3_list_tables.md)
    - [Info de las tablas](SQLite3_table_info.md)
- [Consulta de datos](SQLite3_select.md)
- [Formato de salida de datos](SQLite3_output_formats.md)
- [Llave primaria](SQLite3_primary_key.md)
- [Llave extrangera](SQLite3_foreign_key.md)
- [Ejecutar archivos SQL sobre la base de datos](sqlite3_read_sql_files.md)
- [Tabla sqlite_master](SQLite3_sqlite_master.md)
- [Tipos de datos](sqlite3_data_types.md)
%%

- [CREAR TABLAS](sqlite3_tables.md)
- [INSERTAR REGISTROS](SQLite3_insert.md)
- [LEER REGISTROS](SQLite3_select.md)
- [VALOR POR DEFECTO](SQLite3_default.md)
- [OPERADORES](SQLite3_operators.md)

---

## TIPOS DE DATOS

- [Tipos de datos](https://www.sqlite.org/datatype3.html)

| TIPOS DE SQLITE3 | TIPOS DE PYTHON |
|:---------------- |:--------------- |
| NULL             | None            |
| INTEGER          | Bool            |
| INTEGER          | Int             |
| REAL             | Float           |
| TEXT             | Str             |
| BLOB             | Bytes           |
