from src.Tools.common import ClearConsole
from src.Tools.sql import SQL
from src.Models.user import User
from src.Menus.startMenu import StartMenu


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
        User((0, "", "", adminName, adminPass, True)).Add(sql)


ClearConsole()
sql = SQL()
if sql.IsConnected():
    InitDB()
    StartMenu.MainLoop(StartMenu, sql)
else:
    print("No se ha conseguido conectar con la base de datos.")
print("Programa terminado.")
