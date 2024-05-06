class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {
                    "I" : 1,
                    "V": 5,
                    "X": 10,
                    "L" : 50,
                    "C": 100,
                    "D" : 500,
                    "M" : 1000
        }
        
        num = 0
        
        last ="I"
        
        for number in s[::-1]:
            if last is None or roman_table[number] < roman_table[last]:
                num -= roman_table[number]
            else:
                num += roman_table[number]
                
            last = number
            
        return num