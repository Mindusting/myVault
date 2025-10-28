---
author: Mindusting
corrected: false
tags:
  - Programming/Java/JSON
title: JSON en Java
---

# JSON EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hacer algunos ejemplos de como trabajar con datos de JSON.
> > - [ ] Hacer algunos ejemplos de como transformar de String a JSON y JSON a String.
> > - [ ] Documentar como escribir y leer archivos JSON.

> [!help]- REFERENCIAS WEB
> - [tutorialspoint](https://www.tutorialspoint.com/json/json_java_example.htm)
>
>YouTube:
> - [GOGODEV](https://youtu.be/kSmwtbRgoDs)
> - [Code With Z](https://www.youtube.com/playlist?list=PLllOizrde1zKgv8JGADBTLIdPgncEzA7f)

> [!faq]- FAQ
> - [¿Qué son los archivos JSON?](../../../../dump/json.md)

## DESCARGA DE LA LIBRERÍA

Para poder usar la librería necesaria para poder trabajar con [JSON](../../../../dump/json.md), tendremos que ir a la [página oficial](https://mvnrepository.com/artifact/com.googlecode.json-simple/json-simple) en donde podremos ver las lista de las diferentes versiones y elegiremos la que necesitemos (*generalmente la más moderna; siendo esta en el día en el que se escribe esta documentación la [`1.1.1`](https://repo1.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.jar)*), entramos en el enlace de la versión y en el apartado de ficheros (*Files*), encontraremos la opción [`.jar`](../../java_jar.md) o en caso de que no lo veamos debería haber una opción **ver todo** (*View all*), ahí podremos buscar el [`.jar`](../../java_jar.md).

## IMPORTAR CLASES

Para poder importar a nuestro proyecto las [clases](../../java_class.md) que se encuentran dentro del [`.jar`](../../java_jar.md) tendremos que acceder al siguiente paquete:

```java
import org.json.*;
```

Pudiendo sustituir el **asterisco** (`*`) por cualquiera de las siguientes [clases](../../java_class.md):

- [JSONArray](java_json_jsonarray.md)
- [JSONObject](java_json_jsonobject.md)
