import json
from schema import Schema, And, Use, Optional, SchemaError


class FileDatabase:

    def __init__(self, path: str, create_schema: Schema, update_schema: Schema) -> None:
        self.path = path
        self.create_schema = create_schema
        self.update_schema = update_schema
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
        self.valid_create_input(data)
        id = self.generate_id()
        data.update({"id": id})
        db = self.read()
        db.append(data)
        self.write(db)
        return data

    def update(self, key: str, value: any, data: any):
        self.valid_update_input(data)
        db = self.read()
        for register in db:
            if register[key] == value:
                register.update(data)
                self.write(db)
                return register
        return None

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

    def generate_id(self):
        next_index = len(self.getAll()) + 1
        return next_index

    def valid_create_input(self, input: dict):
        return self.create_schema.validate(input)

    def valid_update_input(self, input: dict):
        return self.update_schema.validate(input)
