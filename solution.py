class FileReader:
    def __init__(self, way):
        self.way = way

    def read(self):
        try:
            with open(self.way, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''
