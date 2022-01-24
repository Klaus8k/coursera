import os

class Dir_file():
    """Класс раобочей директории, с методами:
    наполнения файлами, создания директории, изменением текущей директории"""

    default_dir = os.getcwd()

    def __init__(self, work_dir=None):
        self.work_dir = work_dir
        self.set_dir(work_dir)

    def set_dir(self, path):
        if path:
            os.chdir(path)
            self.work_dir = path
        else:
            self.work_dir = Dir_file.default_dir

    def __str__(self):
        return 'Текущая директория: {}'.format(self.work_dir)

    def fill_dir(self, count): # Тестовый метод для наполнения файлами
        for i in range(count):
            x = str(i) + '.txt'
            with open(x, 'w') as f:
                f.write('i')

    def mk_dir(self, name):
        os.mkdir(name)

def ood_even_func(odd_dir_obj, even_dir_obj):
    """Написать функцию, в котрую подаются 2 объекта.
    Функция из 2х объектов папок, делает 3ю и туда файлы четные и нечетные складывает, разбирая лицевую и оборот"""
    pass


f = Dir_file(r'C:\Users\Professional\Desktop\new_folder')
