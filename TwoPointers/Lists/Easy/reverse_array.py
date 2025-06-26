# BRUTEFORCE
# using pre-allocated version

def rev_arr(nums):
    n = len(nums)
    rev_nums = [0] * n

    for i in range(n):
        rev_nums[n-1-i] = nums[i]  # rev_nums[-1-i] = arr[i] 
    return rev_nums
# we can use append version also
'''
rev_nums = []
rev_nums.append(arr[n-1-i])

'''

# To Reverse an in-place
# no extra space
# two pointers

def rev_arr_tp(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums