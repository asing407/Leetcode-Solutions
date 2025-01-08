class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setnums = set(nums)

        missing = []

        for i in range(1,len(nums) + 1):
            if i not in setnums:
                missing.append(i)
        return missing




                
        