# arr = [1,2,34,5,3,23,9]

# def reverse(arr):
    
#     result = []

#     for i in range(len(arr)-1,-1,-1):
#         result.append(arr[i])

#     print(result)

# reverse(arr)


# using two pointer reversing a list 

def reverse(arr):
    left = 0 
    right = len(arr)-1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr

print(reverse([1,2,3,4,5]))