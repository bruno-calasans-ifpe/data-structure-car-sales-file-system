import json


class FileDatabase:

    def __init__(self, path: str) -> None:
        self.path = path
        try:
            # Tenta carregar o arquivo
            with open(self.path, "r") as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.path, "w") as file:
                json.dump([], file)

    def read(self) -> list[dict]:
        with open(self.path, "r") as file:
            return json.load(file)

    def write(self, data):
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)

    def get(self, key: str, value: any):
        db = self.read()
        for register in db:
            if register[key] == value:
                return register
        return None

    def getAll(self):
        return self.read()

    def create(self, data: dict):
        db = self.read()
        db.append(data)
        self.write(db)

    def update(self, key: str, value: any, data: any):
        db = self.read()
        for register in db:
            if register[key] == value:
                register.update(data)
                self.write(db)
                return True
        return False

    def delete(self, key: str, value: any):
        db = self.read()
        for register in db:
            if register[key] == value:
                db.remove(register)
                self.write(db)
                return register
        return None

    def clear(self):
        try:
            # Tenta carregar o arquivo
            with open(self.path, "w") as file:
                json.dump([], file)
        except:
            print("Erro ao limpar database")
