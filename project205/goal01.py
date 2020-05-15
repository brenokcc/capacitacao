import csv
from collections import namedtuple


class FileParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_dialect(self):
        with open(self.file_name) as f:
            return csv.Sniffer().sniff(f.read(1024))

    # context manager protocol
    def __enter__(self):
        self._file = open(self.file_name, 'r')
        self._reader = csv.reader(self._file, dialect=self.get_dialect())
        headers = map(lambda line: line.lower(), next(self._reader))
        self._namedtuple = namedtuple('Data', headers)
        return self

    def __exit__(self, exception_type, exception_value, exception_tb):
        self._file.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._file.closed:
            raise StopIteration
        else:
            return self._namedtuple(*next(self._reader))
