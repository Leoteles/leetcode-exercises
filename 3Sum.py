# https://leetcode.com/problems/3sum/
#%%
#Solution 51% 44%
class Solution:
    def threeSum(self, nums): 
        nums = sorted(nums)
        out = []
        print(nums)
        #From begining to len-2 (to give space for second and third element in triplet)
        for i in range(len(nums)-2):
            #To avoid dupllicates in result, skip if this number is equal to previous
            if i>0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            #Second and third will act like in a two pointer problem, searching the array from begining and from end
            i2 = i+1#next
            i3 = len(nums)-1#last
            while i2 < i3:
                second = nums[i2]
                third = nums[i3]
                triplet_sum = first + second + third
                # print(first,second,third,'sum',triplet_sum)
                if triplet_sum == 0:
                    out.append([first,second,third])
                    i3 -= 1
                    while i3 > i2 and nums[i3] == nums[i3+1]:
                        i3 -= 1
                #Too big, get smmaller num by decrementing third index, since nums is sorted
                elif triplet_sum > 0:
                    i3 -= 1
                #Too small, get bigger num by incrementing second index, since nums is sorted
                else:# case triplet_sum < 0:
                    i2 += 1
        return out
nums = [-1,0,1,2,-1,-4]
# nums = [-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6]
Solution().threeSum(nums)
#%%

#Second solution, ordering the array and skipping sums greater than 0
class Solution:
    def threeSum(self, nums): 
        nums = sorted(nums)
        out = set()
        for i in range(len(nums)-2):
            n_i = nums[i]
            if n_i > 0:
                break
            for j in range(i+1,len(nums)-1):
                n_j = nums[j]
                if n_i + n_j > 0:
                    break
                for k in range(j+1,len(nums)):
                    # print(i,j,k)
                    if sum([nums[i],nums[j],nums[k]])==0:
                        out.add(tuple(sorted((nums[i],nums[j],nums[k]))))
        return [[i,j,k] for i,j,k in out]
                        

nums = [-1,0,1,2,-1,-4]
# nums = [-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6]
Solution().threeSum(nums)




#%%

#First solution - TLE
class Solution:
    def threeSum(self, nums): 
        out = set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    # print(i,j,k)
                    if sum([nums[i],nums[j],nums[k]])==0:
                        out.add(tuple(sorted((nums[i],nums[j],nums[k]))))
        return [[i,j,k] for i,j,k in out]
                        

nums = [-1,0,1,2,-1,-4]
Solution().threeSum(nums)
