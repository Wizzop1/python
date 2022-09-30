import math
import os
import random
import re
import sys

negCount = 0
zeroCount = 0
posCount = 0
arr = []
print('Choose the length')
n = int(input())
arr = [3] * n
print('Fill in the array: ')
for i in range(n):
    arr[i] = int(input())
for x in range(len(arr)):
    if arr[x]<0:
        negCount = negCount+1
        
    elif arr[x] >0:
        posCount = posCount+1
        
    elif arr[x] == 0:
        zeroCount = zeroCount+1
negRatio = negCount/n
neg_format = '{:.6f}'.format(negRatio)
float_neg = float(neg_format)
posRatio = posCount/n
pos_format = '{:.6f}'.format(posRatio)
float_pos = float(pos_format) 
zeroRatio = zeroCount/n
zero_format = '{:.6f}'.format(zeroRatio)
float_zero = float(zero_format)
print("{:.6f}".format(round(negRatio, 2)))
print("{:.6f}".format(round(posRatio, 2)))
print("{:.6f}".format(round(zeroRatio, 2)))
