class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_words = []
        
        for i in sentences:
            a = i.split(' ')
            max_words.append(len(a))
            
        return max(max_words)
        
        