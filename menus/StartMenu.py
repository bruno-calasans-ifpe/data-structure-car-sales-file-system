from menus.General import show_main_menu
from menus.ClientMenu import client_menu
from menus.CarMenu import car_menu
from menus.SellerMenu import seller_menu
from menus.SaleMenu import sale_menu


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
                seller_menu()

            case 4:
                sale_menu()

            case 5:
                print("Obrigado por utilizado nosso sistema!")
                break
