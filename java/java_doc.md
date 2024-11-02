---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Javadoc
---

# JAVADOC

Javadoc es una utilidad de Oracle para la generación de documentación automática en [HTML](../HTML/html.md) del funcionamiento del código de [Java](java.md), esta documentación se crea a partir de ciertos comentarios que se encuentran en el código fuente.

Para crear esta documentación se utilizan las **etiquetas** (*tags*), las **etiquetas** se indican con una **arroba** (*@*) seguido de una **palabra clave**.

> [!tip] TIPs
> - Escribirlo en inglés.
> - Tiene que ir al grano.
> - Ponlo todo, o no pongas nada, pero no a medias.
> - Si el método puede tener excepciones, explica cuales y bajo qué condiciones.

---

Para crear la documentación, tenemos que crear un [comentario multilínea](java_comments.md) encima de las [funciones](java_method.md) o [clases](java_class.md):

```java
public class MyJavaDoc {

    /**
     * This is the description of my method.
     * @param x This is the description of variable x.
     * @param y This is the description of variable y.
     * @return This is the description of the return.
     */
    public static int add(int x, int y) {
        return x + y;
    }

    public static void main(String[] args) {
        System.out.println(add(3, 2));
    }
}
```

En este caso podemos ver como la [función](java_method.md) `add`, tiene su propio **Javadoc**.

## ETIQUETAS

- `param`: Permite indicar la descripción de los parámetros de una función.
- `return`: Permite indicar la descripción del return de la función.
- `throws`: Permite indicar la descripción de las excepciones que puede lanzar al función.
- `deprecated`:
- `author`: Permite indicar el autor de la función.
- `see`:
- Referencia a funciones:
- Etiquetas [HTML](../HTML/html.md):
