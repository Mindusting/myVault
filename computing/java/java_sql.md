---
author: Mindusting
corrected: true
tags:
  - Programming/Java
  - DB/SQL
title: SQL en Java
---

# SQL EN JAVA

Para poder conectarnos a una [base de datos](../db/db.md) con [SQL](../db/sql/sql.md) en **Java** se usa una **librería** estándar, con ella podremos conectarnos a diferentes tipos de [base de datos](../db/db.md) como las siguientes:

- [SQLite3](java_sqlite3.md)
- [MySQL](java_mysql.md)

> [!important] IMPORTANTE
> Para poder trabajar sobre [bases de datos](../db/db.md) en **Java** se usa el paquete `java.sql`, este contiene todas las [clases](java_class.md) necesarias para desempeñar esta tarea.

## CONEXIÓN

Dependiendo del tipo de [base de datos](../db/db.md) a la que queramos conectarnos el proceso de creación de la conexión cambia un poco, podrás verlo más en detalle en su documentación correspondiente.

Para poder realizar una conexión hace falta importar las siguientes [clases](java_class.md):

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
```

Usaremos la [clase](java_class.md) `Connection` para guardar la conexión, `DriverManager` para realizar la conexión y `SQLException` para poder controlarla, ya que si el proceso de creación de la conexión falla, se lanzará una [excepción](java_exception.md) de este tipo.

```java
// Creación de la variable que contendrá
// la conexión antes de empezar.
Connection cx = null;

try {
    // Ejemplo de conexión a DB de SQLite3
    cx = DriverManager.getConnection(
        "jdbc:sqlite:main.db"
    );
} catch (SQLException ex) {
    System.out.println("Falló la conexión.");
} catch (Exception ex) {
    System.out.println("Fallo general.");
} finally {
    // Cierre de la conexión pase lo que pase
    // al final del proceso.
    try {cx.close();}
    catch (Exception ex) {}
}
```

Dependiendo del tipo de [base de datos](../db/db.md) a la que nos vayamos a conectar tendremos que seguir las siguientes sintaxis a la hora de hacer la conexión:

> [!abstract] SINTAXIS
> getConnection(***\[url\]***)

> [!abstract] SINTAXIS
> getConnection(***\[url\]***, ***\[userName\]***, ***\[password\]***)

Los tres argumentos son de tipo [`String`](data_types/java_string.md) y en la *url* se indica a qué [base de datos](../db/db.md) se debe realizar la conexión, el comó se estructura la *url* se explica en más detalle en cada una de las documentaciones respectivas para cada tipo de [base de datos](../db/db.md).

## DECLARACIONES

Tenemos dos formas de ejecutar sentencias de [SQL](../db/sql/sql.md), estas son a través de las [clases](java_class.md) [`Statement`](#DECLARACIÓN%20SIMPLE) y [`PreparedStatement`](#DECLARACIÓN%20COMPLEJA), cada una de estas se verá más en detalle en sus propios apartados.

### DECLARACIÓN SIMPLE

Para hacer una declaración simple se usa la [clase](java_class.md) `Statement`, para obtener un [objeto](java_class.md) de esta, tendremos que hacerlo mediante la [conexión](#CONEXIÓN) a la [base de datos](../db/db.md), ya que esta contiene el [método](java_method.md) `createStatement`, este no recibe ningún argumento.

```java
// Creación de la variable que contendrá
// la conexión antes de empezar.
Connection cx   = null;
Statement  stmt = null;

try {
    // Ejemplo de conexión a DB de SQLite3
    cx = DriverManager.getConnection(
        "jdbc:sqlite:main.db"
    );
    stmt = cx.createStatement();
} catch (SQLException ex) {
    System.out.println("Falló la conexión.");
} catch (Exception ex) {
    System.out.println("Fallo general.");
} finally {
    // Cierre de la sentencia.
    try {stmt.close();}
    catch (Exception ex) {}
    
    // Cierre de la conexión pase lo que pase
    // al final del proceso.
    try {cx.close();}
    catch (Exception ex) {}
}
```

> [!important] IMPORTANTE
> Es importante cerrar los recursos en el `finally` en el orden inverso al que se han creado para evitar problemas.

El [objeto](java_class.md) `Statement` contiene dos [métodos](java_method.md) (*en realidad tiene más, pero estos son los más usados*) `executeQuery` y `executeUpdate`, dependiendo del tipo del tipo de sentencia que queramos ejecutar tendremos que usar uno u otro, en cualquiera de los dos casos reciben un [`String`](data_types/java_string.md) como argumento y pueden lanzar dos tipos de [excepciones](java_exception.md), `SQLException` y `SQLTimeoutException`, indicando con la primera que la sentencia no se ha podido ejecutar debido a por ejemplo un fallo en la sintaxis y la segunda indicado que ha pasado demasiado tiempo para ejecutar la sentencia, esto último puede ocurrir cuando se pierde la conexión con la [base de datos](../db/db.md).

Si queremos ejecutar una **consulta** tendremos que usar el [método](java_method.md) `executeQuery`, este nos devolverá un [objeto](java_class.md) de tipo [`ResultSet`](#RESULTADO) pudiendo así con el leer el resultado de la **consulta**.

Si queremos ejecutar una **inserción**, **actualización** o **borrado** de datos, tendremos que usar el [método](java_method.md) `executeUpdate`, este nos devolverá un [`int`](data_types/java_integer.md#INT) indicando el número de tuplas afectadas.

### DECLARACIÓN COMPLEJA

> [!important] IMPORTANTE
> Este apartado explica cómo insertar datos de forma dinámica a la sentencia de [SQL](../db/sql/sql.md), no es recomendable usar el [f-string](java_format_string.md) como sustituto a este apartado, ya que si sigues esta documentación estarás evitando la [inyección de SQL](../db/sql/sql_injection.md).

Para hacer una declaración simple se usa la [clase](java_class.md) `PreparedStatement`, para obtener un [objeto](java_class.md) de esta, tendremos que hacerlo mediante la [conexión](#CONEXIÓN) a la [base de datos](../db/db.md), ya que esta contiene el [método](java_method.md) `prepareStatement`, este recibe un argumento de tipo [`String`](data_types/java_string.md) con la sentencia [SQL](../db/sql/sql.md) que queramos ejecutar.

La sentencia [SQL](../db/sql/sql.md) puede tener *interrogantes* (`?`), estos indican donde pondremos los datos que queremos insertar en la sentencia.

Para insertar datos en donde van los interrogantes tendremos que usar una serie de [métodos](java_method.md) cuyos nombres empiezan por `set` seguido del nombre del tipo de dato:

- `setBoolean`
- `setInt`
- `setDouble`
- `setString`
- `setDate`

Todos estos tienen un argumento en común y es el primero, siendo este un número de tipo [`int`](data_types/java_integer.md#INT), con este se indica sobre qué interrogante se quiere poner la información, este número comienza por el 1, esto quiere decir que si queremos introducir el dato en el segundo interrogante, tendremos que poner un 2 y no un 1 como si estuviéramos trabajando con un [array](java_array.md).

El segundo argumento dependerá del [método](java_method.md) que estemos llamando, introduciendo así el dato que queramos insertar.

Un ejemplo de esto lo puedes ver en la [selección de un usuario por `id`](java_sqlite3.md#^selectById-example) en la documentación de [SQLite para Java](java_sqlite3.md).

---

Una vez hemos terminado de insertar los datos que queremos dentro de la sentencia [SQL](../db/sql/sql.md) podremos ejecutarla mediante los [métodos](java_method.md) `executeQuery` y `executeUpdate` sobre el [objeto](java_class.md) `PreparedStatement`, los cuales funcionan igual que como se ha explicado en el apartado de [declaración simple](#DECLARACIÓN%20SIMPLE) son la deferencia que estos al ya haber indicado la sentencia [SQL](../db/sql/sql.md) con anterioridad, no requieren de un argumento de tipo [`String`](data_types/java_string.md).

## RESULTADO

Para obtener el resultado de una [consulta](#DECLARACIONES) está usaremos la [clase](java_class.md) `ResultSet`, este contiene el [método](java_method.md) `next`, este no recibe argumentos y cada vez que lo ejecutamos indicamos que queremos trabajar sobre la siguiente tupla del resultado, empezando por la 0 por lo que de primeras no tendremos acceso a ninguna de ellas, al mismo tiempo este [método](java_method.md) devuelve un valor [`boolean`](data_types/java_boolean.md) indicando si existe una siguiente tupla.

> [!example] EJEMPLO
> Si hacemos una consulta en la que obtenemos dos tuplas de la información de los usuarios, de primeras no podremos acceder a ninguna de ellas, si ejecutamos una vez el [método](java_method.md) `next` este nos devolverá el valor `true`, indicándonos que existe una próxima tupla (*en este caso la primera*), en este punto podremos acceder a la información de ésta como veremos en el [siguiente apartado](#LEER%20TUPLA).
> 
> *Resultado completo:*
> 
> |  id | name   | age |
> | ---:|:------ | ---:|
> |   1 | Adelio |  20 |
> |   2 | Adelia |  22 |
> 
> *Primera tupla a la que se accede con el `next`:*
> 
> |  id | name   | age |
> | ---:|:------ | ---:|
> |   1 | Adelio |  20 |
> 
> Si volvemos a ejecutar el mismo [método](java_method.md) `next` (*como por ejemplo un [bucle `while`](java_loop.md#WHILE)*) nos devolverá el valor `true` indicándonos que hay otra tupla.
> 
> *Segunda tupla a la que se accede con el `next`:*
> 
> |  id | name   | age |
> | ---:|:------ | ---:|
> |   2 | Adelia |  22 |
> 
> Si volvemos a ejecutar el [método](java_method.md) `next` este nos devolverá el valor `false` indicándonos que ya no hay más tupla en el resultado de la consulta.

Debido a que el [método](java_method.md) `next` devuelve un valor [`boolean`](data_types/java_boolean.md), este tiene una muy buena sinergia con la [sentencia `if`](java_control_flow.md#SENTENCIA%20IF) y el [bucle `while`](java_loop.md#WHILE), si queremos hacer una consulta que simplemente devuelva una [entidad](java_entity.md) o varias.

Si quieres ver ejemplos tanto de [un registro](java_sqlite3.md#^selectById-example) como de [varios](java_sqlite3.md#^selectAll-example) los tienes en la documentación de [SQLite3 para Java](java_sqlite3.md)

### LEER TUPLA

Cuando el [método](java_method.md) `next` nos devuelve el valor `true` quiere decir que tenemos acceso a la siguiente tupla (*ya que existe*), para poder leer los datos de esta se usa una serie de [métodos](java_method.md) que empiezan por `get` y el tipo de dato capitalizado.

- `getInt`
- `getDouble`
- `getString`
- `getDate`

Todos estos comparten una misma regla y es que reciben un argumento que puede ser de tipo [`int`](data_types/java_integer.md#INT) o [`String`](data_types/java_string.md) bien indicando el *número* de la columna o el *nombre* de esta, este nos devolverá el tipo de dato que indiquemos de la columna que indiquemos.

> [!important] IMPORTANTE
> Ten en cuenta que cuando usas el [método](java_method.md) `getDate` devuelve un [objeto](java_class.md) de tipo `java.sql.Date` y no de `java.util.Date`, si quieres ver como hacer la conversión puedes ir al apartado de [conversión de datos](#CONVERSIÓN%20DE%20FECHAS)

## CONVERSIÓN DE DATOS

Cuando trabajamos sobre una [base de datos](../db/db.md) en **Java** a veces tenemos que hacer conversiones entre datos, esto es debido a que las librerías tienen sus propios tipos de datos ya que se amoldan a sus necesidades, es por esto que tendremos que hacer las conversiones, para que cuando queramos trabajar de forma normal sobre la información usaremos las [clases](java_class.md) originales de **Java** y cuando interactuamos con la [base de datos](../db/db.md) los convertiremos a las [clases](java_class.md) que necesite.

### CONVERSIÓN DE FECHAS

Para convertir el tipo de dato `java.util.Date` a `java.sql.Date` o viceversa se hace mediante el uso del [método](java_method.md) `getTime` que poseen los dos, este no recibe ningún argumento y devuelve un [`long`](data_types/java_integer.md#LONG), este se puede usar para pasárselo como argumento al constructor de cualquiera de las dos [clases](java_class.md) `Date`, pudiendo hacer así la conversión.

```java
java.util.Date utilDate = null;
java.sql.Date  sqlDate  = null;

utilDate = new java.util.Date();

// Aquí se combierte de java.util.Date a java.sql.Date
sqlDate  = new java.sql.Date(utilDate.getTime());
// Aquí se combierte de java.sql.Date a java.util.Date
utilDate = new java.util.Date(sqlDate.getTime());
```
