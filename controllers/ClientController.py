from models.Client import Client, RequiredClientInput, PartialClientInput, client
from schema import SchemaError


class ClientController:

    # cria um novo cliente
    def create(self, client_input: RequiredClientInput):
        try:
            created_client = client.create(client_input)
            print("Cliente criado com sucesso")
            return created_client

        except SchemaError as e:
            print("Dados inválidos")
            for error in e.errors:
                if error != None:
                    print(error)
            return None
        except:
            print("Erro ao criar cliente")

    # pega um cliente pelo id
    def get(self, id: str) -> Client:
        try:
            found_client = client.get("id", id)

            if found_client == None:
                print("Cliente não encontrado")
            else:
                print("Cliente encontrado")

            return found_client
        except:
            print("Error ao encontrar cliente")
            return None

    # pega todos os clientes cadastrados
    def getAll(self) -> list[Client]:
        try:
            clients = client.getAll()
            return clients
        except:
            print("Erro ao pegar todos os clientes")
            return None

    # atualiza um cliente pelo id
    def update(self, client_id: str, client_input: PartialClientInput) -> Client | None:
        try:
            # tenta encontrar cliente
            found_client = self.get(client_id)
            if found_client == None:
                return None

            updated_client = client.update("id", client_id, client_input)
            if updated_client == None:
                print("Atualização do cliente falhou")
            else:
                print("Cliente atualizado com sucesso")
            return updated_client

        except SchemaError as e:
            print("Dados inválidos")
            for error in e.errors:
                if error != None:
                    print(error)
            return None
        except:
            print("Erro ao atualizar cliente")
            return None

    # deleta um cliente pelo id
    def delete(self, id: int) -> Client | None:
        try:
            deleted_client = client.delete("id", id)
            if deleted_client == None:
                print("Cliente não encontrado")
            else:
                print("Cliente removido com sucesso")
            return deleted_client
        except:
            print("Erro ao remover cliente")
            return None
