---
author: Mindusting
corrected: false
tags:
  - Programming/Java/GUI
title: GUI en Java
---

# INTERFAZ GRÁFICA DE USUARIO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar [Swing](packages/javax/swing/java_swing.md).

> [!help]- REFERENCIAS WEB
> - [geeksforgeeks](https://www.geeksforgeeks.org/java-jframe/)

- [Swing](packages/javax/swing/java_swing.md)

%%
Para crear un entorno gráfico usamos las librerías `javax.swing` y `java.awt`, dentro de estas podemos encontrar las [clases](java_class.md) necesarias para trabajar con entornos gráficos.

```java
import javax.swing.JFrame;

public class GuiMenu {
    
    public static void main(String[] args) {
        // Creamos un objeto JFrame.
        // Este será nuestra ventana.
        JFrame frame = new JFrame();
        
        // Indicamos que quermos que la
        // ventana se cierre cuando pulsemos la
        // equis de la esquina superior de recha.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Indicamos las coordenadas de la
        // pantalla en la que debe situase
        // y el tamaño de esta.
        frame.setBounds(10, 10, 360, 240);
        
        // Indicamos el título de la ventana.
        frame.setTitle("My GUI");
        
        // Indicamos si se el usuario le
        // puede cambiar el tamaño a la
        // ventana.
        frame.setResizable(false);
        
        // Indicamos que la ventana sea visible.
        frame.setVisible(true);
    }
}
```

> [!info]
> Las coordenadas indicadas con el método `setBounds` son respecto al origen de la pantalla, situado en la esquina superior izquierda.

## CAMBIAR EL COLOR DEL FONDO

Para poder cambiarle el color al fondo de nuestra ventana tendremos que importar la clase `Color` de la librería `java.awt`:

```java
import java.awt.Color;
import javax.swing.JFrame;

public class GuiMenu {
    
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(100, 100, 360, 240);
        frame.setTitle("My GUI");
        frame.setResizable(false);
        frame.setVisible(true);
        
        frame.getContentPane()
        // Aquí estoy usando unos valores hexadecimales,
        // peso se puede usar tres números enteros
        // separados por comas indicando los valores RGB.
        .setBackground(new Color(0xffaacc));
    }
}
```

Aquí estoy usando uno valor hexadecimal, peso se puede usar tres números enteros separados por comas indicando los valores RGB.

## USO REAL

Por lo general no se suele hacer como hemos estado viendo hasta ahora en estos ejemplos, esto ha sido simplemente para ver las bases, esta forma de trabajar sobre la [clase](java_class.md) `JFrame` provoca que como queramos hacer algún tipo de modificación, no vamos a poder, para ello, lo que se suele hacer es crear una [clase](java_class.md) que herede de `JFrame`, así podremos usar esta nueva [clase](java_class.md) al igual que `JFrame`, pero podremos modificarla a nuestro antojo.

```java
import javax.swing.JFrame;

public class Window extends JFrame {
    
    public Window() {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setBounds(100, 100, 360, 240);
        this.setTitle("My GUI");
        this.setResizable(false);
        this.setVisible(true);
    }
}
```

```java
public class GuiMenu {
    
    public static void main(String[] args) {
        Window window = new Window();
        
        frame.getContentPane().setBackground(new Color(0xffaacc));
    }
}
```

---

```java
// Creamos un Label (Etiqueta)
JLabel label = new JLabel("Este es mi label.");
//label.setText();
label.setHorizontalTextPosition(JLabel.CENTER);
label.setVerticalTextPosition(JLabel.TOP);
Window window = new Window();
window.add(label);

//window.getContentPane().setBackground(new Color(0xffaacc));
```
%%
