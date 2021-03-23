#!/bin/python3
from typing import ByteString, Dict, final
import unittest
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(a):
    swaps = 0
    mappedVals = dict()
    for c in range(0, len(a)): # associate values with their indices 
        mappedVals.update({a[c]: c})

    for i in range(len(a)-1):
        val = a[i]
        if i+1 != val:
            swaps += 1 #count swaps
            K = mappedVals[i+1] #get actual position of i
            a[i] = a[K] #assign 
            a[K] = val
            #don't forget to update indexes
            mappedVals.update({a[i]: i})
            mappedVals.update({a[K]: K}) 
    return swaps
