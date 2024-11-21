class Solution:
    def maxProfit(self,prices):
        left  = 0
        right = 1
        
        
        maxprofit = 0
        
        while right < len(prices):
            currProfit = prices[right] - prices[left]
            
            if prices[left] <prices[right]:
                maxprofit = max(maxprofit, currProfit)
            else:
                left = right
                
            right += 1
        
        return maxprofit
        
    
       