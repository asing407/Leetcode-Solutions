class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() #split the words
        reversed_words = reversed(words) #reverse each wword individually
        reversed_sentence = ' '.join(reversed_words) #cleaning extra spaces and rejoining al words
        return reversed_sentence



        