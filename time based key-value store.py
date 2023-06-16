# https://leetcode.com/problems/time-based-key-value-store/

#%%
#Solution 85% 77%
import bisect
class TimeMap:
    def __init__(self):
        self.tm = {}
        pass
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = [[timestamp],{timestamp:value}]
        else:
            bisect.insort(self.tm[key][0],timestamp)
            self.tm[key][1][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ''
        else:
            idx = bisect.bisect_right(self.tm[key][0],timestamp)
            if idx == 0:
                return ''
            else:
                timestamp = self.tm[key][0][idx-1]
                return self.tm[key][1][timestamp]

tm = TimeMap()
# print(None)
# print(tm.set("foo", "bar", 1))
# print(tm.get("foo", 1))
# print(tm.get("foo", 3))
# print(tm.set("foo", "bar2", 4))
# print(tm.get("foo", 4))
# print(tm.get("foo", 5))
# #[null, null, "bar", "bar", null, "bar2", "bar2"]


print(None)
print(tm.set("love","high",10))
print(tm.set("love","low",20))
print(tm.get("love",5))
print(tm.get("love",10))
print(tm.get("love",15))
print(tm.get("love",20))
print(tm.get("love",25))
# [null,null,null,"","high","high","low","low"]

