# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 0
        high = n
        
        while (high >= low):
            mid  = (high + low) //2
            
            if isBadVersion(mid) == True:
                high = mid -1
            else:
                low  = mid + 1
                
        return low
        
        
    
        
    
    