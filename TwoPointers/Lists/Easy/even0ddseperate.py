# BRUTE FORCE
# here we return result array that contains evens frst and odds next
# input = [1,3,2,4,5,6,9,8]
# output = [2,4,6,8,1,3,5,9]

def even_odd_sep_brut(arr):

    even = [item for item in arr if item % 2 == 0]
    odd = [item for item in arr if item % 2]

    return even + odd
print(even_odd_sep_brut([1,3,2,4,5,6,9,8]))


# TWO POINTER 
# we will use overwrite approach 
# two pass + in-place

def even_add_sep_tp(arr):
    i = 0
    for item in arr:
        if item % 2 == 0:
            arr[i] = item
            i += 1
    for item in arr:
        if item % 2 :
            arr[i] = item
            i += 1
    return arr[:i]


# alternate even and odd

def alternate_even_odd(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2]

    res = []
    i = j = 0

    while i < len(evens) and j < len(odds):
        res.append(evens[i])
        res.append(odds[j])
        i += 1
        j += 1
    
    # left overs
    # while i < len(evens) and j < len(odds):
    #     res.append(evens[i])
    #     res.append(odds[j])
    #     i += 1
    #     j += 1
    # return res
    # OR
    # by this time any one of array is exhausted
    
    res.extend(evens[i:])
    res.extend(odds[j:])
    return res
