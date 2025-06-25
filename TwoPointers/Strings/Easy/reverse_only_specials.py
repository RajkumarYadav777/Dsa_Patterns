# TWO POINTERS

'''
1 . swap only when bith are special chars and move  pointers
2 . move pointers even when chars are not specials 

'''

def reverse_specials_tp(st):
    lst = list(st)
    left = 0
    right = len(lst)-1

    while left < right:

        if not lst[left].isalnum() and not lst[right].isalum():
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        elif lst[left].isalnum():
            left += 1
        
        elif lst[right].isalnum():
            right -= 1
    
    return ''.join(lst)