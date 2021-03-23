#!/bin/python3
from typing import final
import unittest
import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0

    for i in range(len(arr)): #Not fast enough for hackerrank. HMMM...
        j = i + 1
        e = arr[i]
        if j != e:
            index = arr.index(j)
            arr[i] = arr[index]
            arr[index] = e
            swaps += 1
            print(arr)
    print("Returning-> ", swaps)
    return swaps


