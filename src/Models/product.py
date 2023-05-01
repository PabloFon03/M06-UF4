from src.Tools.input import *


class Product:
    def Fill(self, row):
        self.__id = row[0]
        self.__name = row[1]
        self.__price = row[2]

    def __init__(self, data=None):
        self.__id = 0
        self.__name = ""
        self.__price = 0
        if data:
            self.Fill(data)

    # Getters
    def GetID(self):
        return self.__id

    def GetName(self):
        return self.__name

    def GetPrice(self):
        return self.__price

    def GetPriceText(self):
        return format(self.__price, ".2f")

    # Setters
    def SetName(self):
        self.__name = AskAlphaNum("Introduzca su nombre: ", 1, 64)

    def SetSurname(self):
        self.__surname = AskAlphaNum("Introduzca su apellido: ", 1, 64)

    def SetUsername(self, sql):
        usernameExists = True
        while usernameExists:
            username = AskAlphaNum("Introduzca su username: ", 1, 64)
            usernameExists = User.UsernameExists(User, username, sql)
            if usernameExists:
                print("Lo sentimos, ese username ya está registrado.")
        self.__username = username

    def SetPassword(self):
        self.__password = AskAlphaNum("Introduzca su contraseña: ", 1, 64)

    # SQL Methods
    def Add(self, sql):
        values = (self.__name, self.__price)
        self.__id = sql.Insert("users", "name, price", "%s, %s", values)

    def Update(self, sql):
        values = (self.__name, self.__price, self.__id)
        sql.Update("products", "name = %s, price = %s", "id = %s", values)

    def Delete(self, sql):
        sql.Delete("products", "id = %s", (self.__id,))

    # Static Methods
    def NameExists(self, name, sql):
        return len(sql.Select("users", "name = %s", (name,))) > 0

    def GetProducts(self, sql):
        products = []
        for row in sql.Select("products"):
            products.append(Product(row))
        return products
