class FileReader:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                file_contents = f.read()
        except IOError:
            file_contents = ''
        return file_contents
