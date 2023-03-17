from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # Check if the input list has only one element
    if len(lst) == 1:
        # Return an empty list
        return []
    # Use a list comprehension to create tuples of pairs
    pairs = [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
    # Return the list of pairs
    return pairs
