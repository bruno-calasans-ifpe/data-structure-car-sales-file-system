from menus.General import show_main_menu
from menus.ClientMenu import client_menu
from menus.CarMenu import car_menu


# programa principal
def start_menu():
    while True:
        main_option = show_main_menu()
        match main_option:
            case 1:
                client_menu()

            case 2:
                car_menu()

            case 3:
                print("Obrigado por utilizado nosso sistema!")
                break
