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

def ood_even_func(odd_dir_obj, even_dir_obj = None):
    """Написать функцию, в котрую подаются 2 объекта.
    Функция из 2х объектов папок, делает 3ю и туда файлы четные и нечетные складывает, разбирая лицевую и оборот

    ******************

    Пока просто переименовываем в текущих папках"""
    non_sorted_list = odd_dir_obj.files
    sorted_list = sorted(non_sorted_list, key=lambda non_sorted_list: int(non_sorted_list.split('.')[0]))
    odd_dir_obj.files  = sorted_list

    # non_sorted_list = even_dir_obj.files
    # sorted_list = sorted(non_sorted_list, key=lambda non_sorted_list: int(non_sorted_list.split('.')[0]))
    # even_dir_obj.files = sorted_list
    #
    # print(odd_dir_obj.files, even_dir_obj.files)

    odd = 2 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    print(odd_dir_obj.files)
    for i in reversed(odd_dir_obj.files):
        os.rename(i, str(odd) + str('_.' + i.split('.')[1]))
        odd += 2


dir_1 = Dir_file(r'C:\Users\Copy\Desktop\1')

ood_even_func(dir_1)
