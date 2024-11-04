---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: Modificadores de acceso en Java
---

# MODIFICADORES DE ACCESO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Los modificadores permiten como su nombre indica cambiar desde donde se puede acceder al elemento que estamos aplicando este modificador, esto se suele hacer con la intención de evitar fallos, ya que gracias a estos podemos indicar que un elemento solo se puede modificar desde un lugar concreto, evitando así que por error o maldad alguien acceda a esa información desde fuera de donde nosotros queremos.

| MODIFICADOR   | CLASE | PAQUETE | SUBCLASES | MUNDO |
| ------------- | ----- | ------- | --------- | ----- |
| `public`      | YES   | YES     | YES       | YES   |
| `protected`   | YES   | YES     | YES       | NO    |
| *no modifier* | YES   | YES     | NO        | NO    |
| `private`     | YES   | NO      | NO        | NO    |
^access-modifiers-table
