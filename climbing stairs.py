# https://leetcode.com/problems/climbing-stairs/


#%%
#Response with dynamic programming
class Solution(object):
    def climbStairs(self,n,memo = None):
        if memo is None:
            memo = {}

        #Case 0
        if n == 0:
            return 1
        if n == 1:
            return 1
        #Missing more than one step
        else:
            #So, 2 options in this step
            if n-1 not in memo:
                memo[n-1] = self.climbStairs(n-1,memo)
            next_options1 = memo[n-1]
            if n-2 not in memo:
                memo[n-2] = self.climbStairs(n-2,memo)
            next_options2 = memo[n-2]
            return next_options1 + next_options2


Solution().climbStairs(3)
Solution().climbStairs(4)
#Solution().climbStairs(34)

#%%
#NOT USING DYNAMIC PROGRAMMING...
def climb(n):
    print(n)
    #Case 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    #Missing more than one step
    else:
        print('else')
        
        #So, 2 options in this step
        next_options1 = climb(n-1)
        next_options2 = climb(n-2)
        #print('res',n,next_options1,next_options2)
        return next_options1 + next_options2



# print(climb(1))
# print(climb(2))
print(climb(3))
print(climb(4))
#print(climb(38))



# %%
