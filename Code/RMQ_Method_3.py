# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 05:03:04 2021

@author: mahsa
"""

# Python3 program to do range minimum query
# in O(1) time with O(n Log n) extra space
# and O(n Log n) preprocessing time
from math import log2
 
MAX = 500
 
# lookup[i][j] is going to store index of
# minimum value in arr[i..j].
# Ideally lookup table size should
# not be fixed and should be determined
# using n Log n. It is kept constant
# to keep code simple.
lookup = [[0 for i in range(500)]
          for j in range(500)]
 
# Structure to represent a query range
 
 
class Query:
    def __init__(self, l, r):
        self.L = l
        self.R = r
 
# Fills lookup array lookup[][]
# in bottom up manner.
 
 
def preprocess(arr: list, n: int):
    global lookup
 
    # Initialize M for the
    # intervals with length 1
    for i in range(n):
        lookup[i][0] = i
 
    # Compute values from
    # smaller to bigger intervals
    j = 1
    while (1 << j) <= n:
 
        # Compute minimum value for
        # all intervals with size 2^j
        i = 0
        while i + (1 << j) - 1 < n:
 
            # For arr[2][10], we compare
            # arr[lookup[0][3]] and
            # arr[lookup[3][3]]
            if (arr[lookup[i][j - 1]] <
                    arr[lookup[i + (1 << (j - 1))][j - 1]]):
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i +
                                      (1 << (j - 1))][j - 1]
 
            i += 1
        j += 1
 
# Returns minimum of arr[L..R]
 
 
def query(arr: list, L: int, R: int) -> int:
    global lookup
 
    # For [2,10], j = 3
    j = int(log2(R - L + 1))
 
    # For [2,10], we compare
    # arr[lookup[0][3]] and
    # arr[lookup[3][3]],
    if (arr[lookup[L][j]] <=
            arr[lookup[R - (1 << j) + 1][j]]):
        return arr[lookup[L][j]]
    else:
        return arr[lookup[R - (1 << j) + 1][j]]
 
# Prints minimum of given
# m query ranges in arr[0..n-1]
 
 
def RMQ(arr: list, n: int, q: list, m: int):
 
    # Fills table lookup[n][Log n]
    preprocess(arr, n)
 
    # One by one compute sum of all queries
    for i in range(m):
 
        # Left and right boundaries
        # of current range
        L = q[i].L
        R = q[i].R
 
        # Print sum of current query range
        print("Minimum of [%d, %d] is %d" %
              (L, R, query(arr, L, R)))
 
 
# Driver Code
if __name__ == "__main__":
    a = [2, 3, 4, 3,
         2, 3, 2, 1, 0]
    n = len(a)
    q = [Query(2, 6),
        Query(0, 8)]   
    m = len(q)
 
    RMQ(a, n, q, m)
 
