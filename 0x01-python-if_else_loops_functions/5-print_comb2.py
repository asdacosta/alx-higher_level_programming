#!/usr/bin/python3
for num in range(0, 100):
    if (num < 10):
        print("{:0d}, ".format(num), end="")
    print("{:d}, ".format(num), end="")
