def binary_search(arr, target):

    left = 0 
    right = len(arr)-1

    while left <= right:

        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            mid = left + 1

        else:
            mid = right - 1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38]

print(binary_search(arr, 16))