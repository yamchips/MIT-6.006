#Insertion sort: assume that A[:i] is sorted
#compare A[i] with A[:i] and put A[i] in right order

#Method 1, use 2 recursive calls(given in lec3)
def insertion_sort1(A, i):
    if i < 1:
        return A
    else:
        insertion_sort1(A, i-1)
        compare_last(A, i)

def compare_last(A, i):
    if A[i] < A[i-1] and i > 0:
        A[i], A[i-1] = A[i-1], A[i]
        compare_last(A, i-1)

#Method 2, use loop(given in lec3 recitation)
def insertion_sort2(A):
    for i in range(1,len(A)):
        k = i
        for j in range(k-1,-1,-1):
            if A[j] > A[i]:
                A[i], A[j] = A[j], A[i]
                i -= 1

#Test case
A = [8,2,0,4,1,9,3,7,5]
insertion_sort2(A)
print(A)


