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

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/java/java_files.asp)
> 
> YouTube:
> - [Bro Code](https://youtu.be/MwYRVKfb2M0)
> - [Coding with John](https://youtu.be/ScUJx4aWRi0)

## ESCRITOR DE ARCHIVOS

```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriteFiles {
    public static void main(String[] args) {
        FileWriter     fw = null;
        BufferedWriter bw = null;
        
        try {
            fw = new FileWriter("./myFile.txt");
            bw = new BufferedWriter(fw);

            bw.write("Hola mundo!");

            bw.close();
            fw.close();
        } catch (IOException ex) {
            System.out.println("An error ocurred.");
        } catch (Exception ex) {
            System.out.println("An error ocurred.");
        } finally {
            try {bw.close();}
            catch(Exception ex) {}
            
            try {fw.close();}
            catch(Exception ex) {}
        }
    }
}
```

## LECTOR DE ARCHIVOS

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFiles {
    public static void main(String[] args) {
        FileReader     fr = null;
        BufferedReader br = null;
        
        try {
            fr = new FileReader("./myFile.txt");
            br = new BufferedReader(fr);

            String line = br.readLine();

            while (null != line) {
                System.out.println(line);
                line = br.readLine();
            }

            br.close();
            fr.close();
        } catch (IOException ex) {
            System.out.println("An error ocurred.");
        } catch (Exception ex) {
            System.out.println("An error ocurred.");
        } finally {
            try {br.close();}
            catch(Exception ex) {}
            
            try {fr.close();}
            catch(Exception ex) {}
        }
    }
}
```
