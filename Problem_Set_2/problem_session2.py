#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
@File    : problem_session2.py
@Time    : 2022/10/28 09:42:15
@Author  : yamchips
@Version : 1.0
"""
import numpy as np
#Problem 1-4 Brick Blowing
#subproblem b
def calspecial(D):
    '''
    Input: D is an array that only one element is not special, which 
          means D consists of two sorted arrays
    Output: An array called 'result'. Each element indicates the damage of the wolf
    '''
    result = []
    for j in range(len(D)):
        result.extend([1])
    for i in range(len(D)-1):
        if D[i] > D[i+1]:
            specialnum = i
    i, j = 0, specialnum+1
    while i <= specialnum and j < len(D):
        if D[i] > D[j]:
            result[i] += 1
            j += 1
        else:
            i += 1
 
    result1 = result[:]
    print(type(result))
    for i in range(1,specialnum+1):
        #for j in range(len(result1)):
        #    print(result[j])
        #print('---------------')
        a = result1[i] + sum(result1[:i]) - i
        result[i] = a
    print('result:', result)
    #根据i和j数值不同调试一下
    #for j in range(1,4):
    #    result[j] = result1[j] + sum(result1[:j]) - j

    return result
#max(A) == max(B)
#D = [1,2,3,4,1,2,3]

#max(B) < max(A)
D = [5,6,7,8,1,2,3,4]

#MAX(B)>MAX(A)
#D = [1,2,3,4,1,2,8,9]
print(calspecial(D))


#subproblem c
def caldamage(D):
    '''
    Input: An array D, integer
    Output: An array, each element means the damage of the wolf
    '''
    if len(D) <= 1:
        return D
    else:
        mid = len(D)//2
        left = caldamage(D[:mid])
        right = caldamage(D[mid:])
        return calspecial(left)

