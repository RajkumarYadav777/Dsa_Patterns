
# TWO POINTERS
'''
# here we check first and last as long as they are true
# if not match return immediately False 

'''


def is_palim_tp(st):
    left = 0
    right = len(st)-1

    while left <= right:

        if st[left] != st[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palim_tp('markram'))
    