def lgenerator():
    with open('numbers.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split()
            for strnumber in line:
                if strnumber.isdigit():
                    yield int(strnumber)


summa=0
gener = lgenerator()
for num in gener:
    summa += num
print(summa)