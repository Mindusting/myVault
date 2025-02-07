---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Comment
title: Comentarios en Java
---

# COMENTARIOS

> [!faq] FAQ
> - [¿Qué son los comentario en programación?](../pc/pc_comment.md)

En Java existen dos formas de escribir comentarios, una es para escribir una sola línea y la otra permite escribir múltiples líneas, ahora, un comentario no es más que texto que el compilador de Java va a omitir a la hora de compilar el código, por lo que a efectos de nuestro programa este no va a provocar ningún cambio (*A priori, en un momento veremos eso*), esto nos permite redactar información en el código de nuestro programa para dar indicaciones que cómo funciona nuestro código, esto te puede parecer que no tiene mucho sentido ya que podrías pensar que leyendo el código ya lo vas a entender, pero hazme caso, que leer un texto explicativo va a ser mucho más sencillo que intentar entender qué hace un programa mediante leer el código a piñón (*Historia personal, una vez empecé un proyecto, por cuestiones personales lo dejé apartado y al cabo de un tiempo, al querer retomarlo, me quedé como un bobo pensando “¿Que co\*\*nes se supone que hace esto?”, por lo que recuerda, siempre escribe comentarios **útiles** y hago énfasis en lo de **útiles** por que no quiero que seas de la clase de persona que hace el siguiente tipo de comentario*).

```java
public class Main {
    // Esto es la clase Main.
}
```

En este ejemplo podemos ver un comentario que nos indica que el sitio en el que está situado es la clase Main, cuando literalmente justo encima pone “*class Main*”, por favor no hagáis esta clase de comentarios, no aportan nada, y en el caso de que estéis trabajando en un proyecto con otras personas, esto no hará si no hacer que el resto de programadores duden acerca de nuestros conocimientos de programación.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo!!!");
        /*
        Esto de aquí es la función print,
        permite escribir texto en la
        consola como forma de comunicación
        con el usuario que esté usando
        nuestro programa, pero no te voy
        a explicar más, ya que eso lo
        veremos en el próximo apartado.
        */
    }
}
 ```

A diferencia del anterior ejemplo, en este si damos una información útil (Dentro de lo que cabe, este ejemplo es un poco una tontería ya que una vez estéis familiarizados con el lenguaje, los dos comentarios tendrán el mismo valor, explicar algo que es obvio, pero la cuestión es que si vais a escribir un comentario este tiene que dar información de utilidad, como puede ser tener un bloque de código grande y que haya un comentario explicando qué se supone que hace ese trozo de código).

Sí has estado atento ya deberías saber cómo se escriben los dos tipos de comentarios, igualmente ahora los veremos más en profundidad.

Para escribir un comentario de una línea tendremos que escribir dos barras, todo lo que se escriba en esa línea a partir de ese punto será considerado un comentario.

%%
SINTAXIS

// [comment]
%%

> [!abstract] SINTAXIS
> <span class="comment-color">// ***\[comment\]***</span>

Para escribir un comentario de varias líneas tenemos que escribir una barra y un asterisco esto indica el inicio del comentario, y para terminarlo se escribe un asterisco y una barra, todo el texto que se encuentre entre esta apertura y cierre de comentario se considerará un comentario, esto sin importar el número de líneas que haya de por medio.

%%
SINTAXIS

/*
[comment]
*/
%%

> [!abstract] SINTAXIS
> <span class="comment-color">/*<br>***\[comment\]***<br>*/</span>

¿Recuerdas que antes comenté que “A efectos de nuestro programa este no va a provocar ningún cambio (A priori)”? Bueno, pues ahora te explicaré cómo es que sí puede afectar un comentario a nuestro código, y es que por ejemplo imagínate que estás escribiendo el código de un programa te das cuenta de que hay un trozo de este que té gustaría cambiar y procedes a hacerlo, tras ejecutarlo ves que no funciona como esperabas y quieres devolverlo a como estaba, resulta que ya no puedes y procedes a tirarte de los pelos porque ahora te has metido en un marrón, si no quieres que te ocurran esta clase de cosas (Como me ha pasado a mí) te recomiendo que cojas la costumbre de comentar código, por ejemplo, si quisieras hacer un cambio, puedes copiar el código que quieres cambiar, pegarlo más abajo y comentario con la apertura y cierre de comentarios multilínea, de esta forma si después no quedas satisfecho puedes borrar los cambios y descomentar el código que te habías guardado, lo mismo se aplica a código que ya no quieres tener en tú programa, siempre puedes comentarlo antes que borrarlo por si no estás seguro.
