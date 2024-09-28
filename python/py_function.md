---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Function
title: Funciones de Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

[Functions_Decorators](functions/Functions_Decorators.md)

# FUNCIONES 📞

Una función `encapsula` el código que se encuentra en su sangría, haciendo que este solo se ejecute cuando llamemos a la función en cuestión.

Cabe resaltar que dependiendo del contexto se el da un nombre distinto, estos pueden ser los siguientes:

- Procedimiento: Es el nombre que se le da a un conjunto de instrucciones “encapsuladas”.

- Función: Es un procedimiento el cual devuelve a la llamada de la función un valor.

- Método: Puede ser un procedimiento o una función, su característica distintiva es que forma parte de una [clase](py_class.md).

En cualquier caso, se suele usar “Función” o “Método”, al proceso de “encapsular” código.

Para poder crear un procedimiento se hace uso de la palabra clave `def` seguida del nombre que queramos darle al procedimiento, unos paréntesis indicando entre ellos los argumentos y por último dos puntos, a partir de ese punto, todo lo que metamos en su sangría formará parte del procedimiento.

%%
SINTAXIS

```py
def [func_name]([args]):
    [func_code]
```
%%

>[!abstract] SINTAXIS
> <span class="key-word-color">def</span> <span class="italic function-color">[func_name]</span>(<span class="italic variable-color">[args]</span>):<br><span class="transparency">····</span><span class="italic grey">[func_code]</span>

```py
def func():
    pass
```

```py
# Declaración del procedimiento
# (Sin métodos)
def mi_proce1():
    print("Este es mi procedimiento.")


# Llamada al procedimiento
mi_proce1()

# Declaración del procedimiento
# (Con métodos)
def mi_proce2(name):
    print(f"Hola {name}.")
    # Llamada al procedimiento


mi_proce2("Mindusting")
```

Como se puede ver en el ejemplo primero se declara el procedimiento haciendo uso de la palabra clave `def`, justo debajo de él, dentro de su sangría, indicamos que queremos que se ejecute al llamar al procedimiento, en este caso es simplemente un [`print`](py_print.md).

Los argumentos no son necesarios, pero el usarlos nos puede dar la libertad de hacer cosas más interesantes, en el ejemplo, el primer argumentos es una [variable](py_variable.md) con el nombre `name`, por lo que este procedimiento requiere que le pasemos el valor del argumento en la llamada, como se puede ver en el propio ejemplo, siendo este el valor `Mindusting`.

---

Un argumentos puede ser pre definido para que en caso de que no se introduzca ningún valor, adquiera el predefinido, en el siguiente ejemplo se puede ver como hacerlo.

```py
# Declaración del procedimiento
# (Con argumentos pre definidos)
def saludo(name = None):
    if name == None:
        print("Hola.")
    else:
        print(f"Hola {name}.")


# Llamada al procedimiento
# (Con y sin argumentos)
saludo("Mindusting")
saludo()
```

---

También se puede indicar el tipo de dato que se debe introducir, esto es para que los programadores que estén viendo el código de programa puedan saber el tipo de dato que se debe introducir en cada argumento, de esta forma no hace falta que mire el código para saber el tipo de dato que debe introducir en cada argumento.

```py
from math import sqrt


# Calculate distance
def cal_dis(dis_x: float = 0, dis_y: float = 0):
    return sqrt((dis_x ** 2) + (dis_y ** 2))


print(cal_dis(3, 4))
# SALIDA:
# 5
```

---

[\*Args and \*\*Kwargs in Python](https://youtu.be/4jBJhCaNrWU)

Si quisiéramos que se pudiera poner en la llamada todos los valores que queramos, como argumento se puede poner un (\*\[nom. argumento\]), provocando que convierta todos los valores introducidos en la llamada en una [tupla](collections/Collections_tuple.md), en cualquier caso, también se puede poner un solo argumento y en la llamada indicar múltiples valores en forma de [collection](py_data_structure.md).

**Ej. 1:**
```py
# Declaración del procedimiento
def mi_proce(*x):
    print(x)



# Llamada al procedimiento
mi_proce("Mindusting", 32, 3.141592, False)
```

**Ej. 2:**
```py
# Declaración del procedimiento
def mi_proce(x):
    print(x)


# Llamada al procedimiento
mi_proce(["Mindusting", 32, 3.141592, False])
```

También existe la posibilidad de hacerlo de forma que en vez de una [tupla](collections/Collections_tuple.md) como es el caso del primer ejemplo anterior en el que se hacía uso del asterisco (`*`), se cree un [diccionario](collections/py_dict.md), para ello simplemente se debe escribir dos asteriscos (`*`).

```py
# Mi método
def mi_met(**x):
    # Impresión del "dict"
    print(x)


# Llamada al método
mi_met(name = "Mindusting", age = 18)
```

---

Si quisiéramos crear una función sería siguiendo la misma estructura que la del procedimiento, pero haciendo uso de la palabra clave “return” dentro de su sangría para devolver un valor a la llamada del método.

```py
# Declaración de la variable PI
PI = 3.141592

# Declaración del método
def perimetro(radio):
    return 2 * radio * PI


# Llamada al método
print( perimetro(5) )
```

Como se puede ver en este ejemplo, se mete la llamada al método dentro del [método print](py_print.md) ya que tras calcular el perímetro, devuelve el resultado al mismo punto donde se hizo la llamada al método.

## GENERADORES 🔩

![Generadores](functions/Functions_Generators.md)

## FUNCIONES LAMBDA

![Función Lambda](functions/Functions_Lambda.md)
