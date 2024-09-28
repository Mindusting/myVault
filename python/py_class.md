---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Class
title: Clases y Ojetos en Python
---

<h1 style="text-align:center;">CLASES EN PYTHON</h1>

---

[¿Qué son las clases y objetos en programación?](../pc/pc_class.md)

# VÍDEOS

- [Curso de Python. POO I. Vídeo 24](https://youtu.be/5Ohme4A2Weg?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)
- [Curso de Python. POO II. Vídeo 25](https://youtu.be/2UNrSiKEI8w?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

# CLASES Y OBJETOS 📦

Para crear una clase en Python se usa la palabra clave `class` siguiendo la siguiente sintaxis.

%%
SINTAXIS

```py
class [class_name]:
    [class_code]
```
%%

>[!abstract] SINTAXIS
><span class="key-word-color">class</span> <span class="italic class-color">[class_name]</span>:<br><span class="transparency">····</span><span class="italic grey">[class_code]</span>

Para empezar podemos crear una clase llamada `Numeros` y esta tendrá tres **propiedades** (`PI`, `E` y `AUREO`), después de declararla accedemos a sus **propiedades** mediante la metodología del punto, para imprimir los valores de estos:

```py
# Declaración de la clase
class Numeros:
    PI:    float = 3.141592653589793
    E:     float = 2.718281828459045
    AUREO: float = 1.618033988749895

# Consulta de las propiedades
print(Numeros.PI)
print(Numeros.E)
print(Numeros.AUREO)
# SALIDA:
# 3.141592653589793
# 2.718281828459045
# 1.618033988749895
```

Ahora, estos atributos no pueden ser modificados (*En este caso no interesa ya que son constantes, pero si se podrían modificar, no obstante, más adelante veremos como evitar que se puedan modificar*) ya que forman parte de la clase, si queremos poder modificar los valores tendremos que **instanciar** la clase para crear un **objeto**, esto lo veremos con el ejemplo de un [vector](../math/Vectors/vectors.md):

```py
# Declaración de la clase
class Vector:
    x: float = 0.0
    y: float = 0.0

# Instanciación de la clase
v = Vector()

# Modificación de los
# valores de las
# propiedades
v.x = 3.0
v.y = 4.0

# Consulta de las propiedades
print(v.x)
print(v.y)
# SALIDA:
# 3.0
# 4.0
```

En este ejemplo podemos ver como se declara la clase y se instancia, para ello se le llama a la clase seguida de dos paréntesis, el resultado de esto es un objeto de la clase `Vector` y lo guardamos en la [variable](py_variable.md) `v`, después de esto, como se puede ver se llama a las **propiedades** de este objeto y se le asignan sus nuevos valores, finalmente comprobamos la aplicación de los cambios a las **propiedades** imprimiendo el resultado de sus consultas.

> [!info]- EQUIVALENCIA EN OTRO LENGUAJE
> Si bienes de otro lenguaje, para qué sepas, la línea:
> ```py
> v = Vector()
> ```
> Sería el equivalente en [Java](../java/java.md) a:
> ```java
> Vector v = new Vector();
> ```

Una vez has aprendido lo básico sobre las clases y objetos, puedes empezar con los siguientes apartados:

- [MÉTODOS 📞](classes/py_method.md)
    - [CONSTRUCTOR 👷](classes/Magic_Methods/py_constructor.md)
- [ENCAPSULACIÓN 💊](classes/py_encapsulation.md)
- [HERENCIA 🧓](classes/py_inheritance.md)

>[!warning] ESTE APARTADO ES TEMPORAL, EL CONTENIDO DE ESTE SE MOVERÁ A UN SITIO MÁS INDICADO EN EL FUTURO
>
> # INSTANCIAS
>
> Para poder comprobar si un objeto es una instancia de una clase se usa la [función](py_function.md) `isinstance`:
>
> ```py
> print(isinstance(3.14, float))
> ```
>
> Como se puede ver en este ejemplo, el primer argumento debe ser el objeto, mientras que el segundo debe ser la clase con la que queremos compararlo, también existe la posibilidad de pasar como segundo argumento una [tupla](collections/Collections_tuple.md) con las clases con las que queremos hacer la comparación:
>
> ```py
> print(isinstance(3.14, (int, str, bool)))
> ```

>[!warning] ESTE APARTADO ES TEMPORAL, EL CONTENIDO DE ESTE SE MOVERÁ A UN SITIO MÁS INDICADO EN EL FUTURO
>
> # AÑADIR ATRIBUTOS
> 
> Para poder añadir atributos nuevos a una clase se puede usar la función `setattr`:
> ```py
> setattr([obj], [attr_name], [attr_value])
> ```
> 
> # QUITAR ATRIBUTOS
> 
> Para poder quitar atributos a una clase se puede usar la función `delattr`:
> ```py
> delattr([obj], [attr_name])
> ```
