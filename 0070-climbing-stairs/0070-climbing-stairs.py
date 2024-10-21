class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return 1
        
        # a = 1 
        # b = 1

        # for i in range(2, n + 1):
        #     c = a + b
        #     a = b j
        #     b = c
        # return b

        

        memo = {0: 1, 1: 1}

        def climb(n):
            # Check if the result is already computed
            if n not in memo:
                # Recursive call with memoization
                memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)
