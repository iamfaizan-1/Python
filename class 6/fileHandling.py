""" first method of file handling"""

# file = open("test.txt", mode='r')

# data = file.readline()

# print(data)

# file.close()


""" second method of file handling"""

with open("test.txt",mode = 'r') as file:

    data = file.readline()
    print(data)