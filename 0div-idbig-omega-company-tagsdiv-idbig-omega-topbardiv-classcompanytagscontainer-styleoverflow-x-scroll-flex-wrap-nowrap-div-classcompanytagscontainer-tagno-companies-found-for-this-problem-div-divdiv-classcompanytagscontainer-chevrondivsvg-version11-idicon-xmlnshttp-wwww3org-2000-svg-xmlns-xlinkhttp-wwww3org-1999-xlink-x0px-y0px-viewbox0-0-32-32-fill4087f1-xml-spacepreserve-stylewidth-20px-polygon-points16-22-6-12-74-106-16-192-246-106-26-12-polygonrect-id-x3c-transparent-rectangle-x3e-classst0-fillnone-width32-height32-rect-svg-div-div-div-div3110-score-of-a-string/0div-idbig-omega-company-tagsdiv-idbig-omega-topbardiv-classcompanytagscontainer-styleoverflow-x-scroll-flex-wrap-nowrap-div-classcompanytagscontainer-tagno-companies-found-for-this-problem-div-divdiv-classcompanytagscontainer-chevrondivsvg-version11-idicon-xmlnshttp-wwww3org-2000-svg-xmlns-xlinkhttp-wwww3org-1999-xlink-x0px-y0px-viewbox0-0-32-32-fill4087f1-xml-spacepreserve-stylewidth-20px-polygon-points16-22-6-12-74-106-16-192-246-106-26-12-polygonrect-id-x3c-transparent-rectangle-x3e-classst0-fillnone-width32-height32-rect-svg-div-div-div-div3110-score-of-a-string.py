class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))  ##absolute difference abs(num1 - num2) and ord is used to find the ascii value of ord(num1)   
        return res