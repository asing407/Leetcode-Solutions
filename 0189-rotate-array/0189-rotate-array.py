class Solution:
    def reversedarr(self, left, right, arr):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums = [1,2,3,4,5,6,7]
        k %= len(nums)
        self.reversedarr(0,len(nums)- 1, nums)
        self.reversedarr(0, k- 1, nums)
        self.reversedarr(k, len(nums) - 1, nums)
        


