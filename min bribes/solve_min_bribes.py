#!/bin/python3

import math
import os
import random
import re
import sys

# Q = [12543]
# Q = [12453] #swap q[2] & q[3] because q[2] > q[3]
# Q = [12435] #swap q[3] & q[4] because q[3] > q[4]
# Q = [12345] #swap q[2] & q[3] because q[2] > q[3] #Extra step!

# Q = [12534]
# Q = [12354] #swap q[2] & q[3] because q[2] > q[3]
# Q = [12345] #swap q[3] & q[4] because q[3] > q[4]
# Complete the minimumBribes function below.


def solve(q, i, b):
    for i in range(0, len(q)-1):
        val = q[i]
        k = i
        
    return q,b

            
if __name__ == '__main__':
    f = open("input01.txt", 'r')

    t = int(str(f.readline()))  # read number of test cases
    n = int(str(f.readline().strip()))  # read queue length
    q = list()
    for j in range(t):
        line = f.readline().split()  # read queue
        for i in line:
            q.append(int(str(i).strip()))  # construct queue
        print(q)
        print(solve(q, 0, 0))
        line = f.readline().split()
        q.clear()
    f.close()
