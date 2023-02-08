with open('input.txt','r') as fin,open('output.txt','w') as fout:
    summa = 0
    EOF = True
    while EOF:
        file_line = fin.readline()
        
        chlen =  file_line.strip('\n')
        if chlen.isdigit():
           summa += int(chlen)
        if not file_line:
            EOF = False
    fout.write(str(summa))


