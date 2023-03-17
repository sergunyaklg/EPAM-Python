import os

class Cd:
    def __init__(self, new_dir):
        # check if the new directory is valid
        if not os.path.isdir(new_dir):
            raise ValueError(f"{new_dir} is not a directory or does not exist")
        # save the current directory
        self.old_dir = os.getcwd()
        # change to the new directory
        self.new_dir = new_dir

    def __enter__(self):
        # enter the context and change the directory
        os.chdir(self.new_dir)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # exit the context and restore the old directory
        os.chdir(self.old_dir)
