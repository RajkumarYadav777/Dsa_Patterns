# here we have to solve this using 0(1) space 
# if we use set or hashmap it takes 0(n) space
# that too set is unordered 
# nums = [1, 1, 2, 2, 3]


# BRUTE FORCE

def remove_dups_sorted_brute(nums):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                j += 1
        i += 1
    return nums


# TWO POINTERS

def remove_dups_sorted_tp(nums):
    if not nums:
        return []
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return nums[:slow+1]
