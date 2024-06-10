class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

    
        res =[]
        
        for i in range(k):
            res = max(nums)
            nums.remove(res)
            
            
        return res
    