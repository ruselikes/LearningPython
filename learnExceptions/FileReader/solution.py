class FileReader:
    def __init__(self, path):
        self._path = path

    def read(self):
        try:
            with open(self._path, "r") as file:
                text = file.read()
                return text
        except FileNotFoundError:
            return ''


if __name__ == '__main__':
    reader = FileReader(r'/output.txt')
    print(reader.read())
