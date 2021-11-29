import argparse
import os
import tempfile

def key_vals():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="input key")
    parser.add_argument("--val", help="input value")
    args = parser.parse_args()

    storage_dict = read_from_file()
    if len(storage_dict) != 0:
        key = str(args.key)
        val = str(args.val)
        storage_dict = {key:[val,]}
        write_to_file(storage_dict)



# val присваивается в словаре и записывается. А не должен.
# если  вал нет, то поиск по ключам, если нет то вернуть Ноне
# Если вал есть, то проверить на наличии ключа и добавить к значентю, если нет ключа то сделать новую пару ключ-значение




def write_to_file (storage: dict):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        f.write(str(storage))
        f.close()
#
def read_from_file() -> object:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r+') as f:
        lines = f.readline()
        dic = {}
        for line in lines:  # Проходимся по каждой строчке
            key, value = line.split(': ')  # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
            dic.update({key: value}

    return dict(dic)

key_vals()

# Отправляет в файл, но перезаписывает