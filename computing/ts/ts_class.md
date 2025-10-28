---
author: Mindusting
corrected: false
tags:
  - Programming/TypeScript
title: Clases en TypeScript
---

# CLASES EN TYPESCRIPT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## HERENCIA

```ts
class Animal {
    constructor(public nombre: string) {}
    
    hablar(): void {
        console.log(`${this.nombre} hace un sonido`)
    }
}

class Perro extends Animal {
    hablar(): void {
        console.log(`${this.nombre} ladra`)
    }
}

let p = new Perro("Rex");
p.hablar();
// SALIDA:
// Rex ladra
```

## MODIFICADORES DE ACCESO

- `public`: accesible en todas partes.
- `private`: solo dentro de la clase.
- `protected`: accesible en la clase y subclase.

```ts
class Cuenta {
    private saldo: number = 0;
    
    addSaldo(cantidad: number) {
        this.saldo += cantidad;
    }
    
    getSaldo() {
        return this.saldo;
    }
}

let c = new Cuenta();
c.addSaldo(100);
console.log(c.getSaldo());
// SALIDA:
// 100

//console.log(c.saldo);
// ERROR
```

## ASERCIONES DE TIPO

```ts
let valor: any = "Hola mundo!";
let long: number = (valor as string).length;

console.log(long);
// SALIDA:
// 12
```

## UTILIDADES

`Partial` combierte todas las propiedades en opcionales.

```ts
interface User {
    id: number;
    name: string;
}

let u = Partial<User> = {}; // Usuario vacio.
```

`Readonly` hace que todas las propiedades sean de solo lectura.

```ts
interface User {
    id: number;
    name: string;
}

let u = Readonly<User> = {id: 1}; // Error
```