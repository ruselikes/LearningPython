import json,functools
def to_json(func):
    @functools.wraps(func)
    def wrapper():
        with open('test.json', 'w') as file:
            data = json.dumps(func(), ensure_ascii=False, indent=4)
            file.write(data)
            # json.dump(func(),file,indent=4)#так тоже правильно
            return data
    return wrapper


# @py_to_json
@to_json
def get_data():
    return {'data': 42}

get_data()