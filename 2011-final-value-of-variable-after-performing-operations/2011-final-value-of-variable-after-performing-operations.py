class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        currx = 0

        for i in operations:
            if i == '--X' or i == 'X--':
                currx -= 1
            else:
                currx += 1
        return currx
