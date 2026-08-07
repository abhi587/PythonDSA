
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i!=j and nums[i]+nums[j] == target:
#                 return [i,j]


# print(twoSum([12,45,6,7,2],14))


#using HashMap

arr = [2,7,11,15]
target = 9

def two_sum(arr, target):

    seen = {}

    for i, num in enumerate(arr):

        complement = target - num

        if complement in seen:
            return [seen[complement],i]

        seen[num] = i

    return []

print(two_sum(arr, target))