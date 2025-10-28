---
author: Mindusting
corrected: true
tags:
  - Programming/Concept/Comment
title: Comentarios en la programación
---

# COMENTARIOS EN PROGRAMACIÓN

> [!help]- REFERENCIAS WEB
> - [CodeAesthetic](https://youtu.be/Bf7vDBBOBUA)

> [!quote] Definición de libro
> Un **comentario** es un fragmento de código fuente que **es ignorado** en el proceso de compilación y/o ejecución del programa.

> [!tip] TIP
> Para mejorar la utilidad de los **comentarios**, es recomendable seguir la regla de "no expliques que hace el código, sino porqué".

Un comentarios sirve para dejar anotaciones en el código fuente de nuestro programa, suele tener varios usos:

1. **Comentarios obvios**: Hacer anotaciones acerca de una porción de código cercana para dar una explicación, esta clase de comentarios los hacen generalmente gente que está empezando a programar, además de que para la gente que sí conoce el lenguaje de programación en cuestión, esta clase de comentarios suelen sentirse como el siguiente meme:
    
    ![#logo](../../img/cat_cat.jpg)
    
    Ya que es obvio que es un gato, no hace falta que le pongas una etiqueta indicando lo, igualmente, no pasa nada por poner comentarios de este tipo (*cuando estamos empezando*) ya que a medida que uno va mejorando, deja de poner esta clase de comentarios... *generalmente...*
    Se suele tender a evitar esta clase de comentarios ya que son redundantes, y por tanto se suele decir que "*manchan*" el código sin aportar información relevante.

2. **Documentación**: En algunos [lenguajes de programación](pc_programming_language.md) existe la posibilidad de hacer documentación directamente en el código fuente, de forma que mediante un editor de texto especializado en la programación, podremos consultar esta el comentarios, generalmente esta clase de comentarios se usan en las [clases](pc_class.md) y [funciones](pc_function.md), estos no deben explicar cómo está programado, si no el uso que tienen, es decir si estamos definiendo el uso de una [funciones](pc_function.md), podremos qué *argumentos* recibe, que *devuelve*, y en caso de lanzar alguna *excepción*, bajo qué condiciones lo hace.

3. **Inhabilitación de código**: En ocasiones cuando estamos programando queremos probar diferentes líneas de código para ver cuál se adapta mejor a el objetivo que tenemos, podríamos andar escribiendo y borrando código para hacer las pruebas, pero esto nos puede llevar tiempo, como solución entran los comentarios, podemos comentar el código que queremos tener guardado pero no queremos que se ejecute, y así ir alternando entre las diferentes líneas, permitiendo que no tengamos que reescribir.

## INCONVENIENTES

Aunque los comentarios están muy bien para documentar código y dejar anotaciones acerca de cómo funciona, hay algunos problemas con estos:

1. **Mal código**: Una mala costumbre que cogen algunas personas es escribir código que funciona, pero es difícil de entender (*esto indica que no es un buen código*), *"""solucionando"""* este problema mediante comentarios, esto por supuesto no es una buena solución ya que es mejor un código legible sin comentarios que un código horrible comentado, igualmente, en cualquiera de los dos casos los comentarios nunca están de más.

2. **Mienten!!!**: El código fuente nunca miente, ya que es este el que se usa a la hora de ejecutar el programa, a diferencia de lo que le ocurren a los comentarios, es por esto que un comentario que no diga realmente que es lo que hace el código no nos va a dar un error en el código, sino que nos puede provocar confusiones, un comentario que mienta puede surgir cuando no se actualiza el comentarios después de que el código al que se refiere ha sido modificado, creando así una inconsistencia.
    Es debido a este fenómeno que hay quienes prefieren no escribir nunca comentarios, escribiendo en su lugar código lo más claro posible.
