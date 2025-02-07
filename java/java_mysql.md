---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Java
---

# MYSQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

%%
Para qué funcione el 

Ejemplo de consulta
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
%%
