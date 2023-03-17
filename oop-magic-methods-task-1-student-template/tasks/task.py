from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, other):
        # check if other is a string
        if isinstance(other, str):
            # create a new list of strings
            result = []
            # loop through the elements of self.values
            for num in self.values:
                # append a string with num and other separated by space
                result.append(str(num) + " " + other)
            # return the result list
            return result
        else:
            # raise an exception if other is not a string
            raise TypeError("other must be a string")
