class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        i = 0
        

        nums.sort()

        while(i < len(nums)):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2

        return nums
        
