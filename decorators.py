# '''Передача одной функции другой функции'''
#
# def outer_function():
#     def inner_function():
#         print("Вызвана функция inner_function")
#     print("Вызвана функция outer_function")
#     return inner_function
# # outer_function()
# inn_try = outer_function() #результат функции outer - inner. inn_try содержит ссылку на обьект-функцию inner.
# inn_try()#значит можно вызвать inn_try


# def decorator(func):
#      def wrapper():
#          print("До вызова декорируемой функции")
#          result = func()
#          print("После вызова декорируемой функции")
#          return result
#      return wrapper

# def some_function():
#     print("Вызвана функция some_function")
#
# some_function = decorator(some_function)
# some_function()#type(some_function) >> wrapper. Сама функция ссылается на внутреннюю функцию декоратора

#2 добавим синтаксический сахар
# @decorator#оборачиваем в decorator и передаем ему ниже стоящую some_function
#эквивалентно some_function = decorator(some_function)
# def some_function():
#     print("Вызвана функция some_function")
# some_function()
# print(some_function)#>>wrapper

#3 декорируем функцию с параметрами
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Функции переданы аргументы: args={argsp}, kwargs={kwargsp}".format(argsp=args, kwargsp=kwargs))
#         print('type(args):\t',type(args))
#         print('type(kwargs):\t', type(kwargs))
#         return func(*args,**kwargs)
#     return wrapper
# @decorator
# def some_function(first_argument, second_argument):
#     print("first_argument={first_argument}, second_argument={second_argument}".format(first_argument=first_argument, second_argument=second_argument))
# some_function(42, second_argument="test")
#
# print(some_function)#>>wrapper



#пишу свои цепочки декораторов

# def dec_a(func):
#     def wrapper(*args,**kwargs):
#         print('dec_a start')
#         func(*args,**kwargs)
#         print('dec_a finish')
#
#     return wrapper
#
# def dec_b(func):
#     def wrapper(*args,**kwargs):
#         print('\tdec_b start')
#         func(*args,**kwargs)
#         print('\tdec_b finish')
#
#     return wrapper
#
# @dec_a#dec_a(   dec_b(decorated   ) - выполнение с внутренних функций к внешним
# @dec_b
# def decorated(hier):
#     print('\t\t{} I am decorated function'.format(hier))
#
# decorated('hi')

#Декоратор с аргументами
def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Декоратору переданы аргументы: arg1={arg1}, arg2={arg2}".format(arg1=arg1, arg2=arg2))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def some_function():
    print("Вызвана функция some_function")

@decorator_with_args("A", "B")
def some_function():
    print("Вызвана функция some_function")

some_function()











'''trying to figure  out Decorators'''
#-----------------------------------------------------------------------------------------------------------------------------
# def decorator(func):
#     def wrapper():
#         func()
#         print("Where am i")
#     return wrapper
#
# @decorator
# def first():
#     print('func First in working ')



'''Декоратор, который записывает в файл log.txt результат декорируемой summaror'''
# def summator_decoreted(func):
#     @functools.wraps(func)
#     def inner(*args,**kwargs):
#         result = func(*args,**kwargs)
#         with open('output.txt','w') as fl:
#             fl.writelines(str(result))
#         return result
#     return inner
#
# def logger(file_name):
#
#     def decorator(func):
#         @functools.wraps(func)
#         def inner(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(file_name, 'w') as fl:
#                 fl.write(str(result))
#             return result
#         return inner
#     return decorator
#
# @logger('text1.txt')
# def summator(nums_list):
#     return sum(nums_list)
#
#
# # summator([1,3,5,6])
#
# summator([1,9])
# print('Call summator here: {}'.format(summator((1,2,4))))
# print(summator.__name__)
#-----------------------------------------------------------------------------------------------------------------------------






#/////////
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

