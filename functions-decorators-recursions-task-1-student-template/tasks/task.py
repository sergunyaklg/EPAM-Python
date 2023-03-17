from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    # if the sequence is not a list or a tuple, return it as the sum
    if not isinstance(sequence, (list, tuple)):
        return sequence
    # otherwise, loop through each element in the sequence and add the result of calling seq_sum on it
    else:
        total = 0
        for element in sequence:
            total += seq_sum(element)
        return total
