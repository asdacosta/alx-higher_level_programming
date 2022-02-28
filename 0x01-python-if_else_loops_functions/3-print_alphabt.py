#!/usr/bin/python3
for alp in (97, 123):
    if (alp == 113 or alp == 101):
        continue
    print("{:c}".format(alp), end="")
