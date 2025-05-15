---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Condicionales en MySQL
---

# CONDICIONALES EN MYSQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar el `IF`.
> > - [ ] Documentar el `IF ELSE`.
> > - [ ] Documentar el `IF ELSEIF`.
> > - [ ] Documentar el `CASE WHEN`.

> [!faq]- FAQ
> - [¿Qué es el control de flujo en programación?](../../../pc/pc_control_flow.md)
> - [¿Qué son los operadores de comparación en MySQL?](mysql_operators.md)

## CONDICIONES

Para poder indicar cuando se cumplen una condición y así ejecutar el código que nosotros queramos bajo ciertas circunstancias necesitaremos conocer los [operadores de comparación](mysql_operators.md) en **MySQL**.

### CONDICIÓN

```mermaid
flowchart LR
    inicio(["INICIO"])
    fin(["FIN"])
    cond{"cond"}
    inst["inst"]

    inicio -->
    cond -- Sí --> inst --> fin
    cond -- No --> fin
```

```sql
IF cond THEN
    -- instrucción;
    -- ...
END IF;
```

### CONDICIÓN SINO

```mermaid
flowchart LR
    inicio(["INICIO"])
    fin(["FIN"])
    cond{"cond"}
    inst0["inst A"]
    inst1["inst B"]

    inicio -->
    cond -- Sí --> inst0 --> fin
    cond -- No --> inst1 --> fin
```

```sql
IF condición THEN
    -- instrucción;
    -- ...
ELSE
    -- instrucción;
    -- ...
END IF;
```

### CONDICIÓN MÚLTIPLE

```mermaid
flowchart LR
    inicio(["INICIO"])
    fin(["FIN"])
    cond0{"cond0"}
    cond1{"cond1"}
    inst0["inst A"]
    inst1["inst B"]

    inicio -->
    cond0 -- Sí --> inst0 --> fin
    cond0 -- No -->
    cond1 -- Sí --> inst1 --> fin
    cond1 -- No --> fin
```

```sql
IF condición0 THEN
    -- instrucción;
    -- ...
ELSEIF condición1 THEN
    -- instrucción;
    -- ...
END IF;
```

```mermaid
flowchart LR
    inicio(["INICIO"])
    fin(["FIN"])
    cond0{"cond0"}
    cond1{"cond1"}
    inst0["inst A"]
    inst1["inst B"]
    inst2["inst C"]

    inicio -->
    cond0 -- Sí --> inst0 --> fin
    cond0 -- No -->
    cond1 -- Sí --> inst1 --> fin
    cond1 -- No --> inst2 --> fin
```

```sql
IF condición0 THEN
    -- instrucción;
    -- ...
ELSEIF condición1 THEN
    -- instrucción;
    -- ...
ELSE
    -- instrucción;
    -- ...
END IF;
```

## CASE WHEN

```mermaid
flowchart LR
    inicio(["INICIO"])
    fin(["FIN"])
    cond0{"valor0"}
    cond1{"valor1"}
    proc0["inst A"]
    proc1["inst B"]

    inicio -->
    cond0 -- Sí --> proc0 --> fin
    cond0 -- No -->
    cond1 -- Sí --> proc1 --> fin
    cond1 -- No --> fin
```

```sql
CASE expresión
WHEN valor0 THEN
    -- instrucción;
    -- ...
WHEN valor1 THEN
    -- instrucción;
    -- ...
END CASE;
```

```mermaid
flowchart LR
    inicio(["INICIO"])
    fin(["FIN"])
    cond0{"valor0"}
    cond1{"valor1"}
    proc0["inst A"]
    proc1["inst B"]
    proc2["inst C"]

    inicio -->
    cond0 -- Sí --> proc0 --> fin
    cond0 -- No -->
    cond1 -- Sí --> proc1 --> fin
    cond1 -- No --> proc2 --> fin
```

```sql
CASE expresión
WHEN valor0 THEN
    -- instrucción;
    -- ...
WHEN valor1 THEN
    -- instrucción;
    -- ...
ELSE
    -- instrucción;
    -- ...
END CASE;
```
