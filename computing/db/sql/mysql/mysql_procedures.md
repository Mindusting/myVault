---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Procedimientos en MySQL
---

# PROCEDIMIENTOS EN MYSQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué son los procedimientos en SQL?](../sql_procedures.md)

Los procedimientos ejecutan código y no devuelven nada.

> [!abstract] SINTAXIS
> DELIMITER //
> CREATE PROCEDURE ***\[procedure\_name\]*** (***[\{parameters\}](#PARÁMETROS)***)
> BEGIN
> ***\[instructions\]***
> END//

## PARÁMETROS

> [!abstract] SINTAXIS
> ***[\{mode\_type\}](#MODOS%20DE%20PARÁMETROS) \[name\] \[data\_type\]***, ...

### MODOS DE PARÁMETROS

- `IN`
- `OUT`