#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
@File    : problem_session2.py
@Time    : 2022/10/28 09:42:15
@Author  : yamchips
@Version : 1.0
"""
#Problem 1-4 Brick Blowing
#subproblem b
def calspecial(D):
    '''
    Input: D is a list that only one element is not special, which 
          means D consists of two sorted arrays
    Output: A list 'result'. Each element indicates the damage of the wolf
    '''
    result = [1]*len(D)
    for i in range(len(D)-1):
        if D[i] > D[i+1]:
            specialnum = i
    i, j = 0, specialnum + 1
    while i <= specialnum and j < len(D):
        if D[i] > D[j]:
            result[i] += 1
            j += 1
        else:
            i += 1
    result1 = result[:]
    for i in range(1,specialnum+1):
        result[i] = result1[i] + sum(result1[:i]) - i   
    return result

#subproblem c
def caldamage(D):
    '''
    Input: D is an unsorted list of integer
    Output: A list whose element means the damage of the wolf
    '''
    if len(D) <= 1:
        return D
    else:
        mid = len(D)//2
        left = caldamage(D[:mid])
        right = caldamage(D[mid:])
        return calspecial(left)

#standard solution
def get_damages(H):
    D = [1 for _ in H]
    H2 = [(H[i], i) for i in range(len(H))]
    def merge_sort(A, a=0, b=None):
        if b is None:
            b = len(A)
        if a + 1 < b:
            c = (a+b+1)//2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            i, j, L, R = 0, 0, A[a:c], A[c:b]
            while a < b:
                if (j>=len(R)) or (i<len(L)) and L[i][0] <= R[j][0]:
                    D[L[i][1]] += j
                    A[a] = L[i]
                    i += 1
                else:
                    A[a] = R[j]
                    j += 1
                a += 1
    merge_sort(H2)
    return D

#H = [1,2,3,4,1,2,3,4]
#H = [1,2,3,4,1,3,9,12]
H = [3,2,7,0,5,1,4,6]
print(get_damages(H))