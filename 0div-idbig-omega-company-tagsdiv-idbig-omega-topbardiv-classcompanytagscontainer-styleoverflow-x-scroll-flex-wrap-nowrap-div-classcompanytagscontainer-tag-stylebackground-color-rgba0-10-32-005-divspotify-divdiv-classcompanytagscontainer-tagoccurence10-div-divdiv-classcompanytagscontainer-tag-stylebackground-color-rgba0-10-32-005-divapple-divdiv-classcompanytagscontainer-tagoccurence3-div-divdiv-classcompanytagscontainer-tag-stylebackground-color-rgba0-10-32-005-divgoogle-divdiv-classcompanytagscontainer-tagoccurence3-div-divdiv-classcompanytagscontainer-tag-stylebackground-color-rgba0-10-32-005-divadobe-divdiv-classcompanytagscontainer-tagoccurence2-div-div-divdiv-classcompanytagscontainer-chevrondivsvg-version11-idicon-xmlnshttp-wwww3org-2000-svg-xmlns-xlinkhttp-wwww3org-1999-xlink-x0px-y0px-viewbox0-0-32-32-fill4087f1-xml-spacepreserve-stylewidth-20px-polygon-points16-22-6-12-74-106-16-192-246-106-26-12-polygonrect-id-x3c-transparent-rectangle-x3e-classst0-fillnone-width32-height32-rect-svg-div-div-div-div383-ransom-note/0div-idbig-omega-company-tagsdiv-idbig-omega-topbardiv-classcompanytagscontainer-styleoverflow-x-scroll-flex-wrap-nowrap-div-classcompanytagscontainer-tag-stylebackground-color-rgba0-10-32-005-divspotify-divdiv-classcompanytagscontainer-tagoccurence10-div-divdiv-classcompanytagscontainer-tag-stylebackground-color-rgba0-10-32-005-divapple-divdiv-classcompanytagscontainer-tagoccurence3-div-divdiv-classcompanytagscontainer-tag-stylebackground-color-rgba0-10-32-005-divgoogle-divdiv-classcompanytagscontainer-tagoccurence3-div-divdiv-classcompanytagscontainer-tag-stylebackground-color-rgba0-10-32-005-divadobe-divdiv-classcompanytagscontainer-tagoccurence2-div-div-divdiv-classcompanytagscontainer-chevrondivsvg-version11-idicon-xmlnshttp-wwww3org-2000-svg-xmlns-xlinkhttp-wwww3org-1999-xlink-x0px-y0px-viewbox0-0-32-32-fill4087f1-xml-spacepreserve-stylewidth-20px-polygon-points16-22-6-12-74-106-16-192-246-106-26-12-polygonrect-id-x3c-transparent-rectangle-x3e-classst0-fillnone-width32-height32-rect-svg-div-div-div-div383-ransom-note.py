class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        note = Counter(ransomNote)
        mag = Counter(magazine)
        
        if note & mag != note:
            return False
        return True
    
        
