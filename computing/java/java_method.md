---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Method
title: Métodos en Java
---

# MÉTODOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help]- REFERENCIAS WEB
> - [W3 (method)](https://www.w3schools.com/java/java_methods.asp)

> [!faq]- FAQ
> - [¿Qué son las funciones (*métodos*) en programación?](../pc/pc_function.md)

En Java la creación de métodos es bastante puntilloso a comparación de otros lenguajes ya que ay que tener varias cosas en cuenta a la hora de crearlos, por lo que primero veremos la sintaxis al completo y luego lo iremos desgranando para ver que implica cada cosa:

%%
SINTAXIS

[access_modifier] [<static>] [type_return] \[method_name]([args]) {
    [code_of_method]
}
%%

> [!abstract] SINTAXIS
> <span class="italic"><span class="key-word-color">[access_modifier] [static] [type_return]</span> <span class="function-color">[method_name]</span></span>(<span class="italic grey">[args]</span>) {<br><span class="transparency">····</span><span class="italic grey">[code_of_method]</span><br>}

## LO BÁSICO

Si estás viendo los métodos por primera vez, utiliza de momento siempre el atributo `public` y `static`, al igual que el siguiente ejemplo:

```java
public class MyProgram {

    public static void main(String[] args) {

        int x = 3;
        int y = 2;
        int result = add(x, y); // <-- Se llama al método "add".

        System.out.println(result);

        // Se bulve a llamar al mismo método.
        System.out.println(add(5, 7));

    public static int add(int a, int b) {
        // Este método recive dos número de tipo int,
        // luego los suma y debuelve el resultado.
        return a + b;
    }
}
```

> [!example] Ejemplo
> Este caso es un ejemplo didáctico, realmente los métodos no se usan para hacer cosa como esta en la que solo se hace una suma, se usan generalmente para cosas más complejas, de esta forma tenemos el código troceado en partes más pequeñas y manejables, además de no tener que escribir le mismo código una y otra vez, ya que podemos utilizar el mismo método una y otra vez.
>
> En este ejemplo, el [`type_return`](#TIPO%20DE%20RETORNO) es de un número de tipo [`int`](java_variable.md#INT), esto indica que en donde nosotros llamemos al método, este al terminar de ejecutarse devolverá un valor del tipo especificado, esto se explica más a fondo en el apartado de [retorno](#RETORNO).

## MODIFICADORES DE ACCESO

Los modificadores de acceso tienen el mismo uso en todos los casas, por lo que si quieres ver en qué consisten ve a la nota de *[modificadores de acceso](java_access_modifiers.md)*.

La tabla de accesos es la siguiente:

![Tabla de modificadores de acceso](java_access_modifiers.md#^access-modifiers-table)

## PROPIEDAD STATIC
Cuando indicamos que un método es *estático* (`static`) quiere decir que este va a formar parte de la *clase* por lo que no lo podremos encontrar el los *objetos* que creemos de esta.

Si quieres más información al respecto consulta la documentación de las [clases en java](java_class.md), concretamente el apartado del [`static`](java_class.md#PROPIEDAD%20STATIC).

---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar a que propiedades se pueden acceder y a cuales no.
> > - [ ] Poner ejemplos de uso.

## TIPO DE RETORNO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Cuando nosotros especificamos el tipo de *retorno* tenemos a groso modo dos posibilidades, estas son indicar que no devuelve nada o que sí devuelve algo, si queremos que no devuelva nada hacemos uso de la palabra clave `void` y si queremos que devuelva algún tipo de dato, podemos especificarlo, este último puede ser tanto primitivo como por referencia.

## ARGUMENTOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## RETORNO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
