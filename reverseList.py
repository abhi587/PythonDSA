arr = [1,2,34,5,3,23,9]

def reverse(arr):
    
    result = []

    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])

    print(result)

reverse(arr)