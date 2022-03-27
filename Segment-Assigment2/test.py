import logging
import random
import analytics

print ("hello");


def isEven():
    current_number = random.randint(1,100)
    print (current_number)
    if current_number % 2 != 0:
        return "odd"
    else:
        return "even"

wasiteven = isEven()

print(wasiteven)
print(wasiteven)
print(wasiteven)



