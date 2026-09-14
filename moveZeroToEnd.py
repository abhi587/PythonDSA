arr = [0,1,0,3,12]

# output = [1,3,12,0,0]

def move_zero(arr):
    if not arr:
        return None
    
    write = 0 

    for read in range(len(arr)):

        if arr[read] != 0:

            arr[write], arr[read] = arr[read], arr[write]

            write += 1

    return arr

print(move_zero(arr))