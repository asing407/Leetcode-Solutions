class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        d = collections.Counter(nums)
        
        return [x for x in range(1, len(nums) + 1) if x not in d]