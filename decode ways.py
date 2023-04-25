#%%
# FROM:
# https://leetcode.com/problems/decode-ways/

#First solution
#TLE on s = "111111111111111111111111111111111111111111111"
class Solution:
        
    def numDecodings(self, s: str,i=0) -> int:
        #Finished reading string
        if i == len(s):
            return 1
        
        digit = int(s[i])
        #For one character strings
        # First digit equals 0
        if digit == 0:
            return 0
        # Only one digit between 1 and 9
        elif len(s[i:])==1:
            return 1
        
        #For bigger strings
        first_two_digits = int(s[i:i+2])
        # First two digits smaller or equal to 26
        if first_two_digits <= 26:
            return self.numDecodings(s,i+1) + self.numDecodings(s,i+2)
        else:
            return self.numDecodings(s,i+1) #Analize the rest of the string


#With memoization
#Beats 38% 36%
class Solution:
    def numDecodings(self, s: str,i=0,memo=None) -> int:

        if memo is None:
            memo = {}
        #Finished reading string
        if i == len(s):
            return 1
        
        # First digit equals 0
        if int(s[i]) == 0:
            return 0
        
        #If result for string this big is in memory:
        if i in memo:
            return memo[i]

        # Only one digit between 1 and 9
        if len(s[i:])==1:
            out = 1
        #For bigger strings
        #If first two digits smaller or equal to 26
        elif int(s[i:i+2]) <= 26:
            out =  self.numDecodings(s,i+1,memo) + self.numDecodings(s,i+2,memo)
        #First two digits greater than 26
        else:
            out = self.numDecodings(s,i+1,memo) #Analize the rest of the string
        memo[i] = out
        return out

s = "0"
s = "00"
s = "12"
s = "35"
s = "1"
s = "111111111111111111111111111111111111111111111"

Solution().numDecodings(s)
# %%
