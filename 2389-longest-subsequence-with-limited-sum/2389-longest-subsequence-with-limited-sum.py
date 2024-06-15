class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        res = []
        for q in queries:
            total, count = 0, 0
            for num in nums:
                if total + num > q:
                    break
                total += num
                count += 1
            res.append(count)
        return res