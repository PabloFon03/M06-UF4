from src.Tools.input import *
from src.Models.user import User
from src.Models.product import Product

class Receipt:
    def __Fill(self, row):
        self.__id = row[0]
        self.__userId = row[1]
        self.__productId = row[2]
        self.__price = row[3]

    def __init__(self, data=None):
        self.__id = 0
        self.__userId = 0
        self.__productId = 0
        self.__price = 0
        if data:
            self.__Fill(data)

    # Getters
    def GetID(self):
        return self.__id

    def GetPrice(self):
        return self.__price
    
    def GetUser(self, sql):
        return User.GetUserByID(User, self.__userId, sql)
    
    def GetProduct(self, sql):
        return Product.GetProductByID(Product, self.__productId, sql)

    # SQL Methods
    def Add(self, sql):
        self.__id = sql.Insert(
            "receipts", "userId, productId, price", "%s, %s, %s", (self.__userId, self.__productId, self.__price))

    def Delete(self, sql):
        sql.Delete("receipts", "id = %s", (self.__id,))

    # Static Methods
    def GetAllReceipts(self, sql):
        receipts = []
        for row in sql.Select("receipts"):
            receipts.append(Receipt(row))
        return receipts

    def GetAllUserReceipts(self, userId, sql):
        receipts = []
        for row in sql.Select("receipts", "userId = %s", (userId,)):
            receipts.append(Receipt(row))
        return receipts

    def GetAllProductReceipts(self, productId, sql):
        receipts = []
        for row in sql.Select("receipts", "productId = %s", (productId,)):
            receipts.append(Receipt(row))
        return receipts

    def DeleteAllUserReceipts(self, userId, sql):
        sql.Delete("receipts", "userId = %s", (userId,))

    def DeleteAllProductReceipts(self, productId, sql):
        sql.Delete("receipts", "productId = %s", (productId,))
