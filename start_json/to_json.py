import json,functools
# def to_json(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         with open('test.json', 'w') as file:
#             data = json.dumps(func(), ensure_ascii=False)
#             file.write(data)
#             # json.dump(func(),file,indent=4)#так тоже правильно
#             return data
#     return wrapper

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        not_parsed_result = func(*args, **kwargs)
        return json.dumps(not_parsed_result)
    return wrapped
# @py_to_json
@to_json
def get_data():
    return {'data': 42}


get_data()
