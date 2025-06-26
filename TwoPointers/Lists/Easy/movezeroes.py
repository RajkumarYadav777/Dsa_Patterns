# BRUTE FORCE

# first approach:
# just create two seperate lists with non-zero and zero and merge


def move_zeroes_brute1(nums):
    zeroes = []
    non_zeroes = []

    for item in nums:
        if item > 0:
            non_zeroes.append(item)
        else:
            zeroes.append(item)
    return non_zeroes + zeroes

print(move_zeroes_brute1([2,0,1,3,0,4,0,5,0]))

# second approach
# count zeroes and extend with result

def move_zeroes_brute2(nums):
    result = []
    zero_count =0

    for num in nums:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    return result.extend([0]*zero_count)


# third approach 
# pre allocation and index fill

def move_zeroes_brute3(nums):
    n = len(nums)

    result = [0] * n
      # pointer for filling non zeros
    for num in nums:
        if num != 0:
            result[i] = num
            i += 1
        
    return result
print(move_zeroes_brute3([2,0,1,3,0,4,0,5,0]))


# TWO POINTER

# in this approach we use one pointer for filling non zeros as a tracker and
# one is for scnning and fill remaining positions with zeroes from where tracker stops

def move_zeros_tp(nums):
    n = len(nums)

    start = 0

    for end in range(n):
        if nums[end] != 0:
            nums[start] = nums[end]
            start += 1
    # for zero filling
    while start < n:
        nums[start] = 0
        start += 1
    return nums


# we can use for loop also
'''
for k in range(start, n):
    nums[k] = 0

'''
