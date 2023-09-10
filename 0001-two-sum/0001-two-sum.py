class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif i < j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        res = [j,i]
        return res
                    
        
                
                        