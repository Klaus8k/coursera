import argparse
import os
import tempfile
import json


def dic_form():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="input key")
    parser.add_argument("--val", help="input value")
    args = parser.parse_args()

    key = args.key
    val = args.val

    dic = read_from_file()

    if val is None:
        if key in dic.keys():
            print(', '.join(dic[key]))
        else:
            print(None)

    else:
        if key in dic.keys():
            old_val = dic[key]
            old_val.append(val)
            dic[key] = old_val

        else:
            dic[key] = [val]

        write_to_file(dic)


def write_to_file(storage: dict):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(storage, f)


def read_from_file() -> object:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    try:
        with open(storage_path, 'r') as f:
            json_str = json.load(f)
            return dict(json_str)
    except:
        json_str = {}
        return json_str


dic_form()
