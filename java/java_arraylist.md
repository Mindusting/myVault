---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: ArrayList en Java
---

<h1 align="center">ARRAYLIST EN JAVA</h1>

---

# ARRAYLIST

El `ArrayList` en Java es una [clase](java_class.md) que permite trabajar con un conjunto de valores, al igual que con los [arrays](java_array.md), ahora, la diferencia entre estos dos es que el `ArrayList` no tiene un tamaño fijo, si no que este va variando dependiendo del uso que le vayamos dando, y que estos trabajan sobre [objetos](java_class.md), es por esto que cando queremos trabajar sobre valores primitivos tenemos que hacer lo sobre las [clases](java_class.md) [`wrapper`](java_wrapper_classes.md).

```java
import java.util.ArrayList;

public class ArrayListMain {
    public static void main(String[] args) {
        // Creamos la lista de números
        ArrayList<Double> numbers = new ArrayList<Double>();

        // Amadimos número a la lista.
        numbers.add(3.0);
        numbers.add(2.7182818284);
        numbers.add(1.6180339887);

        // Modificamos un número.
        numbers.set(0, 3.1415926535)

        // Borramos un número.
        numbers.remove(1);

        for (int i = 0; i < numbers.size(); i++) {
            // Obtenemos números de la lista.
            System.out.println(numbers.get(i));
        }
    }
}
```
