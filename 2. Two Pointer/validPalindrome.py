'''A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[r] != s[l]:
                return False
            
            l += 1
            r -= 1

        return True
    
def test(s,result):
    print(f"\ns = {s} | Expected = {result}")
    ispal = Solution.isPalindrome(1,s)

    if ispal is not result:
        print("Test Case Failed.")
    print(f"Result = {ispal}")
    
test("'A man, a plan, a canal: Panama'",True)
test("'race a car'",False)
test("' '",True)