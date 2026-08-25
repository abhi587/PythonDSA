# 1 . getConcatenation

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+numsA


# 2. comtains duplicate

class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
                hashset = set()

                for n in nums:
                        if n in hashset:
                                return True
                        hashset.add(n)
                return False



# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         low = 0 
#         mid = 0 
#         high = len(nums) -1

#         while mid <= high:
#             if nums[mid] == 0:
#                 nums[low],nums[mid] = nums[mid], nums[low]
#                 low += 1
#                 mid += 1 
#             elif nums[mid] == 1:
#                 mid +=1
#             else:
#                 nums[mid], nums[high] = nums[high], nums[mid]
#                 high -= 1
            