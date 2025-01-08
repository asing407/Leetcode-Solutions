class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the array
        for i in range(len(nums) - 1):  # Loop through the array
            if nums[i] == nums[i + 1]:  # Check if the current element is the same as the next
                return True  # Return True if a duplicate is found
        return False
