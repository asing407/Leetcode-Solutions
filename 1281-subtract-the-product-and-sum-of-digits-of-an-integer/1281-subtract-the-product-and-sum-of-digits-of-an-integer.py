class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        
        for digits in str(n):
            product *= int(digits)
            
        sumofdig = 0
        
        for digits in str(n):
            sumofdig += int(digits)
            
        return product - sumofdig
    
    