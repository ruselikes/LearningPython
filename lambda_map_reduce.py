'''Transorm list of integers into list of str using lambda/map'''
from functools import reduce


def stringer(editlst):
    return list(map(str,editlst))
lst = [x for x in range(10)]
lststr = stringer((lst))
print(lststr)

newlststr = list(map(lambda x: str(x),lst))


print(reduce(lambda x,y: x+y,[1,2,-3,5]),print(type(reduce(lambda x,y: x+y,[1,2,-3,5]))))
print(newlststr)