---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Class
title: Clase File en Java
---

# CLASE FILE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar para qué sirve la clase `File`.
> > - [ ] Documentar como importar la clase `File`.
> > - [ ] Documentar métodos de la clase `File`.

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
%%
No sé del todo como funciona esto.
- `isHidden`: Devuelve un valor [booleano](java_variable.md#BOOLEAN) indicado si el archivo o directorio está oculto.
%%
