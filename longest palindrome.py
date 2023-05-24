# https://leetcode.com/problems/longest-palindrome/


# 69% 51%
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for i in s:
            letters[i] = letters.get(i,0) + 1

        seq = 0
        has_odd_qtd = False
        for k,v in letters.items():
            if v == 1:
                has_one = True
            if v % 2 > 0 :
                has_odd_qtd = True
            n = (v // 2) * 2
            seq += n
        return seq+1 if has_odd_qtd else seq
s = 'ccc'
s = "abccccdd"
Solution().longestPalindrome(s)

#%%%