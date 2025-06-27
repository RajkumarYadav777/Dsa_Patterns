# BRUTE FORCE
# here we use brute force qith basic condition and append
# input = [1,2,2,3,2,4]  , x = 2
# output = [1,3,4]

def remove_all_occur_rence_x(arr, x):
    result = []

    for num in arr:
        if num != x:
            result.append(num)
    return result
print(remove_all_occur_rence_x([1,2,2,3,2,4], 2))



# TWO POINTER
# in this we just use tracker to place non-x element and return later up to tracker

def remove_all_x(arr, x):
    i = 0
    for j in range(len(arr)):
        if arr[j] != x:
            arr[i] = arr[j]
            i += 1
    return arr[:i]
print(remove_all_x([1,2,2,3,2,4], 2))
