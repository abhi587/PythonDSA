
#### 1. REVERSE ARRAY #####

# def reverse_arr(arr):
#     left = 0
#     right = len(arr)-1

#     while left < right:

#         #swap
#         arr[left], arr[right] = arr[right], arr[left]

#         left += 1
#         right -= 1

#     return arr

# print(reverse_arr([1,2,3,4,5]))


##### 2. CHECK PALINDROME #####

# def palindrome(s):
#     left = 0
#     right = len(s)-1

#     while left < right:

#         if s[left] != s[right]:
#             return False

#         left += 1
#         right -= 1

#     return True

# print(palindrome("madam"))


##### 3. TWO SUM (sorted array) ######

# def two_sum(arr, target):
#     left = 0 
#     right = len(arr)-1

#     while left < right:

#         curr_sum = arr[left] + arr[right]

#         if curr_sum == target:
#             return [left, right]

#         elif curr_sum < target:
#             left += 1

#         else:
#             right -= 1

#     return -1

# print(two_sum([1,2,4,6,10], 8))


###### 4. REMOVE DUBLICATE ######

# def remove_dub(arr):
#     if not arr:
#         return 0

#     write = 0 
#     for read in range(1, len(arr)):
#         if arr[read] != arr[write]:
#             write += 1
#             arr[write] = arr[read]

#     return write + 1

# arr = [1,1,2,2,3,4,4]

# length = remove_dub(arr)
# print(arr[:length])