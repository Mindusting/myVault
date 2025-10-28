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
> > - [ ] Explicar que las excepciones de los ejemplos no tienen por que ser capturadas en un caso rea.
> > - [ ] Documentar como escribir archivos de texto.
> > - [ ] Documentar como leer archivos de texto.
> > - [ ] Documentar como escribir archivos binarios.
> > - [ ] Documentar como leer archivos binarios.
> > - [ ] Documentar como escribir archivos de objetos.
> > - [ ] Documentar como leer archivos de objetos.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/java/java_files.asp)
> 
> YouTube:
> - [Bro Code](https://youtu.be/MwYRVKfb2M0)
> - [Coding with John](https://youtu.be/ScUJx4aWRi0)

## ARCHIVOS DE TEXTO

### ESCRITOR DE ARCHIVOS

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

### LECTOR DE ARCHIVOS

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFiles {
    public static void main(String[] args)
    throws IOException {
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

## ARCHIVOS BINARIOS

## ARCHIVOS DE OBJETOS

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;


public class ObjectFileManager<T> {
    
    public ObjectFileManager() {}

    
    public void write(T object, String filePath)
    throws FileNotFoundException, IOException {
        File               file = null;
        FileOutputStream   fos  = null;
        ObjectOutputStream oos  = null;
        
        try {
            file = new File(filePath);
            fos  = new FileOutputStream(file);
            oos  = new ObjectOutputStream(fos);
            
            oos.writeObject(object);
        } finally {
            try {if (null != oos) {oos.close();}}
            catch (Exception ex) {}

            try {if (null != fos) {fos.close();}}
            catch (Exception ex) {}
        }
    }
    
    @SuppressWarnings("unchecked")
    public T read(String filePath)
    throws ClassNotFoundException, IOException {
        T                 object = null;
        File              file   = null;
        FileInputStream   fis    = null;
        ObjectInputStream ois    = null;
        
        try {
            file = new File(filePath);
            fis  = new FileInputStream(file);
            ois  = new ObjectInputStream(fis);
            
            object = (T) ois.readObject();
        } finally {
            try {if (null != ois) ois.close();}
            catch (Exception ex) {}

            try {if (null != fis) fis.close();}
            catch (Exception ex) {}
        }

        return object;
    }
}
```
