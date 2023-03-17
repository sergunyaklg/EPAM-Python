class PriceControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Price must be between 0 and 100.")

class NameControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")

class Book:
    price = PriceControl()
    author = NameControl()
    name = NameControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price