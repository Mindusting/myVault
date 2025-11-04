---
author: Mindusting
corrected: false
tags:
  - Programming/TypeScript
title: Enumeradores en TypeScript
---

# ENUMERADORES EN TYPESCRIPT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Chequear que el código funciona.
> > - [ ] Explicar como darle los valores queramos.
> > - [ ] Documentar los valores personalizados.

> [!help]- REFERENCIAS WEB
> - [W3 Schools (Enum)](https://www.w3schools.com/typescript/typescript_enums.php)

> [!faq]- FAQ
> - [¿Qué son los enumeradores en programación?](../pc/pc_enum.md)

Para crear un **enumerador** en **TypeScript** se usa la *palabra clave* `enum` seguida del nombre que le daremos a el **enumerador** en cuestión y finalmente unas llaves (`{}`), entre las que pondremos los distintos valores que queremos que conformen la **enumeración** separados por comas.

> [!abstract] SINTAXIS
> enum ***\[enum\_name\]*** {***\[values\]***}

Imaginemos que queremos hacer que un pedido pueda tener tres estados concretos, una solución puede ser usar un `enum` con los distintos estado:

```ts
// Estado del pedido
enum OrderState {
    InQueue,        // En cola
    InDistribution, // En reparto
    Delivered       // Entregado
}

let ordreState: OrderState = OrderState.InQueue;
```

Más adelante, se podría usar las [**clases**](ts_class.md) para crear la entidad de `Order` la cual podrá tener una propiedad que sea el estado:

```ts
class Order {
    id: number;
    state: OrderState;
    
    constructor(id: number, state: OrderState) {
        this.id    = id;
        this.state = state;
    }
}

let orders: Order[] = {
    Oder(1, OrderState.InDistribution),
    Oder(2, OrderState.InQueue)
};
```

## VALORES PERSONALIZADOS

```ts
enum Rol {
    Admin    = "ADMIN",
    Usuario  = "USUARIO",
    Invitado = "INVITADO"
}

console.log(Rol.Admin);
// SALIDA:
// ADMIN
```
