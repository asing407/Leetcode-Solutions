class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    
    # 1. Create a map to store groups: { "sorted_key": [list_of_anagrams] }
    # defaultdict(list) ensures we don't get a KeyError when adding a new key
        groups = defaultdict(list)
        
        # 2. Iterate through every word in the input list
        for word in strs:
            # Sort the letters of the word to create a 'key'
            # e.g., "eat" -> ['a', 'e', 't'] -> "aet"
            sorted_key = "".join(sorted(word))
            
            # 3. Add the original word to the list matching that key
            groups[sorted_key].append(word)
        
        # 4. Return just the lists of grouped words
        return list(groups.values())