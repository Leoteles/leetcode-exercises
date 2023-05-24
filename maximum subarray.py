# https://leetcode.com/problems/maximum-subarray/

# 8% 82%

class Solution:
    def maxSubArray(self, nums):

        cum_sum = 0
        lowest_cum_sum_value = 0
        max_sum = float('-Inf')
        #Turn nums into cumulative values
        #then get maximum and minimum values for the cumulative values
        for num in nums:
            cum_sum += num
            max_sum = max(max_sum,cum_sum - lowest_cum_sum_value)
            #lastly, update, minimum cum sum value
            lowest_cum_sum_value = min(lowest_cum_sum_value,cum_sum)
            #print(f'num {num} e cumsum{cum_sum} e  maxsum = {max_sum} e lowestcumsum_value {lowest_cum_sum_value}')
        return max_sum