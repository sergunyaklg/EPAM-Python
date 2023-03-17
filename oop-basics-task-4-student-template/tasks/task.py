# Implement a custom dictionary that will memorize the 5 latest changed keys
class HistoryDict:
    # Initialize the dictionary with a given data and an empty history list
    def __init__(self, data):
        self.data = data
        self.history = []

    # Set a new value for a given key and update the history list
    def set_value(self, key, value):
        # Assign the value to the key in the data dictionary
        self.data[key] = value
        # Append the key to the history list
        self.history.append(key)
        # If the history list has more than 5 elements, remove the oldest one
        if len(self.history) > 5:
            self.history.pop(0)

    # Using method "get_history" return these keys
    def get_history(self):
        return self.history
