import argparse
import os
import tempfile
import json


def key_vals():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="input key")
    parser.add_argument("--val", help="input value")
    args = parser.parse_args()


    key = str(args.key)
    val = str(args.val)

    print(key,val)


    if read_from_file():
        dic = read_from_file()
        if val:
            dic[key] = dic[key] + str(val)
            write_to_file(dic)
            print(dic)

        elif str(key) in dic:
            print(dic[key])

        else:
            print('None')


    else:
        dic = {key: val}
        write_to_file(dic)











def write_to_file (storage: dict):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(storage, f)


def read_from_file() -> object:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        if f.read():
            json_str = json.load(f)
            return json_str
        return None



key_vals()

# Отправляет в файл, но перезаписывает