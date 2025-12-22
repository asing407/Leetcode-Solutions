class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []
        nums.sort()
        num_set = set(nums)  # Sort the array

        # Check for missing numbers in the range from 1 to len(nums)
        for i in range(1, len(nums)+1):
            if i not in num_set:  # Check if the number is not in the sorted array
                res.append(i)  # If missing, add to results

        return res
        
        