---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Class
title: Clases en Java
---

# CONTROL DE ARCHIVOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtu.be/MwYRVKfb2M0)
> - [Coding with John](https://youtu.be/ScUJx4aWRi0)

## CLASE FILE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```java
import java.io.File;
import java.io.IOException;

public class MainFile {
    public static void main(String[] args) {
        File file = new File("myFile.txt");

        System.out.println(file.exists());

        try {
            file.createNewFile();
        } catch (IOException ex) {
            System.out.println("No se ha podido crear el archivo.");
        } catch (Exception es) {
            System.out.println("No se ha podido crear el archivo.");
        }

        System.out.println(file.exists());
    }
}
```

### MÉTODOS DE LA CLASE FILE

- `createNewFile`: Crea si es posible el archivo, si no es posible lanza una excepción de tipo `IOException`.
- `exists`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si el archivo o directorio existe.
- `delete`: Borra el archivo o directorio indicado, en caso de no poder, lanza una excepción de tipo `IOException`.
- `isFile`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si es un archivo.
- `isDirectory`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si es un directorio.
%%
No sé del todo como funciona esto.
- `isHidden`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si el archivo o directorio está oculto.
%%

## ESCRITOR DE ARCHIVOS

```java
import java.io.FileWriter;
import java.io.IOException;

public class WriteFiles {
    public static void main(String[] args) {
        try {
            FileWriter fw = new FileWriter("myFile.txt");
            fw.write("Hola mundo!");
            fw.close();
        } catch (IOException ex) {
            System.out.println("An error ocurred.");
        }
    }
}
```

## LECTOR DE ARCHIVOS

```java

```

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException

public class ReadFiles {
    public static void main(String[] args) {
        String fileName = "myTextFile.txt";
        
        try {
            FileReader fr = new FileReader(fileName);
            BufferedReader br = new BufferedReader(fr);
            String fileLine = br.readLine();
            while (null != fileLine) {
                System.out.println(fileLine);
                fileLine = br.readLine();
            }
        } catch (IOException ex) {
            System.out.printf(
                "No se ha encontrado el archivo %s.\n",
                fileName
            );
        } final { // Siempre cierra.
            try {
                if (null != br) {
                    br.close();
                }
            } catch (Exception es) {
                // No importa.
            }
            try {
                if (null != fr) {
                    fr.close();
                }
            } catch (Exception es) {
                // No importa.
            }
        }
    }
}
```
