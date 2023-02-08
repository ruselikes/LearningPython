import json
import functools


# def py_to_json(func):
#     def wrapper():
#         # with open (filename+'.json','w') as file:
#         #     json.dump(to_json,file,indent=4)
#         str_data_json = json.dumps(func(),indent=4)
#
#         return str_data_json
#     return wrapper
#
#
# def to_json(filename):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper():
#             with open (filename+'.json','w') as file:
#                 file.write(json.dumps(func(),ensure_ascii=False,indent=4))
#                 # json.dump(func(),file,indent=4)#так тоже правильно
#         return wrapper
#     return decorator


def to_json(func):
    @functools.wraps(func)
    def wrapper():
        with open('test.json', 'w') as file:
            file.write(json.dumps(func(), ensure_ascii=False, indent=4))
            # json.dump(func(),file,indent=4)#так тоже правильно

    return wrapper


# @py_to_json
@to_json
def get_data():
    return { 'data': 42,'extra_data':{'surname':'Maratkanov','name':'Ruslan'}}

def test():
    with open('blyat.json', 'r') as file:
        # readed_data = file.read()
        readed_data = json.loads(file.read())
        print("r_data type:\t", type(readed_data))
        print("r_data:\t", readed_data['extra_data'])


    # print('type(readed_data)', type(readed_data))
    # j_to_p = json.load(file)
get_data()
