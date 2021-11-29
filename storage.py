import argparse
import os
import tempfile

def key_vals():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="input key")
    parser.add_argument("--val", help="input value")
    args = parser.parse_args()

    storage_dict = {}

    key = str(args.key)
    val = str(args.val)

    if val == None:
        print(storage_dict.values(key))
    else:
        storage_dict[key] = val

    write_to_file(storage_dict)



def write_to_file (storage: dict):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        f.write(storage)
        f.close()






