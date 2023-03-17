from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # Create an empty dictionary to store the frequency of characters
    d = dict()
    # Convert the string to lowercase to ignore the case of letters
    s = s.lower()
    # Loop through each character in the string
    for c in s:
        # If the character is already in the dictionary, increment its value by 1
        if c in d:
            d[c] += 1
        # Otherwise, add the character to the dictionary with an initial value of 1
        else:
            d[c] = 1
    # Return the dictionary with the frequencies of characters
    return d
