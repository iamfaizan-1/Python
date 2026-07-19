x=3
print(x)

# control flow 

# total_bill = int(input("Please enter the bill amount: "))
# discount1 = 10
# discount2 = 20

# if total_bill > 100:
#     print("The bill is greater than 100")
#     total_bill -= discount1
#     print("The total bill is: ",total_bill)

# else:
#     print("The bill is less than 100")



#match statement


# httpStatus = int(input("Enter the http status: "))

# match httpStatus:
#     case 200 | 201:
#         print("Status ok")
#     case 400:
#         print("bad request")
#     case 500 | 501:
#         print("Server error")
#     case _:
#         print("Unknown request")    


#loops
"""for loop"""

favouriteFruits = ["apple","Mango","Grapes"]

# for item in favouritesFruites:
#     print("My favourite fruit is : ",item)


""" while loops """

# count = 0
# while count < len(favouriteFruits):
#     print("My favourite fruit is: ",favouriteFruits[count])
#     count +=1


"""functions"""  

# 1.

# def calculateTax(bill,taxRate):

#     return (bill*taxRate)/100

# print(calculateTax(250,15))

"""Global vs local vs enclosed"""
# globalVariable = 5

# def fn1():
#     enclosedVariable = 2

#     def fn2():  
#         print("This is enclosed variable",enclosedVariable)
#     localVariable = 6
    
#     fn2()


# fn1()    

    
""" variable scope and function """   

# def get_total(a, b):
#     #local variable declared inside a function
#     total = a + b
#     return total

# print(get_total(5, 2))


def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
 

 