---
author: Mindusting
corrected: false
tags:
  - Programming/JavaScript/Variable
title: Variables en JS
---

# VARIABLES IN JS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar `var`.
> > - [ ] Documentar `const`.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/js/js_variables.asp)

> [!faq]- FAQ
> - [¿Qué son las variables en programación?](../pc/pc_variable.md)

## DECLARAR VARIABLES

> [!abstract] SINTAXIS
> ***[\[keyWord\]](#^table-var-key-word) \[varName\]\{ \= \[value\]\};***

| KEY WORD | DESCRIPCIÓN                      |
|:-------- |:-------------------------------- |
| `var`    | Global (*antigua; fuera de uso*) |
| `let`    | Local                            |
| `conts`  | Constante                        |
^table-var-key-word

- `let`: es para declarar **variables** locales del ámbito en el que son declaradas.
- `var`: es para declarar **variables** globales, pudiendo acceder a ellas desde cualquier parte del código.
- `cont`: es para declarar **variables** constantes (*no se pueden modificar una vez declaradas*).

> [!abstract] SINTAXIS
> 
