class Solution:
    def isValid(self, s: str) -> bool:
        res = ''
        
        for i in range(len(s)//2):
            if  s== '':
                return True
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
            
        return s == ""
    