---
author: Mindusting
collaborators:
  - Anonymous
corrected: false
tags:
  - DB
title: Bases de datos
---

# Tema 2: Diseño conceptual de DDBB

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## 2.1 Introducción

El modelo de diseño de **DDBB** más usado a día de hoy es el de **Entidad-Relación** (*E-R*), este modelo fue propuesto por Peter Chen en 1976. Posteriormente otros autores fueron añadiendo cambios, por lo que primero veremos el modelo básico y luego iremos viendo los cambios.

## 2.2 El modelo E-R básico

Los elementos básicos son:
- Entidades.
- Dominios (*Valores permitidos en un campo*).
- Atributos.
- Relaciones.

### 2.2.1 Entidad

Una entidad es cualquier objeto sobre el que queremos guardar información. Si quisiéramos una **DDBB** para gestionar la información de una biblioteca, las entidades podrían ser:

- Libros.
- Autores.
- Editoriales.
- Etc.

Se llama *ocurrencia* a cada registro guardado en una *entidad*, por ejemplo, el libro "*Don quijote*" podría ser una ocurrencia de la entidad "*Libros*".

Una entidad es representada con un rectángulo, dentro de este pondremos el nombre de la entidad.

![#center](figuras/DDBB_Tema_2_figura_1.md)

### 2.2.2 Relación

Una relación se puede definir como una asociación entre entidades. Para relacionar por ejemplo la *entidad* "Empleado" con "Departamento", lo haríamos con la relación "trabaja", indicando así que el empleado trabaja en un departamento.

![#center](figuras/DDBB_Tema_2_figura_2.md)
^figura2

Las relaciones cumplen con las siguientes características:
- Nombre: toda relación debe tener un nombre único.
- Grado: hace referencia al número de entidades que participan en una relación, existen varias:
    - ==Binarias o de grado 2==: son aquellas que [relacionan a dos entidades](#^figura2).
    - ==Reflexivas o de grado 1==: Son aquellas que relacionan una entidad consigo misma.
    ^reflexiva
    
    ![#center](figuras/DDBB_Tema_2_figura_3.md)
    - ==Ternarias, cuaternarios, etc==: son de relaciones de múltiples entidades.
    ![#center](figuras/DDBB_Tema_2_figura_4.md)
    Las relaciones más habituales son las binarias, seguidas por las reflexivas y las superiores al grado 2 son muy escasas.
- ==Tipos de correspondencia==: referencia al número de ocurrencias de una entidad que pueden estar relacionadas a las ocurrencias de otra identidad, esto se suele indicar al lado del rombo (*Relación*).

    - `1:1`: ocurre cuando una ocurrencia de una entidad solo puede estar relacionada con una ocurrencia de otra entidad.
        ![#center](figuras/DDBB_Tema_2_figura_5.md)
        ![#center](figuras/DDBB_Tema_2_figura_6.md)
    - `1:N`: ocurre cuando una ocurrencia de una entidad puede estar relacionada con una o varias ocurrencias de otra entidad.
        ![#center](figuras/DDBB_Tema_2_figura_7.md)
        ![#center](figuras/DDBB_Tema_2_figura_8.md)
    - `N:M`: ocurre cuando varias ocurrencias de una entidad pueden estar relacionadas con varias ocurrencias de otra identidad.
        ![#center](figuras/DDBB_Tema_2_figura_9.md)
        ![#center](figuras/DDBB_Tema_2_figura_10.md)

^tipo-de-correspondencia

### 2.2.3 Atributos y dominios

==Atributo== se define como las características o propiedades de una entidad o relación.

> [!example] Ejemplo:
> La entidad trabajador puede tener los atributos:
> - Código de trabajador.
> - Nombre.
> - Apellidos.
> - DNI.
> - Número de teléfono.

Los ==dominios== en este contexto se refiere a las restricciones que tiene un atributo a la hora de guardar un dato, esto se refiere a que cuando vamos a guardar por ejemplo el **atributo** nombre (*texto*) indicamos que la longitud máxima es 50 caracteres, o si tenemos el **atributo** edad como un número, podremos indicar que el número tienen que estar entre 0 y 120. Estos dominios se suelen indicar junto al **atributo**.

==Tipos de atributos==:
- ==Atributo identificador candidato (*AIC*)==: es el atributo o conjunto de atributos que permite identificar inequívocamente la ocurrencia de una entidad, dependiendo del tipo puede ser *AIP* o *AIA*.
- ==Atributo identificador principal (*AIP*)==: es el atributo que permite por sí solo identificar de forma inequívoca cada ocurrencia, como puede ser el generalmente llamado atributo *ID*.
- ==Atributo identificador alternativo (*AIA*)==: esta clase de atributos suelen ser el *DNI*, ya que permite identificar las concurrencias pero no se suele usar internamente en la **DDBB** para identificarlo, si no que se suele usar para encontrarlo, no para las relaciones entre **entidades**.

Para representar los atributos en un esquema de E-R se puede hacer de las siguientes formas:

- Los atributos se indican cada uno dentro de un círculo u óvalo, subrayando con una línea continua los **AIP** y una discontinua los **AIA**.
- Si se usan círculos pequeños para indicar cada atributo se rellena de color negro el atributo **AIP** y la mitad del círculo a los **AIA**.

![#center](figuras/DDBB_Tema_2_figura_11.md)
![#center](figuras/DDBB_Tema_2_figura_12.md)

Existe un tipo de atributo especial el cual se llama "*derivado*" o "*calculad*", estos son atributos que no se guardan como tal en la **DDBB**, si no que estos son calculados a partir de otros, como puede ser por ejemplo el atributo edad, este no se almacena ya que es dependiente de la fecha de nacimiento de la persona y la fecha actual, es por ello que para obtener este atributo (*edad*), se hace un cálculo, en el que se resta a la fecha actual la fecha de nacimiento, obteniendo así la diferencia (*siendo esta la edad*).

Esta clase de atributos se indican mediante un círculo u óvalo discontinuo:

![#center](figuras/DDBB_Tema_2_figura_13.md)

Un ==atributo *monovalor*== (*a diferencia de los "multivalor"*) es aquel que contendrá ==un valor que no se podrá repetir== entre ocurrencias de una misma entidad, esto se podría aplicar por ejemplo al número de teléfono, ya que no queremos que se repita entre diferentes usuarios, la representación de estos se hace mediante un doble círculo u óvalo en el atributo de tipo "*UNIQUE*":

![#center](figuras/DDBB_Tema_2_figura_14.md)

## 2.3 El modelo E-R extendido

Diversos autores propusieron hacer ciertos cambios al modelo de E-R para añadir ciertas cuestiones, ahora veremos los cambios más importantes.

### 2.3.1 Cardinalidad de las relaciones

Las cardinalidades indican el mínimo y máximo de ocurrencias que pueden estar relacionadas de una entidad a otra.

Existen cuatro tipos:
- (0, 1): de cero a uno.
- (1, 1): de uno a uno.
- (0, n): de cero a varios.
- (1, n): de uno a varios.

Estas se indican sobre las líneas de las relaciones, convirtiéndola en una flecha en los casos *(0, n)* y *(1, n)*.

A su vez, al usar esta forma de anotación, no es necesario usar el [*tipo de correspondencia*](#^tipo-de-correspondencia).

En el siguiente ejemplo podemos encontrar que un artículo puede incluirse en *(0, n)* pedidos, mientras que un pedido puede incluir de *(1, n)* artículos:

![#center](figuras/DDBB_Tema_2_figura_15.md)

En el siguiente ejemplo veremos cómo los empleados pueden ser jefes de ningún o varios empleados, mientras que cada empleado puede no tener jefe o tener un jefe:

![#center](figuras/DDBB_Tema_2_figura_16.md)

En el siguiente ejemplo podemos ver como una pieza puede estar compuesta de cero a varias piezas (*0: engranaje; n: motor; un engranaje no está montado por piezas, mientras que un motor está montado por varias*), mientras que al mismo tiempo una pieza puede formar parte de cero a varias piezas (*0: motor; n: engranaje; un motor no forma parte de ninguna pieza, mientras que podemos encontrar engranajes en varias piezas*):

![#center](figuras/DDBB_Tema_2_figura_17.md)

Para las relaciones de un grado mayor a 2, las cardinalidades se hacen de forma diferente, para ello veamos lo con el siguiente ejemplo:

![#center](figuras/DDBB_Tema_2_figura_18.md)

En este ejemplo podemos ver las siguientes cardinalidades:
- El *(0, n)* al lado de *Suministrador*, indica que cada *Proyecto* los *Componentes* pueden ser suministrados por ningún, uno o varios *Suministradores*.
- El *(0, n)* al lado de *Proyecto*, indica que un *Suministrador* puede suministrar *Componentes* a ningún, uno o varios *Proyectos*.
- El *(0, n)* al lado de *Componente*, indica que un *Suministrador* a un *Proyecto* puede suministrar cero, uno o varios *Componentes*.

### 2.3.2 Atributos en relaciones

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Los atributos a parte de estar enlazados a las entidades, también pueden estar

### 2.3.3 Entidades fuertes y débiles

Existen dos tipos de entidades:
- ==Entidades regulares o fuertes==: son aquellas cuya existencia no está basada en la existencia de otra entidad.
- ==Entidades débiles==: son aquellas cuya existencia es dependiente de la existencia de otra entidad, siendo esta última regular.

> [!example]
> Un ejemplo de esto pueden ser las entidades *países* (*regular*) y *ciudades* (*débil*), en donde *ciudades* es dependiente de *países* ya que sin estos no pueden existir *ciudades*.
^example1

![#center](figuras/DDBB_Tema_2_figura_21.md)

Dependiendo de los tipos de entidades, sus relaciones también son afectadas, haciendo que puedan haber dos:
- ==Relaciones regulares o débiles==: son aquellas que relacionan dos entidades regulares o las que asocian una entidad regular con una entidad débil sin que esta última sea dependiente de la primera.
- ==Relaciones débiles==: son aquellas que relacionan una entidad débil con una regular.

Dentro de las relaciones débiles existen dos tipos:
- ==Dependencia de identificación==: este tipo de dependencia se puede ver en el caso de una librería, en donde tiene diferentes *libros* y puede tener varios *ejemplares* de cada uno de estos, en este caso, si vamos a la entidad de los ejemplares, el campo primario (*NumEjemplar*) se puede repetir, ya que puedes tener dos *libros* y cada uno de estos tendrán el valor `1`, ya que son el primer ejemplar de cada *libro*, por tanto, debido a que con el *NumEjemplar* de por sí, no podemos identificar una de las **ocurrencias** de la **entidad** *ejemplar*, por tanto, este tipo de relación ==es dependiente de la identificación de la entidad regular==.
    ![#center](figuras/DDBB_Tema_2_figura_22.md)
- ==Dependencia de entidad==: este tipo de dependencia ocurren por ejemplo con las *comunidades* y las *provincias*, ya que las *provincias* depende de las *comunidades*, sin embargo, a diferencia de la *dependencia de identidad* debido a que las *comunidades*, aun siendo dependientes de las *provincias*, el código de *comunidad nunca se repite*.
    ![#center](figuras/DDBB_Tema_2_figura_23.md)

### 2.3.4 Jerarquías de tipos y subtipos

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

### 2.3.5 Control de la redundancia

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
