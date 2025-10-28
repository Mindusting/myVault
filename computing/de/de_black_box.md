---
aliases:
  - Black box
author: Mindusting
corrected: false
tags:
  - Programming/DE
title: Caja negra
---

# CAJA NEGRA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que es la caja negra y cual es su objetivo.
> > - [ ] Documentar las clases de equivalencia.
> > - [ ] Documentar los casos de prueba.

El concepto de caja negra representa cuando tenemos una función (*algoritmo, máquina, ...*) de la cual no tenemos ni idea (*o hacemos como que no tenemos*) del funcionamiento interno de esa función (*algoritmo, máquina, ...*), únicamente podemos ofrecerle una serie de valores como argumentos y recibir su resultado, 

## CLASES DE EQUIVALESCIA

| NOMBRE                | ABREV. | CONTIENE                          | EJEMPLO                        |
|:--------------------- |:------ |:--------------------------------- |:------------------------------ |
| Condición de Entrada  | C.E.   | Nom. del arg.                     | `name`, `price`                |
| Clase de Equivalencia | C.Eq.  | Tipo de dato que requiere el arg. | valor, lógica, rango, conjunto |
| Clases válidas        | C.V.   | Valor válido del arg.             | "Adelio"                       |
| Código (Válido)       | Cod.   | Código                            | V1, V2, ...                    |
| Clases no válidas     | C.N.V. | Valor no válido del arg.          | ""                             |
| Código (No válido)    | Cod.   | Código                            | NV1, NV2, ...                  |

## CASOS DE PRUEBA

| NOMBRE                 | ABREV. | CONTIENE            |
|:---------------------- |:------ |:------------------- |
| Caso de Prueba         | C.P.   | Un identificador    |
| Clases de Equivalencia | C.E.   | Conjunto de códigos |
| Condiciones de Entrada | C.En.  | Valores de los arg. |
| Resultado Esperado     | R.E.   | Valor o error       |

## EJEMPLOS

> [!example] Ej. más simple:

```python
def isEven(number: int) -> bool:
    return number % 2 == 0
```

|  C.E.  |     C.Eq.     | C.V. | Cod. |  C.N.V.  | Cod. |
|:------:|:-------------:|:----:|:----:|:--------:|:----:|
| number | Número entero | *0*  |  V1  |  *null*  | NV1  |
|   "    |       "       | *1*  |  V2  | *"Hola"* | NV2  |
|   "    |       "       |      |      | *3.1416* | NV3  |

| C.P. | C.E. |  C.En.   |  R.E.   |
|:----:|:----:|:--------:|:-------:|
| CP1  |  V1  |   *5*    | *false* |
| CP2  |  V2  |   *8*    | *true*  |
| CP3  | NV1  |  *null*  |  Error  |
| CP4  | NV2  | *"Hola"* |  Error  |
| CP5  | NV3  | *3.1416* |  Error  |

---
