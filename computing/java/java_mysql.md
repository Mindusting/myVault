---
author: Mindusting
corrected: false
tags:
  - Programming/Java/MySQL
title: MySQL en Java
---

# MYSQL EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## ARCHIVO JAR DE MYSQL

Para poder trabajar sobre una [base de datos](../db/db.md) de [MySQL](../db/sql/mysql/mysql.md) tendremos que incluir en nuestro proyecto el archivo [JAR](java_jar.md) con el código correspondiente, para ello iremos a la página de [MySQL](https://www.mysql.com/products/connector/) y descargaremos la versión de **Java** (*JDBC Driver for MySQL (Connector/J)*).

## CONEXIÓN

```java
String protocol = "jdbc:mysql:";
String hostname = "localhost";
String port     = "3306";
String database = "main";
String url      =  protocol+"//"+hostname+":"+port+"/"+database;
String username = "admin";
String passwrod = "1234";
```

---
---
---
---
---

driver: `com.mysql.jdbc.Driver`.
database: Nombre de la base de datos.
hostname: Dirección IP de la máquina en la que se encuentra la base de datos (*puede ser `localhost`*).
port: El puerto de conexión.
protocol: `jdbc:mysql:`.
url: `protocol//hostname:port/database`
username: Nombre del usuario con el que nos conectamos.
password: Contraseña del usuario.

```java
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.DriverManager;
import java.util.ArrayList;

public class MyDB {
    public static void main(String[] args) {
        String sql = "SELECT * FROM users;";

        String URL = "jdbc:mysql://localhost:3306/test";
        String USER = "root";
        String PASSWORD = "";

        Connection conn = null;
        Statement statement = null;
        ResultSet resultset = null;

        ArrayList<User> users = new ArrayList<User>();

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriveManager.getConnection(
                URL,
                USER,
                PASSWORD
            );
            statement = conn.createStatement();
            resultSet = statement.executeQuery(sql);

            while (resltSet.next()) {
                User user = new User();
                user.setId(resultSet("id"));
                user.setName(resultSet("name"));

                users.add(user);
            }
        } catch (SQLException sqle) {
            System.out.println(sqle.getMessage());
        } catch (Exception e) {
            System.out.println(sqle.getMessage());
        } final {
            // Siempre cerrarlo todo al final.
            try {
                if (resultSet != null)
                    resultSet.close();
            } catch (Exception e) {}
            try {
                if (statement != null)
                    statement.close();
            } catch (Exception e) {}
            try {
                if (conn != null)
                    conn.close();
            } catch (Exception e) {}
        }
    }
}
```
