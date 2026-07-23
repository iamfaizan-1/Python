# import random
# f = open("pet.txt", "r")
# f_content = f.read()
# f_content_list = f_content.split("\n")
# f.close()
# print(random.choice(f_content_list))



"""advance method"""


import random

f_name = input("Enter file name")

f = open(f_name)
f_content = f.read()

f_content_list = f_content.split("\n")
print(random.choice(f_content_list))
