# BRUTEFORCE
# using pre-allocated version

def rev_arr(nums):
    n = len(nums)
    rev_nums = [0] * n

    for i in range(n):
        rev_nums[i] = nums[n-i-1]  # rev_nums[-1-i] = arr[i] 
    return rev_nums
# we can use append version also
'''
rev_nums = []
rev_nums.append(arr[n-1-i])

'''

# TWO POINTER
# To Reverse an in-place
# no extra space


def rev_arr_tp(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


# Another in-place 

def rev_symmetry(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr
print(rev_symmetry([10,20,30,40,50]))

# with out append current + prev

def without_append(arr):
    result = []
    for i in range(len(arr)):
        result = [arr[i]] + result
    return result
print(without_append([10,20,30,40]))

# appending last value inside loop
def appending_inloop(arr):
    n = len(arr)
    result = []

    for i in range(n):
        result.append(arr[n-i-1])
    return result



# some other 

def rev_arr(arr):
    n = len(arr)
    nums = [0]*n
    i = 0
    while i < n:
        nums[i] = arr[n-i-1]
        i += 1
    return nums


def rever_array(arr):
    n = len(arr)
    nums = [0] * n
    for i in range(n):
        nums[i] = arr[n-i-1]
    return nums
