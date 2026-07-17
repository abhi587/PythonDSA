def hasDublicate(arr):
    hashset = set()

    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)

    return False
    

arr = [1,2,3,1]

print(hasDublicate(arr))