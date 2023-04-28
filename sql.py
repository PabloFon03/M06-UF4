import mysql.connector

class SQL:

    def __init__(self):
        self.__conn = mysql.connector.connect(host="localhost", user="root", password="", database="tienda")
        self.__cursor = self.__conn.cursor(buffered=True) if self.__conn else None

    def IsConnected(self):
        return self.__conn is not None

    def DisconnectFromDB(self):
        if self.__conn:
            self.__conn.close()

    def RunCommand(self, query, params = None):
        if self.__conn:
            if params:
                self.__cursor.execute(query, params)
            else:
                self.__cursor.execute(query)
            self.__conn.commit()
            if self.__cursor.with_rows:
                return self.__cursor.fetchall()
            else:
                return None
        else:
            print("No Connection")
            return None
        
    def CreateTable(self, name, columns):
        return self.RunCommand(f"CREATE TABLE IF NOT EXISTS {name} ({columns})")

    def Select(self, table, conditions = "1=1", params = None, columns = "*"):
        return self.RunCommand(f"SELECT {columns} FROM {table} WHERE {conditions}", params)

    def Update(self, table, columns, conditions = "1=1", params = None):
        return self.RunCommand(f"UPDATE {table} SET {columns} WHERE {conditions}", params)

    def Insert(self, table, columns, values, params = None):
        return self.RunCommand(f"INSERT INTO {table} ({columns}) VALUES ({values})", params)
    
    def Delete(self, table, conditions = "1=1", params = None):
        return self.RunCommand(f"DELETE FROM {table} WHERE {conditions}", params)