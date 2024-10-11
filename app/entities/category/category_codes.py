from enum import Enum


class CategoryCode(str, Enum):
    BURGER = "burger"
    PIZZA = "pizza"
    CHICKEN = "chicken"
    TACOS = "tacos"
    BBQ = "bbq"
    SUSHI = "sushi"
    SALAD = "salad"
    COFFEE = "coffee"
