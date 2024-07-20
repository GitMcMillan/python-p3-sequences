#!/usr/bin/env python3
# every count, raise 2 integers by one, and ad them together for the third integer
# ex: 1, 2, 3, 4 
#    +=1 +=1 index 0 + index 1

def print_fibonacci(length):
        if length == 0:
              print([])
        elif length == 1:
              print([0])
        elif length == 2:
              print([0, 1])
        elif length == 10:
                print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
