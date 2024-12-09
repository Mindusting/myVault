---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Class
title: Clases en Java
---

# CLASES Y OBJETOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo]
> > - [ ] Hacer una explicación a cerca de la estructura del primer ejemplo (*Los paquetes*).
> > - [ ] Explicar qué son los `POJO`.

> [!faq] FAQ
> - [¿Qué son la clases en programación?](../pc/pc_class.md)
> - [¿Qué son los paquetes en Java?](java_package.md)

El uso de distintas clases en Java permite trocear el código en diferentes archivos (*Clases*), pudiendo así tenerlo más organizado, a si vez estos archivos pueden estar organizados en diferentes [paquetes](java_package.md) (*En esencia son carpetas*), ahora veremos una estructura de archivos sencilla de un proyecto de ejemplo:

> [!quote] ESTRUCTURA DE DIRECTORIO
> ```txt
> ./
>  └─/classExample
>    ├─ MyProyect.java
>    └─ ArrayUtilities.java
> ```

```java
package classExample;

public class MyProyect {

    public static void main(String[] args) {

        boolean exists = false;
        int index = 0;
        int[] array = {
            3,
            2,
            5,
            7
        };

        index  = ArrayUtilities.indexInArray(array, 5);
        exists = ArrayUtilities.valueOnArray(array, 2);

        System.out.println(index);
        System.out.println(exists);
        // SALIDA:
        // 2
        // true
    }
}
```

```java
package classExample;

public class ArrayUtilities {

    public static int indexInArray(int[] arr, int value) {
        // Declara a variable `ret` (return) con
        // el valor por defecto siendo -1.
        int ret = -1;

        //Recorre todo el array.
        for (int i = 0; i < arr.length; i++) {

            // Comprobamos si el elemento es igual
            // al valor que se está buscando.
            if (arr[i] == value) {

                // Si lo encuentra, asigna a `ret`
                // el índice del array y se sale
                // del bucle, ya que ya hemos
                // encontrado lo que andabamos
                // buscando.
                ret = i;
                break;
            }
        }

        return ret;
    }

    public static boolean valueOnArray(int[] arr, int value) {
        // Si el valor es diferente de -1 es por que
        // dentro de ese array sí existe el valor,
        // por tanto devuelve true, sin embargo, si
        // devuelve -1, el resultado es false, ya que
        // no lo ha encontrado devido a que -1 es el
        // valor por defecto.
        return indexInArray(arr, value) != -1;
    }
}
```

## PROPIEDAD STATIC

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

La propiedad `static` 

```java
package classExample;

public class MyProyect {

    public static void main(String[] args) {

        boolean exists = false;
        int index = 0;
        int[] array = {
            3,
            2,
            5,
            7
        };

        // Creamos un objeto de
        // tipo ArrayUtilities.
        ArrayUtilities au = new ArrayUtilities();

        index  = au.indexInArray(array, 5);
        exists = au.valueOnArray(array, 2);

        System.out.println(index);
        System.out.println(exists);
        // SALIDA:
        // 2
        // true
    }
}
```

```java
package classExample;

public class ArrayUtilities {

    // No usamos `static`.
    public int indexInArray(int[] arr, int value) {
        int ret = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == value) {
                ret = i;
                break;
            }
        }
        return ret;
    }

    // No usamos `static`.
    public boolean valueOnArray(int[] arr, int value) {
        return indexInArray(arr, value) != -1;
    }
}
```

## CONSTRUCTORES

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## FINALIZA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!faq] FAQ
> - [¿Qué es el recolector de basura de Java?](java_garbage_collector.md)

El [método](java_method.md) `finalize` es especial ya que este se ejecuta cuando el [recolector de basura](java_garbage_collector.md) de Java borra el objeto en cuestión.

> [!abstract] SINTAXIS
> <span class="key-word-color">public</span> <span class="class-color">void</span> <span class="function-color">finalize</span>() {<br><span class="transparency">····</span><span class="italic grey">[finalize_code]</span><br>}

```java
public class Complex {

    private double real      = 0;
    private double imaginary = 0;

    public Complex(Complex complex) {
        this.real      = complejo.getReal();
        this.imaginary = complejo.getImaginary();
    }

    public Complex(double r, double i) {
        this.real      = r;
        this.imaginary = i;
    }

    public double getReal() {
        return this.real;
    }

    public double getImaginary() {
        return this.imaginary;
    }

    public void finalize() {
        System.out.println("A complex has been destroyed.");
    }

    public static void main(String[] args) {

        Complex complex = new Complex(3, 2);
    }
}
```
