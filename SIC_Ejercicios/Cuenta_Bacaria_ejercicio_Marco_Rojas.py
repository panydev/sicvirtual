import time
import sys  # Importamos sys para usar sys.exit()

usuarios = [
    {"id": 123, "nombre": "Jenny", "tipo_cuenta": "Ahorro", "saldo": 50000, "edad": 45},
    {"id": 456, "nombre": "Anderson", "tipo_cuenta": "Corriente", "saldo": 2000, "edad": 67},
]


def edo_cuenta(us):
    return us["saldo"]

def deposito(us, cant):
    us["saldo"] += cant
    return us["saldo"]

def retiro(us, cant):
    if cant > us["saldo"]:
        print("Fondo insuficiente")
        return us["saldo"]
    else:
        us["saldo"] -= cant
        return us["saldo"]


def registrar_usuario():
    try:
        id_user = int(input("Ingrese el ID del nuevo usuario: "))
        nombre = input("Ingrese el nombre del usuario: ")
        tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro/Corriente): ")
        saldo = float(input("Ingrese el saldo inicial: "))
        edad = int(input("Ingrese la edad del usuario: "))

        for usuario in usuarios:
            if usuario["id"] == id_user:
                print("El ID ingresado ya está registrado. Intente con otro ID.")
                return

        nuevo_usuario = {
            "id": id_user,
            "nombre": nombre,
            "tipo_cuenta": tipo_cuenta,
            "saldo": saldo,
            "edad": edad
        }
        usuarios.append(nuevo_usuario)
        print("Usuario registrado exitosamente!")

    except ValueError:
        print("Datos inválidos. Intente nuevamente.")

def gestionar_cuenta():
    intentos = 5
    while intentos != 0:
        try:
            id_user = int(input('Id: '))
            us = next((u for u in usuarios if u["id"] == id_user), None)
            if us is None:
                print('Usuario no encontrado o clave errónea!')
                intentos -= 1
                if intentos == 2:
                    print('Máx de intentos permitidos\nIntente en 5seg ')
                    time.sleep(5)
            else:
                opcion = int(input('''
                    Seleccione la operación que desea realizar
                    ########################
                    1. Estado de cuenta
                    2. Depósito
                    3. Retiro
                    4. Salir
                    ########################
                '''))
                while opcion != 5:
                    if opcion == 1:
                        print(f'Saldo de la cuenta: {edo_cuenta(us)}')
                        break
                    elif opcion == 2:
                        monto = float(input('\nIngrese el monto a depositar: '))
                        print(f'\nSaldo final: {deposito(us, monto)}')
                        break
                    elif opcion == 3:
                        cant = float(input('\nIngrese el monto a retirar: '))
                        print(f'\nSaldo final: {retiro(us, cant)}')
                        break
                    elif opcion == 4:
                        sys.exit()
                        break
                    else:
                        print('Opción no válida. Intente nuevamente.')
                        break
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

        if intentos == 0:
            print('Excedió el número de intentos, clave bloqueada!')

def menu_principal():
    while True:
        print('''
        ########################
        Bienvenido al sistema
        1. Gestionar cuenta de usuario
        2. Registrar nuevo usuario
        3. Salir
        ########################
        ''')
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            gestionar_cuenta()
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()