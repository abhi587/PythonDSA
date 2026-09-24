arr = [1,2,4,5,6,8]

def missing_number(arr):
    
    miss = []

    for i in range(1, max(arr)+1):

        if i not in arr:
            miss.append(i)

    return miss

print(missing_number(arr))