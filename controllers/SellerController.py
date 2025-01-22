from models.Seller import Seller, PartialSellerInput, RequiredSellerInput, seller
from schema import SchemaError


class SellerController:

    # cria um novo vendedor
    def create(self, seller_input: RequiredSellerInput) -> Seller | None:
        try:
            created_seller = seller.create(seller_input)
            print("Vendedor criado com sucesso")
            return created_seller

        except SchemaError as e:
            print("Dados inválidos")
            for error in e.errors:
                if error != None:
                    print(error)
            return None

        except:
            print("Erro ao criar Vendedor")

    # pega um Vendedor pelo id
    def get(self, seller_id: str) -> Seller | None:
        try:
            found_seller = seller.get("id", seller_id)
            if found_seller == None:
                print("Vendedor não encontrado")
            else:
                print("Vendedor encontrado")
            return found_seller
        except:
            print("Error ao encontrar Vendedor")
            return None

    # pega todos os Vendedores cadastrados
    def getAll(self) -> list[Seller] | None:
        try:
            sellers = seller.getAll()
            return sellers
        except:
            print("Erro ao encontrar todos os vendedores")
            return None

    # atualiza um Vendedor pelo id
    def update(self, seller_id: str, seller_input: PartialSellerInput) -> Seller | None:
        try:
            updated_seller = seller.update("id", seller_id, seller_input)
            print("Vendedor atualizado com sucesso")
            return updated_seller
        except:
            print("Erro ao atualizar Vendedor")
            return None

    # deleta um vendedor pelo id
    def delete(self, seller_id: int) -> Seller | None:
        try:
            delete_result = seller.delete("id", seller_id)
            if delete_result == None:
                print("Vendedor não encontrado")
            else:
                print("Vendedor removido com sucesso")
            return delete_result
        except:
            print("Erro ao remover Vendedor")
