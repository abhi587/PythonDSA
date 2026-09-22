### Print Alternative Numbers in a list 

# arr = [1,2,4,2,3,8,4,2,0,7,2,1,6,4,8]

# n = 5
# list = [[] for n in range(n)]
# for i in range(len(arr)):
#     list[i%n].append(arr[i])

# print(list)

# Another way 

# def distribute(arr, n):
#     return [arr[i::n] for i in range(n)]

# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(distribute(arr, 5))


# ### Max and Min of a Array

# arr = [1,3,2,5,10,9,45,3,0,4]

# max = arr[0]
# min = arr[0]

# for num in arr:

#     if num < min:
#         min = num

#     if num > max:
#         max = num

# print(max)
# print(min)



# #### Find second largest Number in a list 


arr = [2,7,3,8,9,3,12,8]

largest = arr[0]
second = arr[0]

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

    
print(second)

