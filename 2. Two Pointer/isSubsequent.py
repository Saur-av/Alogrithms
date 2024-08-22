'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        a = 0
        b = 0

        while (a < len(s) and b < len(t)):
            if s[a] == t[b]:
                a += 1
            b += 1

        return (a == len(s))

def test(s,t,exp):
    print(f"\ns = {s}\nt = {t}\nExpected : {exp}")
    res = Solution.isSubsequence(1,s,t)
    if res is not exp:
        print("Test Case Failed!!")
    print(f"Result = {res}")

test(s = "abc", t = "ahbgdc", exp=True)
test(s = "axc", t = "ahbgdc", exp = False)