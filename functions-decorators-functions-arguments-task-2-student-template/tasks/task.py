def union(*args) -> set:
    # Create an empty set to store the result
    result = set()
    # Loop through each argument
    for arg in args:
        # Convert the argument to a set and union it with the result
        result = result | set(arg)
    # Return the result
    return result

def intersect(*args) -> set:
    # Check if there is at least one argument
    if args:
        # Convert the first argument to a set and assign it to the result
        result = set(args[0])
        # Loop through the remaining arguments
        for arg in args[1:]:
            # Convert the argument to a set and intersect it with the result
            result = result & set(arg)
        # Return the result
        return result
    else:
        # If there are no arguments, return an empty set
        return set()
