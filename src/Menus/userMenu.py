from src.Tools.input import *
from src.Models.product import Product
from src.Tools.common import ClearConsole


class UserMenu:
    def ListProducts(self, sql):
        print(Product.GetProducts(Product, sql))
        input()

    def BuyProducts(self, user, sql):
        shoppingCart = []
        products = Product.GetProducts(Product, sql)
        keepBuying = True
        while keepBuying:
            ClearConsole()
            for i in range(len(products)):
                print(f"[{i}] {products[i].GetName()} ({products[i].GetPrice()}€)")
            shoppingCart.append(
                products[AskNumber("Seleccione un producto: ", 0, len(products) - 1)])
            keepBuying = AskYesNo("Deseas seguir comprando?")
        for product in shoppingCart:
            pass

    def ModifyUser(self, user, sql):
        ClearConsole()
        print(f"Tu nombre es {user.GetName()}.")
        if AskYesNo("Deseas cambiarlo?"):
            user.SetName()
        print(f"Tu nombre es {user.GetName()}.")
        if AskYesNo("Deseas cambiarlo?"):
            user.SetSurname()
        print(f"Tu nombre es {user.GetName()}.")
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
            option = AskNumber(
                "[0] Ver Productos\n[1] Comprar Productos\n[2] Modificar Datos\n[3] Salir\n", 0, 3)
            match option:
                case 0:
                    self.ListProducts(sql)
                case 1:
                    self.BuyProducts(user, sql)
                case 2:
                    self.ModifyUser(user, sql)
