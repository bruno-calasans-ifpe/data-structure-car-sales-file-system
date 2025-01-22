from typing import NotRequired, TypedDict, Required
from db.FileDatabase import FileDatabase
from schema import Schema, And, Use, Optional
from utils.Validation import str_not_empty


class Client(TypedDict):
    id: Required[str]
    name: Required[str]
    cpf: Required[str]


class PartialClientInput(TypedDict):
    name: NotRequired[str]
    cpf: NotRequired[str]


class RequiredClientInput(TypedDict):
    name: Required[str]
    cpf: Required[str]


create_schema = Schema(
    {
        "name": And(Use(str), str_not_empty, error="Nome inválido"),
        "cpf": And(Use(str), str_not_empty, error="CPF inválido"),
    }
)

update_schema = Schema(
    {
        Optional("name"): And(Use(str), str_not_empty, error="Nome inválido"),
        Optional("cpf"): And(Use(str), str_not_empty, error="CPF inválido"),
    }
)

CLIENT_PATH = "./data/clients.json"
client = FileDatabase(CLIENT_PATH, create_schema, update_schema)
