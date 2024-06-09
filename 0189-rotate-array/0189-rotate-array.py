        
class Solution:
    def reversedarray(self, left, right, arr):
        
        while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)          
        self.reversedarray(0, len(nums)-1, nums)
        self.reversedarray(0, k-1, nums)
        self.reversedarray(k, len(nums) - 1, nums)