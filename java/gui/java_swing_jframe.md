---
author: Mindusting
corrected: false
tags:
  - Programming/Java/GUI
title: GUI en Java
---

# CLASE JFRAME

La [clase](../java_class.md) `JFrame` es usada para crear ventanas, para ello, creamos un objeto de esta [clase](../java_class.md):

```java
import javax.swing.JFrame;

public class Gui {
    public static void main(String[] args) {
        // Creación del objeto.
        JFrame frame = new JFrame();

        // Indicamos la posición y el tamaño de la ventana.
        frame.setBounds(10, 10, 300, 200);
        // Indicamos que hacer al pulsar el boton de cerrar.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Indicamos que la ventana se muestre.
        frame.setVisible(true);
    }
}
```

Al crear el objeto `JFrame` le tenemos que establecer unas características a trabes de sus [métodos](java_method.md), ahora explicaremos los usos:
