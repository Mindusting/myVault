---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Variable
title: Variables en Java
---

<h1 align="center">VARIABLES EN JAVA</h1>

---

# VAIRABLES

Una variable permite almacenar información para poder usarla en el futuro, en Java, las variables tienen diferentes **tipos** estos dependerán del contenido que queramos guardar en ella.

> [!note]- Nota para usuarios que programan en otros lenguajes:
> Java por defecto no tiene variables de tipo `unsigned` como puede ser el caso de [`C`](../c/c.md) o [`C++`](../cpp/cpp.md).

%%
SINTAXIS

[accessModifier] [final] [dataType] [name] = [value];
%%

> [!abstract] SINTAXIS
> 

## TIPOS DE VARIABLES

https://youtu.be/xk4_1vDrzzo?t=7158

| TIPO    | ESPACIO        | PRIM/REFE  | RANGO DE VALORES                 |
| ------- | -------------- | ---------- | -------------------------------- |
| boolean | 1 byte (1 bit) | Primitivo  | true o false                     |
| byte    | 1 byte         | Primitivo  | -128 a 127                       |
| short   | 2 bytes        | Primitivo  | -32.768 a 32.767                 |
| int     | 4 bytes        | Primitivo  | -2 mil millones a 2 mil millones |
| long    | 8 bytes        | Primitivo  | -9 trillones a 9 trillones       |
| float   | 4 bytes        | Primitivo  | Núm. frac. de 7 díg. decimales   |
| double  | 8 bytes        | Primitivo  | Núm. frac. de 16 díg. decimales  |
| char    | 2 bytes        | Primitivo  | Un carácter de unicode           |
| String  | 2 bytes * char | Referencia | Una cadena de caracteres         |

| PRIMITIVO                    | REFERENCIA                   |
| ---------------------------- | ---------------------------- |
| 8 types (boolean, byte, ...) | Unlimited (user defined)     |
| Stores data                  | Stores an address            |
| Can only hold 1 value        | Could hold more than 1 value |
| Less memory                  | More memory                  |
| Fast                         | Slower                       |

> [!faq] PREGUNTAS FRECUENTES
> - [¿Qué diferencia hay entre `float` y `double`?](https://www.javatpoint.com/float-vs-double-java)

### PRIMITIVO

Los datos de tipo primitivo son simples  y veloces

En Java existen ocho tipos de datos **primitivos**, estos guardan un valor, usan menos memoria y son más rápidos.

#### BOOLEAN

Las variables **booleanas** pueden almacenar uno de dos valores *verdadero* o *falso*.

```java
public class BooleanVariables {
    public static void main(String[] args) {
        boolean myBooleanVar = true;
        System.out.println(myBooleanVar);
    }
}
```

Al trabajar con este tipo de variables nos puede interesar los siguientes comparadores:
- [Operadores de comparación](<java_operators.md# OPERADORES DE COMPARACIÓN>).
- [Operadores lógicos](<java_operators.md# OPERADORES LÓGICOS>).

#### BYTE

Las variables **byte** pueden almacenar un número entero entre [**\[-128, 127\]**](../math/math_range_notation.md), esto es debido a que usa **un byte** de memoria.

```java
public class ByteVariables {
    public static void main(String[] args) {
        byte number1 = 2;
        byte number2 = 3;
        System.out.println(number1 + number2);
    }
}
```

#### SHORT

Las variables **short** pueden almacenar un número entero entre [**\[-32.768, 32.767\]**](../math/math_range_notation.md), esto es debido a que usa **dos bytes** de memoria.

```java
public class ShortVariables {
    public static void main(String[] args) {
        short number1 = 2;
        short number2 = 3;
        System.out.println(number1 + number2);
    }
}
```

#### INT

Las variables **int** (*Esta es la más usada para trabajar con números enteros*) pueden almacenar un número entero entre [**\[-2.147.483.648, 2.147.483.647\]**](../math/math_range_notation.md), esto es debido a que usa **cuatro bytes** de memoria.

```java
public class IntVariables {
    public static void main(String[] args) {
        int number1 = 2;
        int number2 = 3;
        System.out.println(number1 + number2);
    }
}
```

#### LONG

Las variables **long** pueden almacenar un número entero entre [**\[-9.223.372.036.854.775.808, 9.223.372.036.854.775.807\]**](../math/math_range_notation.md), esto es debido a que usa **ocho bytes** de memoria.

```java
public class LongVariables {
    public static void main(String[] args) {
        long number1 = 2L;
        long number2 = 3L;
        System.out.println(number1 + number2);
    }
}
```

Como se puede ver en los ejemplos, las variables de tipo `long` al ser inicializadas, debemos indicar en el número que es de tipo `long` añadiendo una `L` al final del número.

#### FLOAT

Las variables **float** siguen el estándar de [coma flotante](https://en.wikipedia.org/wiki/Floating-point_arithmetic), su rango es [**\[3.4e-038, 3.4e+038\]**](../math/math_range_notation.md), esto es debido a que usa **cuatro bytes** de memoria.

```java
public class FloatVariables {
    public static void main(String[] args) {
        float number1 = 3.141592F;
        float number2 = 1.618034F;
        System.out.println(number1 + number2);
    }
}
```

Como se puede ver en los ejemplos, las variables de tipo `float` al ser inicializadas, debemos indicar en el número que es de tipo `float` añadiendo una `F` al final del número.

#### DOUBLE

Las variables **double** (*Esta es la más usada para trabajar con números decimales*) siguen el estándar de [coma flotante](https://en.wikipedia.org/wiki/Floating-point_arithmetic), su rango es [**\[1.7e-308, 1.7e+308\]**](../math/math_range_notation.md), esto es debido a que usa **cuatro bytes** de memoria.

```java
public class DoubleVariables {
    public static void main(String[] args) {
        double number1 = 3.141592D;
        double number2 = 1.618034D;
        System.out.println(number1 + number2);
    }
}
```
 Como se puede ver en los ejemplos, las variables de tipo `double` al ser inicializadas, debemos indicar en el número que es de tipo `double` añadiendo una `D` al final del número.

#### CHAR

Las variables de tipo **char** almacenan un solo carácter, siguiendo el estándar [unicode](https://home.unicode.org/), por lo que este tipo de variables usan **dos bytes** de memoria.

```java
public class CharVariables {
    public static void main(String[] args) {
        char myChar = 'J';
        System.out.println(myChar);
    }
}
```

Nota que al la hora de inicializar la variable, el carácter asignado se ha especificado entre comillas simples, esto es obligatorio hacer de esta manera.

### REFERENCIA

En Java no existen límites en los tipos de **referencia**, esto es por que internamente son una dirección de memoria, la cual apunto a un [objeto](java_class.md) (*Los objetos son algo más avanzado, por lo que de momento no tienes por qué saber que son*), por tanto, esta clase de variables son capaces de guardar varios valores, usan más memoria y son más lentos.

#### STRING

Para poder guardar un texto y poder trabajar sobre el de forma sencilla existen las variables de tipo `String`, estas en esencia son un [objeto](java_class.md) el cual guarda un [array](java_array.md) de tipo [char](<# CHAR>), junto a algunos métodos que nos permite el fácil manejo de la información que queramos meter.

```java
public class CharVariables {
    public static void main(String[] args) {
        String myString = "Este es el texto está guardado en mi programa.";
        System.out.println(myString);
    }
}
```

## MODIFICADORES DE ACCESO

Los [modificadores de acceso](java_access_modifiers.md) se pueden usar en las variables, esto permite indicar desde donde 

![tabla de modificadores de acceso](<java_access_modifiers.md#^access-modifiers-table>)
