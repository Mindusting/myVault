import os
import sqlite3
from time import perf_counter

clear = lambda: os.system("cls" if "nt" == os.name else "clear")

def main():
    clear()

    connection = sqlite3.connect("my.db")
    cursor = connection.cursor()

    loop: bool = True
    while loop:
        answer = input("$ ")
        match answer.upper():
            case "EXIT":
                loop: bool = False
            case "CLEAR":
                clear()
            case "LIST":
                cursor.execute("SELECT id, firstName, lastName FROM users;")
                registers: list[tuple] = cursor.fetchall()
                print(f"{len(registers)} results:")
                for register in registers:
                    print(f"{register[0]}: {register[1]} {register[2]}")
            case "NEW":
                first_name: str = input("First name: ")
                last_name: str = input("Last name: ")
                sex_id: int = int(input("Sex: "))
                note: str = input("Note: ")
                cursor.execute(f"INSERT INTO users (firstName, lastName, sex, notes) VALUES ('{first_name}', '{last_name}', {sex_id}, '{note}');")
            case "DEL":
                user_id = int(input("User ID: "))
                cursor.execute(f"SELECT firstName FROM users WHERE id={user_id}")
                user_name = cursor.fetchall()[0][0]
                if int(input(f"Quieres borrar el usuario \"{user_name}\" (1 = True, 0 = False): ")):
                    cursor.execute(f"DELETE FROM users WHERE id={user_id};")
                    print("Borrado completado.")
                else:
                    print("No se ha borrado el registro.")
            case "SAVE":
                if int(input("Quieres guardar los cambios (1 = True, 0 = False): ")):
                    connection.commit()
                    print("Guardado correctamente.")
                else:
                    print("No se han guadado los cambios.")
            case "INFO":
                user_id = int(input("User ID: "))
                cursor.execute(f"SELECT * FROM users WHERE id={user_id};")
                register = cursor.fetchone()
                print(f"""\
Nombre: {register[1]}.
Apellido(s): {register[2]},
Sexo: {"Masculino" if register[3] == 2 else "Femenino"}.
Nota:
{register[4]}""")
            case "EDIT":
                user_id = int(input("User ID: "))
                cursor.execute(f"SELECT * FROM users WHERE id={user_id};")
                register = cursor.fetchone()
                print(f"""\
Nombre: {register[1]}.
Apellido(s): {register[2]},
Sexo: {"Masculino" if register[3] == 2 else "Femenino"}.
Nota:
{register[4]}""")

                first_name: str = input("First name: ")
                last_name: str = input("Last name: ")
                sex_id: int = int(input("Sex: "))
                note: str = input("Note: ")
                if int(input("Confirmar edición (1 = True, 0 = False): ")):
                    cursor.execute(f"UPDATE users SET firstName='{first_name}', lastName='{last_name}', sex={sex_id}, notes='{note}' WHERE id={user_id};")
                    print("Registro modificado.")
                else:
                    print("El registro no se ha modificado.")


    cursor.close()
    connection.close()

if "__main__" == __name__:
    t0: float = perf_counter()
    main()
    t1: float = perf_counter()
    print(f"{t1 - t0:0.6f}")
