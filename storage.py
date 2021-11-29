import argparse
import os
import tempfile

def key_vals():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="input key")
    parser.add_argument("--val", help="input value")
    args = parser.parse_args()

    storage_dict = read_from_file()

    key = str(args.key)
    val = str(args.val)

# val присваивается в словаре и записывается. А не должен.
# если  вал нет, то поиск по ключам, если нет то вернуть Ноне
# Если вал есть, то проверить на наличии ключа и добавить к значентю, если нет ключа то сделать новую пару ключ-значение


    if val == None:
        print(storage_dict.values(key))

    elif key in storage_dict:
        storage_dict[key] += str(val)
        write_to_file(storage_dict)
    else:
        storage_dict[key] = str(val)
        write_to_file(storage_dict)


def write_to_file (storage: dict):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        f.write(str(storage))
        f.close()

def read_from_file() -> object:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        x = f.read()
        # if x == None: Тут надо правльно прочитать файл
        #     return {}
        # f.close()
    return dict(x)

key_vals()

# Отправляет в файл, но перезаписывает