class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []

        openparenthesis = 0
        
        for i in s:
            if i == "(" and openparenthesis > 0:
                res.append(i)
            if i == ")" and openparenthesis > 1:
                res.append(i)

            openparenthesis += 1 if i == "(" else -1
        return "".join(res)
    
