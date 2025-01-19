from typing import NotRequired, TypedDict, Required
from controllers.FileDatabase import FileDatabase


class Client(TypedDict):
    id: Required[str]
    name: Required[str]
    cpf: Required[str]


class PartialClientInput(TypedDict):
    name: NotRequired[str]
    cpf: NotRequired[str]


class RequiredClientInput(TypedDict):
    name: Required[str]
    cpf: Required[str]


CLIENT_PATH = "./data/clients.json"
client_db = FileDatabase(CLIENT_PATH)


class ClientController:

    def generate_index(self):
        next_index = len(client_db.getAll()) + 1
        return next_index

    # cria um novo cliente
    def create(self, client_input: PartialClientInput):
        try:
            # generate id
            client_input.update({"id": self.generate_index()})
            client_db.create(client_input)
            # valid input
            if len(client_input["name"]) == 0 or len(client_input["cpf"]) == 0:
                return print("Dados inválidos")
            print("Cliente criado com sucesso")
        except:
            print("Erro ao criar cliente")

    # pega um cliente pelo id
    def get(self, id: str) -> Client:
        try:
            found_client = client_db.get("id", id)
            if found_client == None:
                print("Cliente não encontrado")
            else:
                print("Cliente encontrado")
            return found_client
        except:
            print("Error ao encontrar cliente")

    # pega todos os clientes cadastrados
    def getAll(self) -> list[Client]:
        clients = client_db.getAll()
        return clients

    # atualiza um cliente pelo id
    def update(self, id: str, client_input: PartialClientInput):
        try:
            update_result = client_db.update("id", id, client_input)
            if update_result == True:
                print("Cliente atualizado com sucesso")
            else:
                print("Cliente não encontrado")
        except:
            print("Erro ao atualizar cliente")

    # deleta um cliente pelo id
    def delete(self, id: int):
        try:
            delete_result = client_db.delete("id", id)
            if delete_result == None:
                print("Cliente não encontrado")
            else:
                print("Cliente removido com sucesso")
            return delete_result
        except:
            print("Erro ao remover cliente")
