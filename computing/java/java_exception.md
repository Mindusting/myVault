---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Excepciones en Java
---

# EXCEPCIONES EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Poner link a la documentación de excepciones.
> > - [ ] Explicar que las excepciones dejan una lista de pasos.
> > - [ ] Documentar el árbol de excepciones.
> > - [ ] Documentar el control de excepciones.
> > - [x] Documentar el finally.
> > - [ ] Documentar la propagación de excepciones.
> > - [ ] Documentar las excepciones personalizadas.
> > - [ ] Documentar el lanzamiento de excepciones.

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Coding with John](https://youtu.be/1XAfapkBQjk)

> [!faq]- FAQ
> - [¿Qué son las excepciones en programación?](../pc/pc_exception.md)

> [!example] EJEMPLO DE EXCEPCIÓN CON ARRAY
> Cuando hacemos una división entre cero Java nos **lanza** una excepción para indicarnos que no puede hacer eso y así nosotros saber que ha habido algún problema.
> 
> ```java
> int[] arr = {3, 2, 5};
> 
> System.out.println(arr[6]);
> ```
> 
> Typo de excepción:
> 
> ```txt
> java.lang.ArrayIndexOutOfBoundsException: Index 6 out of bounds for length 3
> ```

> [!example] EJEMPLO DE EXCEPCIÓN CON DIVISIÓN
> Cuando hacemos una división entre cero Java nos **lanza** una excepción para indicarnos que no puede hacer eso y así nosotros saber que ha habido algún problema.
> 
> ```java
> System.out.println(1 / 0);
> ```
> 
> Typo de excepción:
> 
> ```txt
> java.lang.ArithmeticException: / by zero
> ```

## ARBOL DE EXCEPCIONES

> [!quote] ARBOL DE HERENCIA DE LA CLASE EXCEPCION
> ```txt
> /Object
> └─/Throwable
>   └─/Exception
>     └─ ...
> ```

> [!quote] ARBOL DE EXCEPCIONES
> Como se puede ver todas las excepciones deben heredar de la clase `Exception`, de forma que si la clase `Exception` es la **excepción genérica**.
> 
> ```txt
> /Exception
> └─/RuntimeException
>   ├─ ArithmeticException
>   └─/IndexOutOfBoundsException
>     └─ ArrayIndexOutOfBoundsException
> ```

## CONTROL DE EXCEPCIONES

Para poder controlar excepciones necesitaremos dos palabras clave, teniendo cada una de estas su propio ámbito, estas son `try` y `catch`, dentro del ámbito del `try` pondremos el código que queramos que se controle, mientras que al `catch` le indicaremos bajo qué tipo de excepción se debe ejecutar y en su ámbito indicaremos el código que queremos que se ejecute, este deberá ser un código que resuelva la excepción.

> [!example] EJEMPLO MÁS BÁSICO
> Podemos ver como el código que nos puede dar problemas, siendo en este caso la división, se hace dentro del ámbito del `try`, por lo que en el momento en el que nos da la excepción, esta es atrapada por el `catch` y se indica por consola que no se puede hacer una división entre cero.
> 
> ```java
> try {
>     // Código problemático.
>     System.out.println(1 / 0);
>     //   Tipo y nombre
>     //     v       v
> } catch (Exception ex) {
>     // Qué hacer en caso de excepción.
>     System.out.println("No se puede dividir entre cero.");
> }
> ```
> 
> En este caso no tendría mucho sentido hacer este control de excepciones ya que es tan fácil como cambiar el cero por otro número, pero la idea del esto que nosotros usemos esto con [variables](java_variable.md) que pueden contener número que hemos obtenido del usuario, por lo que no sabremos si nos puede dar una excepción o no, de esta forma si el usuario hiciera algo que podría romper el programa, podemos controlarlo de esta forma.

Como se ve en el anterior ejemplo a los `catch` les precede unos paréntesis, dentro de estos tendremos que poner la clase del tipo de excepción que queremos que controle el `catch` seguido por el nombre en donde se guardará la excepción (*es como el funcionamiento de una [variable](java_variable.md)*), más adelante veremos que usos se le puede dar a esta.

---

Se pueden encadenar múltiples `catch` para poder especificar diferentes tipos de excepciones y así indicar diferentes comportamientos dependiendo de la excepción que se produzca.

> [!example] EJEMPLO BÁSICO
> Un ejemplo didáctico de esto sería el siguiente caso, en el que queremos obtener el inverso de Pitágoras de un vector de tres dimensiones, en este caso tenemos dos excepciones posibles, la división entre cero y acceder a una posición del [array](java_array.md) que no existe, por último, por sea caso, también controlamos cuando ocurra cualquier otra excepción.
> 
> ```java
> public double inversePitagoras(double[] vector) {
>     try {
>         double magnitude = Math.sqrt(
>             (vector[0] * vector[0]) +
>             (vector[1] * vector[1]) +
>             (vector[2] * vector[2])
>         );
>         
>         return 1 / magnitude;
>     } catch (ArithmeticException ex) {
>         System.out.println("La longitud del vector es 0.");
>     } catch (ArrayIndexOutOfBoundsException ex) {
>         System.out.println("El vector no es de tres dimensiones.");
>     } catch (Exception ex) {
>         System.out.println("Ha ocurrido algún problema".);
>     }
>     return 0;
> }
> ```

## EJECUCIÓN FINAL

El `finally` del control de excepciones sirve para introducir un bloque de código que se va a encargar de cerrar todos los recursos que se vayan a crear y utilizar dentro `try`, este bloque siempre se ejecuta, ocurra una excepciones o no.

> [!example] EJEMPLO
> Puedes ver varios ejemplos de uso es en las conexiones a bases de datos, en las que tenemos que crear la conexión (*entre otras cosas*) y luego ocurra lo que ocurra tenemos que cerrarla.
> 
> Un ejemplo de uso de esto mismo lo tienes en la documentación de [SQLite3 para Java](java_sqlite3.md).

---

En las nuevas versiones de Java se puede utilizar el `finally` sin necesidad de un `case`, esto esto es útil cuando queremos poder cerrar/limpiar el código en caso de que ocurra una excepciones pero queremos que se [propague la excepción](#PROPAGACIÓN%20DE%20EXCEPCIONES).

Ahora veremos un ejemplo de esto mismo con el caso del [método](java_method.md) [`selectUserById`](java_sqlite3.md#^selectById-example) de la documentación de [SQLite3 para Java](java_sqlite3.md).

```java
public User selectUserById(int id) throws SQLException, Exception {
    //                                        ^
    // Esta función ahora propaga las excepciones.
    User user = null;

    // Declaración de las variables.
    Connection        cx    = null;
    PreparedStatement pstmt = null;
    ResultSet         rs    = null;

    String sql = "SELECT * FROM users WHERE id=?;";

    try {
        // Se crean los recusos que van a ser usado
        // en el `try` dentro del propio `try`.
        cx = DriverManager.getConnection(this.url);
        pstmt = cx.prepareStatement(sql);

        pstmt.setInt(1, id);

        rs = pstmt.executeQuery();

        if (rs.next()) {
            user = new User (
                rs.getInt("id"),
                rs.getString("name"),
                rs.getInt("age")
            );
        }
        // Se pone un `finally` sin tener ni un catch.
        // v
    } finally {
        // Este `finally` permite que aun cuando
        // ha ocurrido una excepción, antes de
        // propagarse se cierre los recursos que
        // han sido utilizados dentro de este try.
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

## PROPAGACIÓN DE EXCEPCIONES

La propagación de excepciones consiste en indicar que un [método](java_method.md) puede ocasionar una excepción y no la va a controlar, ya que ese será el trabajo del [método](java_method.md) que quiera hacer uso de ella.

```java
public static void main(String[] args) {
    double[] vector = {3};

    try {
        System.out.println(pitagoras(vector));
    } catch (ArrayIndexOutOfBoundsException ex) {
        System.out.println("El vector no tiene dos dimensiones.");
    }
}

public static double pitagoras(double[] vector) throws ArrayIndexOutOfBoundsException {
    return Math.sqrt(
        (vector[0] * vector[0]) +
        (vector[1] * vector[1])
    );
}
```

> [!example] EJEMPLO DE USO
> Si estamos trabajando sobre un entorno gráfico y este debe tener una conexión a una base de datos, podríamos propagas las excepciones que ocurran en la base de datos para tratarlas en el entorno gráfico, haciendo que salga una ventana emergente indicando que ha ocurrido algún problema, de esta forma, con la propagación de excepciones hemos podido comunicar dos [clases](java_class.md) (*la encargada del entorno gráfico y la que se comunica con la base de datos*) para que trabajen en conjunto.

## EXCEPCIONES PERSONALIZADAS

```java
// Herencia de excepción
class Ex extends Exception {
    // Constructor sin argumentos
    public Ex() {}

    // Constructor con mensaje
    public Ex(String errMess) {
        super(errMess);
    }
}
```

## LANZAMIENTO DE EXCEPCIONES

```java
throw new Exception();
```
