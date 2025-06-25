# TWO POINTERS
'''
1. here we have two strings one string must contains another string in exact same order 
2 . we will use pointers for both if one is match then only move i but j should move either way
3 . whenever i is exceeds or equals len of that string we will get output of True/False
'''

def is_sub_sequence(st, t):

    i = 0
    j = 0

    while i < len(st) and  j < len(t):
        if st[i] == t[j]:
            i += 1
        j += 1
    return i == len(st)
    
print(is_sub_sequence("abc", "ahbgdc")) 


# with edge cases and with for loop

def is_subsequence_tp(s,t):

    # if subsequnce is empty it means present
    if s == '':
        return True
    
    # if sub is greater than main that should not be 
    if len(s) > len(t):
        return False
    
    # tracks subsequence
    j = 0

    for i in range(len(t)):

        if s[j] == t[i]:
            if j == len(s)-1:
                return True
            j += 1
    # we have not found specific char of j in an entire t
    return False


# NUMBER OF SUBSEQUENCES