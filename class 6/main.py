""" Args  """


def sumOf(*args):
    sum = 0

    for x in args:
        sum+=x
        
    return sum
    
# print(sumOf(1,2,9,7,5))



""" kwargs """

def totalOf(**kwargs):
    sum = 0

    for x, y in kwargs.items():
        sum+=y
    return sum

print(totalOf(coffee = 3, cake = 4, juice = 2))

