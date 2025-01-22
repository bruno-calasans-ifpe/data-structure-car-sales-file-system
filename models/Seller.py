from typing import NotRequired, TypedDict, Required
from db.FileDatabase import FileDatabase
from schema import Schema, And, Use, Optional
from utils.Validation import str_not_empty


class Seller(TypedDict):
    id: Required[str]
    name: Required[str]
    cpf: Required[str]


class PartialSellerInput(TypedDict):
    name: NotRequired[str]
    cpf: NotRequired[str]


class RequiredSellerInput(TypedDict):
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


SELLER_PATH = "./data/sellers.json"
seller = FileDatabase(SELLER_PATH, create_schema, update_schema)
