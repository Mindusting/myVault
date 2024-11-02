---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Class
title: Clases en Java
---

<h1 align="center">ARCHIVOS DE TEXTO EN JAVA</h1>

![#logo](../img/file_text.png)

---

# CONTROL DE ARCHIVOS DE TEXTO 📄

## LECTURA DE ARCHIVOS

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
            fr.close();
            br.close();
        } catch (IOException ex) {
            System.out.printf(
                "No se ha encontrado el archivo %s.\n",
                fileName
            );
        }
    }
}
```
