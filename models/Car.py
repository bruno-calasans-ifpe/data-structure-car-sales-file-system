from typing import NotRequired, TypedDict, Required
from db.FileDatabase import FileDatabase
from schema import Schema, And, Use, Optional
from utils.Validation import str_not_empty, value_more_than


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


create_schema = Schema(
    {
        "brand": And(Use(str), str_not_empty, error="Marca inválida"),
        "model": And(Use(str), str_not_empty, error="Modelo inválida"),
        "year": And(Use(int), value_more_than(0), error="Ano inválido"),
        "price": And(Use(int), value_more_than(0), error="Preço inválido"),
    }
)

update_schema = Schema(
    {
        Optional("brand"): And(Use(str), str_not_empty, error="Marca inválida"),
        Optional("model"): And(Use(str), str_not_empty, error="Modelo inválida"),
        Optional("year"): And(Use(int), value_more_than(0), error="Ano inválido"),
        Optional("price"): And(Use(int), value_more_than(0), error="Preço inválida"),
    }
)


CAR_PATH = "./data/cars.json"
car = FileDatabase(CAR_PATH, create_schema, update_schema)
