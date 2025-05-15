---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Module
  - Programming/Python/SQLite3
  - DataBase/SQLite3
title: SQLite encriptado en Python
---

# MÓDULO PYSQLCIPHER3 EN PYTHON

> [!help]- REFERENCIAS WEB
> - [pysqlcipher3 (GitHub)](https://github.com/rigglemania/pysqlcipher3)
> 
> YouTube:
> - [NeuralNine](https://youtu.be/8PARZE2aTOQ)

Si estás en Ubuntu primero tendrás que instalar la librería de **SQLCipher**, ya que esta contiene las dependencias necesarias para poder usarse desde Python:

```bash
sudo apt install libsqlcipher-dev
```

> [!note] NOTA
> Si quieres instalar el programa a parte, para poder trastear, puedes hacerlo con el siguiente comando.
> 
> ```bash
> sudo apt install sqlcipher
> ```

Una vez instalada la librería de **SQLCipher** tendremos que instalarla en Python, para eso usaremos el siguiente comando:

```bash
pip install pysqlcipher3
```

## IMPORTAR MÓDULO

Para hacer uso de este [módulo](py_module.md) hay que importarlo, se suele hacer de la siguiente manera para simplificar el uso:

```python
from pysqlcipher3 import dbapi2 as sqlite
```

## USO DEL MÓDULO

Este módulo se usa igual que el de [SQLite3](sqlite3/py_sqlite3.md) con la diferencia que en este se debe indicar la contraseña que se debe usar para poder interactuar con la base de datos, para ello se usa la instrucción [`PRAGMA key`](../db/sql/sqlite3/sqlite3_pragma.md).

```python
from pysqlcipher3 import dbapi2 as sqlite


def main() -> None:
    password: str = "Esta es mi contraseña"

    cx = sqlite.connect("./main.db")
    cr = cx.cursor()

    cr.execute(f"PRAGMA key='{password}';")
    cr.execute("SELECT * FROM users;")
    
    for user in cr.fetchall():
        print(user)

    cr.close()
    cx.close()


if "__main__" == __name__:
    main()
```
