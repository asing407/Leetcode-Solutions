class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        
        curr = 0
        
        
        while(curr<len(command)):
            if command[curr] == 'G':
                output += 'G'
                curr += 1
            elif command[curr + 1] == ')':
                output += 'o'
                curr += 2
            else:
                output += 'al'
                curr += 4
                
        return output 