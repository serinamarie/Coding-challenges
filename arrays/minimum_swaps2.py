# You are given an unordered array consisting of consecutive integers 
# [1, 2, 3, ..., n] without any duplicates. You are allowed to swap 
# any two elements. You need to find the minimum number of swaps 
# required to sort the array in ascending order. 

# Function Description

# Complete the function minimumSwaps in the editor below. 
# It must return an integer representing the minimum number of 
# swaps to sort the array.

# minimumSwaps has the following parameter(s):

    # arr: an unordered array of integers

# Input Format

# The first line contains an integer
# The second line contains space-separated integers

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # UNDERSTANDING THE PROBLEM
    # output: number of swaps as int
    # input: size of arr as int, array
    # constraints: no empty array, ints in array will be > 0
    
    # PLAN/PSEUDOCODE
    # keep track of the number of swaps as we go 
    # swap_counter = 0
    
    # j = get minimum index = 3
    
    # loop through i in range()

        # perhaps, while arr[i] < arr[j]
            # swap value at arr[j] with arr[i]
            # increase our swaps counter
            # j = index(arr[i]+1)
        # else break
    # return swaps counter

    # FIRST-PASS SOLUTION

    swap_counter = 0
    
    # get minimum index o(n)
    j = arr.index(1)
    
    # o(n)
    for i in range(len(arr)-1):
        
        # if out of order
        if arr[i] > arr[j]:
            
            # swap
            arr[j], arr[i] = arr[i], arr[j]
            
            # increment swap counter
            swap_counter += 1
            
        # get index of consecutive int
        j = arr.index(arr[i]+1)
    
    return swap_counter
    
    # 7
    # 1 3 5 2 4 6 7
    
    # swaps = 3
    # 2 3 4 1 5
    # 1 3 4 2 5
    # 1 2 4 3 5
    # 1 2 3 4 5
    # j = 4
    # i = 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
