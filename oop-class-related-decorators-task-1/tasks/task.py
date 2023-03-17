from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        pass

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {self.__class__.__name__}"

    def is_motorcycle(self) -> bool:
        return self.wheels_num() == 2

    @property
    def purchase_price(self) -> float:
        price = self.base_price - 0.1 * self.mileage
        return price if price >= 100_000 else 100_000


class Car(Vehicle):
    def wheels_num(self):
        return 4


class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


class Truck(Vehicle):
    def wheels_num(self):
        return 10


class Bus(Vehicle):
    def wheels_num(self):
        return 6
