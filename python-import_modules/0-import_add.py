#!/usr/bin/python3
add = __import__('0-add').add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
