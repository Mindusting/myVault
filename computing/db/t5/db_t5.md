---
author: Mindusting
collaborators:
  - Anonymous
corrected: false
tags:
  - DB
title: Bases de datos
---

# Normalización de las DDBB relacionales

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## 5.1 La teoría de la normalización

El proceso de diseño de una **DDBB** implica representar una parte del mundo real utilizando un modelo de datos, aplicando sus reglas y restricciones. En el modelo relacional, existen diversas soluciones para representar la realidad, pero no todas son equivalentes; algunas son más adecuadas que otras. ==La normalización es una teoría que aborda este problema de forma rigurosa, optimizando el diseño del esquema relacional==.

La normalización es una técnica formal para organizar datos y corregir problemas en el diseño de **DDBB**. Se basa en las *formas normales*, que son un conjunto de restricciones que un esquema relacional debe cumplir. Existen seis formas normales: 

- Primera (`1FN`)
- Segunda (`2FN`)
- Tercera (`3FN`)
- Boyce/Codd (`FNBC`)
- Cuarta (`4FN`)
- Quinta (`5FN`)

## 5.2 Dependencias funcionales Tipos

### 5.2.1 Dependencia funcional

Se dice que Y depende funcionalmente de X, o que X determina a Y, si cada valor de X está asociado a un único valor de Y. Esta dependencia se representa como:  X -> Y.

==**El grafo** o **diagrama de dependencias funcionales** es una herramienta útil para mostrar las dependencias entre atributos==. En estos diagramas, los atributos se representan con sus nombres, y las flechas indican las dependencias funcionales entre ellos.

### 5.2.2 Dependencia funcional completa

Se dice que Y tiene una *dependencia funcional completa* de X si depende funcionalmente de X, pero no depende de ningún subconjunto propio de X. Esto se representa como: X => Y.

En un diagrama de dependencias funcionales, ==las dependencias funcionales completas se representan partiendo la flecha de un rectángulo en cuyo interior aparece más de un atributo==.

### 5.2.3 Dependencia funcional mutua o interdependencia

Si en una relación existen las dependencias funcionales X -> Y e Y -> X simultáneamente, se dice que hay una ==*dependencia funcional mutua* o *interdependencia*== entre los atributos X e Y, y se representa como: X <-> Y.

### 5.2.4 Dependencia funcional transitiva

Dada la relación R(X, Y, Z) con las dependencias funcionales X -> Y, Y -> Z y 
Y (flecha como las anteriores pero tachada) X, podemos representarlas como: 

```
X -> Y -> Z
```

En este caso, se dice que Z tiene una *dependencia funcional transitiva* respecto de X a través de Y, y se representa como: 

```
X -> Z
``` 

Esto significa que la dependencia de Z respecto a X es indirecta, pasando a través de Y.
## 5.3 Primera forma normal (1FN)

Una relación está en *Primera Forma Normal (1FN)* ==si todos sus componentes son atómicos, es decir, no contienen grupos repetitivos (atributos con valores múltiples)==. 

Para convertir una relación a 1FN, se eliminan los atributos del grupo repetitivo y se crea una nueva relación que incluye la clave primaria de la relación original y los atributos del grupo repetitivo. 

La clave de la nueva relación se forma generalmente por la concatenación de la clave primaria original con la clave del grupo repetitivo.

## 5.4 Segunda forma normal (2FN)

Una relación está en *Segunda Forma Normal (2FN)* ==si, estando en 1FN, cada atributo que no forma parte de una clave candidata depende totalmente de dicha clave, es decir, depende de toda la clave y no solo de una parte de ella==. 

Para convertir una relación a 2FN, se eliminan los atributos que generan dependencias parciales y se crea una nueva relación con esos atributos y la clave primaria que depende de ellos. 

Si una relación en 1FN tiene una clave primaria de un solo atributo, ya está en 2FN. También estarán en 2FN las relaciones en 1FN que no tengan atributos no clave.

## 5.5 Tercera forma normal (3FN)

Una relación está en *Tercera Forma Normal (3FN)* ==si, estando en 2FN, cada atributo que no forma parte de una clave candidata depende directamente de ella, es decir, no existen dependencias transitivas==. **Cualquier relación en 2FN con menos de dos atributos** no clave ya está automáticamente en 3FN. 

Para eliminar dependencias transitivas, se elimina el atributo que genera la dependencia y se crea una nueva tabla con los atributos involucrados en la transitividad y el atributo del que dependen. 

Por ejemplo 

En la relación R(A, B, C) con las dependencias funcionales A -> B -> C, existe una dependencia transitiva de C respecto de A, porque C depende de B, que a su vez depende de A, pero C no depende directamente de A. La forma de pasar la relación a 3FN sería la siguiente: 

```txt
R1(A, B)
      |
   ----
   |
   v
R2(B, C)
```