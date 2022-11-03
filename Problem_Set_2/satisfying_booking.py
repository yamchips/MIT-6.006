def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    # YOUR CODE HERE #
    ##################
    return tuple(B)

def merge_booking(B1,B2):
    '''
    Input: B1 and B2 are two tuples of room booking triples (k,s,t)
    Output:  B | Tuple of request satisfying R1 and R2
    '''
    i, j = len(B1), len(B2)

    pass

a = ((1,2,3),(2,3,4))
print(a[0][1])