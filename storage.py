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
    val = [args.val]

    print(key,val)

    dic = read_from_file()

    if val:
            dic.update([key, val.append(val)])
            write_to_file(dic)
            print(dic)

        elif str(key) in dic:
            print(dic.values(key))

        else:
            print('None')

    else:
        print(1)
        dic = dict.setdefault(key,[val])
        write_to_file(dic)



def write_to_file (storage: dict):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        print(2222)
        json.dump(storage, f)



def read_from_file() -> object:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'a') as f:
        try:
            json_str = json.load(f)
            return dict(json_str)
        except:
            print(1111111111111)
            return None


key_vals()

# Отправляет в файл, но перезаписывает