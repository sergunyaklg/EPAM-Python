class Field:
    __value = None
    def __init__(self):
        self.__value = None

    # get_value method returns the value of the private attribute __value
    def get_value(self):
        return self.__value

    # set_value method assigns a new value to the private attribute __value
    def set_value(self, new_value):
        self.__value = new_value