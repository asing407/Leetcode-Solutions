class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        
        leftcnt = rightcnt = cnt = 0
        
        for i in s:
            if i == 'R':
                rightcnt += 1
            elif i == 'L':
                leftcnt += 1
            
            if leftcnt == rightcnt :
                cnt += 1
                
        return cnt
    
                
                
            
                
                