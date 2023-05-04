from src.Tools.common import *
from src.Tools.input import *
from src.Models.user import User
from src.Models.product import Product
from src.Models.receipt import Receipt


class AdminMenu:
    def AddProduct(self, sql):
        ClearConsole()
        print("[Crear Producto]")
        product = Product()
        product.SetName(sql)
        product.SetPrice()
        product.Add(sql)

    def ModifyProduct(self, sql):
        ClearConsole()
        print("[Modificar Producto]")
        products = Product.GetProducts(Product, sql)
        for i in range(len(products)):
            print(
                f"[{i}] {products[i].ToString()}")
        product = products[AskNumber(
            "Seleccione el producto a modificar: ", 0, len(products) - 1)]
        ClearConsole()
        print("[Modificar Producto]")
        print(f"El nombre del producto es {product.GetName()}.")
        if AskYesNo("Deseas cambiar el nombre del producto?"):
            product.SetName(sql)
        ClearConsole()
        print("[Modificar Producto]")
        print(f"El precio del producto es {FormatPrice(product.GetPrice())}.")
        if AskYesNo("Deseas cambiar el precio del producto?"):
            product.SetPrice()
        product.Update(sql)

    def DeleteUser(self, sql):
        ClearConsole()
        print("[Eliminar usuario]")
        users = User.GetUsers(User, sql)
        for i in range(len(users)):
            print(f"[{i}] {users[i].ToString()}")
        user = users[AskNumber(
            "Seleccione el usuario a eliminar: ", 0, len(users) - 1)]
        # Receipt.DeleteAllUserReceipts(user.GetID())
        user.Delete(sql)

    def ShowReceipts(self, receipts, sectionName, sql):
        ClearConsole()
        print(sectionName)
        sum = 0
        for receipt in receipts:
            sum += receipt.GetPrice()
        print(f"Facturación Total: {FormatPrice(sum)}")
        if len(receipts) > 0:
            if AskYesNo("Mostar Facturas?"):
                spacing = "----------------------------------------------------------------------------"
                for receipt in receipts:
                    print(spacing)
                    user = receipt.GetUser(sql)
                    print("- Usuario: " + user.ToString()
                          if user else "(Usuario Eliminado)")
                    product = receipt.GetProduct(sql)
                    print(
                        "- Producto: " + product.ToString() if product else "(Producto Eliminado)")
                    print(f"- Importe: {FormatPrice(receipt.GetPrice())}")
                    print(spacing)
        else:
            print("No hay facturas que mostrar.")
        input()

    def ShowAllReceipts(self, sql):
        self.ShowReceipts(AdminMenu, Receipt.GetAllReceipts(
            Receipt, sql), "[Calcular Facturación (Total)]", sql)

    def ShowUserReceipts(self, sql):
        ClearConsole()
        print("[Calcular Facturación (Usuario)]")
        receipts = Receipt.GetAllUserReceipts(Receipt, sql)
        sum = 0
        for receipt in receipts:
            sum += receipt.GetPrice()
        print(f"Facturación Total: {FormatPrice(sum)}")
        input()

    def MainLoop(self, sql):
        option = -1
        while option != 6:
            ClearConsole()
            print("[Menú Administrador]")
            option = AskNumber(
                "[0] Crear Producto\n[1] Modificar Producto\n[2] Eliminar Usuario\n[3] Calcular Facturación (Total)\n[4] Calcular Facturación (Usuario)\n[5] Calcular Facturación (Producto)\n[6] Salir\n", 0, 6)
            match option:
                case 0:
                    self.AddProduct(AdminMenu, sql)
                case 1:
                    self.ModifyProduct(AdminMenu, sql)
                case 2:
                    self.DeleteUser(AdminMenu, sql)
                case 3:
                    self.ShowAllReceipts(AdminMenu, sql)
                case 3:
                    self.ShowAllReceipts(AdminMenu, sql)
