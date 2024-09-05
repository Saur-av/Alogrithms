'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
'''

class Solution:
    def wordPattern(self,pattern: str, s: str) -> bool:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Linear | O(n)'''
        m = {}

        sp = s.split()
        if len(pattern) != len(sp):
            return False

        for i,j in zip(pattern,sp):
            if i in m:
                if m[i] != j:
                    return False
            else:
                if j in m.values():
                    return False
                m[i] = j
        
        return True

