def create_options_menu(options: list[str]):
    for index in range(0, len(options)):
        print(f"[{index + 1}] {options[index]}")


def check_valid_option(option, options: list[str]):
    if option <= 0 or option > len(options):
        raise Exception()


def show_main_menu():
    options = ["Cliente", "Carros", "Sair"]
    while True:
        try:
            create_line("-", 40)
            print("[MENU PRINCIPAL]")
            create_line("-", 40)
            print("Esolha uma das opções abaixo: ")
            create_options_menu(options)
            option = int(input().strip())
            check_valid_option(option, options)
            break

        except:
            print("Opção inválida")
    return option


def show_option_menu():
    options = [
        "Cadastrar",
        "Listar todos",
        "Procurar",
        "Excluir",
        "Atualizar",
        "Voltar",
    ]
    while True:
        try:
            print("Esolha uma das opções abaixo: ")
            create_options_menu(options)
            option = int(input().strip())
            check_valid_option(option, options)
            break

        except:
            print("Opção inválida")
    return option


def break_line(num=1):
    print("\n" * num)


def create_line(char="-", lenght=10):
    print(f"{char}" * lenght)
