#My code
def merge_sort(A):
    if len(A) <= 1:
        return A[:]
    else:
        mid = len(A)//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return compare_sort(left, right)

def compare_sort(A, B):
    '''
    Input: Both A and B are array
    Output: an array that is sorted and contains all elements in A and B
    '''
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            result.append(B[j])
            j += 1
        else:
            result.append(A[i])
            i += 1 
    if i < len(A):
        result.extend(A[i:])
    if j < len(B):
        result.extend(B[j:])
    return result

A = [8,4,1,6,5,9,2]
print(merge_sort(A))


