from typing import List, Dict

def combine_dicts(*args):
    # Create an empty dictionary to store the result
    result = {}
    # Loop through each argument
    for arg in args:
        # Check if the argument is a dictionary
        if isinstance(arg, dict):
            # Loop through each key-value pair in the dictionary
            for key, value in arg.items():
                # Check if the key is already in the result
                if key in result:
                    # Add the value to the existing value for the key
                    result[key] += value
                else:
                    # Add a new key-value pair to the result
                    result[key] = value
    # Return the result
    return result
