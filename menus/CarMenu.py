from controllers.Controllers import car_controller
from models.Car import Car
from menus.General import break_line, create_line, show_option_menu


def show_car(car: Car):
    create_line("-", 40)
    print(f"Id = {car['id']}")
    print(f"Marca = {car['brand']}")
    print(f"Modelo = {car['model']}")
    print(f"Ano = {car['year']:.2f}")
    print(f"Preço = R${car['price']:.2f}")


# para criar um carro
def create_car_menu():
    print("Você quer cadastrar um novo carro.")
    print("Insira os dados: ")

    brand = str(input("Marca: ").strip())
    model = str(input("Modelo: ").strip())
    year = int(input("Ano: ").strip())
    price = int(input("Preço: ").strip())

    car_controller.create(
        {
            "brand": brand,
            "model": model,
            "year": year,
            "price": price,
        }
    )


# para mostrar todos os carros
def show_all_cars_menu():
    print("Você quer ver os carros cadastrados")
    print("Listando todos os carros: ")

    cars = car_controller.getAll()
    if len(cars) == 0:
        return print("Nenhum carro cadastrado ainda")

    for car in cars:
        show_car(car)


# para procurar por um carro
def search_carmenu():
    print("Você quuer procurar por um carro")
    print("Insira o id do carro.")
    id = int(input("ID: ").strip())
    found_car = car_controller.get(id)
    if found_car != None:
        show_car(found_car)


# para remover um carro
def delete_carmenu():
    print("Você quer excluir um carro")
    print("Insira o id do carro.")
    id = int(input("ID: ").strip())

    deleted_car = car_controller.delete(id)
    if deleted_car != None:
        show_car(deleted_car)


# para atualizar um carro
def update_carmenu():
    print("Você quer atualizar um carro")

    print("Insira o id do carro que você quer atualizar")
    car_id = int(input("ID: ").strip())
    found_car = car_controller.get(car_id)

    if found_car == None:
        return
    create_line("-", 40)
    show_car(found_car)
    create_line("-", 40)

    print(
        "Insira os dados que você gostaria de atualizar. Deixe em branco caso não queira atualizar"
    )

    data_to_update: dict = {}
    brand = str(input("Marca: ").strip())
    model = str(input("Modelo: ").strip())
    year = int(input("Ano: ").strip() or 0)
    price = int(input("Preço: ").strip() or 0)

    if len(brand) > 0:
        data_to_update.update({"brand": brand})

    if len(model) > 0:
        data_to_update.update({"model": model})

    if year < 0:
        data_to_update.update({"year": year})

    if price < 0:
        data_to_update.update({"price": price})

    car_controller.update(car_id, data_to_update)


# menu de carro principal
def car_menu():
    while True:
        create_line("-", 40)
        print("[MENU DE CARROS]")
        create_line("-", 40)
        caraction_option = show_option_menu()

        match caraction_option:
            case 1:
                create_car_menu()

            case 2:
                show_all_cars_menu()

            case 3:
                search_carmenu()

            case 4:
                delete_carmenu()

            case 5:
                update_carmenu()

            case 6:
                break
