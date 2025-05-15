---
author: Mindusting
corrected: false
tags:
  - Programming/C/Variable
title: Variables en C
---

# VARIABLES EN C

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtu.be/aIQk1O08zpg)

> [!faq]- FAQ
> - [¿Qué son las variables en programación?](../pc/pc_variable.md)

**C** es un lenguaje de tipado fuerte, esto quiere decir que cuando declaramos una **variable**, debemos indicar el tipo de valor que va a almacenar y este no se podrá cambiar en el transcurso del programa, los tipos son los siguientes:

| TYPE    | NAME        | SIZE IN BYTES |
|:------- |:----------- |:------------- |
| Integer | char        | 1             |
| Integer | short       | 2             |
| Integer | int         | 2 or 4        |
| Integer | long        | 8             |
| Decimal | float       | 4             |
| Decimal | double      | 8             |
| Decimal | long double | 16            |

%%
SINTAXIS

```c
[variable_type] [variable_name];
[variable_type] [variable_name] = [value];
```
%%

> [!abstract] SINTAXIS
> <span class="italic key-word-color">[variable_type]</span><span class="italic variable-color">[variable_name]</span>;
> <span class="italic key-word-color">[variable_type]</span><span class="italic variable-color">[variable_name]</span> = <span class="italic grey">[value]</span>;
