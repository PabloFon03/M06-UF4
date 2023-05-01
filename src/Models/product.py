class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
    def GetID(self):
        return self.__id
    def GetName(self):
        return self.__name
    def GetPrice(self):
        return self.__price
    def Update(self, sql):
        values=(self.__name, self.__price, self.__id)
        sql.Update("products", "name = %s, price = %s", "id = %s", values)
    def GetProducts(self, sql):
        return sql.Select("products")