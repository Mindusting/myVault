---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Clases Wapper en Java
---

<h1 align="center">CLASES WRAPPER EN JAVA</h1>

---

# CLASES WRAPPER

## BOOLEAN

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## BYTE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## SHORT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## INTEGER

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## LONG

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## FLOAT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## DOUBLE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## STRING

La clase `String` permite manejar texto de forma sencilla, otorgando diferentes métodos para poder manipular el contenido, este equivale a un [array](java_array.md) de tipo [char](<java_variable.md#CHAR>), ahora veremos como guardaríamos un mensaje con un [array](java_array.md):

```java
public class StringExercise {
    public static void main(String[] args) {
        char[] string = {
            'H', 'o', 'l', 'a', ' ',
            'm', 'u', 'n', 'd', 'o', '!'
        };
        System.out.println(string);
        // SALIDA:
        // Hola mundo!
    }
}
```

Si queremos hacer esto mismo con una [variable](java_variable.md) de tipo `String` lo haríamos de la siguiente forma:

```java
public class StringExercise {
    public static void main(String[] args) {
        String string = "Hola mundo!";

        System.out.println(string);
        // SALIDA:
        // Hola mundo!
    }
}
```

En este segundo caso al usar un objeto de tipo `String`, este tiene métodos para manipular el contenido:

```java
public class StringExercise {
    public static void main(String[] args) {
        String string = "Hola mundo!";

        // Transformamos el texto a todo mayúsculas.
        string = string.toUperCase();

        System.out.println(string);
        // SALIDA:
        // HOLA MUNDO!
    }
}
```
