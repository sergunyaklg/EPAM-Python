from typing import List


def foo(nums: List[int]) -> List[int]:
    # Get the length of the input list
    n = len(nums)
    # Initialize two empty lists to store the left and right products
    left = [0] * n
    right = [0] * n
    # Initialize the output list to store the final result
    output = [0] * n
    # Set the first element of the left list to 1
    left[0] = 1
    # Loop through the input list from left to right
    for i in range(1, n):
        # Compute the cumulative product of the previous elements and store it in the left list
        left[i] = left[i - 1] * nums[i - 1]
    # Set the last element of the right list to 1
    right[n - 1] = 1
    # Loop through the input list from right to left
    for i in range(n - 2, -1, -1):
        # Compute the cumulative product of the next elements and store it in the right list
        right[i] = right[i + 1] * nums[i + 1]
    # Loop through the output list
    for i in range(n):
        # Multiply the corresponding elements from the left and right lists and store it in the output list
        output[i] = left[i] * right[i]
    # Return the output list
    return output
