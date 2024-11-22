class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Convert the number to a string
        nums = str(x)
        
        # Use two pointers: one moving forward (i) and one backward (j)
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != nums[j]:  # Compare characters
                return False
            i += 1
            j -= 1
        
        return True 