from src.Tools.common import ClearConsole
from src.Tools.input import *
from src.Models.user import User
from src.Menus.userMenu import UserMenu
from src.Menus.adminMenu import AdminMenu


class StartMenu:
    def __LogIn(self, sql):
        ClearConsole()
        print("[Iniciar Sesión]")
        username = input("Introduzca su username: ")
        password = input("Introduzca su contraseña: ")
        if User.UserExists(User, username, password, sql):
            return User.GetUserByLogIn(User, username, password, sql)
        else:
            print("Usuario no encontado.")
            input()
            return None

    def __CreateAccount(self, sql):
        ClearConsole()
        print("[Crear Cuenta]")
        user = User()
        user.SetName()
        user.SetSurname()
        user.SetUsername()
        user.SetPassword()
        user.Add(sql)
        return user

    def MainLoop(self, sql):
        currentUser = None
        while currentUser is None:
            ClearConsole()
            print("[Menú Inicio]")
            match AskNumber("[0] Iniciar Sesión\n[1] Registrar Nueva Cuenta\n", 0, 1):
                case 0:
                    currentUser = self.__LogIn(StartMenu, sql)
                case 1:
                    currentUser = self.__CreateAccount(StartMenu, sql)
        if currentUser.IsAdmin():
            AdminMenu.MainLoop(AdminMenu, currentUser, sql)
        else:
            UserMenu.MainLoop(UserMenu, currentUser, sql)
