from controllers.Controllers import client_controller
from models.Client import Client
from menus.General import break_line, create_line, show_option_menu


def show_client(client: Client):
    create_line("-", 40)
    print(f"Id = {client['id']}")
    print(f"Nome = {client['name']}")
    print(f"CPF = {client['cpf']}")


# para criar um cliente
def create_client_menu():
    print("Você quer cadastrar um novo cliente.")
    print("Insira os dados: ")

    name = str(input("Nome: ").strip())
    cpf = str(input("CPF: ").strip())

    client_controller.create({"name": name, "cpf": cpf})


# para mostrar todos os clientes
def show_all_clients_menu():
    print("Você quer ver os clientes cadastrados")
    print("Listando todos os clientes: ")

    clients = client_controller.getAll()
    if len(clients) == 0:
        return print("Nenhum cliente cadastrado ainda")

    for client in clients:
        show_client(client)


# para procurar por um cliente
def search_client_menu():
    print("Você quuer procurar por um cliente")
    print("Insira o id do cliente.")
    id = int(input("ID: ").strip())

    found_client = client_controller.get(id)
    if found_client != None:
        show_client(found_client)
        create_line("-", 40)


# para remover um cliente
def delete_client_menu():
    print("Você quer excluir um cliente")
    print("Insira o id do cliente.")
    id = int(input("ID: ").strip())

    deleted_client = client_controller.delete(id)
    if deleted_client != None:
        show_client(deleted_client)
        create_line("-", 40)


# para atualizar um cliente
def update_client_menu():
    print("Você quer atualizar um cliente")

    print("Insira o id do cliente que você quer atualizar")
    client_id = int(input("ID: ").strip())
    client = client_controller.get(client_id)
    if client == None:
        return

    show_client(client)
    create_line("-", 40)

    print(
        "Insira os dados que você gostaria de atualizar. Deixe em branco caso não queira atualizar"
    )

    data_to_update: dict = {}
    name = str(input("Nome: ").strip())
    cpf = str(input("CPF: ").strip())

    if len(name) > 0:
        data_to_update.update({"name": name})

    if len(cpf) > 0:
        data_to_update.update({"cpf": cpf})

    client_controller.update(client_id, data_to_update)


# menu de cliente principal
def client_menu():
    while True:
        create_line("-", 40)
        print("[MENU DE CLIENTES]")
        create_line("-", 40)
        client_action_option = show_option_menu()

        match client_action_option:
            case 1:
                create_client_menu()

            case 2:
                show_all_clients_menu()

            case 3:
                search_client_menu()

            case 4:
                delete_client_menu()

            case 5:
                update_client_menu()

            case 6:
                break
