from controllers.Controllers import seller_controller
from models.Seller import Seller
from menus.General import break_line, create_line, show_option_menu


def show_seller(seller: Seller):
    create_line("-", 40)
    print(f"Id = {seller['id']}")
    print(f"Nome = {seller['name']}")
    print(f"CPF = {seller['cpf']}")


# para criar um vendedor
def create_seller_menu():
    print("Você quer cadastrar um novo vendedor.")
    print("Insira os dados: ")

    name = str(input("Nome: ").strip())
    cpf = str(input("CPF: ").strip())

    seller_controller.create({"name": name, "cpf": cpf})


# para mostrar todos os vendedores
def show_all_sellers_menu():
    print("Você quer ver os vendedores cadastrados")
    print("Listando todos os vendedores: ")

    sellers = seller_controller.getAll()
    if len(sellers) == 0:
        return print("Nenhum vendedor cadastrado ainda")

    for seller in sellers:
        show_seller(seller)


# para procurar por um vendedor
def search_seller_menu():
    print("Você quer procurar por um vendedor")
    print("Insira o id do vendedor.")
    seller_id = int(input("ID: ").strip())

    found_seller = seller_controller.get(seller_id)
    if found_seller != None:
        show_seller(found_seller)


# para remover um vendedor
def delete_seller_menu():
    print("Você quer excluir um vendedor")
    print("Insira o id do vendedor.")
    id = int(input("ID: ").strip())

    deleted_seller = seller_controller.delete(id)
    if deleted_seller != None:
        show_seller(deleted_seller)


# para atualizar um vendedor
def update_seller_menu():
    print("Você quer atualizar um vendedor")
    print("Insira o id do vendedor que você quer encontrar")

    id = int(input("ID: ").strip())
    seller = seller_controller.get(id)
    if seller == None:
        return

    show_seller(seller)

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

    seller_controller.update(seller["id"], data_to_update)


# menu de vendedor principal
def seller_menu():
    while True:
        create_line("-", 40)
        print("[MENU DE VENDEDORES]")
        create_line("-", 40)
        seller_action_option = show_option_menu()

        match seller_action_option:
            case 1:
                create_seller_menu()

            case 2:
                show_all_sellers_menu()

            case 3:
                search_seller_menu()

            case 4:
                delete_seller_menu()

            case 5:
                update_seller_menu()

            case 6:
                break
