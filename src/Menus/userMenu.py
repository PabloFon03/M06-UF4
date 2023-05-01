from src.Tools.input import *
from src.Models.product import Product
from src.Tools.common import ClearConsole


class UserMenu:
    def __ListProducts(self, sql):
        ClearConsole()
        print("[Lista Productos]")
        for product in Product.GetProducts(Product, sql):
            print(f"- {product.GetName()} ({product.GetPriceText()}€)")
        input()

    def __BuyProducts(self, user, sql):
        shoppingCart = []
        products = Product.GetProducts(Product, sql)
        keepBuying = True
        while keepBuying:
            ClearConsole()
            for i in range(len(products)):
                print(f"[{i}] {products[i].GetName()} ({products[i].GetPriceText()}€)")
            shoppingCart.append(
                products[AskNumber("Seleccione un producto: ", 0, len(products) - 1)])
            ClearConsole()
            print("[Carro Compra]")
            for item in shoppingCart:
                print(f"- {item.GetName()} ({item.GetPriceText()}€)")
            keepBuying = AskYesNo("Deseas seguir comprando?")
        for item in shoppingCart:
            pass

    def __ModifyUser(self, user, sql):
        ClearConsole()
        print(f"Tu nombre es {user.GetName()}.")
        if AskYesNo("Deseas cambiarlo?"):
            user.SetName()
        print(f"Tu apellido es {user.GetSurname()}.")
        if AskYesNo("Deseas cambiarlo?"):
            user.SetSurname()
        print(f"Tu username es {user.GetUsername()}.")
        if AskYesNo("Deseas cambiarlo?"):
            user.SetUsername()
        if AskYesNo("Deseas cambiar tu contraseña?"):
            user.SetPassword()
        user.Update(sql)

    def MainLoop(self, user, sql):
        option = -1
        while option != 3:
            ClearConsole()
            print("[Menú Usuario]")
            print(
                f"Bienvenido/a, {user.GetName()} {user.GetSurname()} ({user.GetUsername()})")
            option = AskNumber(
                "[0] Ver Productos\n[1] Comprar Productos\n[2] Modificar Datos\n[3] Salir\n", 0, 3)
            match option:
                case 0:
                    self.__ListProducts(UserMenu, sql)
                case 1:
                    self.__BuyProducts(UserMenu, user, sql)
                case 2:
                    self.__ModifyUser(UserMenu, user, sql)
