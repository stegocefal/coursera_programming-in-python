import os
import tempfile


class File(object):
    def __init__(self, path):
        self.path = path
        if not os.path.isfile(self.path):
            open(self.path, 'a').close()

        # self.content = self.read().splitlines(keepends=True)

        # For seeking the file
        self._offset = 0
        self._from_what = 0

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

    def read(self):
        with open(self.path, 'r') as f:
            out = f.read()
        return out

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self._offset)
            result = f.readline()
            if result == '':
                self._offset = 0  # Зачем нам это?!
                raise StopIteration
            self._offset = f.tell()

        return result

    def __add__(self, other):
        if not isinstance(other, File):
            return NotImplemented
        temp_dir = tempfile.gettempdir()
        temp_filename = tempfile.gettempprefix()
        obj = File(os.path.join(temp_dir, temp_filename))  # Вместо File можно использовать type(self)!
        obj.write(self.read() + other.read())
        return obj
