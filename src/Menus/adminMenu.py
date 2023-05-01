from src.Tools.input import *
from src.Models.product import Product
from src.Tools.common import ClearConsole


class AdminMenu:
    def ListProducts(self, sql):
        ClearConsole()
        print("[Lista Productos]")
        for product in Product.GetProducts(Product, sql):
            print(f"- {product.GetName()} ({product.GetPrice()}€)")
        input()

    def BuyProducts(self, user, sql):
        shoppingCart = []
        products = Product.GetProducts(Product, sql)
        keepBuying = True
        while keepBuying:
            ClearConsole()
            for i in range(len(products)):
                print(f"[{i}] {products[i].GetName()} ({products[i].GetPriceText()}€)")
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
        while option != 6:
            ClearConsole()
            print("[Menú Administrador]")
            option = AskNumber(
                "[0] Crear Producto\n[1] Modificar Producto\n[2] Eliminar Usuario\n[3] Calcular Facturación (Total)\n[4] Calcular Facturación (Usuario)\n[5] Calcular Facturación (Producto)\n[6] Salir\n", 0, 6)
            match option:
                case _:
                    pass
