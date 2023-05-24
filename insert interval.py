# https://leetcode.com/problems/insert-interval/

#%%

from operator import itemgetter
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        for i in sorted(intervals + [newInterval],key=itemgetter(0)):
            # print(i)
            if not lst:
                lst.append(i)
                continue

            # print('lst',lst[-1],'i',i)
            if lst[-1][1] >= i[0]:
                # print('overlap')
                lst[-1] = [lst[-1][0],max(lst[-1][1],i[1])]
                # print(lst[-1])
            else:
                lst.append(i)

        return lst


intervals = [[1,3],[6,9]]
newInterval = [2,5]
Solution().insert(intervals,newInterval)

#%%
from operator import itemgetter
intervals = [[1,3],[6,9]]
newInterval = [2,5]

lst = []
for i in sorted([*intervals,newInterval],key=itemgetter(0)):
    print(i)
    if not lst:
        lst.append(i)
        continue

    print('lst',lst[-1],'i',i)
    if lst[-1][1] >= i[0]:
        print('overlap')
        lst[-1] = [lst[-1][0],max(lst[-1][1],i[1])]
        print(lst[-1])
    else:
        lst.append(i)


lst


#%%
# Solucao 86% 24%
from bisect import bisect
from operator import itemgetter
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insertion_point = bisect(a=intervals,x=newInterval)
        #print(insertion_point)
        #insert element until new interval, then insert new interval
        if insertion_point > 0:
            lst = intervals[0:insertion_point]
            if lst[-1][1] >= newInterval[0]:
                lst[-1] = [lst[-1][0],max(lst[-1][1],newInterval[1])]
            else:
                lst.append(newInterval)
        else:
            lst = [newInterval]
        
        #print(lst)
        #insert the other elements greater than the new interval
        for i in range(insertion_point,len(intervals)):
            #print(i,lst[-1][1],intervals[i][0])
            if lst[-1][1] >= intervals[i][0]:
                lst[-1] = [lst[-1][0],max(lst[-1][1],intervals[i][1])]
                #print('aqui',lst[-1])

            else:
                return lst + intervals[i:]
                #lst.append(intervals[i])
                #when there are no more overlaps, break
                break
        return lst
        #return lst + intervals[last_idx:]


# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# intervals = [[4,8]]
intervals = [[1,5]]
newInterval = [0,3]
Solution().insert(intervals,newInterval)