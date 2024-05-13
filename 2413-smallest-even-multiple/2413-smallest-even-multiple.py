class Solution:
    def smallestEvenMultiple(self, n: int) -> int:

        res = 0
        return n if n % 2 == 0 else n *2 
            