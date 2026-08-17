class Car:
    model = "toyota",
seats = 6


car1  = Car()


""" House class"""

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass

house = House()
# print(house.num_rooms)
# print(House.num_rooms)

house.num_rooms = 7
House.num_rooms = 8
# print(house.num_rooms)
# print(house.num_rooms)
# print(house.num_rooms)


""" Constructor"""

class Recipe():

    def __init__(self,dish,items,time) -> None:

        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The" + self.dish + "has" +str(self.items) + \
              "and takes " + str(self.time) +"minutes to prepare")

pizza = Recipe("pizza",["tomato","cheese","flour"],45)
pasta = Recipe("pasta",["vegetables","chicken","pasta"],55)
# print(pizza.contents())
# print(pasta.contents())


""" challenge """

class MyFirstClass:
    
    index = "Author book"

    def __init__(self):
        print("who wrote this?")

  #constructor create karne ka sabse bara faida ye hai ke humain har object ki same properties baar baar define nahi karni padti, ek he dafa constructor main define kardete hain      

    def hand_list(self,philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the  book "+ book  )

# whodidthis = MyFirstClass()
# whodidthis.hand_list("shakespear","Tom and jerry")           


#inheritance

class Employees:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last


class Supervisors(Employees):
    def __init__(self,name,last,password) -> None:
      super().__init__(name,last)
      self.password = password

class Chefs(Employees):
     def leave_request(self,days):
         return "May I take leave for "+str(days)+"days"


Faizan = Employees("Faizan",'f')
Emily = Supervisors("Emily",'e','apple')
Ahmed = Chefs('Ahmed','a')

# print(Faizan.name)
# print(Ahmed.last)



class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print(' is sweet')

# apple = FruitFlavour()



# class Swiss:

#     def __init__(self):
#         self.bal = 1000


#     def basicInfo(self):
#         print(self.bal)

# bank = Swiss()
# bank.basicInfo()

class MyAnimal:
    def __init__(self,color):
        self.living = True,
        self.color = color

class Dog(MyAnimal):
        print("This is a dog class")

dog1= Dog("Black")
print(dog1.color)                 

# python