class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        count = 0
        currno = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            currno.append(count)
            
        return currno