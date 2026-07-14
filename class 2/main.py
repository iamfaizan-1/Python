#This is my first python code

print("I like pizza")

#spaces error

if 5>2 :
    print("5 is greater than 2")

else:
    print("5 is not greater")


    #collection unpack


fruits = ["apple","banana","cherry"]   
x,y,z = fruits

print(x)
print(y)
print(z)


cities = ["karachi","Lahore","Islamabad"]

a,b,c = cities
print(a)
print(b)
print(c)

#escape character


print('you are welcome\nfaizan')#newline
print('you are\\ welcome')#backslash
print('you are \t welcome')#tab 
print('who\'s this') #single quotes

# type casting

a = str(1)
print(type(a))