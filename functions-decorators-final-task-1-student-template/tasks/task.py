from typing import List

def split(data: str, sep=None, maxsplit=-1):
    # initialize an empty list to store the result
    result = []
    # if sep is None, use whitespace as the default separator
    if sep is None:
        sep = " "
    # if maxsplit is negative, split as many times as possible
    if maxsplit < 0:
        maxsplit = len(data)
    # loop through the data and find the indices of the separators
    start = 0
    count = 0
    for i in range(len(data)):
        # if the current character is a separator and the count is less than maxsplit
        if data[i] == sep and count < maxsplit:
            # append the substring from start to i to the result list
            result.append(data[start:i])
            # update the start index to i + 1
            start = i + 1
            # increment the count by 1
            count += 1
    # append the remaining substring from start to the end of the data to the result list
    result.append(data[start:])
    # return the result list
    return result
