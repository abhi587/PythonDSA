def majorityElement(nums):
    n = len(nums)
    for num in nums:
        count = sum(1 for i in nums if i == num)
        if count > n // 2:
            return num


def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

nums = [5,5,1,1,1,5,5]

print(majorityElement(nums))