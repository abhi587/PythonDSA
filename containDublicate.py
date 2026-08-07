## Below code return true and false if dublcate present in the list 

# def hasDublicate(arr):
#     hashset = set()

#     for n in arr:
#         if n in hashset:
#             return True
#         hashset.add(n)

#     return False
    

# arr = [1,2,3,1]

# print(hasDublicate(arr))


# Below code Remove the Dublicate elements and return the final list FOR SORTED ARRAY

# arr = [1,1,2,2,3,4,4]

# def removeDuplicate(arr):
#     if not arr:
#         return None

#     write = 0

#     for read in range(1,len(arr)):
#         if arr[read] != arr[write]:
#             write += 1

#             arr[write] = arr[read]

#     return write + 1

# k = removeDuplicate(arr)

# print(k)
# print(arr[:k])


# Below code is to retur the dublicate element from the list 


arr = [1,3,4,2,2,3]

def return_dub(arr):
    
    seen = set()
    result = []

    for num in arr:

        if num in seen:
            result.append(num)

        seen.add(num)
    
    return result


print(return_dub(arr))