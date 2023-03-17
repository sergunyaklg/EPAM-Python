from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    # Use a set comprehension to get all the values from the dictionaries
    result = {value for dic in lst for value in dic.values()}
    return result
