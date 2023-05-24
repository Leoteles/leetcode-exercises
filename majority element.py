# https://leetcode.com/problems/majority-element/

#%%

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        qtd = {}
        maj = 0
        second_maj = 0
        idx_maj= -1
        for idx,n in enumerate(nums):
            qtd[n] = qtd.get(n,0) + 1
            if maj < qtd[n]:
                second_maj = maj
                maj = qtd[n]
                idx_maj = n
            elif maj == qtd[n]:
                second_maj = maj
            els_search = len(nums) - (idx + 1)
            if (maj - second_maj) >= els_search:
                break
        return idx_maj
        




# other solution

def majorityElement1(self, nums):
    nums.sort()
    return nums[len(nums)//2]




#%%

#Solucao O(n)
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        qtd = Counter(nums)
        maj = 0
        maj_idx = -1
        for k,v in qtd.items():
            if maj < v:
                maj = v
                maj_idx = k
        return maj_idx

#%%
