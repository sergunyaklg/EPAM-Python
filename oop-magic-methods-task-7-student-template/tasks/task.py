import datetime
import time
from contextlib import ContextDecorator


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = time.monotonic()
        self.start_date = datetime.datetime.now()
        self.file = open(self.filename, 'a')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        run_time = time.monotonic() - self.start_time
        error_message = 'None' if exc_type is None else str(exc_value)
        log_message = f'Start: {self.start_date} | Run: {datetime.timedelta(seconds=run_time)} | An error occurred: {error_message}\n'
        self.file.write(log_message)
        self.file.close()
        if exc_type is not None:
            raise exc_value

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapped
