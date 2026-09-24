arr = [0,1,0,3,12]

# output = [1,3,12,0,0]

# def move_zero(arr):
#     if not arr:
#         return None
    
#     write = 0 

#     for read in range(len(arr)):

#         if arr[read] != 0:

#             arr[write], arr[read] = arr[read], arr[write]

#             write += 1

#     return arr

# print(move_zero(arr))


def move_zero(nums):

    position = 0
    
    for num in nums:

        if num != 0:
            nums[position] = num
            position += 1

    while position < len(nums):
        nums[position] = 0 
        position += 1
    
    return nums

print(move_zero(arr))

    
        