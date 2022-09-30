import math
import os
import random
import re
import sys

negCount = 0
zeroCount = 0
posCount = 0
n= int(input())
arr = []
for i in range(n):
     arr[i]=input()
for x in range(len(arr)):
    if arr[x]<0:
        negCount = negCount+1
        print(negCount)
    elif arr[x] >0:
        posCount = posCount+1
        print(posCount)
    elif arr[x] == 0:
        zeroCount = zeroCount+1
        print(zeroCount)