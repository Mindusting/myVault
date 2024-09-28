```txt
CREATE TABLE emails (
    id INTEGER PRAIMARY KEY,
    id_user INTEGER,
    email TEXT,
    FOREIGN KEY(id_user) REFERENCES users(id)
);
```
