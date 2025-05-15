---
author: Mindusting
corrected: false
tags:
  - Programming/C
title: Función MAIN en C
---

# FUNCIÓN MAIN EN C

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Añadir enlace al apartado "int" en el tercer párrafo.

> [!faq]- FAQ
> - [¿Qué es una función en programación?](../pc/pc_function.md)

La [función](../pc/pc_function.md) main en es una especie de [función](../pc/pc_function.md) comodín, ya que esta es la primera que empezara a funcionar cuando ejecutemos nuestro programa.

Nuestra primera [función](../pc/pc_function.md) main funcional se tiene que ver así:

```c
int main()
{
    return 0;
}
```

Esta [función](../pc/pc_function.md) como se puede ver en el ejemplo devuelve un `int`, esta es usada para indicar si ha ocurrido un problema en la ejecución, para indicar que no ha ocurrido ninguno se devuelve un `0`, de ahí que al final de esta nos encontremos con la instrucción `return 0;`, indicado así que si se llega a ese puto del programa, este ha terminado sin problemas.

---

Si queremos hacer que nuestro programa funcione tendremos que escribir nuestro código entre las *llaves* (`{}`) y por encima del `return 0;`.

```c
#include <stdio.h>

int main()
{
    printf("Hola mundo!\n");
    return 0;
}
```

En este ejemplo hacemos uso de la [librería `stdio`](stdio/c_stdio.md) para poder imprimir un mensaje por consola.
