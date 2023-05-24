# https://leetcode.com/problems/ransom-note/
# 12% 87%

class Solution:
    from collections import defaultdict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = defaultdict(lambda: 0)
        for i in magazine:
            magazine_dict[i] += 1

        for i in ransomNote:
            if magazine_dict[i] == 0:
                return False
            else:
                magazine_dict[i] -= 1

        return True