# Define the base class Bird
class Bird:
    # Initialize the name attribute
    def __init__(self, name):
        self.name = name

    # Define the fly method
    def fly(self):
        print(f"{self.name} bird can fly")

    # Define the walk method
    def walk(self):
        print(f"{self.name} bird can walk")

    # Define the str method
    def __str__(self):
        return f"{self.name} bird can walk and fly"


# Define the subclass FlyingBird that inherits from Bird
class FlyingBird(Bird):
    # Initialize the name and ration attributes
    def __init__(self, name, ration="grains"):
        super().__init__(name)  # Call the parent constructor
        self.ration = ration  # Set the default value for ration

    # Define the eat method
    def eat(self):
        print(f"It eats mostly {self.ration}")


# Define the subclass NonFlyingBird that inherits from Bird but overrides the fly method
class NonFlyingBird(Bird):
    # Initialize the name and ration attributes
    def __init__(self, name, ration="worms"):
        super().__init__(name)  # Call the parent constructor
        self.ration = ration  # Set the default value for ration

    # Override the fly method with an AttributeError exception
    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    # Define a new swim method
    def swim(self):
        print(f"{self.name} bird can swim")

    # Override the str method to include swimming ability
    def __str__(self):
        return f"{self.name} bird can walk and swim"

        # Define a different eat method than FlyingBird

    def eat(self):
        print(f"It eats mostly {self.ration}")


# Define a subclass SuperBird that inherits from both FlyingBird and NonFlyingBird using multiple inheritance
class SuperBird(FlyingBird, NonFlyingBird):
    pass  # No need to define any new methods or attributes