import functools

def validate(func):
    """A decorator that validates the arguments of set_pixel function."""
    @functools.wraps(func)
    def wrapper(*args):
        # Check if all arguments are integers between 0 and 256
        if all(isinstance(arg, int) and 0 <= arg <= 256 for arg in args):
            # Call the original function
            return func(*args)
        else:
            # Return an error message
            return "Function call is not valid!"
    return wrapper
@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"
