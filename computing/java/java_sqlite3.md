---
author: Mindusting
corrected: true
tags:
  - Programming/Java/SQLite3
title: SQLite3 en Java
---

# SQLITE3 EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Rehacer la documentación para que propague las excepciones.

> [!help]- REFERENCIAS WEB
> - [SQLITE TUTORILA](https://www.sqlitetutorial.net/sqlite-java/)

> [!faq]- FAQ
> - [¿Qué es SQLite3?](../db/sql/sqlite3/sqlite3.md)

## ARCHIVO JAR DE SQLITE3

Para poder trabajar sobre una [base de datos](../db/db.md) de [SQLite3](../db/sql/sqlite3/sqlite3.md) tendremos que incluir en nuestro proyecto el archivo [JAR](java_jar.md) con el código correspondiente, para ello iremos a la página [MVN REPOSITORY](https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc) y descargaremos la versión más reciente del *SQLite JDBC*; en el momento en el que estoy escribiendo esto, la versión más reciente es la [`3.49.1.0`](https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc/3.49.1.0).

Una vez estemos en la página de la versión de *SQLite JDBC* que queramos descargar, podremos ver una tabla centrada en la pantalla, en ella encontraremos una fila con el nombre "*Files*", la columna contigua a esta  contiene contiene tres enlaces, el que nosotros necesitamos es el `jar`, si clicamos sobre el descargaremos el archivo [JAR](java_jar.md) listo para poder importarlo en nuestro proyecto.

## CONEXIÓN

Para crear la conexión tendremos que indicar el **protocolo**, este indica el tipo de [base de datos](../db/db.md) a la que se va a conectar, por lo que es importante poner el correcto, en este caso es `jdbc:sqlite:`, seguido a este se indica la ruta en donde se encuentra el archivo.

```java
// Establecemos el protocolo.
String protocol = "jdbc:sqlite:";
// Establecemos la ruta del archivo.
String path = "main.db";
// Creamos la URL.
String url = protocol + path;
```

## EJEMPLO DE USO

Ahora veremos un ejemplo de una pequeña base de datos con una única tabla de usuarios, esta almacenará un *id* para identificar de forma única a los usuarios, el uso de esta principalmente para la base de datos, también guardaremos el nombre y la edad en forma de número entero (*esto último en realidad no se hace así, es simplemente por propósitos didácticos*).

### ESTRUCTURA DE AL DB

Para este caso la base de datos no tiene un diseño complejo, esto es debido a que no quiero complicar demasiado el ejemplo, pero aplicando la misma lógica que usemos en este caso, se puede aplicar a bases de datos más complejas.

```sql
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INTEGER
);
```

### CLASE USUARIO

La [clase](java_class.md) `Usuario` es simplemente para guardar la información de los usuarios, teniendo sus *propiedades*, *constructores* y *getters*/*setters*.

```java
public class User {

    // Propiedades.
    protected int    age  = 0;
    protected int    id   = 0;
    protected String name = null;

    // Constructores.
    public User() {}

    public User(String name, int age) {
        this.name = name;
        this.age  = age;
    }

    public User(int id, String name, int age) {
        this.id   = id;
        this.name = name;
        this.age  = age;
    }

    // Getters/Setters.
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

### CLASE DE GESTIÓN DE USUARIOS

Aquí podemos ver la [clase](java_class.md) que se va a encargar de hacer de intermediador entre la base de datos y el resto del programa, en este caso se va a encargar de administrar los usuarios, pero en caso de que tuviéramos una base de datos con más tablas lo ideal sería tener un gestor por cada una de ellas, si ese es tu caso, recomiendo tener otra clase a parte en al que se guarde el **protocolo** junto con el nombre de la base de datos y la *URL* así todas las [clases](java_class.md) gestoras podrían acceder a la misma información, evitando así problemas como que podrían estar descoordinadas.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class UserManager {

    // Protocolo.
    protected final String PROTOCOL = "jdbc:sqlite:";

    // Propiedades.
    protected String dbPath = null;
    protected String url    = null;

    // Constructor.
    public UserManager() {}


    // Getters/Setters.
    public void setDbPath(String dbPath) {
        this.dbPath = dbPath;
        this.updateUrl();
    }

    public String getDbPath() {
        return this.dbPath;
    }

    // Métodos.
    public void updateUrl() {
        // Este método actualiza la URL,
        // esta se crea combinando el
        // protocolo y la rula de la DB.
        this.url = this.PROTOCOL + this.dbPath;
    }
}
```

### MÉTODOS DEL GESTOR DE USUARIOS

El gestor debe contener una serie de [métodos](java_method.md) que permitan que el programa se comunique con la base de datos, aquí veremos unos ejemplos, por supuesto dependiendo del uso que le quieras dar tendrás que cambiar algunas cosas par que se ajuste a tus necesidades.

---

Este primer [método](java_method.md) sirve para obtener un [objeto](java_class.md) de tipo `User` de la base de datos referenciando lo por el *id*.

```java
public User selectById(int id) {
    User user = null;

    // Declara las variables necesarias.
    Connection        cx    = null;
    PreparedStatement pstmt = null;
    ResultSet         rs    = null;

    // Establecemos la consulta SQL.
    String sql = "SELECT * FROM users WHERE id=?;";

    try {
        // Creamos la conexión y el patrón.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        // Establece los datos de la consulta.
        pstmt.setInt(1, id);

        // Obtenemos los datos de la consulta.
        rs = pstmt.executeQuery();

        // Usamos IF ya que solo queremos comprobar
        // si hay por lo menos una tupla.
        if (rs.next()) {
            // Si existe algún resultado crea y guarda
            // los datos del usuario en una entidad.
            user = new User (
                rs.getInt("id"),
                rs.getString("name"),
                rs.getInt("age")
            );
        }

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {rs.close();}
        catch (Exception ex) {}

        try {pstmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }

    return user;
}
```
^selectById-example

Este otro [método](java_method.md) devuelve un [`ArrayList`](packages/java/util/java_util_arraylist.md) de todos los usuarios que haya en la base de datos.

```java
public ArrayList<User> selectAll() {
    ArrayList<User> users = null;

    // Declara las variables necesarias.
    Connection cx   = null;
    Statement  stmt = null;
    ResultSet  rs   = null;

    // Establecemos la consulta SQL.
    String sql = "SELECT * FROM users;";

    try {
        // Creamos la conexión, el patrón y ejecutamos.
        cx = DriverManager.getConnection(this.url);
        stmt = cx.createStatement();
        rs = stmt.executeQuery(sql);

        // Usamos WHILE para repetir la creación
        // de entidades mientras haya tuplas
        // disponibles.
        while (rs.next()) {
            if (null == users) {
                users = new ArrayList<>();
            }

            users.add(new User (
                rs.getInt("id"),
                rs.getString("name"),
                rs.getInt("age")
            ));
        }

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {rs.close();}
        catch (Exception ex) {}

        try {stmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }

    return users;
}
```
^selectAll-example

Este [método](java_method.md) inserta un nuevo usuario dentro de la base de datos haciendo uso del `PreparedStatement`.

```java
public void insert(User user) {
    // Declara las variables necesarias.
    Connection         cx    = null;
    PreparedStatement  pstmt = null;

    // Establecemos la consulta SQL.
    String sql = "INSERT INTO users (name, age) VALUES (?, ?);";

    try {
        // Creamos la conexión y el patrón.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        // Establece los datos de la consulta.
        pstmt.setString(1, user.getName());
        pstmt.setInt(2, user.getAge());

        // Obtenemos los datos de la consulta.
        pstmt.executeUpdate();

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {pstmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }
}
```

Con este [método](java_method.md) se puede ver cómo mandar un conjunto de inserciones en una misma tabla de forma eficiente ya que se manda en forma de una única instrucción.

```java
public void insertAll(ArrayList<User> users) {
    // Declara las variables necesarias.
    Connection         cx    = null;
    PreparedStatement  pstmt = null;

    // Establecemos la consulta SQL.
    String sql = "INSERT INTO users (name, age) VALUES ";

    int lastInsert = users.size() - 1;

    for (int i = 0; i < users.size(); i++) {
        if (i == lastInsert) {
            sql += "(?, ?);";
        } else {
            sql += "(?, ?), ";
        }
    }

    try {
        // Creamos la conexión y el patrón.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        for (int i = 0; i < users.size(); i++) {
            int offset = i * 2;
            User user = users.get(i);

            // Establece los datos de la consulta.
            pstmt.setString(offset + 1, user.getName());
            pstmt.setInt(offset + 2, user.getAge());
        }

        // Ejecutamos la actualización de los datos.
        pstmt.executeUpdate();

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {pstmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }
}
```

Este [método](java_method.md) permite actualizar los datos de un usuario que ha exista en la base de datos, es recomendable obtener el [objeto](java_class.md) usuario a través de este mismo gestor con alguno de los métodos anteriores, ya que requiere del *id* interno de la base de datos para identificar al usuario.

```java
public void update(User user) {
    // Declara las variables necesarias.
    Connection         cx    = null;
    PreparedStatement  pstmt = null;

    // Establecemos la consulta SQL.
    String sql = "UPDATE users SET name=?, age=? WHERE id=?;";

    try {
        // Creamos la conexión y el patrón.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        // Establece los datos de la consulta.
        pstmt.setString(1, user.getName());
        pstmt.setInt(2, user.getAge());
        pstmt.setInt(3, user.getId());

        // Ejecutamos la actualización de los datos.
        pstmt.executeUpdate();

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {pstmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }
}
```

Este [método](java_method.md) elimina de la base de datos el usuarios que coincida con el *id* del usuario que le pasemos como argumento.

```java
public void delete(User user) {
    // Declara las variables necesarias.
    Connection         cx    = null;
    PreparedStatement  pstmt = null;

    // Establecemos la consulta SQL.
    String sql = "DELETE FROM users WHERE id=?;";

    try {
        // Creamos la conexión y el patrón.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        // Establece los datos de la consulta.
        pstmt.setInt(1, user.getId());

        // Ejecutamos la actualización de los datos.
        pstmt.executeUpdate();

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {pstmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }
}
```

Este [método](java_method.md) al igual que el anterior elimina de la base de datos el usuario que coincida con el *id*, con la diferencia que este [método](java_method.md) no recibe un usuario sino un *id* en forma de `int`.

```java
public void deleteById(int id) {
    // Declara las variables necesarias.
    Connection         cx    = null;
    PreparedStatement  pstmt = null;

    // Establecemos la consulta SQL.
    String sql = "DELETE FROM users WHERE id=?;";

    try {
        // Creamos la conexión y el patrón.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        // Establece los datos de la consulta.
        pstmt.setInt(1, id);

        // Ejecutamos la actualización de los datos.
        pstmt.executeUpdate();

    } catch (SQLException ex) {
        ex.printStackTrace();
    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        // Cerramos todos los recursos que hayamos usado.
        try {pstmt.close();}
        catch (Exception ex) {}

        try {cx.close();}
        catch (Exception ex) {}
    }
}
```
