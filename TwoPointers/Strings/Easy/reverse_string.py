# we can do using for loop and build reverse string 
# but it takes o(n^2) because it builds each time a new string
# not memory efficient becuase create intermediate strings

# general approach

def rev_str(st):
    rev = ''

    for char in st:
        rev = char + rev
    
    return rev
print(rev_str('rajkumar'))

# we have another methods
'''
1 . [::-1] - very efficient
2.  range(len(s)-1,-1,-1)
3. built-in reversed(st)

'''




# TWO POINTERS
# converging two pointers -> opposite ends meet in the middle (crossed)

'''
# string is immutable we cant reverse in-place
# so convert it list and later join 
# since we just swap so condition is while left < right
# we use while left <= right only when compare two items 

'''
def reverse_two_pointers(st):
    temp_st = list(st)

    left = 0
    right = len(temp_st)-1

    while left < right:
        temp_st[left], temp_st[right] = temp_st[right], temp_st[left]
        left += 1
        right -= 1
    
    return ''.join(temp_st)

print(reverse_two_pointers('rajkumar'))

