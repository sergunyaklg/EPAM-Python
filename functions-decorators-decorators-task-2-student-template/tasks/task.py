import time

def log(fn):
    """
    Write a decorator which logs information about calls of decorated function,
    values of its arguments, values of keyword arguments and execution time.
    Log should be written to a file.
    """
    # Define a wrapper function that takes the same arguments as the original function
    def wrapper(*args, **kwargs):
        # Open a file named log.txt in append mode
        with open("log.txt", "a") as f:
            # Get the start time
            start = time.time()
            # Call the original function and store the result
            result = fn(*args, **kwargs)
            # Get the end time
            end = time.time()
            # Calculate the execution time
            exec_time = end - start
            # Format the arguments and keyword arguments as strings
            args_str = ", ".join([f"{k}={v}" for k, v in zip(fn.__code__.co_varnames, args)])
            kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
            # Write the function name, arguments, keyword arguments and execution time to the file
            f.write(f"{fn.__name__}; args: {args_str}; kwargs: {kwargs_str}; execution time: {exec_time} sec.\n")
        # Return the result of the original function
        return result
    # Return the wrapper function
    return wrapper