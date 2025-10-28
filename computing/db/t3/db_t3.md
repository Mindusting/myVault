---
author: Mindusting
collaborators:
  - Anonymous
corrected: false
tags:
  - DB
title: Bases de datos
---

# El modelo relacional

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## 3.1 Evolución del modelo relacional

El nuevo modelo de **DDBB** relacional formado por tablas y relaciones ofrece las siguientes ventajas:

- ==**Independencia física**==: Esto quiere decir que ==el programa que acceda a los datos no deberá cambiar== en dependencia del medio que se ha usado para almacenar la información.
- ==**Independencia lógica**==: Esto quiere decir que ==tanto el programa como los usuarios no son afectados cuando se modifiquen los objetos== de la **DDBB**.
- ==**Uniformidad**==: Esto quiere decir que ==la **DDBB** tiene una forma uniforme==, facilitando la manipulación de ésta por parte de los usuarios.
- ==**Sencillez**==: Todos los puntos anteriores facilitan el manejo de la **DDBB**.

## 3.2 Estructura del modelo relacional

En un modelo relacional las información se almacena en relaciones.

### 3.2.1 El concepto y propiedades de las relaciones

==Una relación se divide en columnas y tuplas==, teniendo en cada columna un atributo y en cada tupla un registro de la relación.

![#center](figuras/db_t3_f1.md)

Las relaciones tienen las siguientes propiedades:

- ==Todas las relaciones tienen un nombre.==
- ==Los valores de una relación son **atómicos**==, esto quiere decir que por cada celda ==sólo== puede haber ==un valor==.
- ==Todos los atributos de una misma tabla tienen nombres distintos.==
- ==Los atributos de una relación no están ordenados.==
- ==En una tabla no hay dos tuplas iguales== (*No debería haber*).
- ==Las tuplas== de una relación ==no están ordenadas.==

### 3.2.2 Atributos y dominio de los atributos

==Los **atributos** son== las propiedades de una relación y se representan como ==columnas== en una tabla. En la relación "Pedido", hay dos atributos: **RefPed** (*referencia del pedido*) y **FecPed** (*fecha del pedido*). ==Cada atributo tiene un **dominio**==, que ==es el conjunto de valores permitidos==: **RefPed** es una cadena de 5 caracteres, mientras que **FecPed** corresponde a cualquier fecha válida.

> [!example] Pedido
> | RefPed | FecPed     |
> | ------ | ---------- |
> | P0001  | 16/02/2023 |
> | P0002  | 18/02/2023 |
> | P0003  | 23/02/2023 |
> | P0004  | 25/02/2023 |

### 3.2.3 Tupla, grado y cardinalidad

==Cada fila de una relación se llama **tupla**.== La relación *"Pedido"* tiene cuatro **tuplas**. ==El **grado**== de una relación se refiere al ==número de **atributos**==; en este caso, "Pedido" tiene un grado de 2 y una **cardinalidad** de 4.

### 3.2.4 Relaciones y tablas

Aunque a menudo usamos tablas para representar relaciones en DDBB, hay diferencias clave entre ambas.

> [!example]- Ejemplo:
> 1. ==**Terminología**: Usamos "tabla" para referirnos a una **relación**, "columna" para un **atributo** y "fila" para una **tupla**.==
> 2. ==**Duplicados**: En una relación no pueden haber filas duplicadas==, a diferencia de lo que ocurre ==en una tabla convencional==, donde ==sí== se permiten.
> 3. ==**Orden**: Ni las filas ni las columnas tienen un orden definido en una relación.==
> 4. ==**Valores únicos**: En cada cruce de fila y columna solo puede haber un único valor==, sin permitir múltiples valores para un mismo **atributo**.

> [!note] Nota
> Aunque se parecen, las **relaciones** en **DDBB** tienen reglas específicas que las diferencian de las **tablas** comunes.

## 3.3 Claves en el modelo relacional

==En el modelo relacional se puede hablar de distintos tipos de claves==, que se exponen en las siguientes subsecciones.

### 3.3.1 Claves candidatas

==Una clave candidata es un conjunto de **atributos** que identifica de manera **única** a cada **tupla**== en una relación, sin permitir duplicados. Además una clave candidata tiene dos características:

- ==**Unicidad**: No puede haber dos **tuplas** con el mismo valor para la clave candidata.==
- ==**Minimalidad**: Debe ser el conjunto más pequeño posible==; si un solo atributo identifica de manera única, no se deben agregar más.

> [!example]- Ejemplos:
> - En una relación de empleados, el atributo **NEmp** (*número de empleado*) es **clave candidata** porque cada número es único.
> - Si los nombres de los empleados también son únicos, el atributo **Nombre** sería otra clave candidata.
> - En una relación de pedidos, el atributo **RefPed** (*referencia de pedido*) es la única clave candidata, ya que cada pedido tiene una referencia única.

> [!important] Resumen:
> Una clave candidata es esencial para garantizar que cada entrada en una **DDBB** sea **única**, y debe ser lo más simple posible.

### 3.3.2 Claves primarias

==La **clave primaria** es una **clave candidata** elegida para identificar de manera **única** las **tuplas**== de una relación. ==Si solo hay una **clave candidata**, esta se convierte en la **clave primaria**.==:

> [!example]- Ejemplo:
> - En la relación **Empleado**, se podría elegir **NEmp** como clave primaria, o el nombre si es único.
> - En la relación **Pedido**, **RefPed** es la clave primaria porque es la única clave candidata.
> - En la relación **Artículo**, se puede elegir entre **CodArt** y **DesArt** como clave primaria, pero solo uno puede ser seleccionado.

> [!important] Dato importante:
> Las **relaciones** se representan con su **nombre** seguido de los **atributos** entre paréntesis y separados por comas. La **clave primaria** se indica subrayando, el **atributo**/**usando** o anteponiendo el símbolo `#` delante de él.

### 3.3.3 Claves alternativas

==Las **claves alternativas** son aquellas **claves candidatas** que no se han seleccionado como **clave primaria**.==

> [!example]- Ejemplo:
> - En la relación **Empleado**, el atributo **Nombre** sería una clave alternativa si no hay empleados con el mismo nombre.
> - En la relación **Pedido**, no existen claves alternativas.
> - En la relación **Artículo**, **DesArt** podría ser una clave alternativa si la descripción de los artículos es única.

### 3.3.4 Claves ajenas

==Una **clave ajena**, o **clave foránea**, es un conjunto de **atributos** en una **relación** cuyos valores deben coincidir con los de la **clave primaria** de otra **relación**==, y ambas deben estar definidas sobre el mismo dominio.

==Las **claves ajenas** se representan trazando flechas desde cada **clave ajena** hasta su **clave primaria** correspondiente.== Así, la **DDBB** relacional formada por estas tres tablas se puede visualizar gráficamente.

> [!example]- Ejemplo más detallado para entenderlo mejor
> En el contexto de una **DDBB** que incluye las relaciones **Pedido** y **Artículo**, hay una tercera relación llamada **LíneaPedido**, que registra las líneas de pedido de los clientes, donde cada línea corresponde a un artículo diferente solicitado.
> 
> Cada línea de pedido se identifica por los atributos **RefPed** (referente al pedido) y **CodArt** (referente al artículo), y se incluye un tercer atributo, **CantArt**, que indica la cantidad de unidades del artículo solicitadas en el pedido.
> 
> En la tabla **LíneaPedido**, el atributo **RefPed** es una clave ajena que hace referencia a **RefPed** en la tabla **Pedido**, por lo que su valor debe coincidir con uno de los valores en esa tabla (P0001, P0002, P0003 o P0004). Del mismo modo, el atributo **CodArt** en **LíneaPedido** es una clave ajena al atributo **CodArt** en la tabla **Artículo**, y su valor debe coincidir con uno de los cinco valores en esa tabla (A0043, A0078, A0075, A0012 o A0089).

## 3.4 Restricciones de integridad

Las principales restricciones de integridad del modelo relacional son:

1. ==**Clave primaria (PRIMARY KEY)**==: Declara un **atributo** o conjunto de **atributos** como **clave primaria**, lo que implica que ==sus valores no pueden repetirse y no se permiten valores nulos==.
2. ==**Unicidad (UNIQUE)**==: ==Asegura que los valores de un **atributo** o conjunto de **atributos** sean **únicos**== en una relación, permitiendo así la definición de **claves alternativas**. Por ejemplo, en la relación **Artículo**, si no puede haber dos artículos con la misma descripción (**DesArt**), este atributo será una clave alternativa y deberá tener la restricción de unicidad.
3. ==**Obligatoriedad de uno o más atributos (NOT NULL)**: Indica que== un **atributo** o conjunto de **atributos** ==no puede tener valores nulos.==
4. ==**Integridad referencial (FOREIGN KEY)**: Relacionada con **claves ajenas**, asegura que los valores de un **atributo** en una relación coincidan con los de la **clave primaria** en otra.==
5. ==**Restricciones de rechazo y aserciones**==: Permiten al usuario especificar un predicado o condición sobre un atributo o conjunto de atributos. Al realizar operaciones de actualización, se ==verifica si se cumple la condición; sino, la operación es rechazada.==

    > [!important] Existen dos tipos:
   > - **Restricciones de verificación o rechazo**: Afectan a una sola relación.
   > - **Aserciones**: Afectan a varias relaciones.

### 3.4.1 Valores nulos en el modelo

==Un **valor nulo** indica que el dato asociado a un **atributo** es desconocido.== Son útiles para manejar información con lagunas, donde ciertos datos existen en teoría pero no se conocen en un momento dado.

> [!example]- Ejemplos:
> - En una tabla de clientes, si no se conoce el teléfono de un cliente, se utiliza un valor nulo.
> - En la relación **Albarán**, la clave ajena **NumFactura** puede ser nula mientras se genera la factura correspondiente.

> [!info]
> A la hora de **crear  nuevas columnas**, al añadir una nueva columna a una tabla existente, los valores de esa columna suelen iniciarse como **nulos**.

Manejar valores **nulos** es complejo y requiere un estudio detallado, especialmente en operaciones y funciones del modelo relacional.

De este modo, para las operaciones lógicas *AND*, *OR* y *NOT*, se utiliza una lógica trivaluada que incluye **valores nulos**. Las tablas de verdad son las siguientes:

| AND           | VERDADERO | FALSO | NULO  |
| ------------- | --------- | ----- | ----- |
| **VERDADERO** | VERDADERO | FALSO | NULO  |
| **FALSO**     | FALSO     | FALSO | FALSO |
| **NULO**      | NULO      | FALSO | NULO  |

| OR            | VERDADERO | FALSO     | NULO      |
| ------------- | --------- | --------- | --------- |
| **VERDADERO** | VERDADERO | VERDADERO | VERDADERO |
| **FALSO**     | VERDADERO | FALSO     | NULO      |
| **NULO**      | VERDADERO | NULO      | NULO      |

| NOT           | RESULTADO |
| ------------- | --------- |
| **VERDADERO** | FALSO     |
| **FALSO**     | VERDADERO |
| **NULO**      | NULO      |

> [!important] Operador importante
> ==**Operador MAYBE**: Este operador se utiliza para determinar si un valor es **nulo**==, con la siguiente tabla de verdad:
> 
> | MAYBE         | RESULTADO |
> | ------------- | --------- |
> | **VERDADERO** | FALSO     |
> | **FALSO**     | FALSO     |
> | **NULO**      | VERDADERO |

---

**Operaciones Aritméticas**: El resultado de operar un valor **nulo** con cualquier otro valor es siempre **nulo**.

Hay que tener en cuenta que ==en la **selección de tuplas**, las **tuplas** pueden no aparecer en los resultados si presentan valores **nulos**== para las condiciones establecidas, ya que un predicado **nulo** no se evalúa como verdadero.

**Comparaciones**: ==Comparar un valor **nulo** con otro== (*por ejemplo, si 3 es mayor o menor que un valor **nulo***) ==resulta en una respuesta indeterminada== (*"quizás"*).

En cuanto a la **presencia de ==valores nulos en claves==**, se ha de cumplir lo siguiente:

- ==Una **clave primaria** no puede tener valores **nulos**.==
- ==Una **clave ajena** puede contener valores **nulos**, pero se recomienda ser restrictivos== al permitir **nulos**, limitándolos a situaciones donde tenga sentido semántico.

### 3.4.2 Integridad de las entidades

La regla de integridad de la entidad es una restricción fundamental en el modelo relacional que establece que ==**ningún atributo que forme parte de la clave primaria de una relación puede tener un valor nulo**==. Esto asegura que cada **tupla** en la relación pueda ser identificada de manera **única** y que los valores clave sean siempre válidos.

### 3.4.3 Integridad referencial

La restricción de integridad referencial establece que ==una **clave ajena** solo puede tener un valor **nulo** o coincidir con los valores de la **clave candidata**== de la relación a la que apunta.

> [!example]- Ejemplo:
> En las relaciones **Pedido**, **Artículo** y **LineaPedido**:
> - El atributo **RefPed** en la relación **LineaPedido** es una clave ajena que referencia el atributo homónimo en la relación **Pedido**. Sus valores deben ser nulos o concordar con los valores de **RefPed** en **Pedido** (P0001, P0002, P0003 o P0004). Sin embargo, no puede ser nulo, ya que forma parte de la clave primaria de **LineaPedido**.
> - Lo mismo ocurre con el atributo **CodArt** en **LineaPedido**, que también debe ser un valor de la clave primaria de la relación **Artículo** (A0043, A0078, A0075, A0012 o A0089) y no puede ser nulo.

Además de definir las **claves ajenas**, es fundamental considerar las ==consecuencias del **borrado** y **modificación** de **tuplas** en la relación referenciada==.

Se pueden distinguir las siguientes opciones:

1. ==**Operación Restringida (*RESTRICT*)**==: Esta opción ==**no permite** el **borrado** o **modificación** de **tuplas** en la relación referenciada si existen **tuplas** en la otra relación con el mismo valor en la **clave ajena**==. Por ejemplo, para borrar un pedido en la relación **Pedido**, no puede haber filas en **LineaPedido** correspondientes a ese pedido. Asimismo, no se puede modificar el atributo **RefPed** en **Pedido** si hay líneas de pedido asociadas.
2. ==**Operación con Transmisión en Cascada (*ON DELETE CASCADE, ON UPDATE CASCADE*)**==: En este caso, ==el **borrado** o **modificación** de **tuplas** en la relación que contiene la **clave referenciada** resulta en el **borrado o **modificación** en cascada de las **tuplas** correspondientes en la relación que tiene la **clave ajena**.==
3. ==**Operación SET NULL (*con puesta a nulo*)**: Al **borrar** o **modificar tuplas** en una tabla que contiene una **clave referenciada**, se pone a nulo el atributo correspondiente en la tabla que tiene la **clave ajena**.==
4. ==**Operación SET DEFAULT (*con puesta a valor por defect*)**==: Similar a *SET NULL*, pero en lugar de asignar un valor **nulo**, ==se asigna un valor predeterminado previamente definido al atributo de la **clave ajena**.==
5. ==**Operación que desencadena un procedimiento de usuario:** Al **borrar** o **modificar tuplas** en la tabla referenciada, se ejecuta un procedimiento definido por el usuario.==

 Es necesario especificar qué opción se utiliza para cada **clave ajena** en la tabla afectada. Las decisiones de **borrado** y **modificación** son independientes entre sí.

## 3.5 Álgebra relacional

==El **álgebra relacional**== es un lenguaje formal utilizado para realizar **consultas** en **DDBB** relacionales, y ==es la base del lenguaje **SQL**==. Se basa en la teoría de conjuntos y permite construir **consultas** a través de operadores que ==combinan y transforman relaciones para obtener nuevos resultados==. Estos operadores utilizan una o más relaciones como entrada y generan una nueva relación como salida.

### 3.5.1 Clasificación de los operadores

Los operadores del álgebra relacional se clasifican según diferentes criterios:

1. ==**Similitud con la teoría de conjuntos**==:
   - ==**Operadores conjuntistas**==: incluyen unión, intersección, diferencia y producto cartesiano.
   - ==**Operadores relacionales especiales**==: incluyen selección, proyección, combinación y división.

2. ==**Expresividad**==:
   - ==**Operadores primitivos**==: son esenciales y no se derivan de otros; incluyen selección, proyección, producto cartesiano, unión y diferencia.
   - ==**Operadores derivados**==: se obtienen aplicando operadores primitivos y simplifican operaciones comunes; incluyen intersección, combinación y división.

3. ==**Número de relaciones como operando**==:
   - ==**Operadores unarios**==: operan sobre una sola relación, como selección y proyección.
   - ==**Operadores binarios**==: operan sobre dos relaciones, como producto cartesiano, unión, diferencia, intersección, combinación y división. Para la mayoría de estos, las relaciones deben ser compatibles en términos de atributos.

Este marco de clasificación ayuda a entender cómo funcionan los operadores y su aplicación en consultas sobre **DDBB**.

### 3.5.2 Operaciones primitivas

En esta sección se van a estudiar los operadores primitivos del álgebra relacional:

- ==El **operador de selección (*[σ](https://es.wikipedia.org/wiki/%CE%A3)/sigma*)**== en álgebra relacional crea un subconjunto horizontal de una relación, ==incluyendo solo las **tuplas** que cumplen con un predicado específico==. Esto permite ==filtrar los datos== de acuerdo a criterios determinados.
- ==El **operador de proyección (*[π](https://es.wikipedia.org/wiki/%CE%A0)/pi*)**== en álgebra relacional genera un subconjunto vertical de una relación al ==seleccionar solo los atributos especificados en el orden indicado. Además, elimina las **tuplas** duplicadas del resultado.== Por ejemplo, para obtener los puestos de los empleados de una relación llamada *Empleados*, se utilizaría una expresión específica de proyección.
- ==El **producto cartesiano (*A x B*)**== de dos relaciones *A* y *B* ==combina todas las **tuplas** posibles de *A* con las de *B*==. Si *A* tiene un grado de *m* y *B* un grado de *n*, el resultado tendrá un grado de *m+n*. En cuanto a la cardinalidad, si *A* tiene *p* **tuplas** y *B* tiene *q* **tuplas**, la cardinalidad del producto cartesiano será *p x q*.
- ==La **unión (*A ∪ B*)** de las relaciones *A* y *B* combina todas las **tuplas** de ambas, incluyendo aquellas que son exclusivas de cada una. Si hay **tuplas** duplicadas entre *A* y *B*, se **eliminan** en el resultado, dejando solo **tuplas** únicas en la relación resultante.==
- ==La **diferencia (*A - B*)** de las relaciones *A* y *B* es una relación que incluye todas las **tuplas** que pertenecen a *A* pero no pertenecen a *B* y viceversa.==

### 3.5.3 Otras operaciones

En esta sección se van a estudiar diversos operadores derivados del álgebra relacional:

- ==La **intersección (*A ∩ B*)**== de dos relaciones *A* y *B* ==consiste en todas las **tuplas** que están presentes en ambas relaciones==. Es decir, solo se incluyen aquellas **tuplas** que son comunes a *A* y *B* en la relación resultante.
- ==La **combinación (*A \* B*)**==, también conocida como "`join`" de dos relaciones *A* y *B* produce una relación que incluye las **tuplas** obtenidas al concatenar ==**tuplas** de *A* y *B* que cumplan una condición específica sobre un atributo común==. Este proceso implica primero realizar el producto cartesiano de *A* y *B*, seguido de una selección de las **tuplas** que satisfacen la condición establecida.

> [!note] Nota
> Cuando la condición, es una comparación de igualdad, se trata de una `equijoin`, `equirreunión` o *combinación por igualdad*.

La combinación más común entre tablas es el "`join`" o "reunión natural," que se obtiene al realizar una `equijoin` y eliminar los atributos duplicados. En la `equijoin`, se igualan los atributos que establecen la relación entre las tablas, generalmente una clave ajena y su correspondiente clave primaria. El operador que representa esta operación es ⋈.

La **reunión natural** entre dos relaciones *A* y *B* se realiza de la siguiente manera:

1. Se calcula el producto cartesiano de *A* y *B* (*A x B*) para concatenar todas las **tablas**.
2. Se seleccionan las **tuplas** que tengan valores iguales en las columnas de dominio común, como la **clave ajena** y la **clave primaria** correspondiente.
3. Se **eliminan** las columnas duplicadas en el resultado, suprimiendo una de cada par de columnas homónimas.

Este proceso da como resultado una relación que combina los datos relevantes de ambas tablas sin duplicados.

- ==El **operador de división (*A/B*)**== toma una relación *A* de grado *m* y la divide entre una relación *B* de grado *n*, produciendo un resultado de grado *m-n*. Generalmente, *A* tiene un grado de *2* y *B* de *1*. La relación resultante *A/B* consiste en las **tuplas** < x > que, al concatenarse con las **tuplas** de *B* < y >, forman **tuplas** < x, y > que están en *A*. Al realizar el producto cartesiano de *A/B* y *B*, las **tuplas** resultantes deben pertenecer a *A*, garantizando que la relación final respete la estructura de *A*.
