class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []

        i = 0

        while i < len(nums):
            res.append(nums[nums[i]])
            i = i + 1
        return res

            