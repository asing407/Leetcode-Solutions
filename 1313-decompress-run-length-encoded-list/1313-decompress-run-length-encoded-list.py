class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(0, len(nums)-1, 2):
            n = nums[i]
            
            for j in range(n):
                res.append(nums[i+1])
                continue
        return res
    
                