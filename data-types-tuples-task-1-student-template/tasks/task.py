from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    # Convert the integer to a string
    num_str = str(num)
    # Use a list comprehension to get the digits as integers
    digits = [int(char) for char in num_str]
    # Return the list as a tuple
    return tuple(digits)

