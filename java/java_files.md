---
author: Mindusting
corrected: false
tags:
  - Programming/Java/File
title: Archivos de Java
---

# ARCHIVOS DE JAVA

Los archivos de Java son en esencia archivos de texto, con extensión `.java`, estos tienen una convención a la hora de darles un nombre, este consiste en escribir el nombre con las palabras capitalizadas y sin separación, no pueden tener números no tildes (*únicamente letras*) ahora veremos unos ejemplos:

> [!success] Nombres correctos
> - `MyFirstProgram.java`
> - `User.java`

> [!failure] Nombres incorrectos
> - `Mi primer programa.java`
> - `Usuario2.java`

## CLASE DEL ARCHIVO

Todos los archivos de Java deben tener una [clase](java_class.md) con el mismo nombre que el archivo:

```java
public class MyFirstProgram {

}
```

## MÉTODO MAIN

Esta a su vez, es la única [clase](java_class.md) que puede tener un método `main`:

```java
public class MyFirstProgram {
    public static void main(String[] args) {
    
    }
}
```
