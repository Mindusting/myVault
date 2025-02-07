---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Class
title: Clases en Java
---

# CONTROL DE ARCHIVOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar lectura de archivo.
> > - [ ] Documentar escritura de archivo.

> [!help] REFERENCIAS WEB
> - [W3](https://www.w3schools.com/java/java_files.asp)
> 
> YouTube:
> - [Bro Code](https://youtu.be/MwYRVKfb2M0)
> - [Coding with John](https://youtu.be/ScUJx4aWRi0)

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
