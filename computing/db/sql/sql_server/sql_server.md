---
author: Mindusting
corrected: false
tags:
  - DB/SQL
title: SQL-Server
---

<h1 align="center">SQL-Server</h1>

![#logo](../../../../img/db.png)

---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Dividir toda la documentación y pasarla a limpio.

%%
- Las variables con doble arroba son del sistema.
%%

# TODO

>[!todo]- TODO
>- [x] Cambiar los títulos a "Capitalizado".
>    - [x] Cambiar el índice a "Capitalizado".
>- [x] Hacer un apartado explicando como listar las bases de datos (**select \* from sys.databases;**).
>- [x] Hacer un apartado explicando como listar las tablas de datos (**select \* from sys.tables;**).
>- [ ] Como editar una tabla ya creada.
>- [ ] Hacer un apartado explicando como se usa el "**unique index**".
>- [ ] Redactar explicación de las **llave**:
>    - [ ] Redactar explicación de las **llaves primarias**.
>    - [ ] Redactar explicación de las **llaves extranjeras**.
>- [x] Hacer un apartado explicando como hacer un nuevo registro en una tabla.
>- [ ] Hacer un apartado explicando como visualizar datos en pantalla.
>    - [ ] Poner un límite en la búsqueda.
>    - [ ] Visualizar registros unidos.
>- [x] Actualizar un registro.
>- [ ] Hacer un apartado explicando como hacer un rango de valores.
>- [ ] Hacer un apartado explicando como hacer un búsqueda por semejanza.
>- [ ] Hacer un apartado explicando como ordenar los resultados de la búsqueda.
>- [ ] Hacer un apartado explicando como hacer un búsqueda por mínimo y máximo.
>- [x] Hacer un apartado explicando como borrar un registro de una tabla.
>- [x] Hacer un apartado explicando como borrar una tabla.
>- [ ] Hacer un apartado explicando qué es la "**CARDINALIDAD**".

## BUSCAR COMO FUNCIONA

- [ ] count
- [ ] group by

# DOCUMENTACIÓN EXTERNA

- [ATLASSIAN (Documentación en Inglés, tiene muy buena pinta)](https://www.atlassian.com/data/sql)

## VÍDEOS
- [Pildoras informáticas](<https://youtube.com/playlist?list=PLfdtkTXroSltW5yNdKBC1LlhgUpdmPlAa&si=gdLXCu7ATxDQu1Mv>)
- [Lista de reproducción de "Bro Code"](https://youtube.com/playlist?list=PLZPZq0r_RZOMskz6MdsMOgxzheIyjo-BZ&si=rEuSlU1jH1Ko1u7T)
- [Canal de programación Ingenioteca](https://www.youtube.com/@Ingenioteka)

# MYSQL Y SQL SERVER

Existen dos versiones principales de *SQL*, en este documento se va a documentar principalmente *MySQL*, pero en algunas ocasiones podrá dentro de un recuadro el símil para *SQL Server*. 

SQL es un lenguaje que tiene cuatro instrucciones principales llamadas "**CRUD**":

Esta lista está comentada porque ha sido sustituida por la tabla.

- **Create**.
- **Rread**.
- **Update**.
- **Delete**.

| LETRA | PALABRA |
|:-----:|---------|
| **C** | Create  |
| **R** | Read    |
| **U** | Update  |
| **D** | Delete  |

# GLOSARIO

- Base de datos: **DB** (***Data Base***).

# INSTALACIÓN DE MYSQL EN UBUNTU

Instalación de MySQL en Ubuntu:
- sudo apt update
- sudo apt install mysql-server

---

Interactuar con el servicio:
- sudo systemctl status mysql.service
- sudo systemctl start mysql.service

---

MySQL en el terminal:
- sudo mysql

# COMENTARIOS

Los **comentarios** nos permite dejar indicaciones acerca de cómo funciona el código que estamos escribiendo, bien para nosotros mismos ya que en un futuro y se nos podría olvidar cual es la funcionamiento de este o para cuando estemos trabajando en un proyecto con otras personas, y el dejar comentarios puede ayudar a que el resto comprenda que es lo que estamos haciendo.

>[!example] Ej. de comentarios en MySQL:
>```sql
>-- Esto es un comentario de una sola línea.
>
>/*
>Esto es un
>comentario
>de múltiples
>líneas.
>*/
>```

# CREAR UNA DB

Para empezar a almacenar los datos primero debemos crear una base donde se van a almacenar, para ello deberemos hacer uso de la instrucción "*create database*".

> [!abstract] create database ***\[db\_name\]***;

> [!abstract] SINTAXIS
> create database ***\[db\_name\]***;

|              SINTAXIS               |
|:-----------------------------------:|
| create database ***\[db\_name\]***; |

| ID | NOMBRE |
|---:|:-------|
|  0 | admin  |
|  1 | Adelio |
|  2 | Jon    |
|  3 | Alex   |

> [!example] Ej. de como crear una DB en MySQL:
> ```sql
> create database my_database;
> ```

## LISTAR LAS DB CREADAS

Listar las DB nos permite ver que DB tenemos creadas y cuales son sus nombre.

>[!abstract] SINTAXIS
>show databases;

>[!info] Para listar las DB en SQL Server se hace de la siguiente forma:
>```sql
>select * from sys.databases;
>```

## ASIGNAR UNA DB COMO ÁREA DE TRABAJO

Asignar una DB como **área de trabajo** permite que todas las líneas de código  que escribamos a continuación de esta se ejecuten sobre la DB que hayamos indicado.

>[!abstract] SINTAXIS
>use ***\[db\_name\]***;

>[!example] Ej. de establecer una DB como área de trabajo en MySQL:
>```sql
>use "my_database";
>```

## RENOMBRAR UNA DB

Para renombrar una DB es tan simple como usar las **palabras claves** "**rename**", "**database**" y "**to**".

>[!abstract] SINTAXIS
>rename database ***\[db\_name\]*** to ***\[new\_db\_name\]***;

>[!example] Ej. de como renombrar una DB en MySQL:
>```sql
>rename database "my_database" to "u";
>```
>No es recomendable tener nombres tan poco descriptivos, simplemente es un ejemplo para demostrar como se puede hacer.

>[!info] Para renombrar una DB en SQL Server se hace de la siguiente forma:
>>[!abstract] SINTAXIS
>>alter database ***\[db\_name\]*** modify name = ***\[new\_db\_name\]***;
>
>>[!example] Ej. de como renombrar una tabla en MySQL:
>>```sql
>>alter database "my_database" modify name = "my_db";
>>```
>>No es recomendable tener nombres tan poco descriptivos, simplemente es un ejemplo de como se puede hacer.

## BORRAR UNA DB

Para poder borra una DB esta no deber estar establecida como área de trabajo, y deberemos de hacer uso de las **palabras clave** "**drop**" y "**database**".

>[!warning] Cuidado al borra una DB, ya que se perderá todo su contenido, asegura te de que realmente quieres borrar la DB antes de ejecutar la instrucción (Una vez borrado no se podrá recuperar el contenido).

>[!abstract] SINTAXIS
>drop database ***\[db\_name\]***;

>[!example] Ej. de como eliminar una DB en SQL:
```sql
drop database "my_database";
```

# CREAR UNA TABLA

Una tabla nos permite almacenar información de forma ordenada dentro de nuestra DB, una DB puede albergar múltiples tablas, las cuales pueden estar relacionadas entre sí.

>[!abstract] SINTAXIS
>create table ***\[table\_name\]*** (***\[field\_name\]***);

>[!example] Ej. de como crear una tabla en MySQL:
```sql
-- Indicamos que la DB en la que queremos trabajar es "my_database".
use my_database;

-- Indicamos la creación de la DB.
create table "users" (
    -- La DB tendrá un solo campo, siendo este "id".
    "id" int
);
```

Una tabla requiere de al menos un campo en el que se pueda guardar información, el campo indicado en este ejemplo es "*id*", este almacenará un valor entero y se usará para identificar cada [registro](#^Crear-registros)[^registro] (*Por así decirlo, es una matrícula para cada [registro](#^Crear-registros)*), dando le un valor distinto a cada uno, pero tal y como está ahora, diferentes [registro](#^Crear-registros) pueden tener el mismo valor en este capo, para evitar esto hay que [modificarlo](#^Modificar-una-tabla) para convertirlo en un valor *key*.

[^registro]: Un registro es un objeto donde se guardan los datos de por ejemplo un cliente, si creamos una tabla llamada "*clientes*", dentro de estas se guardarán los *registros* "*cliente*", a su vez, cada uno de estos almacenará el \[nombre, apellidos, DNI, email, ...\] del cliente por cada registro (*Objeto "cliente"*).

## LISTAR LAS TABLAS CREADAS

Listar las tablas nos permite ver que tablas tenemos en la DB que tenemos como área de trabajo.

>[!abstract] SINTAXIS
>show full tables from ***\[db_name\]***;

>[!info] Para listar las tablas en SQL Server se hace de la siguiente forma:
>```sql
>select * from sys.tables;
>```

## RENOMBRAR UNA TABLA

Renombrar una tabla nos permite corregir un erro que hayamos cometido a la hora de crear la tabla.

>[!abstract] SINTAXIS
>rename table ***\[table\_name\]*** to ***\[new\_table\_name\]***;

>[!example] Ej. de como renombrar una tabla en MySQL:
>```sql
>rename table "users" to "u";
>```
>No es recomendable tener nombres tan poco descriptivos, simplemente es un ejemplo de como se puede hacer.

>[!info] Para renombrar una tabla en SQL Server se hace de la siguiente forma:
>>[!abstract] SINTAXIS
>>exec sp\_rename ***\[table\_name\]***, ***\[new\_table\_name\]***;
>
>>[!example] Ej. de como renombrar una tabla en MySQL:
>>```sql
>>exec sp_rename "users", "u";
>>```
>>No es recomendable tener nombres tan poco descriptivos, simplemente es un ejemplo de como se puede hacer.

## MODIFICAR UNA TABLA

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

Modificar un capo de una tabla nos puede servir para cambiar las propiedades de estos en sado de que nos hayamos equivocado o queramos darle otro uso.

[^1]: Nota al pie.

>[!abstract] SINTAXIS
>alter table ***\[table\_name\]*** modify column ***\[field\_name\] \[type\] \[propeties\]***;

>[!fail] Esta SINTAXIS no funciona en SQL Server.

>[!info] Para modificar una tabla en SQL Server se hace de la siguiente forma:
># AGREGAR UN CAMPO
>>[!abstract] SINTAXIS
>>alter table ***\[table\_name\]*** add ***\[field\_name\] \[type\] \[propeties\]***; 
># MODIFICAR UN CAMPO
>>[!abstract] SINTAXIS
>>alter table ***\[table\_name\]*** alter column ***\[field\_name\] \[type\] \[propeties\]***;
># BORRAR UN CAMPO
>>[!abstract] SINTAXIS
>>alter table ***\[table\_name\]*** drop column ***\[field\_name\]***;

## TIPOS DE DATOS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO
>- [ ] Desarrollar el apartado "int".
>- [ ] Desarrollar el apartado "float".
>- [ ] Desarrollar el apartado "varchar".

1. int:
    - Número entero.

1. float:
    - Número decimal.

1. varchar:
    - varchar(***\[num_max_char\]***)

## CAMPOS OBLIGATORIO

Tener un capo obligatorio implica que a la hora de crear un nuevo [registro](#^Crear-registros) este no puede quedar vacío,  esto nos puede servir por ejemplo si queremos que para crear un usuario este debe tener un correo electrónico asociado de forma obligatoria.

>[!abstract] SINTAXIS
>***\[field\] \[type\]*** not null

>[!example] Ej. de como crear una tabla en MySQL:
>```sql
>-- Indicamos que la DB en la que queremos trabajar es "my_database".
>use my_database;
>
>-- Indicamos la creación de la DB.
>create table "users" (
>    -- La DB tendrá un solo campo, sinedo este "id".
>    "id" int not null
>    -- Este campo no puede ser igual a null.
>);
>```

## DATOS AUTO INCREMENTALES

Tener un capo **auto incremental** en una tabla permite tener un campo que no se va a repetir, esto se suele usar para asignar *ids*, un ejemplo de esto puede ser que creemos dos registro de dos usuarios distintos y estos dos tengan el mismo nombre, sino tivieramos un *id* exclusivo para cada usuario internamente no podríamos diferenciar a los dos usuarios.

>[!abstract] SINTAXIS
>***\[field\] \[type\] \[not_null\]*** auto_increment

>[!example] Ej. de como crear una tabla en MySQL:
>```sql
>-- Indicamos que la DB en la que queremos trabajar es "my_database".
>use my_database;
>
>-- Indicamos la creación de la DB.
>create table "users" (
>    -- La DB tendrá un solo campo, sinedo este "id".
>    "id" int not null auto_increment
>    -- Este campo no puede ser igual a null y se auto incrementa.
>);
>```

>[!info] Para hacer un campo auto incremental e SQL Server se hace de la siguiente forma:
>>[!abstract] SINTAXIS
>>***\[field\] \[type\] \[not_null\]*** identity(***\[start_num\]***, ***\[num_increase\]***)
>
>>[!example] Ej. de como crear una tabla en MySQL:
>>```sql
>>-- Indicamos que la DB en la que queremos trabajar es "my_database".
>>use my_database;
>>
>>-- Indicamos la creación de la DB.
>>create table "users" (
>>    -- La DB tendrá un solo campo, sinedo este "id".
>>    "id" int not null identity(1, 1)
>>    -- Este campo no puede ser igual a null y se auto incrementa.
>>);
>>```

## LLAVES

En las tablas de *SQL* existen lo que se conoce como **llaves**, estos son campos campos que lo que tienen de especial es que no se pueden repetir, ya que por lo general son **auto incrementales**, existen dos tipos de **llaves**, las **primarias** y las **extranjeras**.

### PRIMARIAS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

Para indicar que un **atributo** del registro tiene que ser una **llave primaria** se usa la **palabra clave** "**primary**" seguido de la **palabra clave** "**key**" y unos paréntesis, dentro de estos deberemos escribir el nombre de **atributo** que queramos que sea la **llave primaria** de nuestra tabla.

>[!example] Ej. de creación de una tabla con llave primaria en MySQL:
>```sql
>create table users (
>    id int not null auto_increment,
>    name varchar(50) not null,
>    edad int not null,
>    email varchar(100) not null,
>    primary key(id);
>);
>```
>En este ejemplo se puede ver como al final de la creación de la tabla, se indica que el atributo "*id*" el cual es de tipo "*auto_increment*" será la llave primaria de esta tabla.

### EXTRANJERAS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

Una llave de tipo "**foreign**" (**Del Inglés "Extranjero"**) es un atributo donde se va a guardar la llave primaria de otra tabla, pudiendo enlazar de esta forma los contenidos de las tablas.

>[!example] Ej. de creación de una tabla con llave extranjera:
>```sql
>create table products (
>    id int not null auto_increment,
>    name varchar(50) not null,
>    created_by int not null,
>    marca varchar(50) not null,
>    primary key(id);
>    foreign key(created_by) references users(id)
>);
>```
>En este ejemplo se puede ver como en al final de la creación de esta de esta tabla se  indica que el atributo "*created_by*" contendrá una **llave extranjera**, seguido de la **palabra clave** "**reference**" (**Del Inglés "Referencia"**) seguido por el nombre de la tabla a la cual queramos que esté vinculada junto con unos paréntesis, indicando entre estos el atributo que se va a usar como **llave extranjera**.

## BORRAR TABLAS

>[!warning] Cuidado al borra una tabla, ya que se perderá todo su contenido, asegura te de que realmente quieres borrar la tabla antes de ejecutar la instrucción (Una vez borrado no se podrá recuperar el contenido).

Para borrar una tabla se usa la instrucción "**drop table**" seguida del nombre de la tabla que se quiera borrar, si se quiere borrar varias tables, estas pueden ser borradas con una sola instrucción separando los nombres con *comas*.

>[!abstract] SINTAXIS
>drop table "***\[table_name\]***", "***\[table_name\]***" ...;

>[!example] Ej. de como borrar tablas en MySQL:
>```sql
>-- Se borra una sola tabla.
>drop table "users";
>
>-- Se borran múltiples tablas.
>drop table "productos", "pedidos";
>```

# CREAR REGISTROS

Un registro no es más que un objeto en nuestra colección de objetos, siendo este último nuestra tabla, esto lo que quiere decir es que nuestra tabla está formada por columnas, en cada una de estas se almacena un valor distinto, bueno, pues los registros son las filas, por cada nuevo registro que se haga se añadirá una fila más a la tabla, almacenando los valores que le exija cada columna.

>[!abstract] SINTAXIS
>insert into ***\[table\_name\]*** (***\[field_name_1\]***, ***\[field_name_2\]*** ...)
>values
>    (***\[value_1\]***, ***\[value_2\]*** ...),
>    (***\[value_1\]***, ***\[value_2\]*** ...),
>    ... ;

>[!example] Ej. de crear un nuevo registro en MySQL:
>```sql
>-- Se crea un nuevo registro.
>insert into users ("name", "email")
>values ("Mindusting", "mindusting@gmail.com");
>
>-- Se crean múltiples registros.
>insert into animales (tipo, estado)
>values
>    ("Adelio", "adelio@mindmail.com"),
>    ("Pepe", "pepe@mindmail.com");
>```

>[!warning]
>En SQL Server se usan comillas simples, no dobles.

## CONSULTAR REGISTROS

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR
>- [ ] Añadir explicación.
>- [ ] Explicar como funciona el "where".

>[!abstract] SINTAXIS
>select ***\[consult_data\]*** from ***\[table_name\]*** where ***\[conditional\]***;

>[!example] Ej. de consulta de registros en MySQL:
>```sql
>select * from users;
>```

### LÍMITE DE CONSULTAS

>[!fail] ESTE APRTADO ESTÁ SIN TERMINAR

>[!abstract] SINTAXIS
>select ***\[consult_data\]*** from ***\[table_name\]*** limit ***\[num_limit\]***;

>[!example] Ej. de establecer límite de consulta en MySQL:
>```sql
>select * from animales limit 2;
>```

### ORDEN EN LA BUSQUEDA

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Si quisiéramos ordenar los resultados de la búsqueda, tendremos que usar la **palabra clave** "**order**", seguida de la **palabra clave** "**by**", seguido del atributo que se va a usar para ordenar y finalmente indicamos si queremos que el orden sea **ascendente** (**asc**) o **descendente** (**desc**).

### BUSQUEDA POR MÁXIMO Y MÍNIMO

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Si quisiéramos buscar entre los registros el **máximo** o el **mínimo** un valor numérico podemos hacerlo con los métodos "**max**" y "**min**".

>[!example] Ej del uso de las funciones "max" y "min": 
>```sql
>select max(edad) as mayor from users;
>select min(edad) as menor from users;
>```

### BUSQUEDA POR SEMEJANZA

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Si queremos buscar un registro y no sabemos algún dato en concreto podemos buscar por una parte de él, para el deberemos usar la **palabra clave** "**like**", seguida por una cadena de caracteres, pudiendo usar el carácter **porcentaje** (**%**)  como indicativo de que puede haber cualquier cadena de caracteres en ese sitio o el **barra baja** (**\_**) para indicar que ahí puede haber un caracter.

>[!example] Ej. de búsqueda por semejanza:
>```sql
>select * from users where email like 'mindusting%.com';
>```
>En este caso se va a mostrar todos los registros cuyo *email* empiece por "**mindusting**" y terminen por "**.com**", por lo que los siguientes valores son válidos:
>- mindusting@gmail.com
>- mindusting@mindmail.com
>- mindustingHolaMundo.com

### RANGO DE VALORES

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Para indicar un trabajo de valores se puede usar la **palabra clave** "**between**" seguido de dos valores separados por el**profesor** "**and**".

>[!abstract] SINTAXIS
>between ***\[value_1\]*** and ***\[value_2\]***;

### CONSULTAR REGISTROS UNIDOS

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Para poder visualizar los registro unido se puede hacer uso de la **palabra clave** "**join**" (**Del Inglés "Juntar"**), esta **palabra clase** se debe usar en conjunto con otras para definir su comportamiento, primero veremos como usarlo con la **palabra clave** "**left**" (**Del Inglés "Izquierda"**).

>[!example] Ej:
>```sql
>select u.id, u.email, p.name from users u left join products p on u.id = p.created_by;
>```
>Como se puede ver en el ejemplo, lo primero es hacer un "*select*" indicando que lo que queremos que se muestres, de la **tabla** "*users*" el "*id*" y el "*email*", seguido de el "*name*" de la **tabla** "*products*", luego indicamos con el "*from*" cual es la **tabla principal** (*users*) y le asignamos un **alias** siendo este "*u*" (Esto permite que la línea sea más corta, ya que de esta forma podemos sustituir la palabra "*users*" por una "*u*"), seguido de la **palabra clave** "**left**" (**Del Inglés "Izquierda"**) y la **palabra clave** "**join**" (**Del Inglés "Juntar"**), luego el nombre de la **segunda tabla** junto con su **alias**, seguido de la **palabra clave** "**on**" (**Del Inglés "en"**) y los dos atributos a compara, en este caso el "**id**" del usuario y el "**created_by**" del producto.

#### LEFT

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Esta **palabra clave** es la usada en el ejemplo anterior, esta, lo que indica es que se debe imprimir todos los registros de la tabla de la izquierda (**En este caso "users"**) seguido de todos los registros de la tabla de la derecha (**En este caso "products"**), estando estos últimos ordenados respecto a los de la tabla de la izquierda, de forma que los productos que no estén asociados a ningún usuario no se mostrarán.

#### RIGHT

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Esta **palabra clave** se puede usar como sustituto de la **palabra clave** "**left**" en el ejemplo anterior, en este caso el funcionamiento de la orden cambiaría, de forma que se mostrarían todos los registros de la tabla de la derecha y los usuarios a los que están relacionados de la tabla de la izquierda, de forma que si algún usuario no está asociado con ningún producto este no se mostrará en la impresión.

#### INNER

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

Esta **palabra clave** se puede usar como sustituto de la **palabra clave** "**left**" en el ejemplo anterior, en este caso el funcionamiento de la ordena cambiaría, de forma que se mostrarían todos los registros que estén vinculados entre las dos tablas quedando fuera los que no estén relacionados.

#### CROS

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

>[!example] Ej:
>```sql
>select u.id, u.name, p.id, p.name from users u cross join products p;
>```
>Esta **palabra clave** funciona de forma que se mostrarían todos los registros de una tabla relacionados con los de la segunda

## ACTUALIZAR REGISTROS

Actualizar registros permite cambiar la información que lo conforma una vez ya creados, para ello se usa la **palabra clave** "**update**" (**Del inglés "actualizar"**) y "**set**" (**Del inglés "poner"**).

>[!abstract] SINTAXIS
>update ***\[table_mane\]*** set ***\[data_update\]*** where ***\[data_discrimination\]***;

>[!example] Ej:
>```sql
>update "users" set name = 'mindusting' where id = 1;
>```

## BORRAR REGISTROS

>[!fail] ESTE APARTADO ESTÁ SIN TERMINAR

>[!warning] Cuidado al borra un registro, ya que se perderá toda su información, asegura te de que realmente quieres borrar la tabla antes de ejecutar la instrucción (Una vez borrado no se podrá recuperar el contenido).

Hay que tener una cosa en cuenta y es que si no ponemos el "***where***" en el "***delete from***" **borrará todos los registro de la tabla**, por lo que se debe tener mucho cuidado cuando se manejan estas sentencias.

> [!abstract] SINTAXIS
>delete from ***\[table_name\]*** where ***\[el qué\]***

>[!example] Ej. de borrar registro:
>
>>[!danger] Borrar todos los registro de la tabla:
>>```sql
>>delete from animales;
>>```
>
>>[!warning] Borrar un registro de una tabla:
>>```sql
>>delete from animales where estado = 'triste';
>>```

>[!info] Múltiples datos a tener en cuanta:
>Si quisiéramos indicar varios valores a tener en cuenta a la hora de discriminar que valores se van a borrar o no se pueden poner separando estos con los operadores "***and***" u "***or***".
>>[!example] Ej. de borrado de registro con varios valores a tener en cuenta:
>>```sql
>>delete from animales where tipo = 'felipe' and estado = "feliz";
