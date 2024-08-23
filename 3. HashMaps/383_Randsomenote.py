'''
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine 
and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Time Complexity : O(N + M)
        Space Complexity : O(N)'''
        wordMap = {}

        for i in magazine:
            wordMap[i] = wordMap.get(i,0) + 1
        for j in ransomNote:
            wordMap[j] = wordMap.get(j,0) - 1
            if wordMap[j] < 0:
                return False
        
        return True

