from src.Tools.input import *


class User:

    def Fill(self, row):
        self.__id = row[0]
        self.__name = row[1]
        self.__surname = row[2]
        self.__username = row[3]
        self.__password = row[4]
        self.__isAdmin = row[5]

    def __init__(self, data=None):
        self.__id = 0
        self.__name = ""
        self.__surname = ""
        self.__username = ""
        self.__password = ""
        self.__isAdmin = False
        if data:
            self.Fill(data)

    # Getters
    def GetID(self):
        return self.__id

    def GetName(self):
        return self.__name

    def GetSurname(self):
        return self.__surname

    def GetUsername(self):
        return self.__username

    def IsAdmin(self):
        return self.__isAdmin

    def ToString(self):
        return f"{self.__name} {self.__surname} ({self.__username})"

    # Setters
    def SetName(self):
        self.__name = AskAlphaNum("Introduzca su nombre: ", 1, 64)

    def SetSurname(self):
        self.__surname = AskAlphaNum("Introduzca su apellido: ", 1, 64)

    def SetUsername(self, sql):
        usernameExists = True
        while usernameExists:
            username = AskAlphaNum("Introduzca su username: ", 1, 64)
            usernameExists = username != self.__username and User.UsernameExists(
                User, username, sql)
            if usernameExists:
                print("Lo sentimos, ese username ya está registrado.")
        self.__username = username

    def SetPassword(self):
        self.__password = AskAlphaNum("Introduzca su contraseña: ", 1, 64)

    # SQL Methods
    def Add(self, sql):
        values = (self.__name, self.__surname,
                  self.__username, self.__password, self.__isAdmin)
        self.__id = sql.Insert(
            "users", "name, surname, username, password, admin", "%s, %s, %s, %s, %s", values)
        print(self.__id)

    def Update(self, sql):
        values = (self.__name, self.__surname,
                  self.__username, self.__password, self.__isAdmin, self.__id)
        sql.Update(
            "users", "name = %s, surname = %s, username = %s, password = %s, admin = %s", "id = %s", values)

    def Delete(self, sql):
        sql.Delete("users", "id = %s", (self.__id,))

    # Static Methods
    def UsernameExists(self, username, sql):
        return len(sql.Select("users", "username = %s", (username,))) > 0

    def UserExists(self, username, password, sql):
        return len(sql.Select("users", "username = %s AND password = %s", (username, password), "id")) > 0

    def GetUserByLogIn(self, username, password, sql):
        userData = sql.Select(
            "users", "username = %s AND password = %s", (username, password))
        if len(userData) > 0:
            return User(userData[0])
        else:
            return None

    def GetUserByID(self, id, sql):
        userData = sql.Select("users", "id = %s", (id,))
        if len(userData) > 0:
            return User(userData[0])
        else:
            return None

    def GetUsers(self, sql):
        users = []
        for row in sql.Select("users"):
            users.append(User(row))
        return users
