---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Usuarios y roles en MySQL
---

# USUARIOS Y ROLES EN MYSQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Documentar cual es la utilidad de crear usuarios en MySQL.
> > - [x] Documentar que los usuarios puede tener o no contraseña.
> > - [x] Documentar que los usuarios pueden tener roles.
> > - [ ] Documentar los privilegios que pueden tener los usuarios.
> > - [ ] Documentar que la contraseña puede expirar.
> > - [ ] Documentar en donde se guardan los usuarios y su información en MySQL.
> > - [ ] Documentar los permisos.
> > - [ ] Documentar los roles.

> [!faq]- FAQ
> - [¿Qué son los usuarios en SQL?](../sql_users.md)

## USUARIOS

### CREACIÓN DE USUARIOS

Para crear un usuario de la forma más sencilla posible se hace siguiendo la siguiente sintaxis, en la que podremos de forma opcional indicar la contraseña que tendrá este usuario, ==no es recomendable que un usuario no tenga contraseña==.

> [!abstract] SINTAXIS
> CREATE USER ***\{IF NOT EXISTS\}***
> ***\[user\] \{IDENTIFIED BY '\[password\]'\}***;

El **usuario** está compuesto por el *nombre* y la *máquina* (*dirección __ip__ o `localhost`*) desde la que se puede conectar, para separarlos se usa la *arroba* (`@`), tanto el *nombre* como la *máquina* debe estar entre comillas simples.

> [!abstract] SINTAXIS (user)
> '***\[userName\]***'@'***\[machine\]***'

También es posible crear varios usuarios en una misma sentencia, simplemente hay que cambiar el *puto y coma* (`;`) por una *coma* (`,`) y volver ha hacer una sentencia igua debajo:

```sql
CREATE USER
    'adelio'@'%' IDENTIFIED BY '1234',
    'adelia'@'%' IDENTIFIED BY '5678';
```

La **máquina** desde la que se puede conectar puede ser indicada con una dirección *ip*, `localhost` o `%` para indicar que desde cualquier sitio.

---

Opcional mete se puede establecer unos **roles** a los usuarios de la sentencia, para esto, tras escribir los *nombres* de los **usuarios** se indica la instrucción `DEFULT ROLE` seguido de uno o varios roles separados por comas.

> [!abstract] SINTAXIS
> CREATE USER ***\{IF NOT EXISTS\}***
> ***\[user\] \{IDENTIFIES BY \[password\], ...\}***
> ***\{DEFAULT ROLE \[roleName\], ...\}***;

Opcional mente se puede sustituir los nombre de los roles por `NONE` para indicar ninguno o `ALL` para indicar todos.

---

Al final de la sentencia se puede indicar cuando expira la contraseña, para hacer esto se indica la instrucción `PASSWORD EXPIRE`, este permite indicar tres valores.

- `DEFAULT`: expira según esté especificado en la variable del sistema `default_password_lifetime` (*en número de días*).
- `NEVER`: indica que no expira nunca.
- *N*: número de días en el que expira.

> [!abstract] SINTAXIS
> CREATE USER ***\{IF NOT EXISTS\}***
> ***\[user\] \{IDENTIFIES BY \[password\], ...\}***
> ***\{DEFAULT ROLE \[roleName\], ...\}***
> ***\{PASSWORD EXPIRE \[option\]\}***;

---

Para establecer los **privilegios** (*se trata este tema más a fondo en los próximos apartados*) se usa la instrucción `WITH` seguido del os **privilegios** y sus valores separador por comas.

> [!abstract] SINTAXIS
> CREATE USER ***\{IF NOT EXISTS\}***
> ***\[user\] \{IDENTIFIES BY \[password\], ...\}***
> ***\{DEFAULT ROLE \[roleName\], ...\}***
> ***\{WITH \[values\], ...\}***
> ***\{PASSWORD EXPIRE \[option\]\}***;

### TABLA DE USUARIOS

Los **usuarios** en **MySQL** se guardan dentro de una [base de datos](../../db.md) llamada `mysql`, esta contiene una [tabla](../sql_table.md) llamada `user` con todos los usuarios registrados y sus permisos.

Para poder ver el esquema de la [tabla](../sql_table.md) de **usuarios** tendremos que ejecutar las siguientes instrucciones:

```sql
USE mysql;
DESC user;
```

| Field                    | Type                              | Null | Key | Default               | Extra |
| ------------------------ | --------------------------------- | ---- | --- | --------------------- | ----- |
| Host                     | char(255)                         | NO   | PRI |                       |       |
| User                     | char(32)                          | NO   | PRI |                       |       |
| Select_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Insert_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Update_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Delete_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Create_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Drop_priv                | enum('N','Y')                     | NO   |     | N                     |       |
| Reload_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Shutdown_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Process_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| File_priv                | enum('N','Y')                     | NO   |     | N                     |       |
| Grant_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| References_priv          | enum('N','Y')                     | NO   |     | N                     |       |
| Index_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Show_db_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Super_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tmp_table_priv    | enum('N','Y')                     | NO   |     | N                     |       |
| Lock_tables_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Execute_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_slave_priv          | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_client_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Create_view_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Show_view_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Create_routine_priv      | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_routine_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Create_user_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Event_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Trigger_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tablespace_priv   | enum('N','Y')                     | NO   |     | N                     |       |
| ssl_type                 | enum('','ANY','X509','SPECIFIED') | NO   |     |                       |       |
| ssl_cipher               | blob                              | NO   |     | NULL                  |       |
| x509_issuer              | blob                              | NO   |     | NULL                  |       |
| x509_subject             | blob                              | NO   |     | NULL                  |       |
| max_questions            | int unsigned                      | NO   |     | 0                     |       |
| max_updates              | int unsigned                      | NO   |     | 0                     |       |
| max_connections          | int unsigned                      | NO   |     | 0                     |       |
| max_user_connections     | int unsigned                      | NO   |     | 0                     |       |
| plugin                   | char(64)                          | NO   |     | caching_sha2_password |       |
| authentication_string    | text                              | YES  |     | NULL                  |       |
| password_expired         | enum('N','Y')                     | NO   |     | N                     |       |
| password_last_changed    | timestamp                         | YES  |     | NULL                  |       |
| password_lifetime        | smallint(5) unsigned              | YES  |     | NULL                  |       |
| account_locked           | enum('N','Y')                     | NO   |     | N                     |       |
| Create_role_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Drop_role_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Password_reuse_history   | smallint(5) unsigned              | YES  |     | NULL                  |       |
| Password_reuse_time      | smallint(5) unsigned              | YES  |     | NULL                  |       |
| Password_require_current | enum('N','Y')                     | YES  |     | NULL                  |       |
| User_attributes          | json                              | YES  |     | NULL                  |       |

Las columnas más importantes al principio son las siguientes:

- `Host`: contiene la *ip* de la **máquina** desde la que se puede conectar el usuario.
- `user`: contiene el *nombre* del **usuario**.
- `authentication_string`: contiene la contraseña del **usuario**.

---

Todas las columnas que terminan en `priv` son privilegios a nivel global, estos se indican si los tiene en base al `Y` (*sí lo tiene*) y `N` (*no lo tiene*).

A la hora de [crear el usuario](#CREACIÓN%20DE%20USUARIOS), podemos indicar los **privilegios** con la instrucción `WITH` en este podemos usar los siguientes **privilegios**:

- `max_queries_per_hour`: hace referencia a la columna `max_questions` e indica cuantas instrucciones del [CRUD](mysql_crud.md) puede ejecutar por hora.
- `max_updates_per_hour`: hace referencia a la columna `max_updates` e indica cuantas instrucciones del [CRUD](mysql_crud.md) excepto los `SELECT` puede ejecutar por hora.
- `max_connections_per_hour`: hace referencia a la columna `max_connections` e indica cuantas conexiones puede hacer por hora.
- `max_user_connections`: hace referencia a la columna `max_user_connections` e indica cuantas conexiones con ese mismo usuario puede haber de forma simultánea.

```sql
CREATE USER
    'adelio'@'%' IDENTIFIES BY '1234'
WITH
    max_queries_per_hour 100,
    max_user_connections 10;
```

### MODIFICACIÓN DE USUARIOS

Para modificar un **usuario** se usa la clausula `ALTER USER` en sustitución a `CREATE USER` el resto es idéntico a la [creación de usuarios](#CREACIÓN%20DE%20USUARIOS).

```sql
ALTER USER
    'adelio' IDENTIFIES BY '4321'
WITH
    max_user_connections 15;
```

#### RENOMBRAR USUARIO

Para renombrar un **usuario** se usa la cláusula `RENAME USER`:

> [!abstract] SINTAXIS
> RENAME USER ***\[user\]*** TO ***\[user\]***;

```sql
RENAME USER 'adelio'@'%' TO 'Adelio'@'%';
```

#### MODIFICAR EL ROL POR DEFECTO
