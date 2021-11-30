import json

def to_json(func):
    def wrapper(*args, **kwargs):

        result = json.dumps(func(*args, **kwargs))
        print(result)
        return result
    return wrapper


def get_data():

    return {
    'data': 42
    }


get_data()


