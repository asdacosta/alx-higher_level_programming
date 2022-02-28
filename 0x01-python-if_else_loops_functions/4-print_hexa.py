#!/usr/bin/python3
for num in range(0, 98):
    print("{} = 0x".format(num), end="")
    if (num < 10):
        print("{}".format(num))
    elif (num == 10):
        print("{:c}".format(97))
    elif (num == 11):
        print("{:c}".format(98))
    elif (num == 12):
        print("{:c}".format(99))
    elif (num == 13):
        print("{:c}".format(100))
    elif (num == 14):
        print("{:c}".format(101))
    elif (num == 15):
        print("{:c}".format(102))
    elif (num >= 16):
        print("{}".format(num = num - (num % 10))
