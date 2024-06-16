class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #nums = [3,5]

        nums.sort()

        n = len(nums)

        for x in range(1, n + 1):
            res = 0

            for num in nums:
                if num >= x:
                    res += 1
            if res == x:
                return x
        return -1