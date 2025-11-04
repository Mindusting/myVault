---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Procesos en Java
---

# PROCESOS EN JAVA

> [!fail]- ESTE PARTADO ESTÁ INCOMLETO
> > [!todo] #TODO

Para ejecutar otro proceso desde **Java** se usan principalmente dos [clases](java_class.md); `ProcessBuilder` y `Process`; el primero se encargará de como tal crear el proceso mientras que el segundo es el tipo de objeto que representará el proceso en cuestión.

---

Para el siguiente ejemplo tendremos la siguiente estructura de archivos; en donde tendremos un proyecto con las carpetas `src` (*en donde guardaremos los archivo `.java`*) y `bin` (*en donde guardaremos los archivos `.class` tras ejecutar el compilador de Java sobre los archivo `.java`*); es importante recalcar esto ya que en la ejecución de procesos, nosotros llamaremos a los archivos `.class` no a los `.java`.

```txt
/MyProyect
├─/src
│ └─/processes
│   ├─/MainProcess.java
│   └─/SecondProcess.java
└─/bin
  └─/processes
    ├─/MainProcess.class
    └─/SecondProcess.class
```

**MainProcess.java:**

```java
package processes;

import java.io.IOException;

public class MainProcess {
    public static void main(String[] args) {
        ProcessBuilder processBuilder = null;
        Process        process        = null;
        
        try {
            processBuilder = ProcessBuilder(
                "java",
                "-cp",
                "bin",
                "processes/SecondProcess"
            );
            // La siguiente instrucción es la que
            // puede lanzar al excepción IOException.
            process = processBuilder.start();
        } catch (IOException ex) {
            // Se ejecuta cuando el proceso no se
            // ha podido ejecutar correctamente.
            System.out.println("Error de proceso.");
        }
    }
}
```

**SecondProcess.java:**

```java
package processes;

import java.io.File;
import java.io.IOException;

public class SecondProcess {
    public static void main(String[] args) {
        File file = null;

        try {
            file = new File("readme.md");
            
            if (!file.exists()) {
                file.createNewFile();
            }
        } catch (IOException ex) {
            System.out.println("No se ha podido crear el archivo.");
        }
    }
}
```

> [!example] CASO DE EJEMPLO
> En este caso como se puede ver en el `MainProcess.java`, el `ProcessBuilder` recibe varios argumentos que conformarán el comando que ejecutará el proceso en cuestión, en este caso son los siguientes:
> - `java`: indica se se debe ejecutar el comando `java`; al igual que lo hacemos con la [ejecución de Java](java_javac.md#EJECUTAR).
> - `-cp`: (*abreviación de `-classpath`*) indica que vamos a especificar la ruta de los archivos `.class`; si quieres más información sobre esto lo tienes en la [documentación de ejecución de Java](java_javac.md#EJECUTAR).
> - `bin`: es el directorio en donde se guardan los archivos `.class`.
> - `processes/SecondProcess`: es la ruta y nombre del archivo `.class` que contiene el [método `main`](java_main_method.md).

## ESPERAR A QUE TERMINE

Si queremos que un proceso espere a que termine el otro lo podemos usar el [método](java_method.md) `waitFor`; este no recibe ningún parámetro y puede lanzar una [excepción](java_exception.md) en 

#TODO
