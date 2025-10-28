---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Hilos en Java
---

# HILOS EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Añadir una descripción.
> > - [ ] Documentar como hacer que un hilo espere a múltiples hilos de un conjunto.
> > - [ ] Documentar como dormir durante un tiempo un hilo.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/java/java_threads.asp)
>
> YouTube:
> - [Bro Code](https://youtu.be/J09TLPgwd0Y)
> - [Coding with John](https://youtu.be/r_MbozD32eo)

> [!faq]- FAQ
> - [¿Qué son los hilos en programación?](../pc/pc_thread.md)

## CREACIÓN DE LA CLASE HILO

Para crear un **hilo** en **Java**, se puede hacer de dos formas; la primera consiste en extender la una [**clase**](java_class.md) a `Thread`, y la otra es implementando `Runnable`; las dos funcionan de la misma forma, por lo que se pueden usar indistintamente.

```java
public class MyThread extends Thread { // <- La diferencia.
    @Override
    public void run() {
        // Código del hilo.
    }
}
```

```java
public class MyRunnable implements Runnable { // <- La diferencia.
    @Override
    public void run() {
        // Código del hilo.
    }
}
```

Como puedes ver ambos formas requieren de un [**método**](java_method.md) llamado `run` el cual tendremos que sobre escribir (*con el decorador `@Override`*); cuando se inicie el hilo, este ejecutará el contendido que pongamos dentro de este [**método**](java_method.md).

> [!important] IMPORTANTE
> Esta parte en la que creamos las [**clases**](java_class.md) que usaremos como *hilos* son muy parecidas, pero dependiendo de qué método elijamos, la creación del **objeto** *hilo* cambia; este punto lo veremos más adelante.

## CREACIÓN DEL OBJETO HILO

Dependiendo de la forma en la que hayamos creado la [**clase**](java_class.md) tendremos que crear los **objetos** de una forma distinta.

Para crear un **objeto** a partir de una [**clase**](java_class.md) que extiende de `Thread`:

```java
public class MainThread {
    public static void main(String[] args) {
        // Se crea el objeto hilo de forma directa.
        //                    V
        MyThread thread = new MyThread();
        //                            ^
        // Si el constructor recibiera argumentos
        // estos se pasarían a la clase Thread.
    }
}
```

Para crear un **objeto** a partir de una [**clase**](java_class.md) que implementa de `Runnable`:

```java
public class MainThread {
    public static void main(String[] args) {
        // Se crea primero el objeto runnable.
        //                        V
        MyRunnable runnable = new MyRunnable();
        //                                  ^
        // Si el contructor recibiera argumentos
        // estos se pasarían a la clase Runnable.

        // Luego se crea el objeto hilo que recibe el runnable.
        //                    V
        Thread thread = new Thread(runnable);
    }
}
```

> [!important] IMPORTANTE
> Fíjate en el apunte del comentario en el código, se indica en donde se tienen que pasar los parámetros para el constructor; esto es importante saberlo, sobre todo para después cuando queramos por ejemplo [sincronizar hilos](#SINCRONIZACIÓN%20DE%20HILOS), o en general darle información a un *hilo* para poder realzar tareas más complejas.

## EJECUCIÓN DE HILOS

Hayamos [creado los *hilos*](#CREACIÓN%20DEL%20OBJETO%20HILO) de una forma u otra, el manejo de estos es igual, ya que ambos terminan convergiendo en la misma [clase](java_class.md) `Thread`; por lo que a partir de aquí la explicación se unifica.

Para ejecutar un *hilo* se usa el [método](java_method.md) `start`; al ejecutar este [método](java_method.md) *Java* creará otro *hilo* (*no una [clase](java_class.md) `Thread` sino un hilo interno*) el cual se encargará de ejecutar el [método](java_method.md) `run` de este.

> [!important] IMPORTANTE
> No ejecutes el [método](java_method.md) `run` del *hilo* directamente, ya que de esta forma se estará ejecutando de forma directa en vez de a través de un nuevo *hilo*; es por esto que se debe ejecutar el [método](java_method.md) `start`, ya que de esta forma creará un *hilo* interno y será este quien de forma automática ejecutará el [método](java_method.md) `run`; así que recuerda que si llamas el [método](java_method.md) `run` no estarás usando el *hilo* correctamente.

**Clase hilo:**

```java
public class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("El hilo ha comenzado a ejecutarse.");

        // Esto es un ejemplo didáctico; en este
        // caso el hilo no hace nada más que contar,
        // la idea es que nosotro aquí podríamos
        // hacer que realice una tarea de peso,
        // como llamar a otros métodos, acceder a
        // archivos o bases de datos etc.
        for (int i = 0; i < 3; i++) {
            System.out.printf("%d\n", i);
        }

        System.out.println("El hilo ha terminado de ejecutarse.");
    }
}
```

**Clase con el método MAIN:**

```java
public class MainThread {
    public static void main(String[] args) {
        System.out.println("Inicio del main.");

        System.out.println("Creación del hilo.");
        MyThread thread = new MyThread();

        System.out.println("Inicio del hilo.");
        thread.start();

        System.out.println("Fin del main.");
    }
}
```

**Resultado del programa:**

```txt
Inicio del main.
Creación del hilo.
Inicio del hilo.
Fin del main.
El hilo ha comenzado a ejecutarse.
0
1
2
El hilo ha terminado de ejecutarse.
```

Como se puede ver en el resultado, el *hilo* principal (*el que ejecuta el [método](java_method.md) `main`*) termina antes que el *hilo* hijo, para que luego, este último realice su tarea (*contar*), termina la ejecución del programa; aunque no esté mal de por sí (*en el sentido de que no da errores*), no se debería hacer esto así, ya que se entiende que el *hilo* principal tiene que ser el primero en iniciar y el último en terminar, para poder hacer esto último se necesaria la [sincronización de *hilos*](#SINCRONIZACIÓN%20DE%20HILOS) (*el siguiente apartado*).

## SINCRONIZACIÓN DE HILOS

Para sincronizar múltiples *hilos* se suele usar el [método](java_method.md) `join`; este en esencia introduce al *hilo* en un bucle infinito en que que estará chequeando si ha terminado o no el *hilo* al que pertenece el [método](java_method.md) en cuestión (*se entiende mejor con un ejemplo*), esto permite hacer que un *hilo* "*espere*" a que otro termine de ejecutarse.

> [!example] Ejemplo:
> En el siguiente ejemplo podemos ver como el *hilo* principal crea un *hilo*, lo inicia (`start`) y luego espera a que este termine de ejecutarse para continuar (`join`).

**Clase con el método MAIN:**

```java
public class MainThread {
    public static void main(String[] args) {
        System.out.println("Inicio del main.");

        System.out.println("Creación del hilo.");
        MyThread thread = new MyThread();

        System.out.println("Inicio del hilo.");
        thread.start();

        try {
            thread.join(); // <- Espera hasta que el hilo termine.
        } catch (Exception ex) {}
        // Si se interrumpe el hilo, lo ignoramos.

        System.out.println("Fin del main.");
    }
}
```

**Resultado del programa:**

```txt
Inicio del main.
Creación del hilo.
Inicio del hilo.
El hilo ha comenzado a ejecutarse.
0
1
2
El hilo ha terminado de ejecutarse.
Fin del main.
```

---

En el ejemplo anterior hemos podido ver como el *hilo* principal espera a que otro termine, pero hay ocasiones en las que tendremos que hacer que un *hilo* cree múltiples *hilos* y estos se tienen que sincronizar, en este caso, algunos de los *hilos* tendrán que recibir la referencia de otros para poder sincronizarse con ellos.

**Clase con el método MAIN:**

```java
public class MainThread {
    public static void main(String[] args) {
        System.out.println("Inicio del main.");

        System.out.println("Creación de los hilos.");
        MyThread1 thread1 = new MyThread1();
        MyThread2 thread2 = new MyThread2(thread1);

        System.out.println("Inicio de los hilos.");
        // Iniciamos primero el segundo hilo para que se pueda
        // ver como le espera al primer hilo; esto es por que
        // es un ejemplo y es muy sencillo, en el mundo real
        // no hace falta que nos iniciemos al revés.
        thread2.start();
        thread1.start();

        try {
            thread1.join(); // <- Esperamos a que los dos hilos
            thread2.join(); //    terminen de ejecutarse.
        } catch (Exception ex) {}

        System.out.println("Fin del main.");
    }
}
```

**Clase Thread1:**

```java
public class MyThread1 extends Thread {
    @Override
    public void run() {
        System.out.println("El hilo1 ha comenzado a ejecutarse.");

        for (int i = 0; i < 3; i++) {
            System.out.printf("%d\n", i);
        }

        System.out.println("El hilo1 ha terminado de ejecutarse.");
    }
}
```

**Clase Thread2:**

```java
public class MyThread2 extends Thread {

    private Thread thread = null;

    public MyThread2(Thread thread) {
        // Guardamos el hilo al que tiene que esperar.
        this.thread = thread;
    }

    @Override
    public void run() {
        System.out.println("El hilo2 ha comenzado a ejecutarse.");

        try {
            this.thread.join(); // <- Espera a que termine.
        } catch (Exception ex) {}

        System.out.println("El hilo2 ha terminado de ejecutarse.");
    }
}
```

**Resultado del programa:**

```txt
Inicio del main.
Creación de los hilos.
Inicio de los hilos.
El hilo2 ha comenzado a ejecutarse.
El hilo1 ha comenzado a ejecutarse.
0
1
2
El hilo1 ha terminado de ejecutarse.
El hilo2 ha terminado de ejecutarse.
Fin del main.
```

---
---
---
---
---

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
