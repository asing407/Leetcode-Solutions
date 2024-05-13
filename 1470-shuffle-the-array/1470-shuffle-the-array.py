class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a, b = nums[:n], nums[n:]
        x = []
        for i in range(n):
            x.append(a[i])
            x.append(b[i])
        
        return x
    
            