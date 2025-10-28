---
author: Mindusting
corrected: false
tags:
  - Programming/Java/IO
title: Clase File en Java
---

# CLASE FILE EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar para qué sirve la clase `File`.
> > - [ ] Documentar como importar la clase `File`.
> > - [ ] Documentar métodos de la clase `File`.

> [!help]- REFERENCIAS WEB
> - [W3 Schools (File)](https://www.w3schools.com/java/java_files.asp)


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
            System.out.println(
                "No se ha podido crear el archivo."
            );
        } catch (Exception es) {
            System.out.println(
                "No se ha podido crear el archivo."
            );
        }

        System.out.println(file.exists());
    }
}
```

## MÉTODOS DE LA CLASE FILE

- `createNewFile`: Crea si es posible el archivo, si no es posible lanza una excepción de tipo `IOException`.
- `exists`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si el archivo o directorio existe.
- `delete`: Borra el archivo o directorio indicado, en caso de no poder, lanza una excepción de tipo `IOException`.
- `isFile`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si es un archivo.
- `isDirectory`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si es un directorio.
- `isHidden`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si el archivo o directorio está oculto.

%%
- `canRead`
- `canWrite`
- `createNewFile`
- `delete`
- `exists`
- `getName`
- `getAbsolutePath`
- `lenght`
- `list`
- `mkdir`
%%