# BRUTE FORCE

# create reverse copy of an array and compare it with original
# 0(n) for rev copy

def is_pal_brute(nums):
    rev_copy = nums[::-1]
    return nums == rev_copy


# TWO POINTERS
# in-place comparision 0(1)space

def is_pal_tp(nums):
    left = 0
    right = len(nums)-1

    while left <= right:
        if left[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True

# symmetric version

def is_pal_sym(arr):
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            return False
    return True
print(is_pal_sym([1,2,3,3,2,1]))

