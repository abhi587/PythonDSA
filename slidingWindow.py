# Flow Diagram

# Initial Window

# [2,1,5,1,3,2]

#  L---R

# Window = [2,1,5]
# Sum = 8

# Slide

# Remove 2
# Add 1

# [2,1,5,1,3,2]

#    L---R

# Window = [1,5,1]
# Sum = 7

# Slide

# Remove 1
# Add 3

# [2,1,5,1,3,2]

#      L---R

# Window = [5,1,3]
# Sum = 9

# Slide

# Remove 5
# Add 2

# [2,1,5,1,3,2]

#        L---R

# Window = [1,3,2]
# Sum = 6

# Done.


####  MAX_SUM_SUBARRAY #####


def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):

        #remove left element 
        window_sum -= arr[right-k]

        #add new right element
        window_sum += arr[right]

        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2,1,5,1,3,2]

print(max_sum_subarray(arr, 3))