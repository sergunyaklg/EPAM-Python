import functools

def decorator_apply(func):
    """A decorator factory that applies a given function to the result of the decorated function."""
    def decorator(decorated_func):
        """A decorator that returns the result of func applied to the result of decorated_func."""
        @functools.wraps(decorated_func)
        def wrapper(*args, **kwargs):
            # Call the decorated function and get its result
            result = decorated_func(*args, **kwargs)
            # Apply the given function to the result and return it
            return func(result)
        return wrapper
    return decorator

@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int): 
    return num