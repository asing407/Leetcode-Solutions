class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity) -> bool:
            days =1
            total = 0

            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    days += 1
                    if days > D:
                        return False

            return True

        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = l + (r - l) //2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1

        return l