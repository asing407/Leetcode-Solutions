class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        nums.sort()

        while l <= r:
            m = (l + r) //2
            if nums[m] != m:
                r -= 1
            else:
                l += 1
        return l
        