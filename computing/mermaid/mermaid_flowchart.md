---
aliases:
  - Flowchart in Mermaid
author: Mindusting
corrected: false
tags:
  - Mermaid
title: Diagrama de flujo en Mermaid
---

# DIAGRAMA DE FLUJO EN MERMAID

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar nodos.
> >     - [ ] Documentar los niveles de los nodos.
> > - [ ] Documentar conexiones.
> >     - [ ] Documentar los tipos de conexiones.
> >     - [ ] Documentar los tipos de puntas.
> >     - [ ] Documentar como meter texto en una conexión.
> > - [ ] Documentar subgrafos.

> [!help]- REFERENCIAS WEB
> - [Mermaid doc (Flowchart)](https://mermaid.js.org/syntax/flowchart.html)

> [!faq]- FAQ
> - [¿Qué es un diagrama de flujo?](../de/de_flowchart.md)

| TOKEM | DIRECCIÓN                                         |
|:-----:|:------------------------------------------------- |
| `TB`  | De arriba a abajo (*Top Bottom*)                  |
| `TD`  | De arriba a abajo (*Top Down*) (*igual que `TB`*) |
| `BT`  | De abajo a arriba (*Bottom Top*)                  |
| `LR`  | De izquierda a derecha (*Left Rigth*)             |
| `RL`  | De derecha a izquierda (*Rigth Left*)             |

> [!abstract] SINTAXIS
> flowchart ***\[direction\]***

```txt
flowchart TB
```

## NODOS

```mermaid
flowchart TB
    inicio([INICIO])
    if1{IF}
    proc[PROCESO]
    fin([FIN])

    inicio -->
    if1 -- Sí -->
    proc ~~~ fin
    proc -->
    if1 -- No -->
    fin

    l1([Nivel 1])
    l2([Nivel 2])
    l3([Nivel 3])
    l4([Nivel 4])

    l1 ~~~ l2 ~~~ l3 ~~~ l4
```

## FORMAS

| ENVOLTORIO  | FOMRA                        |
|:-----------:|:---------------------------- |
|   `[` `]`   | Rectánculo                   |
|   `(` `)`   | Esquinas redondeadas         |
|  `([` `])`  | Laterales redondos           |
|  `[[` `]]`  | Rectanculo con doble lateral |
|  `[(` `)]`  | Cilindro (DB)                |
|  `((` `))`  | Círculo                      |
| `(((` `)))` | Doble círculo                |
|   `>` `]`   | Forma asimétrica             |
|   `{` `}`   | Rombo                        |
|  `{{` `}}`  | Hexágono                     |
|  `[/` `/]`  | Paralelogramo                |
|  `[\` `\]`  | Paralelogramo alternativo    |
|  `[/` `\]`  | Trapezoide                   |
|  `[\` `/]`  | Trapezoide alternativo       |

```mermaid
flowchart TB
    rectangle["[]"]
    smootRectangle("()")
    roundEdges(["([])"])
    doubleLateralRectangle[["[[]]"]]
    cilindre[("[()]")]
    circle(("(())"))
    doubleCircle((("((()))")))
    asimetric>"\>]"]
    rhombus{"{}"}
    hex{{"{{}}"}}
    paralelogram[/"[//]"/]
    paralelogramAlt[\"[\\\\]"\]
    trapezoid[/"[/\\]"\]
    trapezoidAlt[\"[\\/]"/]

    rhombus ~~~
    hex ~~~
    asimetric ~~~
    cilindre

    rectangle ~~~
    smootRectangle ~~~
    roundEdges ~~~
    circle ~~~
    doubleCircle

    doubleLateralRectangle ~~~
    paralelogram ~~~
    paralelogramAlt ~~~
    trapezoid ~~~
    trapezoidAlt
```

## CONEXIONES

| TIPO               | FORMA 1 | FORMA 2 | FORMA 3  |
|:------------------ |:-------:|:-------:|:--------:|
| Línea invisible    |  `~~~`  | `~~~~`  | `~~~~~`  |
| Línea normal       |  `---`  | `----`  | `-----`  |
| Flecha normal      |  `-->`  | `--->`  | `---->`  |
| Línea gorda        |  `===`  | `====`  | `=====`  |
| Flecha gorda       |  `==>`  | `===>`  | `====>`  |
| Línea discontinua  |  `-.-`  | `-..-`  | `-...-`  |
| Flecha discontinua | `-.->`  | `-..->` | `-...->` |

| TIPO      | PUNTAS |
|:--------- |:------:|
| Triángulo | `<-->` |
| Circulo   | `o--o` |
| Equis     | `x--x` |

## SUBGRAFOS

> [!abstract] SINTAXIS
> subgraph ***\[title\]***
> ***\[content\]***
