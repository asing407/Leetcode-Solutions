class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        
        for i in range(len(nums)):
            if nums[i] not in ht:
                ht[nums[i]] = 1
                
            else:
                ht[nums[i]] += 1
        
        for i in range(len(nums)):
            if ht[nums[i]] >= 2:
                return True
        return False
                
                