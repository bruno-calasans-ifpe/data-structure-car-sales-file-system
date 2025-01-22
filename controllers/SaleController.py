from models.Sale import Sale, RequiredSaleInput, PartialSaleInput, sale
from controllers.Controllers import client_controller, car_controller, seller_controller
from schema import SchemaError
from datetime import datetime


class SaleController:

    # cria um nova venda
    def create(self, sale_input: RequiredSaleInput) -> Sale | None:
        try:
            client_id = sale_input["client_id"]
            seller_id = sale_input["seller_id"]
            car_id = sale_input["car_id"]

            found_client = client_controller.get(client_id)
            found_seller = seller_controller.get(seller_id)
            found_car = car_controller.get(car_id)

            if found_client == None or found_seller == None or found_car == None:
                return None

            sale_input.update({"total": found_car["price"]})
            created_sale = sale.create(sale_input)

            print("Venda criada com sucesso")
            return created_sale

        except SchemaError as e:
            print("Dados inválidos")
            print(e.autos)
            for error in e.errors:
                if error != None:
                    print(error)
            return None

        except:
            print("Erro ao criar venda")
            return None

    # pega uma venda pelo id
    def get(self, sale_id: int) -> Sale | None:
        try:
            found_sale = sale.get("id", sale_id)
            if found_sale == None:
                print("Venda não encontrada")
            else:
                print("Venda encontrada")

            return found_sale
        except:
            print("Error ao encontrar venda")
            return None

    # pega todos os vendas cadastrados
    def getAll(self) -> list[Sale] | None:
        try:
            sales = sale.getAll()
            return sales
        except:
            print("Erro ao pegar todas as vendas")
            return None

    # atualiza um venda pelo id
    def update(self, sale_id: str, sale_input: PartialSaleInput) -> Sale | None:
        try:
            # tenta encontrar venda
            found_sale = self.get(sale_id)
            if found_sale == None:
                return None

            if "client_id" in sale_input:
                client_id = sale_input["client_id"]
                found_client = client_controller.get(client_id)
                if found_client == None:
                    print("Id do cliente não encontrado")
                    return

            if "seller_id " in sale_input:
                seller_id = sale_input["seller_id"]
                found_seller = seller_controller.get(seller_id)
                if found_seller == None:
                    print("Id do vendedor não encontrado")
                    return

            if "car_id " in sale_input:
                car_id = sale_input["car_id"]
                found_car = car_controller.get(car_id)
                if found_car == None:
                    print("Id do carro não encontrado")
                    return None
                sale_input.update({"total": found_car["price"]})

            # atualiza venda caso encontre e tenha dados válidos
            updated_sale = sale.update("id", sale_id, sale_input)
            print("Venda atualizada com sucesso")
            return updated_sale

        except SchemaError as e:
            print("Dados inválidos")
            for error in e.errors:
                if error != None:
                    print(error)
            return None
        except:
            print("Erro ao atualizar venda")
            return None

    # deleta um venda pelo id
    def delete(self, sale_id: int) -> Sale | None:
        try:
            # tenta encontrar venda
            found_sale = self.get(sale_id)
            if found_sale == None:
                return None

            deleted_sale = sale.delete("id", sale_id)
            if deleted_sale == None:
                print("Venda não encontrada")
            else:
                print("Venda removida com sucesso")

            return deleted_sale
        except:
            print("Erro ao remover venda")
            return None
