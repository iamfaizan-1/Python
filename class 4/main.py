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

count = 0
while count < len(favouriteFruits):
    print("My favourite fruit is: ",favouriteFruits[count])
    count +=1