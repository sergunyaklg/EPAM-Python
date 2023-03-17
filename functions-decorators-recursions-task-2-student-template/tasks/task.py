from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    # initialize an empty result list
    result = []
    # loop through each element in the sequence
    for element in sequence:
        # try to iterate over the element
        try:
            # extend the result list with another call to linear_seq on that element
            result.extend(linear_seq(element))
        # if the element is not iterable, catch the TypeError exception
        except TypeError:
            # append the element to the result list
            result.append(element)
    # return the result list
    return result
