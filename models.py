from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class Dish(BaseModel):
    name: str
    cost: int
    weight: Optional[int]
    structure: Optional[int]


class Client(BaseModel):
    name: str
    email: str
    telephone: str
    additionally_info: Optional[str]


class Status(str, Enum):
    new = 'new'
    ready = 'ready'
    delivered = 'delivered'


class Order(BaseModel):
    id: int
    status: Status
    dishes: List[Dish]
    client: Client


class OrdersStory(BaseModel):
    items: List[Order]