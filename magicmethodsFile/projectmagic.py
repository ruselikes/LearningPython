import os.path
import tempfile
import random, string



class File:
    @staticmethod
    def randomword(length):
        """Return string consists of random chars(L&Up cases. Choose desire length in args"""
        letters = string.ascii_lowercase + string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(length))

    def __init__(self,fpath):
        self.fpath = fpath
        if not os.path.exists(fpath):
            file = open(fpath,'w')
            file.close()



    def read(self):
        with open(self.fpath,'r') as file:
            return file.read()

    def write(self,new_string):
        with open(self.fpath,'w') as file:
            file.write(new_string)
            return len(new_string)


    def __str__(self):
        return os.path.abspath(self.fpath)

    def __add__(self, other):
        with open(self.fpath,'r') as f1,open(other.fpath,'r') as f2:
            new_data = f1.read()+f2.read()
            # gettemp dir return us a os path of temp folder
            new_file = File (os.path.join(tempfile.gettempdir(),self.randomword(10)))
            new_file.write(new_data)
            return new_file



    def __iter__(self):
        self.file = open(self.fpath,'r')
        return self

    def __next__(self):

        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration

        return line

path_to_file = 'some_filename'
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(file_obj.read())
print(file_obj.write('some text'))
print(file_obj.read())
print(file_obj.write('other text'))
print(file_obj.read())
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
print(file_obj_1.write('line 1\n'))
print(file_obj_2.write('line 2\n'))
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
print(new_file_obj)

for line in new_file_obj:
    print(ascii(line))
# print(File.randomword(10))
# print(tempfile.gettempdir())