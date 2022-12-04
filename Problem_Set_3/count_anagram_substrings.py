def get_strnum(s):
    '''
    Input: s is a character
    Output: the number of s in alphabet, 'a' corresponds to 0
    '''
    return ord(s)-ord('a')

def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    m, k, n = len(T), len(S[0]), len(S)
    #build a data structure in O(m) time
    #transform all character in T to number
    Freq = [0] * 26
    D = {}
    for i in range(m):
        Freq[get_strnum(T[i])] += 1
        if i > k-1:
            Freq[get_strnum(T[i-k])] -= 1
        if i >= k-1:
            key = tuple(Freq)
            if key in D:
                D[key] += 1
            else:
                D[key] = 1

    A = [0] * n
    for i in range(n):
        Freq = [0] * 26
        for j in S[i]:
            Freq[get_strnum(j)] += 1
        key = tuple(Freq)
        if key in D:
            A[i] = D[key]
    return tuple(A)
