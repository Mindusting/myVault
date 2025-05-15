---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Triggers en SQLite3
---

# TRIGGERS IN SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar de forma general que es un trigger.
> > - [ ] Documentar como crear triggers.
> > - [ ] Documentar como modificar triggers.
> > - [ ] Documentar como borrar triggers.

> [!help]- REFERERNCIAS WEB
> - [SQLite doc](https://sqlite.org/lang_createtrigger.html)
> - [SQLite tutorial](https://www.sqlitetutorial.net/sqlite-trigger/)

> [!faq]- FAQ
> - [¿Qué son los triggers en SQL?](../sql_triggers.md)

## CREAR TRIGGERS

```sql
CREATE TRIGGER t_ai_notes
	AFTER INSERT ON notes
BEGIN
	UPDATE notes
	SET
		creationDate = CASE
			WHEN NEW.creationDate IS NULL
        	THEN datetime('now', 'localtime')
			ELSE NEW.creationDate
		END,
		modificationDate = CASE
			WHEN NEW.modificationDate IS NULL
			THEN datetime('now', 'localtime')
			ELSE NEW.modificationDate
		END
	WHERE id = NEW.id;
END;
CREATE TRIGGER t_au_notes
	AFTER UPDATE ON notes
BEGIN
	UPDATE notes
	SET
		modificationDate = CASE
			WHEN NEW.modificationDate IS NULL
			THEN datetime('now', 'localtime')
			ELSE NEW.modificationDate
		END
	WHERE id = NEW.id;
END;
```

```sql
CREATE TRIGGER t_ai_notes
AFTER INSERT ON notes
BEGIN
	UPDATE notes
	SET
		creationDate = datetime('now', 'localtime'),
		modificationDate = datetime('now', 'localtime')
	WHERE id = NEW.id;
END;
CREATE TRIGGER t_au_notes
AFTER UPDATE ON notes
BEGIN
	UPDATE notes
	SET modificationDate= datetime('now', 'localtime')
	WHERE id = NEW.id;
END;
```

## MODIFICAR TRIGGERS

## BORRAR TRIGGERS
