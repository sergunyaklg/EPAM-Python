def replacer(s: str) -> str:
    # create an empty list
    new_s = []
    # loop over each character in the string
    for char in s:
        # check if the character is "
        if char == '"':
            # swap it with '
            new_s.append("'")
        # check if the character is '
        elif char == "'":
            # swap it with "
            new_s.append('"')
        # otherwise
        else:
            # keep it as it is
            new_s.append(char)
    # join the list into a new string
    return "".join(new_s)