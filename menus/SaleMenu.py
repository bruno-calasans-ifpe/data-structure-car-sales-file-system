# from controllers.Controllers import sale_controller
from models.Sale import Sale, PartialSaleInput
from menus.General import break_line, create_line, show_option_menu
from controllers.SaleController import SaleController

sale_controller = SaleController()


def show_sale(sale: Sale):
    create_line("-", 40)
    print(f"Id = {sale['id']}")
    print(f"Id do cliente = {sale['client_id']}")
    print(f"Id do vendedor = {sale['seller_id']}")
    print(f"Id do carro = {sale['car_id']}")
    print(f"Data da venda = {sale['date']}")
    print(f"Total da venda = R${sale['total']}")


# para criar um venda
def create_sale_menu():
    print("Você quer cadastrar uma novo venda.")
    print("Insira os dados: ")

    client_id = int(input("Id do cliente: ").strip())
    seller_id = int(input("Id do vendedor: ").strip())
    car_id = int(input("Id do carro: ").strip())
    date = str(input("Data de venda: ").strip())

    sale_controller.create(
        {"client_id": client_id, "seller_id": seller_id, "car_id": car_id, "date": date}
    )


# para mostrar todos os vendaes
def show_all_sales_menu():
    print("Você quer ver as vendas cadastradss")
    print("Listando todos as vendas: ")

    sales = sale_controller.getAll()
    if len(sales) == 0:
        return print("Nenhum venda cadastrada ainda")

    for sale in sales:
        show_sale(sale)
        create_line("-", 40)


# para procurar por um venda
def search_sale_menu():
    print("Você quuer procurar por um venda")
    print("Insira o id do venda.")

    sale_id = int(input("ID: ").strip())
    found_sale = sale_controller.get(sale_id)

    if found_sale != None:
        show_sale(found_sale)


# para remover um venda
def delete_sale_menu():
    print("Você quer excluir um venda")
    print("Insira o id do venda.")
    id = int(input("ID: ").strip())

    create_line("-", 40)
    deleted_sale = sale_controller.delete(id)
    if deleted_sale != None:
        show_sale(deleted_sale)


# para atualizar um venda
def update_sale_menu():
    print("Você quer atualizar uma venda")
    print("Insira o id do venda que você quer encontrar")

    sale_id = int(input("ID: ").strip())
    sale = sale_controller.get(sale_id)

    if sale == None:
        return

    show_sale(sale)
    create_line("-", 40)

    print(
        "Insira os dados que você gostaria de atualizar. Deixe em branco caso não queira atualizar"
    )

    data_to_update: PartialSaleInput = {}

    client_id = int(input("Id do cliente: ").strip() or 0)
    seller_id = int(input("Id do vendedor: ").strip() or 0)
    car_id = int(input("Id do carro: ").strip() or 0)
    date = str(input("Data de venda: ").strip())

    if client_id > 0:
        data_to_update.update({"client_id": int(client_id)})

    if seller_id > 0:
        data_to_update.update({"seller_id": int(seller_id)})

    if car_id > 0:
        data_to_update.update({"car_id": int(car_id)})

    if len(date) > 0:
        data_to_update.update({"date": date})

    sale_controller.update(sale_id, data_to_update)


# menu de venda principal
def sale_menu():
    while True:
        create_line("-", 40)
        print("[MENU DE VENDAS]")
        create_line("-", 40)
        sale_action_option = show_option_menu()

        match sale_action_option:
            case 1:
                create_sale_menu()

            case 2:
                show_all_sales_menu()

            case 3:
                search_sale_menu()

            case 4:
                delete_sale_menu()

            case 5:
                update_sale_menu()

            case 6:
                break
