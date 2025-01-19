from typing import NotRequired, TypedDict, Required
from controllers.FileDatabase import FileDatabase


class Car(TypedDict):
    id: Required[str]
    brand: Required[str]
    model: Required[str]
    year: Required[int]
    price: Required[int]


class PartialCarInput(TypedDict):
    brand: NotRequired[str]
    model: NotRequired[str]
    year: NotRequired[int]
    price: NotRequired[int]


class RequiredCarInput(TypedDict):
    brand: Required[str]
    model: Required[str]
    year: Required[int]
    price: Required[int]


CAR_PATH = "./data/cars.json"
car_db = FileDatabase(CAR_PATH)


class CarController:

    def generate_index(self):
        next_index = len(car_db.getAll()) + 1
        return next_index

    # cria um novo carro
    def create(self, car_input: RequiredCarInput):
        try:
            # generate id
            car_input.update({"id": self.generate_index()})
            car_db.create(car_input)
            print("Carro salvo com sucesso")
        except Exception:
            print("Erro ao salvar carro")

    # pega um carro pelo id
    def get(self, car_id: int) -> Car:
        try:
            found_car = car_db.get("id", car_id)
            if found_car == None:
                print("Carro não encontrado")
            else:
                print("Carro encontrado")
            return found_car
        except:
            print("Error ao encontrar carro")

    # pega todos os carros cadastrados
    def getAll(self) -> list[Car]:
        cars = car_db.getAll()
        return cars

    # atualiza um carro pelo id
    def update(self, car_id: str, car_input: PartialCarInput):
        try:
            car_db.update("id", car_id, car_input)
            print("Carro atualizado com sucesso")
        except:
            print("Erro ao atualizar carro")

    # deleta um carro pelo id
    def delete(self, car_id: int):
        try:
            deleted_car = car_db.delete("id", car_id)
            if deleted_car == None:
                print("Carro não encontrado")
            else:
                print("Carro removido com sucesso")

            return deleted_car
        except:
            print("Erro ao remover carro")
