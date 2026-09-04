# def second_largest(arr):

#     largest = float("-inf")
#     second = float("-inf")

#     for num in arr:

#         if num > largest:
#             second = largest
#             largest = num

#         elif largest > num > second:
#             second = num

#     return second

# arr = [10, 5, 8, 20, 20]

# print(second_largest(arr))