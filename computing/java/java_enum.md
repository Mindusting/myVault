---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Enum en Java
---

# ENUM EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools (Enum)](https://www.w3schools.com/java/java_enums.asp)
> - [W3 Schools (Enum constructor)](https://www.w3schools.com/java/java_enum_constructor.asp)

```java
enum Mode {
    READ,
    WRITE
}

public class EnumMain {
    public static void main(String[] args) {
        Mode mode = Mode.READ;

        System.out.println(mode);
        System.out.println(Mode.WRITE);
    }
}
```
