import tempfile
import os

class File():

    def __init__(self, path):
        self.path = path
        self.start = 0
        if os.path.exists(self.path) == False:
            self.write('')

    def __iter__(self):

        return self

    def __next__(self):
        lst_file = self.read().split('\n')
        if not lst_file[self.start]:
            self.start = 0
            raise  StopIteration
        self.start += 1
        return  lst_file[self.start-1] + '\n'


    def __str__(self):
        return self.path

    def read(self):
        f = open(self.path, 'r')
        x = f.read()
        f.close()
        return x

    def write(self, string):
        with open(self.path, 'w') as f:
            f.write(string)


    def __add__(self, other):
        temp = tempfile.gettempdir()
        # print(temp)
        temp = os.path.join(temp, tempfile.NamedTemporaryFile().name)
        # print(temp)
        new_file = File(temp)
        new_file.write(self.read() + other.read())
        new_file.path = temp
        return new_file



a = File('1.txt')
b = File('2.txt')
a.write('1-aaaaaaaaa\n')
b.write('2-bbbbbbbbb\n3-ggggggggggggg\n')
print(a.read())
print(b.read())
c = a + b
print(c.read())

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# #
for line in c:
    print(ascii(line))

for line in c:
    print(ascii(line))