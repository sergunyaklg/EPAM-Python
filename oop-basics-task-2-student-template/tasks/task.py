# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
# Create a class SchoolMember which represents any person in school
class SchoolMember:
    # Move the same logic of initialization to the class SchoolMember
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Classes should have the same interface with the public show () method
    def show(self):
        return f"Name: {self.name}, Age: {self.age}"

# Classes Teacher and Student are inherited from SchoolMember
class Teacher(SchoolMember):
    # Teacher accepts name (str), age (int), salary (int)
    def __init__(self, name, age, salary):
        # Call the parent class constructor
        super().__init__(name, age)
        self.salary = salary

    # Override the show method to include salary
    def show(self):
        return f"{super().show()}, Salary: {self.salary}"

# Classes Teacher and Student are inherited from SchoolMember
class Student(SchoolMember):
    # Student accepts name (str), age (int), grades
    def __init__(self, name, age, grades):
        # Call the parent class constructor
        super().__init__(name, age)
        self.grades = grades

    # Override the show method to include grades
    def show(self):
        return f"{super().show()}, Grades: {self.grades}"
