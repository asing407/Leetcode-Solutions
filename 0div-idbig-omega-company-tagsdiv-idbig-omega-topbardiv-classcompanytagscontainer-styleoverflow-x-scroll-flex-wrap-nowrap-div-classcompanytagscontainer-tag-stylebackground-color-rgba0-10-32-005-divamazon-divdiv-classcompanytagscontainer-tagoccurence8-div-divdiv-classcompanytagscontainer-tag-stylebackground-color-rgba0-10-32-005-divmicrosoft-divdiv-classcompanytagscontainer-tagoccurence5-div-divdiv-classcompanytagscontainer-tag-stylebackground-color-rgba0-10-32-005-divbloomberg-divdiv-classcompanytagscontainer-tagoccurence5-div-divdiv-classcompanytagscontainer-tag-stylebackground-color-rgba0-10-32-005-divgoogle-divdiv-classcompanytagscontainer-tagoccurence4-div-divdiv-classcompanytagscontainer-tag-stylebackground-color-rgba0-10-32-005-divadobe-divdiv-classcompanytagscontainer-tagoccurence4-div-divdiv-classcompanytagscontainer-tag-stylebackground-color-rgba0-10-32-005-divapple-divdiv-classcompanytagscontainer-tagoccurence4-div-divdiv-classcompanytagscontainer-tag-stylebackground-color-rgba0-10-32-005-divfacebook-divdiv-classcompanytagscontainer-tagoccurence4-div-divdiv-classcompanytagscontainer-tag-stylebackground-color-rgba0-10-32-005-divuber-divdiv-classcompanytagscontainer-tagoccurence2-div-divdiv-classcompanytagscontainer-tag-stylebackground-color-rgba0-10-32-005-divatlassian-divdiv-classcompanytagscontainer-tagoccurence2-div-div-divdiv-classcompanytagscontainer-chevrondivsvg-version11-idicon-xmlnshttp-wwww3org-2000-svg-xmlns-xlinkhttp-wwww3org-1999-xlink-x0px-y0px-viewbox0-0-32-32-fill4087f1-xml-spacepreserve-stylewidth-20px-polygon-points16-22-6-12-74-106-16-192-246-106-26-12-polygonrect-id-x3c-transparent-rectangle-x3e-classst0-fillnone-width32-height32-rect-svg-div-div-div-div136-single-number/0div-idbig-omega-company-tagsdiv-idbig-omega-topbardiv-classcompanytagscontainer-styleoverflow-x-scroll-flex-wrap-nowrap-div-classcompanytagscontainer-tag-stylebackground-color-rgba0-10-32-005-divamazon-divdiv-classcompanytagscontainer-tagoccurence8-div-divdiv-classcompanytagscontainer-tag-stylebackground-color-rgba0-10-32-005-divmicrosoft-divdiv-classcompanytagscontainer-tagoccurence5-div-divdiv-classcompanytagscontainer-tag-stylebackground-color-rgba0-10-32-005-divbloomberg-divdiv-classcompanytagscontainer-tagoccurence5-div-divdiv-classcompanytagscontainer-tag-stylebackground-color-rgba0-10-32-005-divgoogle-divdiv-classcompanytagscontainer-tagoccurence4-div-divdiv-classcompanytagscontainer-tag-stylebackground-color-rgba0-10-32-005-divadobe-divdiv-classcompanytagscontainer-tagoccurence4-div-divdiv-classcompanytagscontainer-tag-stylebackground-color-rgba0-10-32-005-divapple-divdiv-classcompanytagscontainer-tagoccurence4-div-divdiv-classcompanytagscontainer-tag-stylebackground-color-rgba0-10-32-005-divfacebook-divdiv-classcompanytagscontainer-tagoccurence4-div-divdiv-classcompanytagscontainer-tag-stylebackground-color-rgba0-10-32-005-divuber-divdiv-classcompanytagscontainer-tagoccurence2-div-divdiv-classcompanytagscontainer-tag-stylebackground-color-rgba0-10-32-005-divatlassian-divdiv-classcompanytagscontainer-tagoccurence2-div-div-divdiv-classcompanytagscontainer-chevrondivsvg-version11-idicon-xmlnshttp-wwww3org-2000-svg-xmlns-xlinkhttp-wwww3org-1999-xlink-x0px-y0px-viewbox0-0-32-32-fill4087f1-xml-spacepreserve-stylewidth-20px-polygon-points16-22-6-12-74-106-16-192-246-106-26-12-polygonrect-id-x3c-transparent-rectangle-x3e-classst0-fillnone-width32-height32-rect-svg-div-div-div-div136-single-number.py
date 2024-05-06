class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        
        count = Counter(nums)
        
        for i in nums:
            if count[i] == 1:
                return i

