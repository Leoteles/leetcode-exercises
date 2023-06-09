#%%
#https://leetcode.com/problems/product-of-array-except-self/

#Solution 44% 34%
class Solution:
    def productExceptSelf(self, nums):

        cum_prod = 1
        right_prod = [1]*len(nums)
        #Iterate backwards
        for i in range(len(nums)-2,-1,-1):
            cum_prod *= nums[i+1]
            right_prod[i] = cum_prod

        out = [right_prod[0]]
        left_prod = 1
        for i in range(1,len(nums)):
            if i>0:
                left_prod *=  nums[i-1]
            out.append(left_prod*right_prod[i])

        return out


nums = [1,2,3,4]
# Output: [24,12,8,6]
Solution().productExceptSelf(nums)



#%%
# O(n^2) solution
class Solution:
    def productExceptSelf(self, nums):
        out = []
        for i in range(len(nums)):
            prod = 1
            for  j in range(len(nums)):
                if j !=i:
                    prod *= nums[j]
            out.append(prod)
        return out

nums = [1,2,3,4]
# Output: [24,12,8,6]
Solution().productExceptSelf(nums)







#%%

class Solution:
    def productExceptSelf(self, nums):
        N = len(nums)
        left_cum_prod = 1
        right_cum_prod = 1
        result_lst = [1] * N

        for idx in range(N):
            #print('idx:',idx,'num',nums[idx])
            if idx > 0:
            #    print('acumula esquerda')
                left_cum_prod *= nums[idx-1]
            #    print(left_cum_prod)
                result_lst[idx] *= left_cum_prod
            
            #Running the list backwards with right_idx
            right_idx = N-idx-1
            #print('right idx',right_idx,'num',nums[right_idx])
            if right_idx < N -1:
                #print('acumula direita')
                right_cum_prod *= nums[right_idx+1]
                #print(right_cum_prod)
                result_lst[right_idx] *= right_cum_prod
        return result_lst
