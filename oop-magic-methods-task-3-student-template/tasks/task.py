from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    rate = {
        "EUR": 1.0,
        "USD": 2.0,
        "GBP": 0.01,
    }

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        rate = cls.rate[other_cls.__name__] / cls.rate[cls.__name__]
        return f"{rate} {other_cls.__name__} for 1 {cls.__name__}"

    def to_currency(self, other_cls: Type[Currency]):
        rate = self.rate[other_cls.__name__] / self.rate[self.__class__.__name__]
        value = self.value / self.rate[self.__class__.__name__] * self.rate[other_cls.__name__]
        return other_cls(value=value)


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass
