class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0

        for account in accounts:
            currsum = sum(account)
            if currsum >= res:
                res = currsum

        return res
