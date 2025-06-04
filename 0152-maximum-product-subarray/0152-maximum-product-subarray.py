class Solution:
    def maxProduct(self, nums: List[int]) -> int:

    
        res = nums[0]
        
        maxx = res
        minn = res
        
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxx, minn = minn, maxx
                
            minn = min(nums[i], minn * nums[i])
                
            maxx = max(nums[i], maxx* nums[i])
                
            res = max(res,maxx)
                
        return res