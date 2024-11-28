import os
import sqlite3
from time import perf_counter

clear = lambda: os.system("cls" if "nt" == os.name else "clear")

def main():
    clear()

    connection = sqlite3.connect("my.db")
    cursor = connection.cursor()
    
    #cursor.execute("CREATE TABLE IF NOT EXISTS files (id INTEGER NOT NULL, fileName TEXT NOT NULL, fileData BOLB NOT NULL, PRIMARY KEY(id))")
    """
    with open("Mindusting.png", "rb") as FILE:
        DATA = FILE.read()
        cursor.execute(f"INSERT INTO files (fileName, fileData) VALUES (?, ?);", ("Mindusting.png", DATA))
    #"""
    """
    cursor.execute("SELECT * FROM files;")
    print(cursor.fetchone())
    #"""
    #"""
    cursor.execute("SELECT fileName, fileData FROM files;")
    file_name, file_data = cursor.fetchone()
    with open(file_name, "wb") as FILE:
        FILE.write(file_data)
    #"""

    connection.commit()
    cursor.close()
    connection.close()

if "__main__" == __name__:
    t0: float = perf_counter()
    main()
    t1: float = perf_counter()
    print(f"{t1 - t0:0.6f}")
