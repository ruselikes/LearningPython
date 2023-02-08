'''This part response to lists'''
# lst = ['qwerty',]
# print(lst)
# lst.append([])
# print(lst, "append empty list")
# lst.extend([51,2,314])
# print(lst, "Extend by new list",f"Length {len(lst)}")
# lst.insert(3,"inserted data")
# print(lst, "Inserting value on [3]",f"Length{len(lst)}")
# lst[1].extend(["new value in inner list",25])
# print(lst, "Extend lst[1](inner list) by using [not empry list]")
# print("In conclusion we can see list can exist in each other, can be extended, values can called use indexes")

'''Part of dictionaries'''
my_dict = {}
my_dict['first'] = 1
my_dict.update({'first1':31})
print(my_dict,'\nvalues',my_dict.values(),"\nkeys",my_dict.keys())
b = my_dict.get("first4", 'f4')
a = my_dict.setdefault('new',555)
print(my_dict)
print(a)
print(b)

