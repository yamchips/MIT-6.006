#Selection sort: find the max or min index in A
#put it on right/left side of the array
#then deal with the remaining len(A)-1 elements

#Principle: find the max index and put it on the right

#Method 1, use 2 recursive functions(given in lecture3)
def selection_sort1(A, i):
    #i is the max index of A
    if i < 1:
        return A
    else:
        a = find_max_index(A, i)
        A[a], A[i] = A[i], A[a]
        selection_sort1(A, i-1)

def find_max_index(A, i):
    if i < 1:
        return 0
    else:
        j = find_max_index(A, i-1)
        if A[j] > A[i]:
            return j
        else:
            return i

#Method 2, use 1 recursive call and 1 loop
def selection_sort2(A,i):
    #i is the biggest index in A
    if i < 1:
        return A
    else:
        selection_sort2(A, i-1)
        for  j in range(len(A)-1):
            if A[j] > A[i]:
                A[i], A[j] = A[j], A[i]

#Method 3, use 2 loops
def selection_sort3(A):
    for i in range(len(A)-1, 0,-1):
        for j in range(i):
            if A[j] > A[i]:
                A[i], A[j] = A[j], A[i]

#Test case
A = [8,2,0,4,6,9,3,7,5,1]
#selection_sort1(A, len(A)-1)
#selection_sort2(A, len(A)-1)
selection_sort3(A)
print(A)

