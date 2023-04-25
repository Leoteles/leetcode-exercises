# https://leetcode.com/problems/valid-palindrome/

# 51% 94%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #has_a_letter = False
        N = len(s)
        right_i = N -1
        for i in range(N):
            #print(i,s[i])
            if s[i].isalnum():
                #has_a_letter = True
                while right_i > i and not s[right_i].isalnum():
                    right_i -= 1
                
                if s[right_i].isalnum() and s[i].lower() != s[right_i].lower():
                    return False
                
                if right_i - i <= 2:
                    return True
                right_i -= 1 #next character
        return True
