from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    This function prints a part of the multiplication table with proper formatting
    """
    # Create an empty list to store the results
    result = []
    # Loop over the rows from row_start to row_end
    for row in range(row_start, row_end + 1):
        # Create an empty list to store the current row
        current_row = []
        # Loop over the columns from column_start to column_end
        for col in range(column_start, column_end + 1):
            # Append the product of row and col to the current row
            current_row.append(row * col)
        # Append the current row to the result list
        result.append(current_row)
    # Loop over the result list and print each row with formatting
    for row in result:
        # Use a list comprehension to convert each number to a string with 4 spaces
        print_row = [f"{num:4}" for num in row]
        # Join the strings with a space and print them
        print(" ".join(print_row))
    # Return the result list
    return result