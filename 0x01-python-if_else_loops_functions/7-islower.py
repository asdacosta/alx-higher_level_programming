#!/usr/bin/python3
def islower(c):
    c = 65
    while (c <= 122):
        for c in range(65, 90):
            print("{:02c} is upper".format(c))
        for c in range(97, 123):
            print("{:02c} is lower".format(c))
        else:
            continue

        c += 1
