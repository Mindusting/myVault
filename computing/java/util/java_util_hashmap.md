---
author: Mindusting
corrected: false
tags:
  - Programming/Java/HashMap
title: Hash-Map en Java
---

# HASHMAP EN JAVA

> [!fail]- ESTE PARATADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 (Hash Map)](https://www.w3schools.com/java/java_hashmap.asp)

> [!faq]- FAQ
> - [¿Qué son los Hash-Map en programación?](../../pc/pc_hash_map.md)

Para crear un `HashMap` en Java, tendremos que importar la clase desde el paquete `java.util`.

```java
import java.util.HashMap;
```

```java
import java.util.HashMap;

public class HashMapFile {
    public static void main(String[] args) {
        HashMap<String, Integer> hp = new HashMap<>();

        hp.put("Mindusting", 18);

        System.out.println(hp);
    }
}
```

## MÉTODOS

- put(*\[key]*, *\[value]*):
    Añade un nuevo par (`key`, `value`), si la llave (`key`), ya existe en el `HashMap`, sobrescribe el valor (`value`) indicado.
<br>
- get(*\[key]*) -> *\[value]*
    Devuelve el valor relacionado a la llave (`key`) especificada.
    Si la llave especificada, no tiene un valor asociado, devuelve `null`.
<br>
- size():
    Devuelve un `int` indicando el número de pares (`key`, `value`).
<br>
- containsKey(*\[key]*) -> *\[boolean]*:
    Devuelve un valor `booleano` indicando si la llave (`key`) indicada existe dentro del `HashMap`.
<br>
- containsValue(*\[value]*) -> *\[boolean]*:
    Devuelve un valor `booleano` indicando si el valor (`value`) indicada existe dentro del `HashMap`.
<br>
- replace(*\[key]*, *\[new_value]*):
    Si dentro del `HashMap` existe la llave (`key`), el valor (`value`) relacionada a esta se remplaza por el valor indicado.
<br>
- putIfAbsent(*\[key]*, *\[value]*):
    Si la llave (`key`) indicada, no existen en el `HashMap`, se introduce el nuevo par (`key`, `value`) en el `HashMap`, de lo contrario, no hace nada.
<br>
- remove(*\[key]*):
    Borra del `HashMap` el par (`key`, `value`) que coincida con la llave (`key`) indicada.
<br>
- clear():
    > [!fail]- ESTE PARATADO ESTÁ INCOMPLETO
    > > [!todo] #TODO
