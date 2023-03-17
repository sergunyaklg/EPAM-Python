# Implement a Counter class that optionally accepts the start value and the counter stop value
class Counter:
    # If the start value is not specified the counter should begin with 0
    def __init__(self, start=0, stop=None):
        self.value = start
        self.stop = stop

    # Implement two methods: "increment" and "get"
    def increment(self):
        # If the counter reaches the stop value, print "Maximal value is reached."
        if self.stop is not None and self.value == self.stop:
            print("Maximal value is reached.")
        else:
            # Increment the counter by one
            self.value += 1

    def get(self):
        # Return the current value of the counter
        return self.value