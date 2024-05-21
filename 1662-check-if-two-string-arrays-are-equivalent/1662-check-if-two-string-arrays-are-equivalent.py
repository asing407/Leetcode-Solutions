class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        w_word1 = ''.join(word1)

        w_word2 = ''.join(word2)

        if w_word1 == w_word2:
            return True
        else:
            return False