import os
from input import *
from sql import SQL
from user import User
from product import Product


def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def InitDB():
    sql.CreateTable(
        "users", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(64), surname VARCHAR(64), username VARCHAR(64), password VARCHAR(64), admin BIT")
    adminName = "admin"
    adminPass = "1234"
    if not User.UserExists(User, adminName, adminPass, sql):
        adminUser = User()
        adminUser.Fill((0, "", "", adminName, adminPass, True))
        adminUser.Add(sql)


def LogIn(sql):
    ClearConsole()
    print("[Iniciar Sesión]")
    username = input("Introduzca su username: ")
    password = input("Introduzca su contraseña: ")
    if User.UserExists(User, username, password, sql):
        return User.GetUserByLogIn(User, username, password, sql)
    else:
        return None


def CreateAccount(sql):
    ClearConsole()
    print("[Crear Cuenta]")
    user = User()
    user.SetName()
    user.SetSurname()
    user.SetUsername()
    user.SetPassword()
    user.Add(sql)
    return user


def AdminMenu(sql):
    option = -1
    while option != 6:
        option = AskNumber(
            "[0] Crear Producto\n[1] Modificar Producto\n[2] Eliminar Usuario\n[3] Calcular Facturación (Total)\n[4] Calcular Facturación (Usuario)\n[5] Calcular Facturación (Producto)\n[6] Salir\n", 0, 6)
        match option:
            case 0:
                currentUser = LogIn(sql)
            case 1:
                currentUser = CreateAccount(sql)


sql = SQL()
if sql.IsConnected():
    InitDB()
    currentUser = None
    while currentUser is None:
        match AskNumber("[0] Iniciar Sesión\n[1] Registrar Nueva Cuenta\n", 0, 1):
            case 0:
                currentUser = LogIn(sql)
            case 1:
                currentUser = CreateAccount(sql)
    if currentUser.IsAdmin():
        pass
    else:
        pass
else:
    print("No se ha conseguido conectar con la base de datos.")
