---
author: Mindusting
corrected: false
tags:
  - Programming/Java/JSON
title: JSON en Java
---

# JSON

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [tutorialspoint](https://www.tutorialspoint.com/json/json_java_example.htm)
>
>YouTube:
> - [GOGODEV](https://youtu.be/kSmwtbRgoDs)
> - [Code With Z](https://www.youtube.com/playlist?list=PLllOizrde1zKgv8JGADBTLIdPgncEzA7f)

> [!faq] FAQ
> - [¿Qué son los archivos JSON?](../dump/json.md)

| JSON       | Java              |
|:---------- |:----------------- |
| string     | java.lang.String  |
| number     | java.lang.Number  |
| true/false | java.lang.Boolean |
| null       | null              |
| array      | java.util.List    |
| object     | java.util.Map     |

## ARRAY

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```java
import org.json.simple.JSONArray;

public class JSON {

    public static void main(String[] args) {

        JSONArray jsonArray = new JSONArray();

        jsonArray.add("Adelio");
        jsonArray.add("Adelia");

        System.out.println(jsonArray);
    }
}
```

### MÉTODOS DEL ARRAY

- **add(*\[obj]*)**: Añade al final del array el **objeto** indicado.
- **add(*\[index]*, *\[obj]*)**: Añade en el **índice** indicado el nuevo **objeto**.
- **addFirst(*\[obj]*)**: Añade al principio del array el elemento indicado.
- **addLast(*\[obj]*)**: Añade al final del array el **objeto** indicado.
- **get(*\[index]*)**: Devuelve el **objeto** situado en el **índice** indicado.
- **getFirst()**: Devuelve el **objeto** situado en la primera posición del array.
- **getLast()**: Devuelve el **objeto** situado en la última posición del array.
- **remove(*\[index]*)**: Borra del array el **objeto** con el **índice** indicado.
- **remove(*\[obj]*)**: Borra del array el **objeto** el objeto indicado.
- **removeFirst()**: Borra del array el primer **objeto**.
- **removeLast()**: Borra del array el último **objeto**.
- **indexOf(*\[obj]*)**: Devuelve el **índice** del **objeto** indicado.
- **isEmpty()**: Devuelve un valor **booleano** indicando si el array está bacío.
- **lastIndexOf(*\[obj]*)**: Devuelve el **índice** del último **objeto** especificado.
- **size()**: Devuelve el número de **elementos** en el array.
- **toString()**: Devuelve un `String` con el contenido del array en formato JSON.


## OBJETOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```java
import org.json.simple.JSONObject;

public class JSON {

    public static void main(String[] args) {

        JSONObject jsonObj = new JSONObject();

        jsonObj.put("Adelio", 22);
        jsonObj.put("Adelia", 20);

        system.out.println(jsonobj.get("Adelio"));
        system.out.println(jsonobj.get("Adelia"));
    }
}
```

### MÉTODOS DEL OBJETO

- **put(*\[key]*, *\[value]*)**: Añade al **objeto** el par de **clave** y **valor** indicado.
- **get(*\[key]*)**: Devuelve el **valor** de la **clave** indicada.
- **remove(*\[key]*)**: Borra el par de **clave** y **valor**, con la **clave** especificada.
- **replace(*\[key]*, *\[new_value]*)**: Remplaza el **valor** de la **clave** especificada.
- **keySet()**: Devuelve un **set** con todas las **claves** del **objeto**.
- **values()**: Devuelve una **colección** con los valores del **objeto**.
- **size()**: Devuelve un `int` indicando el número de pares del **objeto**.
- **isEmpty()**: Devuelve un `booleano` indicando si está vacío o no.

## PARSER

```java
package JSON;

import java.util.Objects;

//import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class MainJSON {
    
    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        
        // https://www.tutorialspoint.com/json/json_java_example.html
    
        String jsonString = "{\"a\":3}";
        
        JSONObject jsonObj = new JSONObject();
        
        try {
            jsonObj = (JSONObject)(new JSONParser()).parse(jsonString);
        } catch (ParseException ex) {
            System.out.println("Ocurrio un error en el parse.");
        }
        
        jsonObj.put("Adelio", 22);
        jsonObj.put("Adelia", 20);

        System.out.println(jsonObj.get("Adelio"));
        System.out.println(jsonObj.get("Adelia"));
        
        System.out.println(jsonObj.toString());
        
        System.out.println(Objects.hash(""));
    }
}
```
