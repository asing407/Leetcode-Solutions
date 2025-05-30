from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        middle_index = len(nums) // 2

        return nums[middle_index]
            

        