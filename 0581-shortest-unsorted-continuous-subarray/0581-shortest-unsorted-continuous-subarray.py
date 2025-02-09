class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums = [2,6,4,8,10,9,15]

        num = sorted(nums)

        start = 0 
        end = len(nums) - 1

        while start < len(nums) and nums[start] == num[start]:
            start += 1
        while end > start and nums[end] == num[end]:
            end -=1
        return end - start + 1
        



        
