def majorityElement(nums):
    n = len(nums)
    for num in nums:
        count = sum(1 for i in nums if i == num)
        if count > n // 2:
            return num

nums = [5,5,1,1,1,5,5]

print(majorityElement(nums))