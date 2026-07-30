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


