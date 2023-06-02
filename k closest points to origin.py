

#Solution 58% 40%

class Solution:
    def kClosest(self, points, k):
        closest = []
        for i,point in enumerate(points):
            dist = (point[0]**2) + (point[1]**2)
            if len(closest)<k:
                heapq.heappush(closest,(-dist,i))#minus dist, because heapq defaults to min heap
            else:
                heapq.heappushpop(closest,(-dist,i))
        return [points[i] for _,i in closest]





#Solution 5% 40%
class Solution:
    def kClosest(self, points, k):
        closest = {}#index:dist
        for i,point in enumerate(points):
            dist = (point[0]**2) + point[1]**2
            if len(closest) < k:
                closest[i] = dist
            elif dist < max(closest.values()):
                max_key = max(closest, key=closest.get)
                del closest[max_key]
                closest[i] = dist
        return [points[i] for i in closest.keys()]
    
