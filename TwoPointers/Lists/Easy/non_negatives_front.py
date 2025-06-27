# BRUTE FORCE
# in this we just place / shift/ overwrite non negative s to the left and remaining could be ignored

# input = [1,-3,-4,5,6,2,-8]
# output = [1,5,6,2]

def move_front_brut(arr):
    res = []
    for num in arr:
        if num >= 0 :
            res.append(num)
    return res

print(move_front_brut([1,-3,-4,5,6,2,-8]))

# TWO POINTER
# we use overwrite version usig two pointers

def move_front_tp(arr):
    i = 0 # track to add non negatives to front

    for num in arr:
        if num >= 0:
            arr[i] = num
            i += 1
    return arr[:i]
print(move_front_tp([1,-3,-4,5,6,2,-8]))