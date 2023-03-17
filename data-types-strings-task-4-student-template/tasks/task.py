def check_str(s: str):
    # Convert the string to lowercase and remove any spaces
    string = s.lower().replace(" ", "")
    # Initialize two pointers at the start and end of the string
    left = 0
    right = len(string) - 1
    # Loop until the pointers meet in the middle
    while left < right:
        # Compare the characters at the pointers
        if string[left] != string[right]:
            # If they don't match, return False
            return False
        # Move the pointers one step closer to the middle
        left += 1
        right -= 1
    # If the loop ends without returning False, return True
    return True