
#  TWO POINTERS
'''
1.vowels set is for fast membership checks
2.if both are vowles then only swap (symmetric checks)
3.if either of the pointers are not vowels  move pointers

'''

# string is immutable , convert it to list
def reverse_vowels_tp(st):
    vowels = set('aeiouAEIOU')

    lst = list(st)
    left = 0
    right = len(lst)-1

    while left < right:
        if lst[left] in vowels and lst[right] in vowels:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        elif lst[left] not in vowels:
            left += 1
        
        elif lst[right] not in vowels:
            right -= 1
        
    return ''.join(lst)


# another version for tp


def reverse_vowels_tp1(st):
    lst = list(st)
    vowels = set('aeiouAEIOU')
    left = 0
    right = len(lst)-1

    while left < right :

        #skips non vowels from left
        while left < right and lst[left] not in vowels:
            left += 1
        
        # skips non vowels from right

        while left < right and lst[right] not in vowels:
            right -= 1
        
        # by this time two pointers at the vowels ;swap

        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -=1
    return ''.join(lst)
        



# naive approach
#in this we extract vowels first and pop when vowels match to append


def reverse_vowels_naive(st):
    vowels = set('aeiouAEIOU')
    vow_lst = [ch for ch in st if ch in vowels]

    result = []

    for ch in st:
        if ch in vowels:
            result.append(vow_lst.pop())
        else:
            result.append(ch)
    return ''.join(result)




