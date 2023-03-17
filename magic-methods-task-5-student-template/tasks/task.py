import os
import shutil

class TempDir:
    def __init__(self):
        self.temp_dir = None
        self.old_dir = None

    def __enter__(self):
        # create a new temporary directory with a random name
        self.temp_dir = os.path.join(tempfile.gettempdir(), uuid.uuid4().hex)
        os.mkdir(self.temp_dir)
        # save the current working directory
        self.old_dir = os.getcwd()
        # change the current working directory to the temporary one
        os.chdir(self.temp_dir)
        # return the temporary directory name
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # change the current working directory back to the old one
        os.chdir(self.old_dir)
        # remove the temporary directory and all its contents
        shutil.rmtree(self.temp_dir)