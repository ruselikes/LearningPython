a = [1,2,3]
b = a
# b = a.copy()
print('a:', a)
print('b:', b)

b.extend([4,5,6])
print('b modified:', b)

print('a:',a)