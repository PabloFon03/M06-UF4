from src.Tools.common import ClearConsole
from src.Tools.input import *
from src.Tools.sql import SQL
from src.Models.user import User
from src.Menus.userMenu import UserMenu


def InitDB():
    # Users Table
    sql.CreateTable(
        "users", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(64), surname VARCHAR(64), username VARCHAR(64), password VARCHAR(64), admin BIT")
    # Products Table
    sql.CreateTable(
        "products", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(64), price FLOAT")
    # Receipts Table
    sql.CreateTable(
        "receipts", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, userId INT NOT NULL, productId INT NOT NULL, price FLOAT")
    # Admin User
    adminName = "admin"
    adminPass = "1234"
    if not User.UserExists(User, adminName, adminPass, sql):
        adminUser = User((0, "", "", adminName, adminPass, True))
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


ClearConsole()
sql = SQL()
if sql.IsConnected():
    # Borrar esto
    # Borrar esto
    # Borrar esto
    # Borrar esto
    # Borrar esto
    sql.RunCommand("DROP TABLE users")
    # sql.RunCommand("DROP TABLE products")
    sql.RunCommand("DROP TABLE receipts")
    # Borrar esto
    # Borrar esto
    # Borrar esto
    # Borrar esto
    # Borrar esto
    InitDB()
    currentUser = None
    menu = UserMenu()
    menu.MainLoop(currentUser, sql)
    while currentUser is None:
        match AskNumber("[0] Iniciar Sesión\n[1] Registrar Nueva Cuenta\n", 0, 1):
            case 0:
                currentUser = LogIn(sql)
            case 1:
                currentUser = CreateAccount(sql)
    if currentUser.IsAdmin():
        AdminMenu(sql)
    else:
        print("b")
else:
    print("No se ha conseguido conectar con la base de datos.")
print("Programa terminado.")
