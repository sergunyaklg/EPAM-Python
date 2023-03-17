from typing import Dict
import time

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    # Define a wrapper function that takes the same arguments as the original function
    def wrapper(*args, **kwargs):
        # Get the start time
        start = time.time()
        # Call the original function and store the result
        result = fn(*args, **kwargs)
        # Get the end time
        end = time.time()
        # Calculate the execution time
        exec_time = end - start
        # Store the execution time in the dictionary with the function name as the key
        execution_time[fn.__name__] = exec_time
        # Return the result of the original function
        return result
    # Return the wrapper function
    return wrapper