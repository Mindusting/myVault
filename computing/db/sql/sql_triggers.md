---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite
title: Triggers en SQL
---

# TRIGGERS EN SQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar las 

Los **triggers** en [**SQL**](sql.md) van de la mano en con el [**CRUD**](sql_crud.md), esto es debido a que los **triggers** son un componente que se activa cuando ejecutamos una [*inserción*](sql_insert.md), [*modificación*](sql_update.md) o [*borrado*](sql_delete.md) de los datos, de ahí el nombre, ya que se "*disparan*" en cuanto se ejecuta una de estas instrucciones.

Cuando un **trigger** se dispara este ejecuta el código que nosotros hayamos especificado a la hora de crearlo, pudiendo complementar o modificar de esta forma 

> [!abstract] SINTAXIS
> CREATE TRIGGER ***\[triggerName\]***
> ***\[moment\] \[acction\]*** ON ***\[tableName\]***
> BEGIN
> ***\[process\]***
> END;