class Sun:
    __instance = None

    @staticmethod
    def inst():
        """Static access method."""
        if Sun.__instance == None:
            Sun()
        return Sun.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Sun.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Sun.__instance = self
