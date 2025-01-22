from typing import NotRequired, TypedDict, Required
from db.FileDatabase import FileDatabase
from schema import Schema, And, Use, Optional
from utils.Validation import str_not_empty


class Sale(TypedDict):
    id: Required[str]
    seller_id: Required[str]
    client_id: Required[str]
    car_id: Required[str]
    date: Required[str]
    total: Required[int]


class PartialSaleInput(TypedDict):
    seller_id: NotRequired[str]
    client_id: NotRequired[str]
    car_id: NotRequired[str]
    date: NotRequired[str]
    total: NotRequired[int]


class RequiredSaleInput(TypedDict):
    seller_id: Required[str]
    client_id: Required[str]
    car_id: Required[str]
    date: Required[str]
    total: Required[int]


create_schema = Schema(
    {
        "client_id": And(Use(str), str_not_empty, error="Id de cliente inválido"),
        "seller_id": And(Use(str), str_not_empty, error="Id de vendedor inválido"),
        "car_id": And(Use(str), str_not_empty, error="Id de carro inválido"),
        "date": And(Use(str), str_not_empty, error="Data de venda inválida"),
        "total": And(Use(int)),
    }
)

update_schema = Schema(
    {
        Optional("client_id"): And(
            Use(str), str_not_empty, error="Id de cliente inválido"
        ),
        Optional("seller_id"): And(
            Use(str), str_not_empty, error="Id de vendedor inválido"
        ),
        Optional("car_id"): And(Use(str), str_not_empty, error="Id de carro inválido"),
        Optional("date"): And(Use(str), str_not_empty, error="Data de venda inválida"),
        Optional("total"): And(Use(int)),
    }
)

SALE_PATH = "./data/sales.json"
sale = FileDatabase(SALE_PATH, create_schema, update_schema)
