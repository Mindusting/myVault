---
author: Mindusting
corrected: false
tags:
  - Programming/TypeScript
title: TypeScript
---

# VARIABLES EN TYPESCRIPT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué son las variables en programación?](../pc/pc.md)

> [!abstract] SINTAXIS
> let ***\[var\_name\]***: [***\[data\_type\]***](#TIPOS%20DE%20DATOS) = ***\[value\]***;

## TIPOS DE DATOS

El tipo de dato de una **variable** indica que es capaz de guardar la **variable** en cuestión; existen diferentes tipos de datos y estos mismos se pueden agrupar en diferentes categorías:

- [BÁSICOS](#TIPOS%20DE%20DATOS%20BÁSICOS)
- [ARRAYS](ts_array.md)
- [ENUM](ts_enum.md)
- [INTERFACES](ts_interface.md)
- [CLASES Y OBJETOS](ts_class.md)

### TIPOS DE DATOS BÁSICOS

- `boolean`:
    Las **variables** de tipo `boolean` son capaces de guardar un valor entre *verdadero* (*`true`*) y *falso* (*`false`*).
- `number`:
    Las **variables** de tipo `number` son capaces de guardar tanto números ente como decimales.
- `string`:
    Las **variables** de tipo `string` (*cadena*) son capaces de guardar *cadenas de caracteres* (*texto*).

## OPCIONALES

%% También conocidos como nulables %%

```ts
let name?;
```

## ALIAS DE TIPOS

```ts
type ID = string | number;
```

## GENÉRICOS

```ts
function fun<T>(valor: T): T {
    return valor;
}

fun<number>(1);
```

## TIPOS UNIÓN

```ts
let x: string | number = 42;
// Puede ser de los dos tipos.
```

## LITERALES

```ts
let x: "N" | "O" | "S" | "E" = "N";
```
