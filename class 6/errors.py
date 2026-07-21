def division(a,b):
    
    return a/b
try:
    print(division(4,0))

except ZeroDivisionError as e:
    print(e,"we cannot divide by zero") #this is exception, especially for zero division

except Exception as e:
    print(e,"something went wrong") #this is exception for default


    