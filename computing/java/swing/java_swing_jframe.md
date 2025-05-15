---
author: Mindusting
corrected: false
tags:
  - Programming/Java/GUI/Swing
title: JFrame de Swing en Java
---

# CLASE JFRAME EN JAVA SWING

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Explicar que esta clase es para crear la ventana.
> > - [x] Explicar como crear tu propia clase `JFrame`.
> > - [x] Documentar la visibilidad de la ventana.
> > - [x] Documentar como cambiar el tamaño de la ventana.
> > - [x] Documentar como cambiar la posición de la ventana.
> > - [x] Documentar como indicar la acción en el cierre.
> > - [x] Documentar como cambiar el título de la ventana.
> > - [ ] Documentar como establecer el panel de contendido.
> > - [x] Documentar como cambiar el icono de la ventana.
> > - [x] Documentar como centrar la ventana (`setLocationRelativeTo(null)`).
> > - [x] Documentar el método `pack` (*Ajusta la ventana a los elementos en su interior.*).
> > - [ ] Añadir links a las palabras `int` a su apartado correspondiente.

La [clase](../java_class.md) `JFrame` se encuentra en el paquete `javax.swing` y es la encargada de crear la ventana, en esta configuraremos cosas como el tamaño, la posición, el título, entre otras cosas, generalmente por cuestiones de comodidad se usa la herencia para crear nuestra propia [clase](../java_class.md).

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {}
}
```

Dentro de esta clase podremos poner toda la configuración que queramos para nuestra ventana, una ver hayamos terminado con ella, podremos mostrar la ventana creando un [objeto](../java_class.md) de esta.

```java
public class ProyectMain {

    public static void main(String[] args) {
        // Aquí se genera la ventana.
        //    v
        new Window();
    }
}
```

Antes de continuar con la documentación más específica, veamos como podemos hacer que se vea la ventana ya que tal y como está ahora no veremos nada, ya que no tiene nada de configuración.

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Indicamos que el tamaño de la ventan
        // debe ser de 480 px de alto por
        // 360 px de alto.
        this.setSize(480, 360);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

## ACCIÓN AL CERRAR

Para indicar que queremos que se haga cuando se pulse la "X" de la ventana se usa el [método](../java_method.md) `setDefaultCloseOperation`, este recibe un `int` con uno de cuatro opciones, podemos indicarlo mediante las [variables](../java_variable.md) constantes de la [clase](../java_class.md) `JFrame` o escribiendo sus valores directamente:

> [!abstract] SINTAXIS
> setDefaultCloseOperation(***\[mode\]***)

| VARIEBL NAME        | VALUE |
|:------------------- |:-----:|
| DO_NOTHING_ON_CLOSE |   0   |
| HIDE_ON_CLOSE       |   1   |
| DISPOSE_ON_CLOSE    |   2   |
| EXIT_ON_CLOSE       |   3   |

## POSICIÓN Y TAMAÑO

Para establecer al posición y tamaño (*medido en píxeles*) de la ventana se utiliza el [método](../java_method.md) `setBounds`, este recibe cuatro argumentos de tipo `int`, indicando primero las coordenadas en pantalla, de en donde tiene que situarse la ventana y luego el tamaño en los ejes *X* e *Y*.

Se debe tener en cuenta que cuando indicamos en qué coordenadas se debe situar la ventana, se hará respecto al punto de origen, siendo este la esquina superior izquierda de la pantalla, a medida que incrementamos le eje *X* nos iremos desplazando hacia la derecha y si incrementamos el eje *Y* nos iremos hacia abajo.

![#center](../imgs/java_swing_jframe_position.md)

> [!abstract] SINTAXIS
> setBounds(***\[xPos\]***, ***\[yPos\]***, ***\[width\]***, ***\[height\]***)

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece la posición y
        // dimensiones de la ventan.
        this.setBounds(100, 100, 480, 360);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

Existen otras formas de indicar el tamaño y la posición de forma individual que veremos en los siguientes apartados.

### TAMAÑO

Para establecer el tamaño (*medido en píxeles*) de la ventana se usa el [método](../java_method.md) `setSize`, este recibe dos argumentos de tipo `int` indicando el *ancho* y *alto* de la ventana.

> [!abstract] SINTAXIS
> setSize(***\[width\]***, ***\[height\]***)

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece las dimensiones
        // de la ventan.
        this.setSize(480, 360);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

### TAMAÑO RELATIVO

Para que el tamaño de la ventana se adapte automáticamente al contenido de esta, una vez hemos terminado de configurar todo se usa el [método](../java_method.md) `pack`, este no recibe argumentos.

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Aquí se crearía el contenido que
        // queremos que contenga la ventana.

        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Establecemos el tamaño de la ventana
        // respecto al contenido de esta.
        this.pack();
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

### POSICIÓN

Para establecer la posición (*medido en píxeles*) de la ventana se usa el [método](../java_method.md) `setLocation`, este recibe dos argumentos de tipo `int` indicando el eje *X* y eje *Y* del monitor.

> [!abstract] SINTAXIS
> setLocation(***\[xPos\]***, ***\[yPos\]***)

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece las dimensiones
        // de la ventan.
        this.setSize(480, 360);
        // Se establece las coordenadas
        // en donde se va a colocar la
        // ventana.
        this.setLocation(100, 100);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

### POSICIÓN RELATIVA

Para establecer la posición relativa al centro del monitor se usa el [método](../java_method.md) `setLocationRelativeTo`, este recibe un argumento el cual tendremos que establecer a `null` para centrar el `JFrame` en el monitor.

> [!abstract] SINTAXIS
> setLocationRelativeTo(null)

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece las dimensiones
        // de la ventan.
        this.setSize(480, 360);
        // Se centra la ventana
        // respecto al monitor.
        this.setLocationRelativeTo(null);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

## VISIBILIDAD

La visibilidad de una ventana puede estar en dos estados (*visible y no visible*), esto nos permite esconder la ventana sin perder todo lo que haya cargado en ella, por defecto las ventanas están ocultas es por esto que tenemos que establecerla a visible al inicio con el [método](../java_method.md) `setVisible`, este recibe un argumento de tipo [`boolean`](../data_types/java_boolean.md) con el cual indicaremos si queremos que sea visible o no.

> [!abstract] SINTAXIS
> setVisible(***\[visible\]***)

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece las dimensiones
        // de la ventan.
        this.setSize(480, 360);
        // Indicamos si se puede redimensionar
        // la ventana.
        this.setResizable(false);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

## REDIMENSIONABLE

La redimensionabilidad de una ventana consiste en si permitimos que el usuario puede clicar en el borde de la ventana y arrastrar para cambiar el tamaño de esta, para poder indicarlo se usa el [método](../java_method.md) `setResizable`, este recibe un argumento de tipo [`boolean`](../data_types/java_boolean.md) indicando si queremos que se puede redimensionar.

> [!abstract] SINTAXIS
> setResizable(***\[resizable\]***)

## TÍTULO

Para establecer un título a nuestra ventana se usa el [método](../java_method.md) `setTitle`, este recibe un argumento de tipo [`String`](../data_types/java_string.md) indicando el título.

> [!abstract] SINTAXIS
> setTitle(***\[title\]***)

```java
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {
        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece las dimensiones
        // de la ventan.
        this.setSize(480, 360);
        // Indicamos el título de la ventana.
        this.setTitle("Esta es mi ventana.");
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```

## ICONO

Para establecer una imagen como icono de la ventana primero tendremos que cargarla con la [clase](../java_class.md) `ImageIcon` la cual también se encuentra en el módulo `javax.swing`, una vez hayamos cargado imagen podremos establecerla como icono como se puede ver en el ejemplo, haciendo uso de del [método](../java_method.md) `setIconImage`, esta recibe un argumento de tipo `Image`.

```java
import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class Window extends JFrame {

    private static final long serialVersionUID = 1L;

    public Window() {

        // Guardamos la imagen un una variable.
        ImageIcon icon = new ImageIcon("img/icon.png");
        // Establecemos la imagen como icono
        // de la ventana.
        this.setIconImage(icon.getImage());

        // Indicamos que cuando se pulse la "X"
        // se cierre la ventana acabando con
        // el programa.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Se establece las dimensiones
        // de la ventan.
        this.setSize(480, 360);
        // Indicamos que la ventana debe ser visible.
        this.setVisible(true);
    }
}
```
