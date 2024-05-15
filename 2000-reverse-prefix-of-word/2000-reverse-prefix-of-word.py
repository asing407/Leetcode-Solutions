class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
            
            
        if ch not in word:
            return word
        
        index = word.index(ch)
        
        res = word[:index + 1][::-1]
        
        res += word[index + 1:]
        
        return res