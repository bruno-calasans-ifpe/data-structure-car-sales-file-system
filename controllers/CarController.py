from models.Car import Car, RequiredCarInput, PartialCarInput, car
from schema import SchemaError


class CarController:

    # cria um novo carro
    def create(self, car_input: RequiredCarInput) -> Car | None:
        try:
            created_car = car.create(car_input)
            print("Carro criado com sucesso")
            return created_car

        except SchemaError as e:
            print("Dados inválidos")
            for error in e.errors:
                if error != None:
                    print(error)
            return None
        except:
            print("Erro ao criado carro")

    # pega um carro pelo id
    def get(self, car_id: int) -> Car | None:
        try:
            found_car = car.get("id", car_id)
            if found_car == None:
                print("Carro não encontrado")
            else:
                print("Carro encontrado")
            return found_car
        except:
            print("Error ao encontrar carro")
            return None

    # pega todos os carros cadastrados
    def getAll(self) -> list[Car] | None:
        try:
            cars = car.getAll()
            return cars
        except:
            print("Erro ao pegar todos os carros")
            return None

    # atualiza um carro pelo id
    def update(self, car_id: str, car_input: PartialCarInput) -> Car | None:
        try:
            # tenta encontrar carro
            found_sale = self.get(car_id)
            if found_sale == None:
                return None

            updated_car = car.update("id", car_id, car_input)
            print("Carro atualizado com sucesso")
            return updated_car

        except SchemaError as e:
            print("Dados inválidos")
            for error in e.errors:
                if error != None:
                    print(error)
            return None

        except:
            print("Erro ao atualizar carro")
            return None

    # deleta um carro pelo id
    def delete(self, car_id: int) -> Car | None:
        try:
            deleted_car = car.delete("id", car_id)
            if deleted_car == None:
                print("Carro não encontrado")
            else:
                print("Carro removido com sucesso")

            return deleted_car
        except:
            print("Erro ao remover carro")
            return None
