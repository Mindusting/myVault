---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Hilos en Java
---

# HILOS

> [!help] REFERENCIAS WEB
> - [W3](https://www.w3schools.com/java/java_threads.asp)
>
> YouTube:
> - [Bro Code](https://youtu.be/J09TLPgwd0Y)
> - [Coding with John](https://youtu.be/r_MbozD32eo)

[¿Qué son los hilos en programación?](../pc_thread.md)

## EJEMPLO

Para crear en Java un proceso que ocurra en un hilo distinto se hace creando una clase que herede de la clase `Thread` como veremos en el próximo ejemplo:

```java
public class ThreadMain {

    public static void(String[] args) {
        // Creación del hilo.
        MyThread thread = new MyThread();
        // Iniciar el hilo.
        // Al iniciar el hilo se ejecutará el
        // contenido del método "run".
        thread.start();
    }
}
```

```java
// Hereda de la clase Thread.
public class MyThread extends Thread {

    @Override
    public void run() {
        // Aquí podremos el proceso que queremos
        // que se haga en un hilo independiente.
        for (int i = 0; i < 3; i++) {
            System.out.println(i);
            try {
                // El hilo se detiene por 1 segundo.
                Thread.sleep(1000);
            } catch (InterruptedException ex) {}
        }
    }
}
```

En este caso hemos creado la clase `MyThread`, esta hereda de `Thread` y para que esta clase haga lo que nosotros que ramos, debemos sobre escribir el método `run` como se ve en el ejemplo, usando el decorador `@Override`. Como se puede ver, este hilo lo que hace es contar desde **\[0, 3)**, esperando un intervalo de un segundo entre cada número.

---

Ahora, la ventaja que nos da esto es que podemos crear varios hilos al mismo tiempo, en este caso usaremos el mismo tipo de hilo, pero se puedes ejecutar varios hilos distintos, haciendo así varias tares al mismo tiempo.

Para que podáis ver como es que sí se están ejecutando varios hilos al mismo tiempo, ahora vamos a identificar cada hilo con un número que le daremos en el constructor, para que imprima también el número del hilo.

```java
public class ThreadMain {

    public static void(String[] args) {
        // Creamos tres hilos que trabajarán
        // de forma independiente.
        for (int = 0; i < 3; i++) {
            MyThread thread = new MyThread(i);
            thread.start();
        }
    }
}
```

```java
// Hereda de la clase Thread.
public class MyThread extends Thread {

    protected int threadId = 0;

    public MyThread(int id) {
        this.threadId = id;
    }

    @Override
    public void run() {
        // Aquí podremos el proceso que queremos
        // que se haga en un hilo independiente.
        for (int i = 0; i < 3; i++) {
            System.out.printf("%d: %d\n", this.threadId, i);
            try {
                // El hilo se detiene por 1 segundo.
                Thread.sleep(1000);
            } catch (InterruptedException ex) {}
        }
    }
}
```

**Resultado:**
```txt
1: 0
0: 0
2: 0
0: 1
1: 1
2: 1
0: 2
1: 2
2: 2
```

Como podéis ver, en este caso, el resultado es que los tres hilos han estado trabajado de forma separada y a la vez, por eso unos terminaban antes que otros, en el primer ciclo, terminó primero el hilo 1 luego el 0 y luego el 2, el en el segundo ciclo, termino primero el hilo 0, luego el 1 y luego el 2.

## USO REAL

Esta forma de trabajar con hilos no es la ideal, ya que para poder hacer esto se está heredando a nuestra clase (`MyThread`) la clase `Thread`, esto provoca que nuestra clase no pueda heredar de otra clase que nos pueda interesar más, el uso real se hace implementando le la clase `Runnable` como se muestra en el siguiente ejemplo:

```java
public class ThreadMain {

    public static void(String[] args) {
        // Creamos tres hilos que trabajarán
        // de forma independiente.
        for (int = 0; i < 3; i++) {
            MyRunnable runnable = new MyRunnable(i);
            // Creamos el hile a partir del "runnable".
            Thread thread = new Thread(runnable);
            thread.start();
        }
    }
}
```

```java
// Le implementamos la clase Runnable.
public class MyRunnable implements Runnable {

    protected int runnableId = 0;

    public MyRunnable(int id) {
        this.runnableId = id;
    }

    @Override
    public void run() {
        for (int i = 0; i < 3; i++) {
            System.out.printf("%d: %d\n", this.runnableId, i);
            try {
                // El hilo se detiene por 1 segundo.
                Thread.sleep(1000);
            } catch (InterruptedException ex) {}
        }
    }
}
```

Usando esta forma de trabajar con hilos funciona de la misma forma, lo único que cambia es que en vez de heredar, implementamos y que a la hora de crear el objeto (*En este caso `MyRunnable`*), no es directamente el hilo, si no que después se tiene que crear un hilo a partir de este objeto.

> [!info]
> Es importante saber que si en uno de los hilos ocurre una excepción, el resto de hilos seguirán ejecutando se, ya que trabajan de forma independiente.

## MÉTODOS ÚTILES

### UNIÓN

Si queremos hacer que un proceso espere a que un hilo termine su proceso, podemos usar el método `join`

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

### SIGUE VIVO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
