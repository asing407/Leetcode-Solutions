class Solution:
    def findMin(self, nums: List[int]) -> int:
        #nums[3,4,5,1,2]

        l = 0 
        r = len(nums) - 1
        res = sys.maxsize

        while l <= r:
            mid = (l + r) //2
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                res = min(res,nums[mid])
                r = mid - 1
        return res