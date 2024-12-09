---
author: Mindusting
corrected: false
tags:
  - Programming/C
title: C
alias: EL LENGUAJE DE PROGRAMACIÓN C
---

<h1 style="text-align:center;color:#888;">EL LENGUAJE DE PROGRAMACIÓN C</h1>

![#logo](../img/c_logo.png)

---

# C

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtube.com/playlist?list=PLZPZq0r_RZOOzY_vR4zJM32SqsSInGMwe&si=pHjRGW8tcjLduB9E)

## ÍNDICE

- [ARCHIVOS DE C](c_file.md)
- [COMENTARIOS](c_comment.md)
- [ESTRUCTURA BÁSICA](c_basic_structure.md)
- [VARIABLES](c_variable.md)
- [ARRAYS](c_array.md)
- [POINTERS](c_pointer.md)

## USO DE VARIBLES Y FORMATERO DE STRING

```c
#include <stdio.h>

int main()
{
    int age = 18;
    float height = 1.75;
    char chr = 'C';
    char name[] = "Mindusting";

    printf("Tu nombre es %s.\n", name);           // String
    printf("Tienes %d años.\n", age);             // Decimal
    printf("Mides %.2f metros.\n", height);       // Float
    printf("Tu lenguage favorito es %c.\n", chr); // Char

    return 0;
}
```

## TIPOS DE VARIBLES

Una variable puede ser `const`.

Las variables pueden ser `unsigned`.

Las variables `char` se pueden usar tanto como un número o un caracter (`%d` or `%c`).
Los Strings no exsiten, en cambio tenemos los array(s) de char (`%s`).

Las varibles `bool` son la booleanas (`%d`).

Los enteros cortos son `short int` o `sort` (`%d`).

Los valores enteros son `long int` o `int` (`%d` or `%u`).

Los valores largos son `long long int` o `long long` (`%lld` or `%llu`)

Los valores decimales son `float` (`%f`).

Los valores decimales son `double` (`%lf`).

### PRINT FORMAT

- <https://youtu.be/iLZOL-hmr7M?list=PLZPZq0r_RZOOzY_vR4zJM32SqsSInGMwe>

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char name[32];

    printf("Escribe tu nombre: ");
    // fgets(name, 32, stdin)
    // name[strlen(name) - 1] = '\0'

    scanf("%s", &name);

    printf("Hola %s.\n", name);

    return 0;
}
```
