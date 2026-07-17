def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i<j:
        while i <= high-1 and nums[i] <= pivot:
            i += 1
        while j >= low+1 and nums[j] > pivot:
            j -=1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        q_index = partition(nums, low, high)

        quick_sort(nums, low, q_index-1)
        quick_sort(nums, q_index+1, high)

# Driver Code
arr = [5, 7, 3, 2, 9, 6, 3]

print("Before Sorting:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("After Sorting :", arr)



# time complexity :- 
# Best	O(n log n)
# Average	O(n log n)
# Worst	O(n²)
# space complexity :- O(log n)