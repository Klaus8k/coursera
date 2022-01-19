import tempfile
import os

class File():

    def __init__(self, path):

        self.path = path
        self.write('') # Тест 5.2. Изменено содержание файла. Для случая, когда при создании экземпляра класса
                    # File в конструктор был передан путь до существующего файла, содержание файла не должно изменяться при инициализации.

    def __str__(self):
        x = os.path.abspath(self.path)
        return 'Path: {}'.format(x)

    def read(self):
        with open(self.path, 'r') as f:
            x = f.read()
            return x

    def write(self, string):
        with open(self.path, 'w') as f:
            f.write(string)


    def __add__(self, other):
        temp = tempfile.gettempdir()
        print(temp)
        temp = os.path.join(temp, tempfile.NamedTemporaryFile().name)
        print(temp)
        new_file = File(temp)
        new_file.write(self.read() + other.read())



a = File('1.txt')
b = File('2.txt')
a.write('aaaaaaaaa')
b.write('bbbbbbbbb')
print(a.read())
print(b.read())
print(a)
print(b)
c = a + b
print(isinstance(c, File))
g = File('1.txt')
print(g.read())