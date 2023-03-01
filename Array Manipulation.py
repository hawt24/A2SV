#!/bin/python3

import math
import os
import random
import re
import sys



def arrayManipulation(n, queries):
    arr=[0]*(n+2)
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
    print(arr)
    temp=0
    maxm=0
    for i in arr:
        temp+=i
        maxm=max(temp,maxm)
    return maxm
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
