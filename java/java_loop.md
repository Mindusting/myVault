---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Loop
title: Bucles en Java
---

# BUCLES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que es el [ámbito](../pc/pc_scope.md) y referenciarlo.
> > - [ ] Documentar el bucle for.
> > - [ ] Documentar el bucle do-while.
> > - [ ] Documentar el bucle for-each.

> [!help] REFERENCIAS WEB
> - [¿Qué son lo bucles en la programación?](../pc/pc_loop.md)

## WHILE

Para crear un bucle `while` en Java, simplemente tendremos que usar la palabra clave `while` seguida de unos **paréntesis** (`()`) en donde podremos la condición bajo la cual el bucle se repetirá, seguido a esto pondremos unas **llaves** (`{}`), dentro de estas pondremos el código que se va a repetir mientras la **condición** indicada en los **paréntesis** (`()`) se cumpla.

%%
SINTAXIS

while ([condition]) {
    [code_to_loop]
}
%%

> [!abstract] SINTAXIS
> <span class="flow-word-color">while</span> (<span class="italic grey">[condition]</span>) {<br><span class="transparency">····</span><span class=" italic grey">[code_to_loop]</span><br>}

La condición de un bucle consiste en un valor [booleano](<java_variable.md#BOOLEAN>), si este es *verdadero* el bucle ejecutará su contenido, si es *falso*, dejará de ejecutarse y continuará con el código que le preceda.

El valor [booleano](<java_variable.md#BOOLEAN>) no tiene porque venir de una [variable](java_variable.md), puede ser fruto de una operación como las que se muestran en el apartado de los valores [booleanos](<java_variable.md#BOOLEAN>), pero sin tener porque pasar por una [variable](java_variable.md), si no hacer la operación directamente en los **paréntesis** (`()`).

```java
public class LoopClass {
    public static void main(String[] args) {
        int i = 0;
        System.out.println("Inicio del bucle.");
        while (i < 10) {
            System.out.printf("Ciclo: %d.\n", i);
            i++;
        }
        System.out.println("Fin del bucle.");
    }
}
```

## FOR

Para crear un bucle `for` se 

```java
public class LoopClass {
    public static void main(String[] args) {
        System.out.println("Inicio del bucle.");
        for (int i = 0; i < 10; i++) {
            System.out.printf("Ciclo: %d.\n", i);
        }
        System.out.println("Fin del bucle.");
    }
}
```

## DO-WHILE

```java
public class LoopClass {
    public static void main(String[] args) {
        int i = 0;
        System.out.println("Inicio del bucle.");
        do {
            System.out.printf("Ciclo: %d.\n", i);
            i++;
        } while (i < 10);
        System.out.println("Fin del bucle.");
    }
}
```

## FOR-EACH

```java
public class LoopClass {
    public static void main(String[] args) {
        String[] foods = {
            "Manzana",
            "Naranja",
            "Platano",
            "Pera",
            "Arandano",
            "Berengena"
        };
        System.out.println("Inicio del bucle.");
        for (String food: foods) {
            System.out.printf("%s.\n", food);
        }
        System.out.println("Fin del bucle.");
    }
}
```
