# filename = input("Enter the name of the file: ")
# text = input("Enter the text you want to write: ")
#
# try:
#
#     with open(filename, "x") as file:
#         file.write(text)
# except FileExistsError:
#     print("File already exists.")
# except:
#     print("An unexpected error occurred while opening the file.")
# else:
#     print("Text has been written successfully.")
# finally:
#     print("The process of writing to a file is completed.")
#

# атрибут args
import os.path
filename = "tttd"
assert os.path.exists(filename), 'пиздец'
try:
    if not os.path.exists (filename):
        raise ValueError (f"Файл не существует:",filename)
except ValueError as err:
    message, filename = err.args [0], err.args [1]
    print (message+ f"'{filename}'")
