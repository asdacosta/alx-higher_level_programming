#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
print("Last digit of {} is ".format(number), end=" ")
if (number >= 0):
    print("{} and is ".format(number % 10), end=" ")
else:
    print("{} and is less than 6 and not 0".format(number % -10))

if ((number % 10) > 5):
    print("greater 5")
elif ((number % 10) == 0):
    print("0")
elif ((number % 10) < 6 and not(number % 10) == 0):
    print("{} and is less than 6 and not 0".format(number % 10))

