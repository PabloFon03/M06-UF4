from src.Tools.input import *
from src.Tools.common import FormatPrice


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

    def ToString(self):
        return f"{self.__name} ({FormatPrice(self.__price)})"

    # Setters
    def SetName(self, sql):
        nameExists = True
        while nameExists:
            name = AskAlphaNum("Introduzca el nombre del producto: ", 1, 64)
            nameExists = Product.NameExists(Product, name, sql)
            if nameExists:
                print("Ya existe un producto con ese nombre.")
        self.__name = name

    def SetPrice(self):
        self.__price = AskDecimalNumber(
            "Introduzca el precio del producto: ", 0.01, 99999999)

    # SQL Methods
    def Add(self, sql):
        values = (self.__name, self.__price)
        self.__id = sql.Insert("products", "name, price", "%s, %s", values)

    def Update(self, sql):
        values = (self.__name, self.__price, self.__id)
        sql.Update("products", "name = %s, price = %s", "id = %s", values)

    def Delete(self, sql):
        sql.Delete("products", "id = %s", (self.__id,))

    # Static Methods
    def NameExists(self, name, sql):
        return len(sql.Select("products", "name = %s", (name,))) > 0

    def GetProductByID(self, id, sql):
        userData = sql.Select("products", "id = %s", (id,))
        if len(userData) > 0:
            return Product(userData[0])
        else:
            return None

    def GetProducts(self, sql):
        products = []
        for row in sql.Select("products"):
            products.append(Product(row))
        return products
