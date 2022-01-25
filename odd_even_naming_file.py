import os

class Dir_file():
    """Класс раобочей директории, с методами:
    наполнения файлами, создания директории, изменением текущей директории"""

    default_dir = os.getcwd()

    def __init__(self, work_dir=None):
        self.work_dir = work_dir
        self.set_dir(work_dir)
        self.files = os.listdir(self.work_dir)

    def set_dir(self, path):
        if path:
            os.chdir(path)
            self.work_dir = path
        else:
            self.work_dir = Dir_file.default_dir

    def __str__(self):
        return 'Текущая директория: {}'.format(self.work_dir)

    def fill_dir(self, count): # Тестовый метод для наполнения файлами
        for i in range(1,count+1):
            x = str(i) + '.txt'
            with open(x, 'w') as f:
                f.write('i')

    # def file_list(self):
    #     files = os.listdir(self.work_dir)
    #     self.__setattr__('files', files)
    #     return self.files

    def mk_dir(self, name):
        os.mkdir(name)

def ood_even_func(odd_dir_obj, even_dir_obj):
    """Написать функцию, в котрую подаются 2 объекта.
    Функция из 2х объектов папок, делает 3ю и туда файлы четные и нечетные складывает, разбирая лицевую и оборот

    ******************

    Пока просто переименовываем в текущих папках"""
    odd, even = 1,2
    print(odd_dir_obj.file_list())
    for i in odd_dir_obj.file_list():
        print(i)
        try:
            os.rename(i, str(odd))
        except FileExistsError:
            odd += 2
            continue


dir_1 = Dir_file(r'C:\Users\Copy\Desktop\1')
dir_1.fill_dir(30)
# dir_1.file_list()
print(dir_1.files)
# dir_2 = Dir_file(r'C:\Users\Copy\Desktop\2')
# dir_2.fill_dir(30)


# ood_even_func(dir_1, dir_2)
